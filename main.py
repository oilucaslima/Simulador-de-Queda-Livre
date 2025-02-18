import includes
import functions as f
import graph as g
import matplotlib.pyplot as plt
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
    tempo = f.iniciar_arduino(arduino)
    if tempo:
        posicao = [0,0.15,0.30,0.45,0.60,0.75,0.90]
        # Gera uma lista de tempo com base no número de valores
        g.plotar_grafico_na_janela(tempo, posicao, titulo="Posição vs. Tempo", xlabel="Tempo (s)", ylabel="Posição (m)")

        velocidades = f.calcular_velocidade(tempo, posicao)
        print("Velocidades calculadas:", velocidades)
        g.plotar_grafico_na_janela_velocidade(tempo, velocidades, titulo="Velocidade vs. Tempo", xlabel="Tempo (s)", ylabel="Velocidade (m/s)")

        #includes.messagebox.showinfo("Velocidades Calculadas", f"Velocidades calculadas: {velocidades}")

btn_start = includes.tk.Button(root, text="Start", command=start_arduino, font=("Arial", 14), bg="green", fg="white")
btn_start.pack(pady=10)

# Botão para fechar
btn_close = includes.tk.Button(root, text="Fechar", command=lambda: f.fechar_janela(arduino, root), font=("Arial", 12), bg="red", fg="white")
btn_close.pack(pady=10)

# Garante que o Arduino feche corretamente ao sair
root.protocol("WM_DELETE_WINDOW", lambda: f.fechar_janela(arduino, root))

# Executa o loop principal da interface gráfica
root.mainloop()