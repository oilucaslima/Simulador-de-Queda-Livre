import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

def plotar_grafico_na_janela_velocidade(x, y, titulo="Velocidade vs. Tempo", xlabel="Tempo (s)", ylabel="Velocidade (m/s)"):
   
    # Cria uma nova janela
    nova_janela = tk.Toplevel()
    nova_janela.title(titulo)
    nova_janela.geometry("600x400")

    x = np.array(x) / 1_000_000 
    fig, ax = plt.subplots(figsize=(5, 3))  
    ax.plot(x, y, marker='o', linestyle='-', color='b', label="Velocidade vs. Tempo")

    # Configurando o gráfico
    ax.set_title(titulo, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.grid(True)
    ax.legend()

    # Cria o canvas e adiciona o gráfico à interface
    canvas = FigureCanvasTkAgg(fig, master=nova_janela)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Inicia o loop da nova janela
    nova_janela.mainloop()

def plotar_grafico_na_janela(x, y, titulo="Gráfico", xlabel="Eixo X", ylabel="Eixo Y"):
    # Converte x de microssegundos para segundos (divide por 1.000.000)
    x = np.array(x) / 1_000_000  # Converte o tempo de microssegundos para segundos

    # Cria uma nova janela
    nova_janela = tk.Toplevel()
    nova_janela.title(titulo)
    nova_janela.geometry("600x400")

    # Plotando os dados originais
    fig, ax = plt.subplots(figsize=(5, 3))  
    ax.plot(x, y, marker='o', linestyle='None', color='b', label="Dados Originais")

    # Regressão polinomial de grau 2 (para modelar a queda livre)
    coef = np.polyfit(x, y, 2)  # Ajuste de um polinômio de grau 2 (quadrático)
    y_pred = np.polyval(coef, x)  # Calcula os valores ajustados pela regressão

    # Plota a curva ajustada (regressão quadrática)
    ax.plot(x, y_pred, color='r', linestyle='-', label="Regressão Quadrática")

    # Exibe os coeficientes da equação ajustada
    coef_text = f"s = {coef[0]:.2e} t² + {coef[1]:.2e} t + {coef[2]:.2e}"
    ax.text(0.05, 0.9, coef_text, transform=ax.transAxes, fontsize=10, color="red")

    # Configurando o gráfico
    ax.set_title(titulo, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.grid(True)
    ax.legend()

    # Cria o canvas e adiciona o gráfico à interface
    canvas = FigureCanvasTkAgg(fig, master=nova_janela)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Inicia o loop da nova janela
    nova_janela.mainloop()

