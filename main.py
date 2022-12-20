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
    "///   0. Sair                    ///\n"
    "///                              ///\n"
    "////////////////////////////////////\n"
    "Informe a opção: ")
while op != "0":
    sistema = config.LerArquivo("files/sistema.dat",sistema)
    cartao = config.LerArquivo("files/cartao.dat",cartao)
    dividas = config.LerArquivo("files/dividas.dat",dividas)
    if op == "1":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Devedor       ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarDevedor(sistema)
        config.SalvaArquivo("files/sistema.dat",sistema)
    elif op == "2":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Dívidas       ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarDividas(dividas)
        config.SalvaArquivo("files/dividas.dat",dividas)
    elif op == "3":
        print(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///      Cadastrar Cartão        ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "")
        config.CadastrarCartao(cartao)
        config.SalvaArquivo("files/cartao.dat",cartao)
    
    op = input(""
            "////////////////////////////////////\n"
            "///                              ///\n"
            "///   1. Cadastrar Devedor       ///\n"
            "///   2. Cadastrar Dívidas       ///\n"
            "///   3. Cadastrar Cartão        ///\n"
            "///                              ///\n"
            "////////////////////////////////////\n"
            "Informe a opção: ")