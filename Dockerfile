FROM python:3.6-slim-jessie
WORKDIR /app
ADD . /app
RUN mkdir ./output
RUN apt-get update
RUN apt-get install -yq \
    curl \
    wget \
    gnupg \
    gnupg2 \
    nano \
    apt-transport-https
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME DOCKJENTEST
CMD [ "python", "/app/obja.py" ]
