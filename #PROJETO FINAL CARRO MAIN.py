#PROJETO FINAL CARRO MAIN
import M_OPERACIONAL as ope





while True:

    print("#" * 60)
    print("Gestão Carangos S/A")
    print("Menu principal \n" \
    "Escolha opção.\n" \
    "1 - Gestão Operacional\n" \
    "2 - Gestão de Estoque\n" \
    "3 - Gestão Financeira\n" \
    "4 - RH\n" \
    "5 - Sair")
    menu = input("Informe opção: ")
    match menu:
        case "1":
            while True:
                print("#" * 60)
                print("Gestão Operacional")
                print("Menu Operacional\n" \
                "1 - Cadastro e projeções da produção\n" \
                "2 - Relatorio de produção\n" \
                "3 - Menu principal ")
                sub_menu = input("Informe opção: ")
                match sub_menu:
                    case "1":
                        print("#" * 60)
                        print("Cadastro e projeções da produção")
                        ope.cadastro_producao()





                    case "2":
                        print("#" * 60)
                        print("Relatorio de produção")
                    
                    case "3":
                        break

                    case _:
                        print("Opção invalida.")


        


        case "2":
            print()


        


        case "3":
            print()




        

        case "4":
            print()



        
        case "5":
            print("Finalizando!")
            break




        case _:
            print("Opção invalida.")



    


