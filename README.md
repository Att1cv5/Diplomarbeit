# Dateien der Diplomarbeit

In diesem Repository sind alle relevanten Dateien zu finden, die zur Bearbeitung der Diplomarbeit verwendet wurden.


## Anleitung Performancetest

Im Ordner Performancetest sind alle benötigten Dateien zur Durchführung des Performancetests.

### Voraussetzungen

- Debian-Linux auf dem Server oder Rechner
- Performancetest Ordner liegt im Zielverzeichnis
- Docker.io ist installiert
- ausreichend Ressourcen verfügbar

### Ablauf

1. Mount-Ordner erstellen
   - Prometheus Ordner: mkdir prometheus_data
   - Checkmk Ordner: mkdir checkmk_data
2. ggf. Leseberechtigungen anpassen
   - chmod 755 directory
3. docker-compose starten
   - docker-compose up -d
4. tmux öffnen
   - tmux
- bei Prometheus
1. Messungsskript starten
   - ./memoryAndCpuAndDiskUsage.sh
- bei Checkmk
1. der Pfad checkmk_data/cmk/var/pnp4nagios/perfdata benötigt Lese- und Schreibrechte (Besitzer ist Checkmk-Image)
   1. sudo chmod 755 var
   2. sudo chmod 755 pnp4nagios
   3. sudo chmod 755 perfdata
2. Checkmk öffnen
   1. docker logs monitoring
   2. Nutzername und Passwort für cmkadmin finden
   3. auf Webserver anmelden
   4. Host-Folder anlegen
     - IP-Range-Scan
     - Haken entfernen von "do not monitor this host"
     - speichern
   6. Service-Discovery auf dem kompletten Ordner starten
   7. Messungsskript starten
    - ./memoryAndCpuAndDiskUsage.sh
