import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from numpy import sin, cos, log, log10, exp, pi, tan, abs, sqrt
import os.path
import string

x = np.arange(-3*pi, 3*pi, 0.05)

# Todas as funções devem ser passadas nesta lista.
# As funções ainda são passadas de maneira estática, irei resolver isso
# por meio de um arquivo externo.
funcoes = [x, -x, x+2, -x+2, x-2, 2*x, -2*x, 2*x+2, -2*x-2, -3*x+2, x**2,
           -x**2, 2*x**2, x**2+1, x**2-1, x**2+3*x-2, -x**2-3*x+2, x**3,
           -x**3, log(x), 1/(sin(x)), exp(x), 1/(cos(x)),
           tan(x), 1/tan(x), exp(1)**-x, log10(x), log(x)/log(3),
           log(x**2), 1/log(x**2), sin(x)-cos(x), cos(x**2+3*x-2),
           x**4+3*x**2-x+1, 2*cos(2*pi*x+pi), -4*pi*sin(2*pi*x+pi),
           32*x, 9-x, 1-log(x), 3*x**2+3*x-3, x**3+tan(x), abs(x),
           9/x, x**-2, x**-3, x**-4, x**-5, sqrt(x), x**2+sqrt(x**3),
           1/sqrt(x), sqrt(2*pi)*exp(-x**2/2), (4*x**2)**(1/3),
           9*x**2-log10(x), x*sqrt((9-x)/(9+x)), -x*sqrt((9-x)/(9+x)),
           9/(x**2+9), cos(exp(x)), exp(cos(x)), 9*exp(-3*x),
           (pi*x**3)/(1-x**2), -x**2+pi, sin(cos(x))]

alfabeto = list(string.ascii_lowercase)
num_exercicio = 1
i_alfabet = 0

# Funções que precisam limitar o Eixo Y para ficarem mais visíveis
logaritimos = [19, 26, 27, 29]
trigonometricas = [20, 22, 23, 24]
outros = [39, 41, 42, 43, 44, 45, 52, 53, 58]

# Para cada função dentro da lista "funcoes" ele plota os gráficos
# e salva dentro da devida pasta.
for i in range(len(funcoes)):
    plt.grid(True)
    plt.plot(x, funcoes[i])

    # Limitando o Eixo Y dos logarítimos
    if (i in logaritimos):
        plt.ylim(-4, 4)

    # Limitando o Eixo Y das funções trigonométricas
    elif (i in trigonometricas):
        plt.ylim(-6, 6)

    elif (i in outros):
        plt.ylim(-12, 12)

    elif (i == 51):
        plt.ylim(0, 3)
        plt.xlim(0, 1)

    elif (i == 57):
        plt.ylim(0, 40)
        plt.xlim(-0.5, 2)

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
