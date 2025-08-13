import pandas as pd
import folium
import re

# Les inn CSV-filen
df = pd.read_csv('elbiler.csv', comment='/', skipinitialspace=True)

# Funksjon for å hente ut koordinater fra 'Vehicle Location'
def extract_coords(point_str):
    match = re.search(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)', str(point_str))
    if match:
        lon, lat = float(match.group(1)), float(match.group(2))
        return lat, lon
    return None, None

# Legg til kolonner for latitude og longitude
df['lat'], df['lon'] = zip(*df['Vehicle Location'].map(extract_coords))

# Lag et kart sentrert på et gjennomsnittspunkt
center = [df['lat'].mean(), df['lon'].mean()]
m = folium.Map(location=center, zoom_start=8)

# Legg til punktene
for _, row in df.iterrows():
    if not pd.isnull(row['lat']) and not pd.isnull(row['lon']):
        folium.Marker([row['lat'], row['lon']], popup=row['City']).add_to(m)

# Lagre kartet til en HTML-fil
m.save('elbiler_kart.html')
print("Kart lagret som elbiler_kart.html")