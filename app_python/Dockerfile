FROM python:3.9.6-alpine
LABEL maintainer="a.brisilin@innopolis.university"

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm requirements.txt && \
    adduser --disabled-password clocker -s /bin/sh -h clock

USER clocker
WORKDIR /clock

ENV MODE=PROD

EXPOSE 5000

COPY --chown=clocker:clocker config.ini /clock/ 
COPY --chown=clocker:clocker src /clock/src

CMD ["python3", "-m", "src.main.main"]