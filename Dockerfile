# Koster Object Detection - Koster Lab Database
# author: Jannes Germishuys

FROM nvidia/cuda:10.0-devel-ubuntu18.04 as builder

RUN apt-get update && \
    apt-get install -y python3.8 python3-pip git vim && \
    apt-get clean

RUN update-alternatives --install /usr/bin/pip pip /usr/local/lib/python3.8/site-packages/pip 1

RUN pip --version
