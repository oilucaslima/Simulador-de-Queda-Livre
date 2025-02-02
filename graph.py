import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plotar_grafico_na_janela(root, x, y, titulo="Gráfico", xlabel="Eixo X", ylabel="Eixo Y"):
    """
    Função para criar e exibir um gráfico dentro da interface Tkinter.
    """
    root.title("Gráfico de Queda Livre")
    fig, ax = plt.subplots(figsize=(5, 5))  
    ax.plot(x, y, marker='o', linestyle='-', color='b', label="Posição vs. Tempo")
    ax.set_title(titulo, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.grid(True)
    ax.legend()

    # Cria o canvas e adiciona o gráfico à interface
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criando a interface gráfica
# root = tk.Tk()
# root.title("Gráfico de Queda Livre")

# # Dados experimentais de posição vs. tempo
# tempo = [0, 1, 2, 3, 4, 5]  # Tempo em segundos
# posicao = [100, 80, 50, 20, 0, -30]  # Posição em metros

# # Chamando a função para exibir o gráfico
# plotar_grafico_na_janela(root, tempo, posicao, titulo="Posição vs. Tempo", xlabel="Tempo (s)", ylabel="Posição (m)")

# # Iniciando o loop do Tkinter
# root.mainloop()
