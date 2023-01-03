import os
import pandas as pd
import numpy as np

from typing import Any
from typing import Type

from joblib import load
from sklearn.feature_extraction.text import CountVectorizer


dir_path = os.path.dirname(os.path.realpath(__file__))


def create_model() -> Any:
    pass


class Pipeline(CreateModel):

    def __init__(self):
        super().__init__()
        self._cv = CountVectorizer()
        self._data = pd.read_csv(f"{dir_path}/dataset.csv")
        self._cv.fit_transform(np.array(self._data['Text']))
        self._model = load(f'{dir_path}/model.pkl')

    def vectorize(self, text: str) -> Type[np.array]:
        return self._cv.transform([text]).toarray()

    def predict(self, text: str) -> str:
        return self._model.predict(self.vectorize(text))[0]
