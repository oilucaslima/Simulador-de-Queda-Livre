import includes
import functions as f
import matplotlib.pyplot as plt
import graph as g
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Botão START
def start_arduino():
    valores = f.iniciar_arduino(arduino)
    if valores:
        tempo = list(range(len(valores)))  # Gera uma lista de tempo com base no número de valores
        g.plotar_grafico_na_janela(root, tempo, valores, titulo="Posição vs. Tempo", xlabel="Tempo (s)", ylabel="Posição (m)")

btn_start = includes.tk.Button(root, text="Start", command=start_arduino, font=("Arial", 14), bg="green", fg="white")
btn_start.pack(pady=10)

# Botão para fechar
btn_close = includes.tk.Button(root, text="Fechar", command=lambda: f.fechar_janela(arduino, root), font=("Arial", 12), bg="red", fg="white")
btn_close.pack(pady=10)

# Garante que o Arduino feche corretamente ao sair
root.protocol("WM_DELETE_WINDOW", lambda: f.fechar_janela(arduino, root))

# Executa o loop principal da interface gráfica
root.mainloop()