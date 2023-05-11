# Koster Object Detection - Koster Lab Database
# author: Jannes Germishuys

FROM nvidia/cuda:10.0-devel-ubuntu18.04 as builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y make automake gcc g++ subversion git && \
    apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev build-essential yasm cmake libtool libc6 libc6-dev unzip wget libnuma1 libnuma-dev pkg-config && \
    apt-get install -y libmagic-dev

# Build ffmpeg with CUDA support from source
RUN git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git && \
    cd nv-codec-headers && \
    make install && \
    cd ..

RUN git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg/ && cd ffmpeg && \
    ./configure --enable-nonfree --enable-cuda-nvcc --enable-libnpp --extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64 && \
    make -j 8 && \
    make install

FROM nvidia/cuda:10.0-devel-ubuntu18.04

RUN apt-get update && \
    apt-get install -y python3.8 python3-pip git vim wget && \
    apt-get clean

COPY --from=builder /usr/local/bin/ffmpeg /usr/local/bin/ffmpeg

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.8 get-pip.py
RUN pip install --upgrade pip --user
    
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD https://api.github.com/repos/ocean-data-factory-sweden/koster_data_management/git/refs/heads/main version.json
RUN git clone --recurse-submodules https://github.com/ocean-data-factory-sweden/koster_data_management.git
WORKDIR /usr/src/app/koster_data_management
RUN pip install -r requirements.txt
# Install all packages except ffmpeg
RUN grep -v "ffmpeg==" kso_utils/requirements.txt > filtered_requirements.txt && \
    pip install -r filtered_requirements.txt && \
    rm filtered_requirements.txt
# Install SNIC-specific requirements
RUN pip install ipywidgets==8.0.1
RUN pip install ipysheet==0.4.4 
RUN jupyter nbextension install --user --py widgetsnbextension
RUN jupyter nbextension enable --user --py widgetsnbextension
RUN jupyter nbextension enable --user --py jupyter_bbox_widget
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/koster_data_management
ENV PYTHONPATH=/path/to/your/new/folder:$PYTHONPATH

# Create user
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# Make sure the contents of our repo are in ${HOME}

COPY . ${HOME}
USER root
RUN chown ${NB_USER} -R ${HOME}
USER ${NB_USER}
WORKDIR ${HOME}
# Make sure this is run another time for new user
RUN jupyter nbextension enable --user --py widgetsnbextension
RUN jupyter nbextension enable --user --py jupyter_bbox_widget
