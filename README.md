# Clock

[![Build and push Docker image](https://github.com/Mexator/devops/actions/workflows/build-image.yml/badge.svg)](https://github.com/Mexator/devops/actions/workflows/build-image.yml)

A simple Python ap that shows current time in Moscow

## Description

This is a Python ap that shows current time in Moscow (GMT+3). It is built with
Flask.

## Getting Started

### Dependencies

Python 3, Flask+Jinja2, pytz. For more details check out `app_python/requirements.txt`

### Installing & Running

Clone this repository, enter `app_python` and execute following commands to
run the app

```sh
source .env
pip install -r requirements.txt
python -m flask run
```

Then you can open [http://localhost:5000] in your browser.

### Running with Docker

There is a [Docker image](https://hub.docker.com/repository/docker/mexator/clock)
built with app. To run it you need Docker. Simply launch

```sh
docker run --publish 5000:5000 mexator/clock
```

## Unit tests

Clone this repository, enter `app_python` and execute following command to
run tests

```sh
pip install -r requirement.test.txt
pytest src/test
```

```sh
python -m src.test.test
```

## Authors

[Anton Brisilin](https://github.com/Mexator)

## License

This project is licensed under the MIT license - see the License.txt file for
details
