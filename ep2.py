#Exercício Prático 2
import random
import numpy as np
import time

def reactive_agent_half_blind(row_size, column_size, elapsed_time):
    
    score = 0
    
    #posição do agente inicial desconhecida:
    ini_row = random.randint(0,row_size-1) 
    ini_col = random.randint(0,column_size-1)
    
    #células do ambiente inicializadas
    cells = np.full((row_size, column_size), 0)

    if(row_size == 1):
        
        right = 0
        left = 0
    
        for i in range(0,elapsed_time):

            #aleatoriedade de sujeira
            random_dust = random.randint(0,1)
            if random_dust == 1:
                cells[random.randint(0,row_size-1)][random.randint(0,column_size-1)] = 1
                
            #testar se sempre limpa quando está sujo
            
            #for j in range(0, column_size):
                #cells[0][j] = 1
                #print("Sujeira", cells)
            
            #sensor
            reactive_agent.sensor = cells[ini_row][ini_col]

            #estado inicial
            print("Ambiente")
            print(cells)
            
            #operação de limpeza
            if(reactive_agent.sensor == 0):
                print("posição: ", ini_row, ini_col)
                print("Célula limpa.")
                print("Procurando nova célula para limpar...")

            elif(reactive_agent.sensor == 1):
                print("posição: ", ini_row, ini_col)
                print("Célula suja.")
                print("Limpando Célula do Ambiente...")
                cells[ini_row][ini_col] = 0
                print("Limpeza finalizada!")
                score = score +1
                print(cells)

            else:
                print("ERRO! Célula com dados desconhecidos!")
                print(cells)
            
            #limites do ambiente
            if(ini_col+1 == column_size):
                    right = 0
                    left = 1
            elif(ini_col-1 < 0):
                    left = 0
                    right = 1
                    
            #operação de movimento
            if(left == 0):
                if(ini_col < column_size-1):
                    ini_col = ini_col+1
                    score = score-1

                    
            elif(right == 0):
                if(ini_col > 0):
                    ini_col = ini_col-1
                    score = score-1
                
                
            print("-----------------------------------------------------------")
    else:
        print("ERRO! Ambiente 3D! Projeto conta apenas com ambiente 2D!")
        
    
    return score
    

    
def reactive_agent_bulls_eye(row_size, column_size, elapsed_time):
    
    score = 0
    
    #posição do agente inicial desconhecida:
    ini_row = random.randint(0,row_size-1) 
    ini_col = random.randint(0,column_size-1)
    
    #células do ambiente inicializadas
    cells = np.full((row_size, column_size), 0)
    
    
    environment_state = np.full((row_size, column_size), 0)

    if(row_size == 1):
        
        right = 0
        left = 0
    
        for i in range(0,elapsed_time):

            #aleatoriedade de sujeira
            random_dust = random.randint(0,1)
            if random_dust == 1:
                cells[random.randint(0,row_size-1)][random.randint(0,column_size-1)] = 1
                
            #testar se sempre limpa quando está sujo
            
            #for j in range(0, column_size):
                #cells[0][j] = 1
                #print("Sujeira", cells)
                
                
            #estado inicial
            print("Ambiente")
            print(cells)
            
            #sensor
            for i in range(1):
                for j in range(2):
                    if cells[i][j] == 0:
                        #noop
                        print("Nada para fazeeeer")
                        
                    elif cells[i][j] == 1:
                            
                            if ini_col != j:
                                ini_col = j
                                score = score-1
                            else:
                                #noop
                                ini_col = ini_col
                            
                            #limites do ambiente
                            if ini_col > 1:
                                ini_col = 1                  
                            elif ini_col < 0:
                                ini_col = 0
                        
                            print("posição: ", ini_row, ini_col)
                            print("Célula suja.")
                            print("Limpando Célula do Ambiente...")
                            cells[ini_row][ini_col] = 0
                            print("Limpeza finalizada!")
                            score = score +1
                
                
            print("-----------------------------------------------------------")
    else:
        print("ERRO! Ambiente 3D! Projeto conta apenas com ambiente 2D!")
        
    
    return score    
