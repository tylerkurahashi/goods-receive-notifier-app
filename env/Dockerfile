FROM python:3.9

# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update --fix-missing && apt-get install -y \
    ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
    python3 python3-dev python3-tk python3-pip libzmq3-dev libpng-dev \
    zip unzip htop sl git openssh-server vim curl screen\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# env
COPY env/requirements.txt /env/requirements.txt
RUN pip install -r /env/requirements.txt
COPY env/requirements_dev.txt /env/requirements_dev.txt
RUN pip install -r /env/requirements_dev.txt

# SSH
RUN mkdir /var/run/sshd
RUN echo 'root:ss' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd 
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# workspace
ENV PYTHONPATH $PYTHONPATH:/workspace
WORKDIR /workspace/

# run
ENTRYPOINT ["/usr/sbin/sshd", "-D"]