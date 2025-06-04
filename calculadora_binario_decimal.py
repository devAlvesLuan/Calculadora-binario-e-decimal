import tkinter as tk # Importa a biblioteca Tkinter como tk, isso siginica que quando eu chamar a bilbioteca no código, eu apenas preciso digitar tk
from tkinter import messagebox # Da biblioteca tkinter, importei messagebox

# Função para calcular o número de decimal para binário
def calcula_decimal_binario(): 
    decimal = entrada.get() # Pega o valor da caixa de entrada e coloca numa variável
    binario = "" # Inicia a variável como uma string
    
    if decimal == "": # Erro caso a entrada esteja vazia
        messagebox.showerror("ERRO","Adicione um número")
    
    else:
        valor_decimal = int(decimal) # Se não estiver vazia, transforma a entrada como inteiro
    
    if valor_decimal > 0: # Analisar se o decimal não é 0
        while valor_decimal > 0: # Loop para continuar ate o valor decimal for maior que 0
            resto = valor_decimal%2 # Pega o resto do número para saber se é 0 ou 1
            
            binario = str(resto) + binario # Atualiza a variável colocando o ultimo valor a direita para ficar na ordem correta 
            
            valor_decimal = valor_decimal // 2 # Divide o valor_decimal (ignorando seu resto) até que fique menor que 0
    
    else:
        messagebox.showerror("ERRO","Insira um número válido") # Mensagem de erro caso seja um número menor que 0
        
    messagebox.showinfo("resultado",binario) # Apresenta uma caixa com o resultado 
        

# Função para calcular o número de binário para decimal
def calcula_binario_decimal():
    
    valor_binario = entrada.get() # Pega o valor da caixa de entrada e coloca numa variável
    decimal = 0 #   Iniciando a variável, pois irei acumlar valores nela
    indice = 0  #   Inicia o indíce em 0 para pegar o primeiro valor da array 
    
    if valor_binario == "": # Erro caso a entrada esteja vazia
        messagebox.showerror("ERRO","Adicione um número")
    
    
    if not all(c in ["0", "1"] for c in valor_binario): # Erro caso a entrada seja um número com outros digitos sem ser 0 e 1, ele percorre todo o valor_binario para saber se tem 0 e 1 dentro dele
        messagebox.showerror("ERRO", "Digite apenas 0 e 1") # Caso seja verdade, apresenta uma caixa de erro
        valor_binario = entrada.delete(0, tk.END) # Apaga o valor da entrada
        return

    for indice, digito in enumerate(reversed(valor_binario)): 
    # Pega o indice, e o digito da respectiva posição do array. O enumerate(reversed(binario) serve para localizar o indice e o valor do elemento, e o "reversed" inverte esses indices as posições dos valores
    
        decimal += int(digito) * (2**(indice))
        # Acumula o resultado para no final ter a soma total e descobrir qual é o respectivo número
        
    if valor_binario != "": # Caso a variável não seja vazia, apresenta o resultado
        messagebox.showinfo("resultado", decimal)
    
    

janela = tk.Tk() # Inicia o Tkinter 
janela.title("Calculadora binario <-> decimal") # Add o título
janela.geometry("500x350") # Ajustando o tamanho
janela.configure(background="#000") # Add cor de fundo

rotulo = tk.Label(janela, text="Bem-vindo a Calculadora binario <-> decimal!", font=("Arial", 14, "bold"), foreground="grey") # Rótulo apresentando a janela
rotulo.pack(pady=10) # Torna o rótulo visivél na janela e adiciona uma posição na reta Y

entrada = tk.Entry(janela, text="Digite o número: ", font=("Arial", 8) , foreground="#000", width=50) # Caixa de entrada do número
entrada.pack(pady=20) # Torna a caixa de texto visivél na janela e adicionauma posição na reta Y

botao_binario = tk.Button(janela, text="1. Transformar em binário", font=("Arial", 10), command=calcula_decimal_binario, width=50, height=2 ) # Criando um botão adicionando a função relativa a ele
botao_binario.pack(pady= 6) # Torna o botão visivél na janela e adiciona uma posição na reta Y

botao_decimal = tk.Button(janela, text="2. Transformar em decimal", font=("Arial", 10), command=calcula_binario_decimal, width=50, height=2 ) # Criando um botão adicionando a função relativa a ele
botao_decimal.pack() # Torna o botão visivél na janela



janela.mainloop() # Loop que faz a janela continuar aberta
        





