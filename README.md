# Language Detection
## Detect languages with machine learning

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

Language detection is a fastapi and scikit-learn based machine learning api
to detect languages.

- Docker Compose
- Sqlite
- Fastpi
- scikit-learn

## Features
- Supply text to the api and get the detected language back

## Tech

Dillinger uses a number of open source projects to work properly:

- [FastApi](https://fastapi.tiangolo.com/) - Fast python webframework
- [Sqlite](https://www.sqlite.org/index.html) - Minimalistic filesystem based database
- [scikit-learn](https://scikit-learn.org/stable/) - Python machine learning library
- [Docker](https://www.docker.com/) - Container Engine
- [Docker Compose](https://github.com/docker/compose) - Tool for running multi-container applications on Docker defined using the Compose file format.

And of course Language Detection itself is open source with a [public repository](https://github.com/Shock55/CAS-Data-Engineering)
 on GitHub.

## Installation

Language Detection requires [Python3](https://www.python.org/download/releases/3.0/) to run.

Clone the repository and fire up docker compose

```sh
git clone https://github.com/Shock55/CAS-Data-Engineering.git && cd CAS-Data-Engineering
docker-compose run
```

Afterwards go to http://localhost:5000/docs
![Alt text](/relative/path/to/img.jpg?raw=true "Optional Title")
