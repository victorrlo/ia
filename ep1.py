#Exercício Prático 1 - Simulador e Agente Reativo Simples em Ambiente Parcialmente Observável
import random
import numpy as np
import time

def reactive_agent(row_size, column_size, cells, elapsed_time, score):
    
    #posição do agente inicial desconhecida:
    ini_row = 0#random.randint(0,row_size-1) 
    ini_col = 1#random.randint(0,column_size-1)

    #sensor do agente
    reactive_agent.sensor = cells[ini_row][ini_col]

    if(row_size == 1):
    
        for i in range(0,elapsed_time):

            #aleatoriedade de sujeira
            random_dust = random.randint(0,1)
            if random_dust == 1:
                cells[random.randint(0,row_size-1)][random.randint(0,column_size-1)] = 1

            #estado inicial
            print("Ambiente")
            print(cells)
            
            #operação de limpeza
            if(reactive_agent.sensor == 0):
                print("Célula limpa.")
                print("Procurando nova célula para limpar...")
                #time.sleep(5)
                print(cells)

            elif(reactive_agent.sensor == 1):
                print("Célula suja.")
                print("Limpando Célula do Ambiente...")
                #time.sleep(5)
                cells[ini_row][ini_col] = 0
                print("Limpeza finalizada!")
                score = score +1
                print(cells)

            else:
                print("ERRO! Célula com dados desconhecidos!")
                print(cells)

            #operação de movimento
            right = 0
            left = 0
        
            if((ini_col == 0 or ini_col+1 < column_size-1) and left == 0): #existe espaço para a direita
                if(ini_col < column_size-1):
                    right = 1
                    #movimento para a direita
                    ini_col = ini_col+1
                    reactive_agent.sensor = cells[ini_row][ini_col]
                else:
                    right = 0
                    print("posicao: ", ini_row, ini_col)
                    print("Agente no limite direito do ambiente")
            
            
            elif((ini_col == column_size-1) and right == 0): #não existe espaço para a direita
                left = 1
                if(ini_col > 0):
                    left = 1
                    #movimento para a esquerda
                    ini_col = ini_col-1
                    reactive_agent.sensor = cells[ini_row][ini_col]
                else:
                    left = 0
                    print("posicao: ", ini_row, ini_col)
                    print("Agente no limite esquerdo do ambiente")

            else: #saiu do ambiente
                print("ERRO! Posição impossível!")

                if(ini_col > column_size-1):
                        ini_col = ini_col-1

                elif(ini_col < 0):
                    ini_col = ini_col+1
        print("-----------------------------------------------------------")
    else:
        print("ERRO! Ambiente 3D! Projeto conta apenas com ambiente 2D!")
        
    return score
    
                             

#dimensões do ambiente
row_size = 1
column_size = 2 

#pontuação
score = 0

#tempo de simulação
elapsed_time = 1000

#células do ambiente inicializadas
cells = np.full((row_size, column_size), 0)

cells[0][0] = 1
cells[0][1] = 0

#simulação
score = reactive_agent(row_size, column_size, cells, elapsed_time, score)
print(score)
