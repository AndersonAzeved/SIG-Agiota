import config

sistema = {}

op = input("Informe a opção: ")
if op == "1":
    sistema = config.LerArquivo("files/sistema.dat",sistema)
    config.CadastrarUsuario(sistema)
    config.SalvaArquivo("files/sistema.dat",sistema)