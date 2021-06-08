FROM ubuntu

RUN apt-get update && \
    apt-get install sudo && \
    apt-get install -y tzdata && \
    sudo apt-get install -y \
    python3.7 \
    apache2

CMD [ "sudo", "service", "apache2", "start"]
