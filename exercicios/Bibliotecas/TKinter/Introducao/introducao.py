import tkinter as tk

r"""O pacote tkinter ("Ou Tk interface") é a interface padrão de Python para o toolkit Tcl\Tk.

- O Tcl consiste em uma linguagem interpretada, comumente embutida em aplicações C ou utilizada como
interface para o Tk toolkit. A biblioteca Tcl possui uma interface em C capaz de criar e administrar
várias instâncias do interpretador Tcl. Diferente de Python, sua execução é moldada em vista de multitasking
cooperativo, sendo algo aproveitado pelo Tkinter.

- O Tk é um pacote Tcl implementado em C que adiciona comandos personalizados para criar e manipular widgets. Cada
objeto Tk embui uma instância do interpretador com ele. Apesar da costumização avançada de recursos visuais, o Tk 
fornece um visual bem datado.

- O Ttk (Ou Tk temático) é uma família nova de widgets Tk que fornece um visual melhorado para diferentes plataformas.
Ttk é distribuído como parte do Tk (A partir da versão 8.5), sendo acessado pelo módulo 'tkinter.tkk'.

- Tanto o Tk como Ttk utilizam de facilidades do sistema operacional em que são executados, utilizando dispositivos,
frameworks e bibliotecas específicos de cada sistema.

- Ao criar um widget com esses pacotes, é enviada uma string de comando Tcl\Tk para um módulo binário do tkinter.
Esse módulo chama o interpretador Tcl para avaliar a situação, a fim de avaliar que chamadas realizar (Para Xlib, Cocoa
ou GDI)."""

root = tk.Tk()  # Inicializa janela principal do widget.

