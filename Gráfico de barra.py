# -*- coding: cp1252 -*-
from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

#barras possuem o tamanho padr�o de 0.8, ent�o adicionaremos 0.1 �s
#coordenadas � esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(movies)]

#as barras do gr�fico com as coordenadas x � esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel('# de premiacoes')
plt.title('Meus filmes favoritos')

#nomeia o eixo x com nomes de filmes na barra lateral
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()
