import config

sistema = {}
cartao = {}
dividas = {}

op = input(""
    "////////////////////////////////////\n"
    "///                              ///\n"
    "///         SIG-AGIOTA           ///\n"
    "///                              ///\n"
    "///                  by Anderson ///\n"
    "////////////////////////////////////\n"
    "///                              ///\n"
    "///   1. Cadastrar Devedor       ///\n"
    "///   2. Cadastrar Dívidas       ///\n"
    "///   3. Cadastrar Cartão        ///\n"
    "///   4. Calcular Fatura         ///\n"
    "///   0. Sair                    ///\n"
    "///                              ///\n"
    "////////////////////////////////////\n"
    "Informe a opção: ")
sistema = config.LerArquivo("sistema.dat",sistema)
cartao = config.LerArquivo("cartao.dat",cartao)
dividas = config.LerArquivo("dividas.dat",dividas)
while op != "0":
    sistema = config.LerArquivo("sistema.dat",sistema)
    cartao = config.LerArquivo("cartao.dat",cartao)
    dividas = config.LerArquivo("dividas.dat",dividas)
    if op == "1":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Devedor       ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarDevedor(sistema)
        config.SalvaArquivo("sistema.dat",sistema)
    elif op == "2":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Dívidas       ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarDividas(dividas)
        config.SalvaArquivo("dividas.dat",dividas)
    elif op == "3":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Cartão        ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarCartao(cartao)
        config.SalvaArquivo("cartao.dat",cartao)
    
    elif op == "4":
        config.CalculandoFatura(sistema,dividas)
        config.SalvaArquivo("sistema.dat",sistema)
    
    else:
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///       Opção Inválida         ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
    
    op = input(""
    "////////////////////////////////////\n"
    "///                              ///\n"
    "///         SIG-AGIOTA           ///\n"
    "///                              ///\n"
    "///                  by Anderson ///\n"
    "////////////////////////////////////\n"
    "///                              ///\n"
    "///   1. Cadastrar Devedor       ///\n"
    "///   2. Cadastrar Dívidas       ///\n"
    "///   3. Cadastrar Cartão        ///\n"
    "///   4. Calcular Fatura         ///\n"
    "///   0. Sair                    ///\n"
    "///                              ///\n"
    "////////////////////////////////////\n"
    "Informe a opção: ")
    
if op == "0":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///       Encerrando SIG         ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")