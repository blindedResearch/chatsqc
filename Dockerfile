FROM rockylinux/rockylinux:8
LABEL maintainer 'Jeff Ohrstrom <johrstrom@osc.edu>'

ARG OPENAI_API_KEY

RUN dnf update -y && dnf clean all && rm -rf /var/cache/dnf/*
RUN dnf install -y \
        python3.11 python3.11-pip

COPY . /app
RUN rm /app/.env

RUN cd app; pip3 install -r requirements.txt
RUN cd app; OPENAI_API_KEY=$OPENAI_API_KEY python3 preprocess.py

WORKDIR /app

ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false

ENTRYPOINT streamlit run chatsqc.py
