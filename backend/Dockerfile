FROM rasa/rasa:latest-full 

USER root

WORKDIR /app
COPY . /app
COPY ./data /app/data

RUN pip3 install nltk
RUN  python3 -m rasa train

# Switch back to a non-root user
USER 1001

VOLUME /app
VOLUME /app/data
VOLUME /app/models


CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug"]