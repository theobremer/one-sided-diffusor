import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
filename = "output/resultSteadyState/postProcessing/solverInfo/0/solverInfo.dat" 

# Spaltennamen definieren
colnames = [
    "Time", "U_solver", "Ux_initial", "Ux_final", "Ux_iters",
    "Uy_initial", "Uy_final", "Uy_iters", "U_converged",
    "k_solver", "k_initial", "k_final", "k_iters", "k_converged",
    "p_solver", "p_initial", "p_final", "p_iters", "p_converged"
]

# Daten einlesen
df = pd.read_csv(filename, sep=r'\s+', skiprows=2, names=colnames)

# Plot
plt.figure(figsize=(10, 6))

# Verschiedene Residuals über die Zeit plotten
plt.plot(df["Time"], df["Ux_final"], label="Ux_final")
plt.plot(df["Time"], df["Uy_final"], label="Uy_final")
plt.plot(df["Time"], df["k_final"], label="k_final")
plt.plot(df["Time"], df["p_final"], label="p_final")

# Achsenbeschriftung und Titel
plt.xlabel("Time")
plt.ylabel("Final residuals (log)")
plt.title("Final residuals")

# Y-Achse logarithmisch
plt.yscale('log')

# Gitter und Legende
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()

# Speichern und anzeigen
plt.savefig("Final_Residuals.png", dpi=150)
plt.show()
