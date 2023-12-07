# Use the Grafana base image with version 10.2.2 on Ubuntu
FROM grafana/grafana:latest-ubuntu

# install tools with the root user
USER root
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y jq sudo nodejs npm python3 python3-pip

# add new user factory
RUN useradd -ms /bin/bash factory && \
    usermod -aG sudo factory

# disable sudo password
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER 1001

# Set factory as default user
USER factory
WORKDIR /home/factory


# Expose port 3000 for Grafana
EXPOSE 3000 8000 9000 8086

# Command to start the Grafana container with the name "grafana"
CMD ["grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana", "cfg:default.paths.logs=/var/log/grafana"]

########################################################################
# docker build -t grafana-image .
# docker run -d -p 3000:3000 --name grafana grafana-image
########################################################################
