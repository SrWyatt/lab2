import pandas as pd

# 1. Cargar el dataset
df = pd.read_csv("football_matches.csv")

# 2. Resumen con describe()
print("Resumen con describe()")
print(df.describe(include="all"))

# 3. Tipos de datos con dtypes
print("\nTipos de datos por columna")
print(df.dtypes)

# 4. Primeros y últimos registros
print("\nPrimeros registros (head)")
print(df.head())
print("\nÚltimos registros (tail)")
print(df.tail())


# 5. Ordenar resultados
print("\nOrdenados por goles locales (ascendente)")
print(df.sort_values(by="goal_home_ft").head())
print("\nOrdenados por goles locales (descendente)")
print(df.sort_values(by="goal_home_ft", ascending=False).head())

# 6. Medidas estadísticas 
col = "goal_home_ft"
media = df[col].mean()
mediana = df[col].median()
desv_std = df[col].std()

print(f"\nMedidas estadísticas para {col}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desv_std:.2f}")

report_data = {
    "a_descripcion": {
        "total_partidos": df.shape[0],
        "total_temporadas": df["season"].nunique(),
        "rango_temporadas": (df["season"].min(), df["season"].max()),
        "total_equipos": df["home_team"].nunique()
    },
    "b_resumen_estadistico": df.describe().to_dict(),
    "c_tendencias": {
        "primeros_partidos": df.head(5).to_dict(orient="list"),
        "ultimos_partidos": df.tail(5).to_dict(orient="list")
    },
    "d_categorias_sobresalientes": {
        "equipo_mas_frecuente_local": df["home_team"].value_counts().idxmax(),
        "equipo_mas_frecuente_visitante": df["away_team"].value_counts().idxmax()
    },
    "f_medidas_estadisticas_goal_home_ft": {
        "media": media,
        "mediana": mediana,
        "desviacion_estandar": desv_std
    }
}


