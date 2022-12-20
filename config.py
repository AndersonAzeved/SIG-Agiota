import biblioteca
import pickle

def CadastrarDevedor(dicionario):
  print("Cadastramento do Devedor")
  cpf = input("CPF: ")
  cpf = TirarPontosCpf(WhileCpf(cpf,dicionario,1))
  nome = input("Nome: ")
  dicionario[cpf] = [nome,{}]

def WhileCpf(cpf,dicionario,op):
  if not biblioteca.ValidaCpf(cpf):
      while not biblioteca.ValidaCpf(cpf):
          cpf = TirarPontosCpf(input("CPF Inválido! Tente Novamente: "))
  if VerificarIndice(dicionario,cpf):
      while VerificarIndice(dicionario,cpf):
        if op == 1:
          cpf = TirarPontosCpf(input("CPF Já Cadastrado! Tente Novamente: "))
        else:
          cpf = TirarPontosCpf(input("CPF Não Cadastrado! Tente Novamente: "))
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

def CadastrarDividas(dicionario):
  cpf = TirarPontosCpf(input("Informe o CPF do Devedor: "))
  cpf = WhileCpf(cpf, dicionario, 2)
  nome_compra = input("Nome da Compra: ")
  valor = input("Valor da Compra: ")
  op = input("Pagamento a prazo (SIM-S ou NÃO-N): ").lower()
  while not(op == "sim" or op == "s") or not(op == "não" or op == "n" or op == "nao"):
    op = input("Informação Inválida, Tente Novamente!\nPagamento a prazo (SIM-S ou NÃO-N): ").lower()
  if op == "sim" or op == "s":
    prazo = input("Em quantas vezes? ")
    parcela = input("Valor das Parcelas: ")
  else:
    parcela = input("Valor àvista: ")
  data = input("Informe a data da compra: ")

def CadastrarCartao(dicionario):
  cpf = TirarPontosCpf(input("Informe o CPF do dono do cartão: "))
  cpf = WhileCpf(cpf, dicionario, 2)
  nome = input("Como deseja chamar o cartão: ")
  dicionario[cpf] = [nome]

def WhileCartao(cartao,dicionario,op):
  if VerificarIndice(dicionario,cartao):
      while VerificarIndice(dicionario,cartao):
        if op == 1:
          cartao = TirarPontosCpf(input("Cartão Já Cadastrado! Tente Novamente: "))
        else:
          cartao = TirarPontosCpf(input("Cartão Não Cadastrado! Tente Novamente: "))
  return cartao