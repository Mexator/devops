FROM python:3.9.6-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

ENV FLASK_APP=src/main/main.py    
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]