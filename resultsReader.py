import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Nome do arquivo CSV gerado
CSV_FILE = "respostas_reais.csv"

# Dicionários para armazenar os dados
dados = defaultdict(list)
cpu_usage = []
memory_usage = []

# Ler os dados do CSV
with open(CSV_FILE, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho

    for row in reader:
        endpoint, tempo_resposta, uso_cpu, uso_memoria = row
        dados[endpoint].append(float(tempo_resposta))
        cpu_usage.append(float(uso_cpu))
        memory_usage.append(float(uso_memoria))

# Criar o gráfico de tempos de resposta
plt.figure(figsize=(12, 6))

for endpoint, tempos in dados.items():
    plt.hist(tempos, bins=20, alpha=0.7, label=endpoint, edgecolor="black")

plt.xlabel("Tempo de Resposta (s)")
plt.ylabel("Frequência")
plt.title("Distribuição dos Tempos de Resposta por Endpoint")
plt.legend()
plt.grid(True)
plt.show()

# Criar o gráfico de uso de CPU e Memória
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel("Teste")
ax1.set_ylabel("Uso da CPU (%)", color="tab:blue")
ax1.plot(cpu_usage, color="tab:blue", label="CPU (%)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()  # Criar um segundo eixo para memória
ax2.set_ylabel("Uso de Memória (%)", color="tab:red")
ax2.plot(memory_usage, color="tab:red", linestyle="dashed", label="Memória (%)")
ax2.tick_params(axis="y", labelcolor="tab:red")

plt.title("Uso da CPU e Memória Durante os Testes")
fig.tight_layout()
plt.show()
