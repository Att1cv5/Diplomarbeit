import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Pfad/zur/CSV')

# Timestamp in echtes Datetime-Format umwandeln
df['timestamp'] = pd.to_datetime(df['timestamp'])

# cpu_usage Prozentzeichen entfernen
df['cpu_usage(in %)'] = df['cpu_usage(in %)'].str.replace('%', '', regex=False).astype(float)

# disk_usage ist in KB – in MB umwandeln
df['disk_usage(in MB)'] = df['disk_usage(in KB)'] / 1024

# memory_usage als float sicherstellen
df['memory_usage'] = df['memory_usage'].astype(float)

# Durchschnitt und Median für CPU-Auslastung
cpu_mean = df['cpu_usage(in %)'].mean()
cpu_median = df['cpu_usage(in %)'].median()

print(f"Durchschnittliche CPU-Auslastung: {cpu_mean:.2f}%")
print(f"Median der CPU-Auslastung: {cpu_median:.2f}%")

# Durchschnittliche RAM-Auslastung berechnen
memory_mean = df['memory_usage'].mean()
memory_median = df['memory_usage'].median()
print(f"Durchschnittliche RAM-Auslastung: {memory_mean:.2f} MB")
print(f"Median der RAM-Auslastung: {memory_median:.2f} MB")

# Kleinster und größter Wert für CPU-Auslastung
cpu_min = df['cpu_usage(in %)'].min()
cpu_max = df['cpu_usage(in %)'].max()
print(f"Kleinste CPU-Auslastung: {cpu_min:.2f}%")
print(f"Größte CPU-Auslastung: {cpu_max:.2f}%")

# Kleinster und größter Wert für RAM-Auslastung
memory_min = df['memory_usage'].min()
memory_max = df['memory_usage'].max()
print(f"Kleinste RAM-Auslastung: {memory_min:.2f} MB")
print(f"Größte RAM-Auslastung: {memory_max:.2f} MB")

# Kleinster und größter Wert für Festplattennutzung
disk_min = df['disk_usage(in MB)'].min()
disk_max = df['disk_usage(in MB)'].max()
print(f"Kleinster Speicherverbrauch: {disk_min:.2f} MB")
print(f"Größter Speicherverbrauch: {disk_max:.2f} MB")

# Plotten
# CPU Usage Plot
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['cpu_usage(in %)'], color='blue')
plt.title('CPU Auslastung (%)')
plt.ylabel('CPU Auslastung (%)')
plt.xlabel('Zeit')
plt.grid(True)
plt.show()

# Memory Usage Plot
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['memory_usage'], color='green')
plt.title('RAM-Auslastung (MB)')
plt.ylabel('RAM-Auslastung (MB)')
plt.xlabel('Zeit')
plt.grid(True)
plt.show()

# Disk Usage Plot
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['disk_usage(in MB)'], color='red')
plt.title('Speicherverbrauch (MB)')
plt.ylabel('Speicherverbrauch (MB)')
plt.xlabel('Zeit')
plt.grid(True)
plt.show()