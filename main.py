import includes
import functions as f

# Configuração da porta serial
arduino = includes.serial.Serial(port='/dev/ttyUSB1', baudrate=9600, timeout=1)

# Aguarda o Arduino inicializar
includes.time.sleep(2)

# Criação da janela principal
root = includes.tk.Tk()
root.title("Controle do Arduino")
root.geometry("300x300")  # Tamanho da janela (largura x altura)

# Título
titulo = includes.tk.Label(root, text="Controle do Arduino", font=("Arial", 16))
titulo.pack(pady=10)

# Botão START
btn_start = includes.tk.Button(root, text="Start", command=lambda: f.iniciar_arduino(arduino), font=("Arial", 14), bg="green", fg="white")
btn_start.pack(pady=10)

# Botão para fechar
btn_close = includes.tk.Button(root, text="Fechar", command=lambda: f.fechar_janela(arduino, root), font=("Arial", 12), bg="red", fg="white")
btn_close.pack(pady=10)

# Executa o loop principal da interface gráfica
root.protocol("WM_DELETE_WINDOW", lambda: f.fechar_janela(arduino, root))  # Garante que o Arduino feche ao sair
root.mainloop()
