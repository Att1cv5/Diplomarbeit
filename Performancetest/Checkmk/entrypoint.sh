#!/bin/bash

MODE="${MODE:-checkmk}"  # Default ist checkmk

if [ "$MODE" = "checkmk" ]; then
    echo ">> Starting in Checkmk Agent mode (xinetd on port 6556)"
    exec /usr/sbin/xinetd -dontfork
elif [ "$MODE" = "prometheus" ]; then
    echo ">> Starting in Prometheus Node Exporter mode (port 9100)"
    exec /usr/local/bin/node_exporter --web.listen-address=:9100
else
    echo "Unknown MODE: $MODE"
    exit 1
fi
