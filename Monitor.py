import csv
import psutil
import time
import numpy as np

# Nome do arquivo CSV
CSV_FILE = "respostas_reais.csv"

# Número de testes por endpoint
num_testes = 100

# Lista de endpoints simulados
endpoints = ["play", "change", "load_playlist", "battery"]

# Criar o CSV e adicionar o cabeçalho
with open(CSV_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["endpoint", "tempo_resposta", "uso_cpu", "uso_memoria"])

# Loop para simular requisições e medir CPU/Memória
for _ in range(num_testes):
    for endpoint in endpoints:
        # Simulando tempos de resposta
        if endpoint == "play":
            tempo_resposta = np.random.normal(1.2, 0.3)
        elif endpoint == "change":
            tempo_resposta = np.random.normal(0.8, 0.2)
        elif endpoint == "load_playlist":
            tempo_resposta = np.random.normal(1.5, 0.4)
        elif endpoint == "battery":
            tempo_resposta = np.random.uniform(5, 15) / 100  # Convertendo para segundos

        # Medindo CPU e Memória antes da execução
        uso_cpu = psutil.cpu_percent(interval=0.1)  # Percentual de uso da CPU
        uso_memoria = psutil.virtual_memory().percent  # Percentual de uso da Memória RAM

        # Salvar os resultados no CSV
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([endpoint, tempo_resposta, uso_cpu, uso_memoria])

        # Pequena pausa para não sobrecarregar o sistema
        time.sleep(0.1)

print(f"Dados coletados e salvos em {CSV_FILE}")
