# -*- coding: cp1252 -*-
from matplotlib import pyplot as plt


mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel('# de vezes que ouvimos alguem dizer "data science"')

# se você não fizer isso, matplotlib nomerá o eixo x de 0, 1

# e entao adiciona a +2.013e3 para fora do canto (matplotlib feio!)
plt.ticklabel_format(useOffset = False)

#enganar o eixo y mostra apenas a parce acima de 500
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Olhe o 'Grande' Aumento!")
plt.show()