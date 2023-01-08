FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

USER admin

COPY requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r /requirements.txt

COPY ./backend /app
