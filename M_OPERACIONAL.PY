import json

def get_turnos(escolha):
    turnos = {"1":"Manhã", "2":"Tarde", "3":"Noite"}
    turno = turnos[escolha]
    return turno

def dia_semana():
    dias = {"1" : "Segunda", "2" : "Terça", "3" : "Quarta", 
    "4" : "Quinta", "5" : "Sexta", "6" : "Sábado", "7" : "Domingo"}
    print("Escolha dia da semana.")
    print("1 - Segunda, 2 - Terça, 3 - Quarta,\n" \
    "4 - Quinta, 5 - Sexta, 6 - Sábado , 7 - Domingo")
    escolha = input("Informe opção: ")
    while True:
        match escolha:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                dia = dias[escolha]
                return dia, escolha
            case _:
                print("Opção invalida!!")

def cadastro_producao():
    dia, numero = dia_semana()
    print(dia, numero)
    while True:
        escolha = input("1 - Manhã\n" \
        "2 - Tarde\n" \
        "3 - Noite\n" \
        "Informe Turno: ")
        match escolha:
            case "1" | "2" | "3":
                while True:
                    turno = get_turnos(escolha)
                    print(turno)

                    try:
                        carro = float(input("Informe números de carros produzidos: "))
                        break
                    except ValueError:
                        print("Informe apenas números")
            case _:
                print("Opção invalida!!")


cadastro_producao()







    
