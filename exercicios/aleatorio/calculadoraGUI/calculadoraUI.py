import tkinter as tk

expressao = ""

def digitaExpressao(caractere):
    global expressao
    expressao += str(caractere)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, expressao)

def confirmaExpressao():
    global expressao
    try:
        expressao = str(eval(expressao))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, expressao)
    except:
        limpaCampo()
        text_result.insert(1.0, "Erro")
        pass

def limpaCampo():
    global expressao
    expressao = ""
    text_result.delete(1.0, "end")
    pass

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

botao1 = tk.Button(root, text="1", command=lambda: digitaExpressao(1), width=5, font=("Arial", 14))
botao1.grid(row=2, column=1)

botao2 = tk.Button(root, text="2", command=lambda: digitaExpressao(2), width=5, font=("Arial", 14))
botao2.grid(row=2, column=2)

botao3 = tk.Button(root, text="3", command=lambda: digitaExpressao(3), width=5, font=("Arial", 14))
botao3.grid(row=2, column=3)

botao4 = tk.Button(root, text="4", command=lambda: digitaExpressao(4), width=5, font=("Arial", 14))
botao4.grid(row=2, column=4)

botao5 = tk.Button(root, text="5", command=lambda: digitaExpressao(5), width=5, font=("Arial", 14))
botao5.grid(row=3, column=1)

botao6 = tk.Button(root, text="6", command=lambda: digitaExpressao(6), width=5, font=("Arial", 14))
botao6.grid(row=3, column=2)

botao7 = tk.Button(root, text="7", command=lambda: digitaExpressao(7), width=5, font=("Arial", 14))
botao7.grid(row=3, column=3)

botao8 = tk.Button(root, text="8", command=lambda: digitaExpressao(8), width=5, font=("Arial", 14))
botao8.grid(row=3, column=4)

botao9 = tk.Button(root, text="9", command=lambda: digitaExpressao(9), width=5, font=("Arial", 14))
botao9.grid(row=4, column=1)

botao0 = tk.Button(root, text="0", command=lambda: digitaExpressao(0), width=5, font=("Arial", 14))
botao0.grid(row=4, column=2)

botaoMais = tk.Button(root, text="+", command=lambda: digitaExpressao("+"), width=5, font=("Arial", 14))
botaoMais.grid(row=4, column=3)

botaoMenos = tk.Button(root, text="-", command=lambda: digitaExpressao("-"), width=5, font=("Arial", 14))
botaoMenos.grid(row=4, column=4)

botaoVezes = tk.Button(root, text="*", command=lambda: digitaExpressao("*"), width=5, font=("Arial", 14))
botaoVezes.grid(row=5, column=1)

botaoDivide = tk.Button(root, text="/", command=lambda: digitaExpressao("/"), width=5, font=("Arial", 14))
botaoDivide.grid(row=5, column=2)

botaoPrnts1 = tk.Button(root, text="(", command=lambda: digitaExpressao("("), width=5, font=("Arial", 14))
botaoPrnts1.grid(row=5, column=3)

botaoPrnts2 = tk.Button(root, text=")", command=lambda: digitaExpressao(")"), width=5, font=("Arial", 14))
botaoPrnts2.grid(row=5, column=4)

botaoLimpa = tk.Button(root, text="C", command=limpaCampo, width=5, font=("Arial", 14))
botaoLimpa.grid(row=6, column=1)

botaoIgual = tk.Button(root, text="=", command=confirmaExpressao, width=5, font=("Arial", 14))
botaoIgual.grid(row=6, column=2)

root.mainloop()

