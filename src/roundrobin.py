import time;

process_input = int (input("Digite a quantidade de processos: "))
process_array = []

for count in range(1, process_input + 1):
    process_value_input = float(input(f"Digite a duração total em segundos do processo {count}: "))
    process_array.append(process_value_input)

quantum = 5

resultado = (quantum/process_input)

print(process_array)

    # time.sleep(resultado);