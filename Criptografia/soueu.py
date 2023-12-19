import sys
import random
#este é o algoritmo de euclides padrão
def euclides(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
#este é o algoritmo de euclides estendido
def euclidesEstendido(a,b):
    s,t,x,y = 1,0,0,1
    while b != 0:
        c = a % b
        q = a // b
        i = s - (q * x)
        j = t - (q * y)
        a,b = b,c
        s,t = x,y
        x,y = i,j
        
    return(a,s,t)
#este é o algoritmo do inverso multiplicativo
def inversoMultiply(a,n):
    (m,s,t) = euclidesEstendido(a,n)
    if m == 1:
        if t >= 0:
            return t
        else:
            return n + t 
    else:
        return -1 # retorna "falha"  

def main():
    pessoa = sys.argv[1] # pessoa = é quem vai ter as tarefas executadas

    if pessoa == "F": # Fábio
        
        entrada = input()
        lista = entrada.split(" ")
        tarefa = lista[0]

        #Valores padrões de falha
        n = -1
        s = -1
        r = -1

        while tarefa != "T": #Enquanto não terminamos as nossas instruções
            
            if tarefa == "I": # Tarefa: Identificar
                n = int(lista[1])
                s = int(lista[2])
                v = int(lista[3])

                continha = ((s**2) % n * v) % n 
                
                if (continha == 1):
                    print("C")
                else:
                    print("E")
            
            elif tarefa == "X": # Tarefa: Iniciar  
                if (n == -1): # Tarefa não pode ser executada
                    print("E")
                else:
                    r = random.randint(1,n)
                    #mdc entre r e n tem que dar 1
                    mdc = euclides(r,n)
                    #enquanto não der 1 no mdc, gera de novo
                    while (mdc != 1):
                        r = random.randint(1,n)
                        mdc = euclides(r,n)
                    x = (r**2) % n
                    print("C",x)

            elif tarefa == "P": #Tarefa: Preparar
                if (n == -1): # Tarefa não pode ser executada
                    print("E")
                else:
                    r = int(lista[1])
                    x = (r**2) % n
                    print("C",x)

            elif tarefa == "R": #Tarefa: Responder
                #Se um dos elementos não estiverem lá, não dá pra executar a tarefa
                if (n == - 1) or (r == - 1) or (s == - 1): 
                    print("E")
                else:    
                    bit = int(lista[1])
                    if bit == 0:
                        bitX = r
                        print("C",bitX)
                    elif bit == 1:
                        bitX = (r * s) % n
                        print("C",bitX)
                    else:
                        print("E")

            #Pegando a próxima tarefa ...
            entrada = input()
            lista = entrada.split(" ")
            tarefa = lista[0]

        #reconhece T, sai do while, fecha o programa
        print("C")

    if pessoa == "P": #Patrícia

        entrada = input()
        lista = entrada.split(" ")
        tarefa = lista[0]

        #Valores padrões de falha
        n = -1
        v = -1
        r = -1
        t = -1
        x = -1
        t2 = -1

        while tarefa != "T": # Enquanto não terminamos ...
            if tarefa == "I": # Tarefa: Iniciar
                n = int(lista[1])
                v = int(lista[2])
                t = int(lista[3])
                t2 = t

                if (t >= 3 and t <= 50 and n > v):
                    print("C")
                else:
                    print("E")
            
            elif tarefa == "Q": #Tarefa: Recebe Compromisso
                if (n == -1): # Tarefa não pode ser executada
                    print("E")
                x = int(lista[1])
                bit = random.randint(0,1)
                if (x > n):
                    x = -1
                    print("E")
                else: 
                    print("C",bit)

            elif tarefa == "V": #Tarefa: Validar Resposta
                if (x == -1 or t == 0):
                    print("E")
                    
                bitX = int(lista[1])
                #Se bit == 0, bitX == r e se r^2 == x
                #Se bit == 1, bitX == y e se v * y^2 == x
                if bit == 0:
                    r = bitX
                    if ((r**2)% n == x):
                        t -= 1
                        print("C",t)                        
                    else:
                        print("E",t)
                        t = t2
                        #reinicia o contador
                else:
                    y = bitX
                    if ((v * (y**2)) % n == x ):
                        t -= 1
                        print("C",t)
                    else:
                        print("E",t)
                        t = t2
                        #reinicia o contador

            elif tarefa == "C": #Testa compromisso
                if (n == -1):
                    print("E")

                x = int(lista[1])
                bit = int(lista[2])
                bitX = int(lista[3])

                if bit == 0: 
                    r = bitX
                    if ((r**2)% n == x): #Deu certo
                        t -= 1
                        print("C",t)                        
                    else:
                        print("E",t)
                        t = t2
                        #reinicia o contador
                else:
                    y = bitX
                    if ((v * (y**2)) % n == x ):
                        t -= 1
                        print("C",t)
                    else:
                        print("E",t)
                        t = t2
                        #reinicia o contador
            
            #Recebendo novas tarefas...
            entrada = input()
            lista = entrada.split(" ")
            tarefa = lista[0] 

        #reconhece T, sai do while, fecha o programa
        print("C")
        
    if pessoa == "T":
        entrada = input()
        lista = entrada.split(" ")
        tarefa = lista[0]
        
        #Valores padrão de erro
        n = -1
        p = -1
        q = -1
        
        while tarefa != "T":# Enquanto não terminamos
            if tarefa == "I":# Tarefa: Iniciar
                p = int(lista[1])
                q = int(lista[2])
                if (p < 0 or q < 0):
                    print("E")
                else:    
                    n = p*q
                    print("C",n)
                    
            elif tarefa == "A":
                # X : Não fiz
                pass
            elif tarefa == "F":
                # X : Não fiz
                pass    

        #Recebendo novas tarefas...            
            entrada = input()
            lista = entrada.split(" ")
            tarefa = lista[0] 

        #reconhece T, sai do while, fecha o programa
        print("C")            

    if pessoa == "E":
        entrada = input()
        lista = entrada.split(" ")
        tarefa = lista[0]

        #Valores padrão de erro
        n = -1
        v = -1

        while tarefa != "T":# Enquanto não terminamos
            if tarefa == "I":# Tarefa: Iniciar
                n = int(lista[1])
                v = int(lista[2])
                if (n < 0 or v > n):
                    print("E")
                else:    
                    print("C")

            elif tarefa == "P":
                # X : Não fiz
                pass
            elif tarefa == "S":
                # X : Não fiz
                pass                     

        #Recebendo novas tarefas...
        entrada = input()
        lista = entrada.split(" ")
        tarefa = lista[0] 

        #reconhece T, sai do while, fecha o programa
        print("C")
main()