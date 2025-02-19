import includes
import functions as f
import graph as g
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

# Configuração da porta serial
arduino = includes.serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

# Aguarda o Arduino inicializar
includes.time.sleep(2)

# Criação da janela principal
root = includes.tk.Tk()
root.title("Velocidade de Cubos em Queda Livre")
root.geometry("400x400")  # Ajustei para acomodar o gráfico

# Título
titulo = includes.tk.Label(root, text="Controle do Arduino", font=("Arial", 16))
titulo.pack(pady=10)

# Função para calcular e plotar gráficos
def calcular_e_plotar(valores):
    posicao = [0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90]
    # Gera uma lista de tempo com base no número de valores
    root.after(0, g.plotar_grafico_na_janela, valores, posicao, "Posição vs. Tempo", "Tempo (s)", "Posição (m)")
    print("Até aqui...")
    velocidades = f.calcular_velocidade(valores, posicao)
    print("Velocidades calculadas:", velocidades)
    root.after(0, g.plotar_grafico_na_janela_velocidade, valores[:-1], velocidades, "Velocidade vs. Tempo", "Tempo (s)", "Velocidade (m/s)")

# Botão START
def start_arduino():
    print("Iniciando leitura do Arduino...")
    valores = f.iniciar_arduino(arduino)
    if valores:
        print("Valores recebidos:", valores)
        calcular_e_plotar(valores)
    else:
        print("Nenhum valor recebido do Arduino.")

btn_start = includes.tk.Button(root, text="Start", command=start_arduino, font=("Arial", 14), bg="green", fg="white")
btn_start.pack(pady=10)

# Botão para fechar
btn_close = includes.tk.Button(root, text="Fechar", command=lambda: f.fechar_janela(arduino, root), font=("Arial", 12), bg="red", fg="white")
btn_close.pack(pady=10)

# Garante que o Arduino feche corretamente ao sair
root.protocol("WM_DELETE_WINDOW", lambda: f.fechar_janela(arduino, root))

# Executa o loop principal da interface gráfica
root.mainloop()