import time;

#Quantidade de processos
process_input = int (input("Digite a quantidade de processos: "))

#Array para armazenar a duração de cada processo
process_array = []

#Array para auxiliar na contagem de processos finalizadoz
process_executed = []

#For para inserir a duração de cada processo
for count in range(1, process_input + 1):
    process_value_input = float(input(f"Digite a duração total em segundos do processo {count}: "))
    process_array.append(process_value_input)


quantum = 5

#Tempo que cada processo terar para executar
res = (quantum/process_input)

#Enquanto o tamanho da lista que contém o tempo de cada processo for diferente da lista auxiliar o programa será executado
while len(process_array) != len(process_executed):

#For para percorrer cada processo e seu valor de druação
    for c in range(0, process_input):

        #Valor atual do array que está no loop
        value = process_array[c]
        
        #Caso o tamanho de ambos arrays forem iguais, o break é acionado para sair do for
        if len(process_array) == len(process_executed):
            break

        #Caso o valor atual do loop seja maior que 0 significa que o processo ainda não finalizou sua execução    
        if value > 0:

            #Subtraindo o tempo de execução total do processo no loop pelo tempo da "rodada de processamento" (cálculo quantum/número de processos)
            process_op = value - res

            #Removendo o valor antigo do preocesso, antes de ter passado pela "rodada de processamento"
            process_array.remove(value)

            #Adicionando o novo tempo restante para o processo ser finalizado
            process_array.insert(c, process_op)

            # print(process_array)

            #Caso o processo tenha sido finalizado (Menor ou igual a 0 segundos)
            if process_op <= 0:
                print(f"Processo {c + 1} finalizado")

                #Time para simular o período de execução do processo
                time.sleep(res)
                
                #Adicionando valor ao array auxiliar para informar que o processo foi finalizado
                process_executed.append(1)
            
            #Caso o processo ainda precise ser executado
            else:
                print(f"processo {c + 1} executando = agora faltam {process_op}s para completar sua execução")
                time.sleep(res)
                
        #Caso o processo ainda precise ser executado
        else:
            print(f"Processo {c + 1} finalizado")
            process_executed.append(1)
            # print(f"{len(process_array) == len(process_executed)} = {len(process_array)} --- {len(process_executed)})")
            # time.sleep(res)