from tela.tela_abstrata import AbstractTela


class TelaPaciente(AbstractTela):

    def __init__(self, controlador_sistema):
        super().__init__()
        self.__controlador_sistema = controlador_sistema

    def mostra_opcoes(self):
        print(self.titulo("------ ÁREA DE PACIENTES --------"))
        print("Escolha uma das opções abaixo: ")
        print("1 - Incluir paciente")
        print("2 - Listar pacientes")
        print("3 - Alterar informações do paciente")
        print("4 - Excluir pacientes")
        print("5 - Buscar paciente")
        print("6 - Retornar a tela principal do sistema")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])

    def pega_dados_paciente(self, opcao):

        dados_requeridos = {0: self.pegar_nome, 1: self.pegar_telefone, 2: self.pegar_cpf,
                            3: self.pegar_nome, 4: self.pegar_nome, 5: self.pegar_num,
                            6: self.pegar_complemento, 7: self.pegar_data_nascimento}

        mensagem_requerimento = {0: "Insira o nome do paciente: ", 1: "Insira o telefone do paciente: ",
                                 2: "Insira o cpf do paciente: ", 3: "Insira o bairro: ",
                                 4: "Insira a rua: ", 5: "Insira o número: ", 6: "Insira o complemento: ",
                                 7: "Insira a data de nascimento do paciente (DD/MM/AAAA): "}

        dados_cadastro = ["nome", "telefone", "cpf", "bairro", "rua", "numero",
                          "complemento", "data_nascimento", "dose"]

        if opcao == 1:
            print(self.titulo(" ---- CADASTRAR PACIENTE  ----"))

            lista_dados_requeridos = list(dados_requeridos.values())
            dados_paciente = []

            for dado in range(len(lista_dados_requeridos)):
                dados_paciente.append(lista_dados_requeridos[dado](mensagem_requerimento[dado]))
            return dict(zip(dados_cadastro, dados_paciente))

        else:
            opcao_escolhida = self.mostra_opcao_alteracao_cadastro()

            opcoes_mudanca = {0: "nome", 1: "telefone", 2: "cpf ", 3: "bairro", 4: "rua",
                              5: "numero", 6: "complemento", 7: "data_nascimento"}

            if opcao_escolhida == 3:
                dados_endereco = [dados_requeridos[opcao_escolhida](mensagem_requerimento[3]),
                                  dados_requeridos[opcao_escolhida](mensagem_requerimento[4]),
                                  dados_requeridos[opcao_escolhida](mensagem_requerimento[5]),
                                  dados_requeridos[opcao_escolhida](mensagem_requerimento[5])]
                return [opcoes_mudanca[opcao_escolhida], dados_endereco]
            else:
                dado = dados_requeridos[opcao_escolhida](mensagem_requerimento[opcao_escolhida])
                return [opcoes_mudanca[opcao_escolhida], dado]

    def mostra_dados(self, dados_paciente):
        for paciente in dados_paciente:
            print("\n Nome do paciente: ", self.info(paciente.nome))
            print("Telefone do paciente: ", self.info(paciente.telefone))
            print("CPF do paciente: ", self.info(paciente.cpf))
            print("Endereço do paciente: ", self.info(paciente.endereco))
            print("Data de nascimento do paciente: ", self.info(paciente.data_nascimento))
            if paciente.dose == None and paciente.tipo_dose == None:
                print(self.erro("Paciente ainda não vacinado"))
            else:
                print("O paciente está no estãgio: ", self.info(str(paciente.dose)))
                print("Tipo da vacina usada no paciente: ", self.info(str(paciente.tipo_dose)))
        print(input(("\nAperte enter para continuar: ")))


    def mostra_opcao_alteracao_cadastro(self):
        print(self.titulo("------ ALTAREÇÃO DE CADASTRO DO PACIENTE --------"))
        print("Escolha a opção que você deseja alterar:  ")
        print("0 - alterar o nome do paciente")
        print("1 - alterar o telefone do paciente")
        print("2 - alterar o cpf do paciente")
        print("3 - alterar o endereço do paciente")
        print("4 - alterar a data de nascimento do paciente")
        print("5 - alterar o estágio da dose do paciente")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [0, 1, 2, 3, 4, 5])

    def mostra_opcao_busca(self):
        print(self.titulo("------ OPÇÃO DE BUSCA DE PACIENTE ----------"))
        print("1 - buscar pelo nome do paciente")
        print("2 - busca pelo cpf do paciente")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])

    def mostra_paciente(self, paciente):
        print("\n Nome do paciente: ", self.info(paciente.nome))
        print("Telefone do paciente: ", self.info(paciente.telefone))
        print("CPF do paciente: ", self.info(paciente.cpf))
        print("Endereço do paciente: ", self.info(paciente.endereco))
        print("Data de nascimento do paciente: ", self.info(paciente.data_nascimento))
        if paciente.dose == None and paciente.tipo_dose == None:
            print(self.erro("Paciente ainda não vacinado"))
        else:
            print("O paciente está no estãgio: ", self.info(str(paciente.dose)))
            print("Tipo da vacina usada no paciente: ", self.info(str(paciente.tipo_dose)))

        print(input(("\nAperte enter para continuar: ")))

    def busca_paciente_nome(self):
        return self.pegar_nome("Insira o nome do paciente: ")

    def busca_paciente_cpf(self):
        return self.pegar_cpf("Insira o cpf do paciente: ")
