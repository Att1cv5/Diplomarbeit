#!/bin/bash

echo "prometheus,timestamp,cpu_usage(in %),memory_usage,disk_usage(in KB)" > cpu_mem_disk_usageDataPrometheus.csv

COUNTER=0;
MAX_ITERATIONS=5760;
CONTAINER_NAME="prometheus"

while (("$COUNTER" < "$MAX_ITERATIONS")); do
    COUNTER=$((COUNTER+1))

    TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)

    USAGE=$(du -sk ./prometheus_data | awk '{print $1}' | sed 's/K//');
    docker stats --no-stream --format "{{.Name}},{{.CPUPerc}},{{.MemUsage}}" "$CONTAINER_NAME" | while IFS=',' read -r NAME CPU MEM; do
        MEM_USED=$(echo $MEM | awk -F' / ' '{print $1}')
        if [[ $MEM_USED == *GiB ]]; then
            MEM_USED=$(echo "$MEM_USED" | sed 's/GiB//' | awk '{print $1 * 1024}')
        elif [[ $MEM_USED == *MiB ]]; then
            MEM_USED=$(echo "$MEM_USED" | sed 's/MiB//')
        fi
        echo "$CONTAINER_NAME,$TIMESTAMP,$CPU,$MEM_USED,$USAGE" >> cpu_mem_disk_usageDataPrometheus.csv;
    done
    sleep 15;
done
