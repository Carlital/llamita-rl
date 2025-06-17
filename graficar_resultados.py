import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("resultados_entrenamiento.csv")

# Crear etiqueta para cada configuración
df["Configuración"] = df.apply(lambda row: f"α={row['Alpha']}, γ={row['Gamma']}, ε={row['Epsilon']}, ep={row['Episodio']}", axis=1)

# Configurar estilo
plt.style.use("ggplot")
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Gráfico 1: Recompensa Total
axs[0].bar(df["Configuración"], df["Recompensa Total"], color="steelblue")
axs[0].set_title("Comparación de Recompensa Total")
axs[0].set_ylabel("Recompensa")
axs[0].tick_params(axis='x', labelrotation=45)

# Gráfico 2: Pasos Promedio
axs[1].bar(df["Configuración"], df["Pasos Promedio"], color="mediumseagreen")
axs[1].set_title("Comparación de Pasos Promedio")
axs[1].set_ylabel("Pasos promedio")
axs[1].tick_params(axis='x', labelrotation=45)

# Gráfico 3: Tasa de Éxito
axs[2].bar(df["Configuración"], df["Tasa de Éxito (%)"], color="darkorange")
axs[2].set_title("Comparación de Tasa de Éxito")
axs[2].set_ylabel("Éxito (%)")
axs[2].tick_params(axis='x', labelrotation=45)

# Ajuste final y guardar
plt.tight_layout()
plt.savefig("grafica_comparativa_resultados.png")
plt.show()
