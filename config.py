import biblioteca
import pickle

def CadastrarUsuario():
    sistema = {}
    print("Cadastramento do Usuário")
    cpf = input("CPF: ")
    cpf = WhileCpf(cpf)
    nome = input("Nome: ")
    sistema[cpf] = [nome,{}]
    SalvaArquivo("files/sistema.dat",sistema)

def WhileCpf(cpf):
    if not biblioteca.ValidaCpf(cpf):
        while not biblioteca.ValidaCpf(cpf):
            cpf = input("CPF Inválido! Tente Novamente: ")
    return cpf

def SalvaArquivo(nome_arquivo, dicionario):
  arquivo = open(nome_arquivo, "wb")
  pickle.dump(dicionario, arquivo)
  arquivo.close()