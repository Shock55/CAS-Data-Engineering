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


Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

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
