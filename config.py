import biblioteca

def CadastrarUsuario():
    sistema = {}
    print("Cadastramento do Usuário")
    cpf = input("CPF: ")
    cpf = WhileCpf(cpf)
    nome = input("Nome: ")
    sistema[cpf] = [nome]

def WhileCpf(cpf):
    if not biblioteca.ValidaCpf(cpf):
        while not biblioteca.ValidaCpf(cpf):
            cpf = input("CPF Inválido! Tente Novamente: ")
    return cpf