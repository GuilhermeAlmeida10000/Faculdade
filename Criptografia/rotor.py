# A biblioteca sys é importada para trabalharmos com entradas no terminal em Python 
import sys
# Função para printar a matriz
def matrizPrint(rotor):
    for i in range(256):
        print(rotor[i], end=" ")
        if (i % 16 == 15):
            print("\n")

def main ():
    # Declaração de variáveis
    palavras = []           #equivalente a frase
    intervalo_simbolos = [] #equivalente ao l
    posicoes_simbolos = []  #equivalente ao k
    vetorTamk = []          #equivalente ao tamk
    vetor_t = []
    entrada = sys.argv[-2]
    saida = sys.argv[-1]
    modo = sys.argv[1]
    num_rotores = int(sys.argv[2])
    for i in range(num_rotores):
        palavras.append(sys.argv[3+i])
        intervalo_simbolos.append(int(sys.argv[3 + num_rotores+(i*2)]))
        posicoes_simbolos.append(int(sys.argv[4+num_rotores+(i*2)]))
    
    #Vamos colocar aqui todas as informações da nossa instrução
    if (modo == "C") or (modo == "D"):
        print(f"{modo}, {num_rotores}, {intervalo_simbolos}, {posicoes_simbolos}")

    #Estruturando o nosso vetor de rotores e o vetor_t
    rotores = [[0] * 256, [0] * 256, [0] * 256, [0] * 256, [0] * 256]
    vetor_t = [[0] * 256, [0] * 256, [0] * 256, [0] * 256, [0] * 256]

    # For para pegar o tamanho das palavras
    for y in range(len(palavras)):
        tamk = len(palavras[y])
        vetorTamk.append(tamk)

        # For para pegar o char de cada letra e armazena em vetor_t
        for i in range(tamk):
            vetor_t[y][i] = ord(palavras[y][i])    
    
    # For para inicializar a matriz de rotores com 0 a 255, baseado na qtd de rotores
    for y in range(num_rotores):
        for i in range(255):
            rotores[y][i] = i

    j = 0
    #Inicializando os rotores
    for y in range(num_rotores): 
        for i in range(255):
            j = (j + rotores[y][i] + vetor_t[y][i % vetorTamk[y]]) % 256
            temp = rotores[y][i]
            temp2 = rotores[y][j]
            rotores[y][i] = temp2
            rotores[y][j] = temp
    
    #Estruturando os vetores para contabilizar as letras já cifradas e os giros de cada rotor
    qtd_letras_cifradas = [0, 0, 0, 0, 0]  
    qtd_giros_rotor = [0, 0, 0, 0, 0]

    #Modo: Criptografia
    if (modo == 'C'):
        arquivo_saidaC = open(saida, "w+")
        
        for i in range(num_rotores):
            print(f"Rotor: {i}")
            matrizPrint(rotores[i])

        try: #Abrindo nosso arquivo
            with open (entrada, "r") as arquivo_entrada:
                while True:
                    elemento = arquivo_entrada.read(1) # Elemento: cada "número" que é lido do
                                                       # arquivo de entrada (000 a 255)                  
                    if not elemento:
                        break
                    
                    # Transformando em inteiro
                    elemento = ord(elemento)
                    
                    for i in range(num_rotores):
                        # Quando a quantidade de letras for igual ao intervalo colocado,
                        # os giros serão contabilizados
                        if (qtd_letras_cifradas[i] == intervalo_simbolos[i]):
                            qtd_letras_cifradas[i] = 0
                            qtd_giros_rotor[i] += posicoes_simbolos[i]
                            qtd_giros_rotor[i] = qtd_giros_rotor[i] % 256

                        # Somamos o elemento com a quantidade de giros que o rotor já teve
                        elemento = (elemento + qtd_giros_rotor[i]) % 256

                        # E passamos ele pelo rotor, pra acontecer a cifra
                        elemento = rotores[i][elemento]

                        qtd_letras_cifradas[i] += 1
                    
                    #Máscara para a impressão dos nossos elementos
                    if (elemento <= 9):
                        elemento = "00" + str(elemento)

                    elif (elemento <= 99):
                        elemento = "0" + str(elemento)
                    
                    else:
                        elemento = str(elemento)

                    arquivo_saidaC.write(elemento)

        except EOFError:
            pass
    
    else: #Modo Descriptografia 
        arquivo_saidaD = open(saida, "w+", encoding="utf-8")

        rotoresD = [[0] * 256, [0] * 256, [0] * 256, [0] * 256, [0] * 256]

        # Permutação para a descriptografia
        for i in range(num_rotores):
            for j in range(256):
                auxiliar = rotores[i][j]
                rotoresD[i][auxiliar] = j

        for i in range(num_rotores):
            print(f"Rotor: {i}")
            matrizPrint(rotoresD[i])

        try:
            with open (entrada, "r") as arquivo_entrada:
                while True:
                    elemento = arquivo_entrada.read(3) # Elemento: cada "número" que é lido do
                                                       # arquivo de entrada (000 a 255)
                    if not elemento:
                        break

                    # Transformando em inteiro
                    elemento = int(elemento)

                    for i in range(num_rotores-1, -1, -1):
                        # Quando a quantidade de letras for igual ao intervalo colocado,
                        # os giros serão contabilizados
                        if (qtd_letras_cifradas[i] == intervalo_simbolos[i]):
                            qtd_letras_cifradas[i] = 0
                            qtd_giros_rotor[i] += posicoes_simbolos[i]
                            qtd_giros_rotor[i] = qtd_giros_rotor[i] % 256

                        #Elemento recebe o que está na matriz de descriptografia
                        elemento = rotoresD[i][elemento]

                        #E a quantidade de giros é descontada do elemento    
                        elemento = elemento - qtd_giros_rotor[i]

                        if (elemento < 0): 
                            elemento += 256
                        
                        qtd_letras_cifradas[i] += 1

                    arquivo_saidaD.write(chr(elemento))
        except EOFError:
            pass
main()    
