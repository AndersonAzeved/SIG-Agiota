import biblioteca
import pickle

def CadastrarUsuario(dicionario):
    print("Cadastramento do Usuário")
    cpf = input("CPF: ")
    cpf = TirarPontosCpf(WhileCpf(cpf,dicionario))
    nome = input("Nome: ")
    dicionario[cpf] = [nome,{}]

def WhileCpf(cpf,dicionario):
    if not biblioteca.ValidaCpf(cpf):
        while not biblioteca.ValidaCpf(cpf):
            cpf = TirarPontosCpf(input("CPF Inválido! Tente Novamente: "))
    if VerificarIndice(dicionario,cpf):
        while VerificarIndice(dicionario,cpf):
            cpf = TirarPontosCpf(input("CPF Já Cadastrado! Tente Novamente: "))
    return cpf

def SalvaArquivo(nome_arquivo, dicionario):
  arquivo = open(nome_arquivo, "ab")
  pickle.dump(dicionario, arquivo)
  arquivo.close()
  
def LerArquivo(nome_arquivo,dicionario):
  try:
    arquivo = open(nome_arquivo, "rb")
    dicionario = pickle.load(arquivo)
    arquivo.close()
    
  except:
    arquivo = open(nome_arquivo, "wb")
    arquivo.close()

  return dicionario
    
def VerificarIndice(dicionario,indice):
    if indice in dicionario:
        return True
    else:
        return False

def TirarPontosCpf(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    return cpf