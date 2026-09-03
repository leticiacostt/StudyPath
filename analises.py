#pega os dados do banco e usa pandas para analisá-los
import pandas as pd
from banco import buscar_estudos

def carregar_dados():
    resultados = buscar_estudos()

    df = pd.DataFrame(
        resultados,
        columns=['ID', 'Matéria', 'Assunto', 'Data', 'Horas']
    )

    df['Horas'] = pd.to_numeric(df['Horas'])

    return df

df = carregar_dados()

print("=" * 40)
print("        ANÁLISE DOS ESTUDOS")
print("=" * 40)

# total de horas estudadas
total_horas = (df["Horas"].sum())
quantidade_estudos = len(df)
media_horas = df['Horas'].mean()

horas_por_dia = df.groupby('Data')['Horas'].sum()
media_horas_por_dia = horas_por_dia.mean()

print("\nRESUMO")
print("-" * 40)
print(f"Total de horas: {total_horas}")
print(f"Quantidade de estudos: {quantidade_estudos}")
print(f"Média por estudo: {media_horas:.1f} horas")
print(f"Média por dia: {media_horas_por_dia:.1f} horas")

# horas por matéria
horas_por_materia = (df.groupby("Matéria")["Horas"].sum())
print("\nHORAS POR MATÉRIA")
print("-" * 40)

for materia, horas in horas_por_materia.items():
    print(f"{materia}: {horas} horas")

materia_mais_estudada = horas_por_materia.idxmax()
print("\nMATÉRIA MAIS ESTUDADA")
print("-" * 40)
print(f"{materia_mais_estudada}")

maior_estudo = df['Horas'].max()
menor_estudo = df['Horas'].min()
print("\nMAIOR E MENOR ESTUDO")
print("-" * 40)
print(f"Maior estudo: {maior_estudo} horas")
print(f"Menor estudo: {menor_estudo} horas")

print("\nHORAS POR DIA")
print("-" * 40)

for data, horas in horas_por_dia.items():
    print(f"{data}: {horas} horas")

dia_mais_estudado = horas_por_dia.idxmax()
horas_dia_mais_estudado = horas_por_dia.max()
print("\nDIA MAIS ESTUDADO")
print("-" * 40)
print(f"Dia: {dia_mais_estudado}")
print(f"Horas: {horas_dia_mais_estudado}")

porcentagem_por_materia = (horas_por_materia / total_horas) * 100
print("\nPORCENTAGEM POR MATÉRIA")
print("-" * 40)

for materia, porcentagem in porcentagem_por_materia.items():
    print(f"{materia}: {porcentagem:.1f}%")

print("\n" + "=" * 40)