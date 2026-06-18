import json

list_producao = {}
dic = {}
try:
    with open("carros.produzidos.json", "r") as arquivo:
        list_producao = json.load(arquivo)
except (ValueError,FileNotFoundError):
    pass

try:
    with open("relatorio.final.json","r") as arquivo:
        dic = json.load(arquivo)
except ValueError, FileNotFoundError:
    pass

# print(list_producao)

# medias = {}
# for chave in dic:
#     sum = dic[chave]
#     media = sum / 7
#     medias[chave + "_media"] = media


somas = {}

# for dia in list_producao:
#     soma = sum(list_producao[dia].values())
#     print(soma)

total_geral = sum(sum(internos.values()) for internos in list_producao.values())
print(total_geral)  # Saída: 85




# add = 0
# dic = list_producao
# for dia_semana in list_producao:
#     for turno in list_producao[dia_semana]:
#             print(list_producao[dia_semana][turno])
#             print(turno)
#     #         if not dic:
#     #             dic = {}
#     #             dic[turno] = 0
#     #         try:
#     #             test = dic[turno]
#     #         except KeyError:
#     #             test = None
#     #         if not test:
#     #             dic[turno] = 0
#     #         add += list_producao[dia_semana][turno]
#     # dic[turno] += (add)

# list_producao = dic
# print(list_producao)