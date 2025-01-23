import includes

def ler_dados_arduino(arduino):
    cont = 0
    valores = [] 

    while cont < 5:
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
                        print(f"Valor recebido: {linha_decodificada}")
                    else:
                        print(f"Mensagem ignorada: {linha_decodificada}")
                except UnicodeDecodeError:
                    print(f"Erro de decodificação: {linha}")
        except Exception as e:
            print(f"Erro ao ler dados: {e}")
            break

    # Exibe os valores capturados no final
    if valores:
        includes.messagebox.showinfo("Valores Recebidos", f"Valores capturados: {valores}")
    else:
        includes.messagebox.showwarning("Aviso", "Nenhum valor foi recebido.")

def iniciar_arduino(arduino):
    try:
        # Envia o comando "START" para o Arduino
        arduino.write(b'START\n')
        
        includes.messagebox.showinfo("Informação", "Comando START enviado com sucesso!")
        
        # Inicia a leitura dos dados em uma thread separada
        thread_leitura = includes.Thread(target=ler_dados_arduino(arduino), daemon=True)
        thread_leitura.start()

    except Exception as e:
        includes.messagebox.showerror("Erro", f"Erro ao enviar comando: {e}")

def fechar_janela(arduino,root):
    arduino.close()
    root.destroy()

