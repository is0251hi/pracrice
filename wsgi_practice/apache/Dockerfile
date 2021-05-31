FROM ubuntu

RUN apt-get update && \
    apt-get install sudo && \
    sudo apt-get install -y \
    python3.7 \
    apache2

CMD [ "sudo", "service", "apache2", "start"]
