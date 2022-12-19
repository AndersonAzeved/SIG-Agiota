import config

sistema = {}

op = input("Informe a opção: ")
while op != "0":
    sistema = config.LerArquivo("files/sistema.dat",sistema)
    if op == "1":
        config.CadastrarUsuario(sistema)
        config.SalvaArquivo("files/sistema.dat",sistema)
    elif op == "2":
        print("Parte 2")