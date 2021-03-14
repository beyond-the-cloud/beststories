FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN python --version
RUN pip --version
RUN python3 --version
RUN pip3 --version
RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "hackernews.py"]