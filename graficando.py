import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from numpy import sin, cos, log, log10, exp, pi, tan
import os.path
import string

x = np.arange(-2*pi, 2*pi, 0.1)
funcoes = [x, -x, x+2, -x+2, x-2, 2*x, -2*x, 2*x+2, -2*x-2, -3*x+2, x**2,
           -x**2, 2*x**2, x**2+1, x**2-1, x**2+3*x-2, -x**2-3*x+2, x**3,
           -x**3, log(x), 1/(sin(x)), exp(x), 1/(cos(x)),
           tan(x), 1/tan(x), exp(1)**-x, log10(x)]
alfabeto = list(string.ascii_lowercase)
num_exercicio = 1
i_alfabet = 0

for i in range(len(funcoes)):
    plt.grid(True)
    plt.plot(x, funcoes[i])
    if (i == 20 or i == 22 or i == 24):
        plt.ylim(-4, 4)
    elif (i == 19):
        plt.ylim(-5, 5)
    elif (i == 23):
        plt.ylim(-6, 6)
    plt.xlabel("X")
    plt.ylabel("Y")

    nome_arquivo = "Exercicio " + str(num_exercicio) + alfabeto[i_alfabet]
    plt.title(nome_arquivo)
    diretorio = "./Exercicio %i" % (num_exercicio)

    if (not os.path.exists(diretorio)):
        Path.mkdir(Path(diretorio))
    plt.savefig(diretorio + "/" + nome_arquivo)

    plt.close()
    print(i_alfabet)
    if (i_alfabet == 25):
        i_alfabet = 0
        num_exercicio += 1
    else:
        i_alfabet += 1
