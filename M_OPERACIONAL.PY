import json
import os

def inciar_cadastro():
    list_producao = {}
    try:
        with open("carros.produzidos.json", "r") as arquivo:
            list_producao = json.load(arquivo)
    except ValueError,FileNotFoundError:
        pass

    list_producao = cadastro_producao(list_producao)
    with open("carros.produzidos.json", "w") as arquivo:
        json.dump(list_producao, arquivo, indent =4)

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
                return dia
            case _:
                print("Opção invalida!!")

def carros_produidos():
    while True:
        try:
            carro = float(input("Informe números de carros produzidos: "))
            print(f"Carros produzidos {carro}")
            confirm = input("Deseja confirmar? S/N: ").lower()
            match confirm:
                case "s":
                    return carro
                case "n":
                    continue
                case _:
                    print("Opção invalida!!")
        except ValueError:
            print("Informe apenas números")

def cadastro_dicionario_producao(list_producao,dia,turno,carro):
    dic = list_producao
    if not dic:
        dic[dia] = {}
    try:    
        test = dic[dia]
    except KeyError:
        test = None
    if not test:
        dic[dia] = {}
    dic[dia][turno] = carro
    return dic

def cadastro_producao(list_producao):
    dic = list_producao
    dia = dia_semana()
    while True:
        escolha = input("1 - Manhã\n" \
        "2 - Tarde\n" \
        "3 - Noite\n" \
        "Informe Turno: ")
        match escolha:
            case "1" | "2" | "3":
                turno = get_turnos(escolha)
                carro = carros_produidos()
                dic = cadastro_dicionario_producao(dic,dia,turno,carro)
                return dic
              
            case _:
                print("Opção invalida!!")


"####################################"
def relatorio_producao():
    list_producao = {}
    try:
        with open("carros.produzidos.json", "r") as arquivo:
            list_producao = json.load(arquivo)
    except ValueError, FileNotFoundError:
        if FileNotFoundError:
            print("Sem cadastro de carros.")
            return
        pass
    add_dicionario_relatorio(list_producao)
    soma_dias()
    media_turnos()
    producao_ideal()
    print_relatorio()


def abrir_json_2():
    try:
        with open("relatorio.final.json","r") as arquivo:
            dic = json.load(arquivo)
    except ValueError, FileNotFoundError:
        return None
    return dic


def soma_turno_relatorio(list_producao,turno,dia_semana):
    add = 0
    dic = abrir_json_2()
    if not dic:
        dic = {}
        dic[turno] = 0
    try:
        test = dic[turno]
    except KeyError:
        test = None
    if not test:
        dic[turno] = 0
    add += list_producao[dia_semana][turno]
    dic[turno] += (add)
    with open("relatorio.final.json","w") as arquivo:
        json.dump(dic, arquivo, indent =4)

def soma_dia_relatorio(list_producao,turno,dia_semana):
    add = 0
    dic = abrir_json_2()
    if not dic:
        dic = {}
        dic[dia_semana] = 0
    try:
        test = dic[dia_semana]
    except KeyError:
        test = None
    if not test:
        dic[dia_semana] = 0
    add += list_producao[dia_semana][turno]
    dic[dia_semana] += (add)
    with open("relatorio.final.json","w") as arquivo:
        json.dump(dic, arquivo, indent =4)


        
def add_dicionario_relatorio(list_producao):
    for dia_semana in list_producao:
        for turno in list_producao[dia_semana]:
            soma_turno_relatorio(list_producao,turno,dia_semana)
            soma_dia_relatorio(list_producao,turno,dia_semana)
    soma_turno_relatorio(list_producao,turno,dia_semana)

def soma_dias():
    list_producao = {}
    try:
        with open("carros.produzidos.json", "r") as arquivo:
            list_producao = json.load(arquivo)
    except ValueError,FileNotFoundError:
        pass
    semana = sum(sum(internos.values()) for internos in list_producao.values())
    media_dia = semana/7
    mes_total = semana * 4 + (media_dia*2)
    ano_simulado = mes_total * 12
    dic = abrir_json_2()
    dic["semana"] = semana
    dic["media_dia"] = media_dia
    dic["mes_total"] = mes_total
    dic["ano_simulado"] = ano_simulado
    with open("relatorio.final.json","w") as arquivo:
        json.dump(dic, arquivo, indent =4)

def media_turnos():
    dic = abrir_json_2()
    manha = dic["Manhã"]
    tarde = dic["Tarde"]
    noite = dic["Noite"]
    media_manha = manha / 7
    media_tarde = tarde / 7
    media_noite = noite / 7
    dic["media_manha"] = media_manha
    dic["media_tarde"] = media_tarde
    dic["media_noite"] = media_noite
    with open("relatorio.final.json","w") as arquivo:
        json.dump(dic, arquivo, indent =4)

def producao_ideal():
    manha_tarde_100 = 500/60
    noite_100 = manha_tarde_100 * 1.5
    dia_100 = manha_tarde_100 + noite_100
    mes_100 = dia_100 * 30
    ano_100 = mes_100 * 12
    dic = abrir_json_2()
    dic["manha_tarde_100"] = manha_tarde_100
    dic["noite_100"] = noite_100
    dic["dia_100"] = dia_100
    dic["mes_100"] = mes_100
    dic["ano_100"] = ano_100
    with open("relatorio.final.json","w") as arquivo:
        json.dump(dic, arquivo, indent =4)


def print_relatorio():
    dic = abrir_json_2()
    if not dic:
        print("Nenhum dado de relatório encontrado.")
        return
    try:
        with open("carros.produzidos.json", "r") as arquivo:
            list_producao = json.load(arquivo)
    except ValueError,FileNotFoundError:
        pass
    try:
        print(f"Produção Segunda-feira, {dic["Segunda"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Terça-feira, {dic["Terça"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Quarta-feira, {dic["Quarta"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Quinta-feira, {dic["Quinta"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Sexta-feira, {dic["Sexta"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Sábado-feira, {dic["Sábado"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção Domingo-feira, {dic["Domingo"]:.2f} carros,\n"
            f"Media de produção diaria de {dic["media_dia"]:.2f}\n"
            f"Produção ideal {dic["dia_100"]:.2f}.")
        print("#" * 60)
    except KeyError:
        pass
    try:
        print(f"Produção do mês, {dic["mes_total"]:.f} carros,\n"
              f"Produção ideal {dic["mes_100"]:.2f} carros.")
    except KeyError:
        pass
    try:
        print(f"Produção do ano, {dic["ano_simulado"]:.f} carros,\n"
              f"Produção ideal {dic["ano_100"]:.2f} carros.")
    except KeyError:
        pass      
    os.remove("relatorio.final.json")
    
    























    
