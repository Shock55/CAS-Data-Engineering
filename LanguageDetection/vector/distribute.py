import os
import sys
import string
import logging
import pandas as pd
import numpy as np

from typing import List
from typing import Any
from typing import Type
from typing import Dict

from redis import Redis
from rq.job import Job
from rq import Queue
from rq.registry import FinishedJobRegistry
from rq.registry import StartedJobRegistry

from pipeline import clean_data


logging.basicConfig(stream = sys.stdout, level = logging.DEBUG)
logger = logging.getLogger(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))


def clean_data(path: str, language: str) -> Dict:
    translate_table = dict((ord(char), None) for char in string.punctuation)
    text = []
    lang = []
    df = pd.read_csv(path, 'utf-8', header = None, names = [language])
    for i, line in df.iterrows():
        line = line[language]
        if len(line) != 0:
            line = line.lower()
            line = re.sub(r"\d+", "", line)
            line = line.translate(translate_table)
            text.append(line)
            lang.append(language)
    
    return {'language': lang, 'text': text}


def create_dataframe(q: Any, *frames) -> Type[pd.DataFrame]:
    for frame in frames:
        q.enqueue(clean_data, frame['data'], frame['lang'])


def extract_work(con: Type[Redis], start_registry: Any, end_registry: Any, state: bool = False) -> Dict:

    logger.info("start working")

    text = []
    lang = []
    while state == False:
        job_ids = start_registry.get_job_ids()
        if not job_ids:
            state = True
    for e in end_registry.get_job_ids():
        job = Job.fetch(e, connection = con)
        result = job.result
        text.append(result.text)
        lang.append(result.language)
    
    return pd.DataFrame({"text": text, "language": lang})


def prepare_data():
    redis = Redis()
    que = Queue(connection = redis)
    start_registry = StartedJobRegistry(queue=que)
    end_registry = FinishedJobRegistry(queue=que)

    raw_data = [
            {'data': 'europarl-v7.sv-en.sv', 'lang': 'Swedish'},
            {'data': 'europarl-v7.fr-en.fr', 'lang': 'France'},
            {'data': 'europarl-v7.de-en.de', 'lang': 'German'},
            {'data': 'europarl-v7.da-en.da', 'lang': 'danish'},
            {'data': 'europarl-v7.es-en.es', 'lang': 'spanish'},
            {'data': 'europarl-v7.el-en.el', 'lang': 'greel'},
            {'data': 'europarl-v7.cs-en.cs', 'lang': 'tschechian'}
        ]

    create_dataframe(que, *raw_data)
    print(extract_work(redis, start_registry, end_registry))


if __name__ == '__main__':
    prepare_data()
