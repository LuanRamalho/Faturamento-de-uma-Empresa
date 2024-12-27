import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Função para exibir o gráfico de faturamento
def mostrar_grafico():
    try:
        # Coletar os valores digitados
        faturamentos = [float(entry.get()) for entry in entradas]
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        # Criar gráfico
        plt.figure(figsize=(10, 6))
        bars = plt.bar(meses, faturamentos, color='skyblue', edgecolor='blue')
        plt.title("Faturamento Mensal da Empresa", fontsize=16, color='darkblue')
        plt.xlabel("Meses", fontsize=12)
        plt.ylabel("Faturamento (R$)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Adicionar os valores no topo das barras
        for bar, faturamento in zip(bars, faturamentos):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, 
                     f"{faturamento:.2f}", ha='center', fontsize=10, color='black')

        plt.tight_layout()
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos em todas as caixas de texto.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Faturamento Anual da Empresa")
janela.geometry("500x600")
janela.configure(bg="lightblue")

# Título
titulo = tk.Label(janela, text="Faturamento Anual", font=("Helvetica", 16, "bold"), bg="lightblue", fg="darkblue")
titulo.pack(pady=10)

# Criando os campos de entrada para os meses
entradas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for mes in meses:
    frame = tk.Frame(janela, bg="lightblue")
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=f"{mes}:", font=("Helvetica", 12), bg="lightblue")
    label.pack(side=tk.LEFT, padx=5)
    
    entry = tk.Entry(frame, width=20, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT)
    entradas.append(entry)

# Botão para mostrar o gráfico
botao = tk.Button(janela, text="Mostrar Gráfico", font=("Helvetica", 14), bg="darkblue", fg="white", command=mostrar_grafico)
botao.pack(pady=20)

# Executar a janela
janela.mainloop()
