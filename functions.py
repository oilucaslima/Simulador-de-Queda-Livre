import includes
import sys

def ler_dados_arduino(arduino):
    cont = 0
    valores = [] 

    while cont < 7:
        try:
            linha = arduino.readline()
            if linha:
                try:
                    # Decodifica a linha e remove espaços em branco
                    linha_decodificada = linha.decode('utf-8').strip()
                    # Filtra apenas os valores numéricos
                    if linha_decodificada.isdigit():
                        valores.append(int(linha_decodificada))
                        cont += 1
                        #print(f"Valor recebido: {linha_decodificada}")
                    else:
                        print(f"Mensagem ignorada: {linha_decodificada}")
                except UnicodeDecodeError:
                    print(f"Erro de decodificação: {linha}")
        except Exception as e:
            print(f"Erro ao ler dados: {e}")
            break

    # Exibe os valores capturados no final
    if valores:
        #includes.messagebox.showinfo("Valores Recebidos", f"Valores capturados: {valores}")
        return valores
    else:
        #includes.messagebox.showwarning("Aviso", "Nenhum valor foi recebido.")
        return None

def iniciar_arduino(arduino):
    try:
        # Envia o comando "START" para o Arduino
        arduino.write(b'START\n')
        includes.messagebox.showinfo("Informação", "Comando START enviado com sucesso!")
        resultado = ler_dados_arduino(arduino)
        return resultado
    except Exception as e:
        includes.messagebox.showerror("Erro", f"Erro ao enviar comando: {e}")
        return None

def calcular_velocidade(tempo, posicao):
    velocidades = []
    for i in range(1, len(tempo)):
        delta_tempo = tempo[i] / 1_000_000 
        delta_posicao = posicao[i]
        if delta_tempo != 0:
            velocidade = delta_posicao / delta_tempo
        else:
            velocidade = 0
        velocidades.append(velocidade)
    return velocidades

def fechar_janela(arduino, root):
    print("Fechando a janela...")
    if arduino.is_open:
        print("Fechando a porta serial...")
        arduino.close()
    print("Fechando a aplicação Tkinter...")

    # Aguarda um tempo antes de fechar a interface
    root.after(100, lambda: root.destroy())  # Aguarda 100ms para finalizar a operação antes de fechar
    print("Aplicação encerrada.")
    sys.exit()  # Após 100ms, encerra completamente o programa