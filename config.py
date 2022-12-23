import biblioteca
import pickle

def CadastrarDevedor(dicionario):
  print("Cadastramento do Devedor")
  cpf = input("CPF: ")
  cpf = TirarPontosCpf(WhileCpf(cpf,dicionario,1))
  nome = input("Nome: ")
  status = "a"
  dicionario[cpf] = [nome,status]

def WhileCpf(cpf,dicionario,op):
  if not biblioteca.ValidaCpf(cpf):
      while not biblioteca.ValidaCpf(cpf):
          cpf = TirarPontosCpf(input("CPF Inválido! Tente Novamente: "))
  if VerificarIndice(dicionario,cpf):
      while VerificarIndice(dicionario,cpf):
        if op == 1:
          cpf = TirarPontosCpf(input("CPF Já Cadastrado! Tente Novamente: "))
        elif op == 2:
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
  cpf = WhileCpf(cpf, dicionario, 3)
  nome_compra = input("Nome da Compra: ")
  valor = input("Valor da Compra: ")
  op = input("Pagamento a prazo (SIM-1 ou NÃO-2): ")
  while op < "1" and op > "2":
    op = input("Informação Inválida, Tente Novamente!\nPagamento a prazo (SIM-S ou NÃO-N): ").lower()
  prazo = False
  parcela = False
  if op == "1":
    prazo = input("Em quantas vezes? ")
    parcela = input("Valor das Parcelas: ")
  data = input("Informe a data da compra: ")
  cartao = TirarPontosCpf(input("Informe o CPF do Cartão: "))
  cartao = WhileCartao(cpf,dicionario,2)
  status = "a"
  dicionario[nome_compra] = [cpf,valor,prazo,parcela,data,cartao,status]

def CadastrarCartao(dicionario):
  cpf = TirarPontosCpf(input("Informe o CPF do dono do cartão: "))
  cpf = WhileCartao(cpf, dicionario, 1)
  nome = input("Como deseja chamar o cartão: ")
  status = "a"
  dicionario[cpf] = [nome,status]

def WhileCartao(cpf,dicionario,op):
  if not biblioteca.ValidaCpf(cpf):
      while not biblioteca.ValidaCpf(cpf):
          cpf = TirarPontosCpf(input("CPF Inválido! Tente Novamente: "))
  if VerificarIndice(dicionario,cpf):
      while VerificarIndice(dicionario,cpf):
        if op == 1:
          cpf = TirarPontosCpf(input("Cartão Já Cadastrado! Tente Novamente: "))
        elif op == 2:
          cpf = TirarPontosCpf(input("Cartão Não Cadastrado! Tente Novamente: "))
  return cpf

def CalculandoFatura(dicionario1,dicionario2):
  lista = []
  soma_t = 0
  for i in dicionario1:
    for j in dicionario2:
      lista = dicionario2[j]
      if i == lista[0] and lista[2] == False and lista[3] == False:
        soma_t+=float(lista[1])
      else:
        soma_t+=float(lista[3])
  print("Valor foi: ", soma_t)
      