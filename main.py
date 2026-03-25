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

# Web data extraction (example)
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population"

tables = pd.read_html(url)
web_df = tables[0]

print("\nWeb Data:")
print(web_df.head())
