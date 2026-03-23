import pandas as pd

# Daten laden
df = pd.read_csv("data.csv")

# Verzerrung berechnen
df["distortion"] = df["perceived_time"] - df["real_time"]

# Ganze Tabelle anzeigen
print("Full Data:")
print(df)

# Durchschnitt berechnen
print("\nAverage distortion:", df["distortion"].mean())
