# Use the Grafana base image with version 10.2.2 on Ubuntu
FROM grafana/grafana:latest

# Expose port 3000 for Grafana
EXPOSE 3000

# Command to start the Grafana container with the name "grafana"
CMD ["grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana", "cfg:default.paths.logs=/var/log/grafana"]

########################################################################
# docker build -t grafana-image .
# docker run -d -p 3000:3000 --name grafana grafana-image
########################################################################
