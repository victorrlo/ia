#Exercício Prático 1 - Simulador e Agente Reativo Simples em Ambiente Parcialmente Observável
import random
import numpy as np

def environment(row_size, column_size):
     #sujeira na célula do ambiente = 1
     #limpo = 0

    x = []
    y = []

    #initiate cells
    #randomize dust
    deck = list(range(0,100))
    cells = np.full((row_size, column_size), 0)
    for i in range(row_size):
        for j in range(column_size):
            random.shuffle(deck)
            c = deck.pop()
            if(c >= 50):
                cells[i][j] = 1
            elif(c < 50):
                cells[i][j] = 0
                
    return cells

print(environment(1, 2))
