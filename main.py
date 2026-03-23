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


import matplotlib.pyplot as plt

# Beispiel Daten
real_time = [10, 10, 10]
perceived_time = [14, 8, 13]

# Diagramm
plt.plot(real_time, label="Real Time")
plt.plot(perceived_time, label="Perceived Time")

plt.title("Time Perception Comparison")
plt.xlabel("Participants")
plt.ylabel("Time")
plt.legend()

plt.show()
