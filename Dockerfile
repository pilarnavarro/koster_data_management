# Koster Object Detection - Koster Lab Database
# author: Jannes Germishuys

FROM nvidia/cuda:10.0-devel-ubuntu18.04 as builder

RUN apt-get update && \
    apt-get install -y python3.8 python3-pip git vim && \
    apt-get clean

RUN python3.8 -m ensurepip --upgrade

RUN export PATH="$HOME/.local/bin:$PATH"

#RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/python3 -m pip 1

RUN pip --version
