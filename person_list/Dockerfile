FROM python:3.5
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD wait-for-it.sh /code/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
