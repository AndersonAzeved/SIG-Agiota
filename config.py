def CadastrarUsuario():
    sistema = {}
    print("Cadastramento do Usuário")
    cpf = input("CPF: ").replace(".",",","-","/")
    nome = input("Nome: ")
    sistema[cpf] = [nome]
    