import pandas as pd
import numpy as np

# Simulierte psychologische Daten (Zeitwahrnehmung)
data = {
    "participant": ["P1", "P2", "P3", "P4", "P5"],
    "real_time_sec": [10, 10, 10, 10, 10],
    "perceived_time_sec": [12, 9, 15, 8, 11]
}

df = pd.DataFrame(data)

# Berechnung der Verzerrung (Bias)
df["time_distortion"] = df["perceived_time_sec"] - df["real_time_sec"]

# Durchschnitt berechnen
mean_distortion = df["time_distortion"].mean()

print("Data:\n", df)
print("\nAverage time distortion:", mean_distortion)