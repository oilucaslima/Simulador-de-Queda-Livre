import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plotar_grafico_na_janela(root, x, y, titulo="Gráfico", xlabel="Eixo X", ylabel="Eixo Y"):
    """
    Função para criar e exibir um gráfico dentro de uma janela Tkinter.
    
    Args:
        root (tk.Tk): A janela principal do Tkinter onde o gráfico será inserido.
        x (list): Dados do eixo X.
        y (list): Dados do eixo Y.
        titulo (str): Título do gráfico.
        xlabel (str): Rótulo do eixo X.
        ylabel (str): Rótulo do eixo Y.
    """
    fig, ax = plt.subplots(figsize=(6, 4))  # Tamanho do gráfico
    ax.plot(x, y, marker='o', linestyle='-', color='b', label="Dados")
    ax.set_title(titulo, fontsize=14)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True)  # Adiciona uma grade
    ax.legend()  # Adiciona uma legenda

    # Cria um canvas para embutir o gráfico na janela Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)  
    canvas.draw()  # Atualiza o gráfico
    canvas.get_tk_widget().pack()  # Adiciona o gráfico à janela principal
