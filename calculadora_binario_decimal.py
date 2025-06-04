import tkinter as tk
from tkinter import messagebox


def calcula_decimal_binario():
    decimal = entrada.get()
    binario = ""
    
    if decimal == "":
        messagebox.showerror("ERRO","Adicione um número")
    
    else:
        valor_decimal = int(decimal)
    
    if valor_decimal > 0:
        while valor_decimal > 0:
            resto = valor_decimal%2 # pega o resto do número para saber se é 0 ou 1
            
            binario = str(resto) + binario
            
            valor_decimal = valor_decimal // 2
    
    else:
        messagebox.showerror("ERRO","Insira um número válido")
        
    messagebox.showinfo("resultado",binario)
        
    return binario


def calcula_binario_decimal():
    
    valor_binario = entrada.get()
    decimal = 0 #   INICALIZANDO A VARIÁVEL, pois irei acumlar valores nela
    indice = 0  #   INICIA O INDICE EM 0 PARA PEGAR O PRIMEIRO VALOR DA ARRAY
    
    if valor_binario == "":
        messagebox.showerror("ERRO","Adicione um número")
    
    
    if not all(c in ["0", "1"] for c in valor_binario):
        messagebox.showerror("ERRO", "Digite apenas 0 e 1")
        valor_binario = entrada.delete(0, tk.END)
        return

    for indice, digito in enumerate(reversed(valor_binario)): 
    # Pega o indice, e o digito da respectiva posição do array. O enumerate(reversed(binario) serve para localizar o indice e o valor do elemento, e o "reversed" inverte esses indices as posições dos valores
    
        decimal += int(digito) * (2**(indice))
        # Acumula o resultado para no final ter a soma total e descobrir qual é o respectivo número
        
    if valor_binario != "":
        messagebox.showinfo("resultado", decimal)
    
    
    return decimal
    

janela = tk.Tk()
janela.title("Calculadora binario <-> decimal")
janela.geometry("500x350")
janela.configure(background="#000")

rotulo = tk.Label(janela, text="Bem-vindo a Calculadora binario <-> decimal!", font=("Arial", 14, "bold"), foreground="grey")
rotulo.pack(pady=10)

entrada = tk.Entry(janela, text="Digite o número: ", font=("Arial", 8) , foreground="#000", width=50)
entrada.pack(pady=20)

botao_binario = tk.Button(janela, text="1. Transformar em binário", font=("Arial", 10), command=calcula_decimal_binario, width=50, height=2 )
botao_binario.pack(pady= 6)

botao_decimal = tk.Button(janela, text="2. Transformar em decimal", font=("Arial", 10), command=calcula_binario_decimal, width=50, height=2 )
botao_decimal.pack()


janela.mainloop()   
        





