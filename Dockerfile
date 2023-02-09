# Koster Object Detection - Koster Lab Database
# author: Jannes Germishuys

FROM nvidia/cuda:10.0-devel-ubuntu18.04 as builder

RUN apt-get update && \
    apt-get install -y python3.8 python3-pip git vim wget && \
    apt-get clean

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.8 get-pip.py

RUN export PATH="$HOME/.local/bin:$PATH"

#RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/python3 -m pip 1

RUN pip --version
