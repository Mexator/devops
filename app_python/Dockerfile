FROM python:3.9.6-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 
ENV MODE=PROD
CMD ["python3", "-m", "src.main.main"]