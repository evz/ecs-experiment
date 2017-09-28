FROM python:3.5
RUN apt-get -y update
RUN apt-get -y install gcc make
RUN apt-get -y install wget unzip
RUN wget https://github.com/StackExchange/blackbox/archive/master.zip && \
    unzip master.zip && \
	cd blackbox-master && \
	make manual-install
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN gpg --import gpg-deploy-key.key
RUN blackbox_postdeploy
RUN mv /code/configs/app_config.py /code/api/app_config.py
