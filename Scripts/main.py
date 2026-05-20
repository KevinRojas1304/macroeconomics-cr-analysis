import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv ("data/raw/pib_mundial.csv", skiprows=4)
costa_rica = datos[datos["Country Name"] == "Costa Rica"]
columnas_Importantes = [
    "2020",
    "2021",
    "2022",
    "2023"
]
pib_cr = costa_rica [columnas_Importantes]
print ("Datos del PIB")
print (pib_cr)

promedio_pib = pib_cr.mean (axis=1)
maximo_pib = pib_cr.max (axis=1)
minimo_pib = pib_cr.min (axis=1)

#print("\nPromedio PIB:", promedio_pib.values[0])
print("Máximo PIB:", maximo_pib.values[0])
print("Mínimo PIB:", minimo_pib.values[0])

años = ["2020", "2021", "2022", "2023"]

valores_pib = [
    pib_cr["2020"].values[0],
    pib_cr["2021"].values[0],
    pib_cr["2022"].values[0],
    pib_cr["2023"].values[0]
]
plt.figure(figsize=(8,5))

plt.plot(años, valores_pib, marker="o")
plt.title("Crecimiento del PIB de Costa Rica")
plt.xlabel("Año")
plt.ylabel("PIB (%)")

plt.grid(True)

plt.savefig("outputs/charts/pib_costa_rica.png")

plt.show()