FROM debian:12

# Installiere benötigte Pakete für beide Modi
RUN apt-get update && apt-get install -y \
    xinetd wget curl ca-certificates && \
    apt-get clean

# Installiere Checkmk Agent
COPY check-mk-agent_2.3.0p30-1_all.deb /tmp/
RUN dpkg -i /tmp/check-mk-agent_2.3.0p30-1_all.deb && rm /tmp/check-mk-agent_2.3.0p30-1_all.deb

# Installiere Node Exporter (Binary direkt von Prometheus Projekt)
RUN curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-amd64.tar.gz && \
    tar xzf node_exporter-1.8.1.linux-amd64.tar.gz && \
    mv node_exporter-1.8.1.linux-amd64/node_exporter /usr/local/bin/ && \
    rm -rf node_exporter-1.8.1.linux-amd64*

# Exponiere beide Ports (Checkmk Agent und Node Exporter)
EXPOSE 6556 9100

# Entry Script, der basierend auf MODE Umgebungsvariable startet
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


