import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from numpy import sin, cos, log, log10, exp, pi, tan
import os.path
import string

x = np.arange(-2*pi, 2*pi, 0.1)

# Todas as funções devem ser passadas nesta lista
# As funções ainda são passadas de maneira estática, mas irei resolver isso
# por meio de um arquivo externo.
funcoes = [x, -x, x+2, -x+2, x-2, 2*x, -2*x, 2*x+2, -2*x-2, -3*x+2, x**2,
           -x**2, 2*x**2, x**2+1, x**2-1, x**2+3*x-2, -x**2-3*x+2, x**3,
           -x**3, log(x), 1/(sin(x)), exp(x), 1/(cos(x)),
           tan(x), 1/tan(x), exp(1)**-x, log10(x)]
alfabeto = list(string.ascii_lowercase)
num_exercicio = 1
i_alfabet = 0

# Para cada função dentro da lista "funcoes" ele plota os gráficos
# e salva dentro da devida pasta.
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

    # Verifica se o diretório existe, se não, ele cria um com o nome
    # atual do exercicio EX: Exercicio 2
    if (not os.path.exists(diretorio)):
        Path.mkdir(Path(diretorio))
    plt.savefig(diretorio + "/" + nome_arquivo)

    plt.close()
    print(nome_arquivo)
    if (i_alfabet == 25):
        i_alfabet = 0
        num_exercicio += 1
    else:
        i_alfabet += 1
