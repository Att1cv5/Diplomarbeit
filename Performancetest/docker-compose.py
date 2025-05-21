NUM_CONTAINERS = 150
BASE_IP = "10.0.0."
START_IP = 10

PROMETHEUS_PORT = 9100
CHECKMK_PORT = 6556

# Modus festlegen: "prometheus" oder "checkmk"
TARGET_MODE = "checkmk"  # Ändern Sie diesen Wert, um den gewünschten Modus zu setzen

IMAGE_NAME = "fakehost"

with open("docker-compose.yml", "w") as f:
    f.write("version: '3.8'\n\n")
    f.write("services:\n")

    if TARGET_MODE == "checkmk":
        f.write("  monitoring:\n")
        f.write("    image: checkmk/check-mk-raw:2.3.0p30\n")
        f.write("    container_name: monitoring\n")
        f.write("    ports:\n")
        f.write("      - \"8080:5000\"\n")
        f.write("      - \"8000:8000\"\n")
        f.write("    tmpfs:\n")
        f.write("      - /opt/omd/sites/cmk/tmp:uid=1000,gid=1000\n")
        f.write("    volumes:\n")
        f.write("      - ./checkmk_data:/omd/sites\n")
        f.write("      - /etc/localtime:/etc/localtime:ro\n")
        f.write("    restart: always\n")
        f.write("    networks:\n")
        f.write("      custom_net:\n")
        f.write("        ipv4_address: 10.0.0.2\n\n")
    else:
        # Prometheus Service
        f.write("  prometheus:\n")
        f.write("    image: prom/prometheus\n")
        f.write("    container_name: prometheus\n")
        f.write("    ports:\n")
        f.write("      - \"9091:9090\"\n")
        f.write("    volumes:\n")
        f.write("      - ./prometheus.yml:/etc/prometheus/prometheus.yml\n")
        f.write("      - ./prometheus_data:/prometheus\n")
        f.write("    restart: always\n")
        f.write("    networks:\n")
        f.write("      custom_net:\n")
        f.write("        ipv4_address: 10.0.0.2\n\n")


    # Image einmalig bauen
    f.write(f"  builder:\n")
    f.write(f"    build:\n")
    f.write(f"      context: .\n")
    f.write(f"      dockerfile: Dockerfile.dockerfile\n")
    f.write(f"    image: {IMAGE_NAME}\n")
    f.write(f"    networks:\n")
    f.write(f"      custom_net:\n")
    f.write(f"        ipv4_address: 10.0.0.3\n")
    f.write(f"    restart: unless-stopped\n\n")

    # Custom Container mit statischen IPs und Modus
    for i in range(NUM_CONTAINERS):
        ip_last = START_IP + i
        depends_on = f"builder" if i == 0 else f"app{i}"
        port = PROMETHEUS_PORT if TARGET_MODE == "prometheus" else CHECKMK_PORT
        f.write(f"  app{i+1}:\n")
        f.write(f"    image: {IMAGE_NAME}\n")
        f.write(f"    container_name: fakehost{i+1}\n")
        f.write(f"    depends_on:\n")
        f.write(f"      - {depends_on}\n")
        f.write(f"    environment:\n")
        f.write(f"      - MODE={TARGET_MODE}\n")  # Modus setzen
        f.write(f"    networks:\n")
        f.write(f"      custom_net:\n")
        f.write(f"        ipv4_address: {BASE_IP}{ip_last}\n")
        f.write(f"    restart: unless-stopped\n\n")

    # Volumes & Netzwerk
    f.write("volumes:\n")
    f.write("  checkmk_data:\n")
    f.write("  prometheus_data:\n\n")
    f.write("networks:\n")
    f.write("  custom_net:\n")
    f.write("    driver: bridge\n")
    f.write("    ipam:\n")
    f.write("      config:\n")
    f.write("        - subnet: 10.0.0.0/24\n")