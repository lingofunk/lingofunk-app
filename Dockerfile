FROM ubuntu:16.04

COPY Miniconda3-4.3.31-Linux-x86_64.sh .
COPY requirements.txt .

# adapted from daten-und-bass.io/blog/fixing-missing-locale-setting-in-ubuntu-docker-image/
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8 
ENV LC_ALL en_US.UTF-8

# for miniconda and python libs
# git: for nonpip python libs
RUN apt-get install --allow-unauthenticated -y bzip2 gcc g++ git cmake libboost-all-dev wget

# python main utils
RUN bash Miniconda3-4.3.31-Linux-x86_64.sh -b

# make conda python the main python
ENV PATH /root/miniconda3/bin:$PATH

# enable docker-specific logic for mongoDB connection
ENV AM_I_IN_A_DOCKER_CONTAINER Yes

# test python
# RUN python --version

# python pip libs and cleanup
RUN  pip install --upgrade pip && pip install -r requirements.txt && \
     apt-get install swig3.0 && pip install -I --no-cache-dir jamspell==0.0.11 && \
     ls -d -1 ~/miniconda3/lib/python3.6/site-packages/spacy/lang/** | grep -v -e "\.py" -e"ru" | xargs rm -rf && \
     rm -rf ~/.cache/

COPY . /opt/lingofunk/
WORKDIR /opt/lingofunk/handler
EXPOSE 8001
CMD [ "/root/miniconda3/bin/python", "-c", "'import pandas; print(pandas)'"]
