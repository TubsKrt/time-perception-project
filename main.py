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


import matplotlib.pyplot as plt

plt.scatter(df["real_time"], df["perceived_time"])
plt.xlabel("Real Time")
plt.ylabel("Perceived Time")
plt.title("Time Perception Bias")

plt.show()


print("\nInterpretation:")
print("Participants tend to overestimate time on average.")
