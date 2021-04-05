from tela.tela_abstrata import AbstractTela


class TelaAgendamento(AbstractTela):

    def __init__(self, controlador_agendamento):
        super().__init__()
        self.__controlador_agendamento = controlador_agendamento

    def mostra_opcoes(self):
        print(self.colorir_titulo("----------- AGENDAMENTOS---------------"))
        print("1 - Inserir agendamento")
        print("2 - Editar agendamento")
        print("3 - Excluir agendamento")
        print("4 - Listar agendamentos")
        print("5 - Relatório de agendamentos")
        print("6 - Retornar a tela principal")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2, 3, 4, 5, 6])

    def pegar_dados_agendamento(self, agenda):
        print(self.colorir_titulo("---------------- AGENDAMENTO ----------------"))
        dia = {1: "segunda", 2: "terca", 3: "quarta", 4: "quinta", 5: "sexta"}
        opcao = self.pega_dia()
        horarios_preenchidos = agenda[dia[opcao].title()]
        horarios_disponiveis = self.mostra_horas(horarios_preenchidos)
        hora = int(self.pegar_num("Insira o numero referente a hora escolhida: "))
        return [dia[opcao], horarios_disponiveis[hora]]

    def pega_dia(self):
        print("Escolha a opção que referente ao dia da vacina:  ")
        print("1 - Segunda")
        print("2 - Terça")
        print("3 - Quarta")
        print("4 - Quinta")
        print("5 - Sexta")
        opcao = int(self.pegar_num("Insira o número da opção escolhida: "))
        return opcao

    def mostra_horas(self, horarios_preenchidos):

        horarios = [{0: "8:00"}, {1: "8:15"}, {2: "8:30"}, {3: "8:45"}, {4: "9"}, {5: "9:15"}, {6: "9:30"},
                    {7: "9:45"}, {8: "10:00"}, {9: "10:15"}, {10: "10:30"}, {11: "10:45"}, {12: "11:00"},
                    {13: "11:15"}, {14: "11:30"}, {15: "11:45"}, {16: "12:00"}, {17: "12:15"}, {18: "12:30"},
                    {19: "12:45"}, {20: "13:00"}, {21: "13:15"}, {22: "13:30"}, {23: "13:45"}, {24: "14:00"},
                    {25: "14:15"}, {26: "14:30"}, {27: "14:45"}, {28: "15:00"}, {29: "15:15"}, {30: "15:30"},
                    {31: "15:45"}, {32: "16:00"}, {33: "17:15"}, {34: "17:30"}, {35: "17:45"}, {36: "18:00"}]

        horarios_disponiveis = []
        for item in range(len(horarios)):
            horarios_disponiveis.append(horarios[item][item])

        for horario in horarios_preenchidos:
            if horario in horarios_disponiveis:
                horarios_disponiveis.remove(horario)

        count = 0
        identificador = 0
        for horario_disponivel in horarios_disponiveis:
            if count % 10 == 0:
                print(f'\n{self.colorir_info(f"({identificador})")} {horario_disponivel}', end=" ")
            else:
                print(f'{self.colorir_info(f"({identificador})")}  {horario_disponivel}', end=" ")
            identificador += 1
            count += 1
        print("\n")
        return horarios_disponiveis

    def mostra_dados(self, agendamentos):
        for agendamento in agendamentos:
            print("\nNome do paciente: ", self.colorir_info(agendamentos[agendamento]["paciente"].nome))
            print("Informações do agendamento:  ", self.colorir_info("A vacina está marcada para " +
                                                          agendamentos[agendamento]["agendamento"][0] + " às " +
                                                          agendamentos[agendamento]["agendamento"][1]))
            print("Nome do Enfermeiro(a): ", self.colorir_info(agendamentos[agendamento]["enfermeiro"].nome))
        print(input(("\nAperte enter para continuar: ")))


    def mostra_msg_enfermeiro_nao_castrado(self):
        print(self.colorir_erro("ENFERMEIRO NÃO ENCONTRADO, POR FAVOR, REALIZE O CADASTRO"))


    def mostra_opcao_alteracao(self):
        print(self.colorir_titulo("------ ALTAREÇÃO DE ANGENDAMENTO --------"))
        print("Escolha a opção que você deseja alterar:  ")
        print("1 - alterar o dia da vacinação")
        print("2 - alterar o horario da vacinação")
        print("3 - alterar o dia e a horario da vacinação")
        print("4 - alterar o enfermeiro")
        return int(input("Insira o número da opção escolhida: "))

    def pega_novos_dados(self, opcao, agendamentos, paciente, agenda):
        print(self.colorir_titulo("\n------ INSERIR NOVO DADO PARA ALTERAR O AGENDAMENTO --------"))
        opcoes_mudanca = {1: "dia", 2: "hora", 3: "dia e hora", 4: "enfermeiro"}
        dia = {1: "Segunda", 2: "Terca", 3: "Quarta", 4: "Quinta", 5: "Sexta"}

        if opcao == 1:
            hora = agendamentos[paciente.nome]["agendamento"][1]
            dia_escolhido = dia[self.pega_dia()]
            if hora not in agenda[dia_escolhido]:
                return [opcoes_mudanca[opcao], dia_escolhido]
            else:
                print(self.colorir_erro("HORÁRIO INDISPONIVEL"))
                print(self.colorir_info_correta("\nESCOLHA OUTRO HORÁRIO ENTRA AS OPÇÕES ABAIXO"))
                horarios_preenchidos = agenda[dia_escolhido]
                horarios_disponiveis = self.mostra_horas(horarios_preenchidos)
                hora = int(self.pegar_num("Insira o numero referente a hora escolhida: "))
                print(self.colorir_info("\nAGENDAMENTO ALTERADO!"))
                return [dia[opcao], horarios_disponiveis[hora]]


        elif opcao == 2:
            print(self.colorir_info("ESCOLHA UM HORÁRIO ENTRA AS OPÇÕES ABAIXO"))
            dia_agendado = agendamentos[paciente.nome]["agendamento"][0]
            horarios_preenchidos = agenda[dia_agendado]
            horarios_disponiveis = self.mostra_horas(horarios_preenchidos)
            hora = int(self.pegar_num("Insira o numero referente a hora escolhida: "))
            print(self.colorir_info("\nAGENDAMENTO ALTERADO!"))
            return [opcoes_mudanca[opcao], horarios_disponiveis[hora]]

        elif opcao == 3:
            dia_escolhido = dia[self.pega_dia()]
            horarios_preenchidos = agenda[dia_escolhido]
            horarios_disponiveis = self.mostra_horas(horarios_preenchidos)
            hora = int(self.pegar_num("Insira o numero referente a hora escolhida: "))
            return [opcoes_mudanca[opcao], [dia_escolhido, horarios_disponiveis[hora]]]

        elif opcao == 4:
            return [opcoes_mudanca[opcao]]

    def mostra_mensagem_agendamento_exlcuido(self):
        print(self.colorir_info("ANGENDAMENTO EXCLUÍDO COM SUCESSO!"))
        print(input(("Aperte enter para continuar: ")))

    def mostra_msg_sem_agendamento(self):
        print(self.colorir_erro("NÃO HÁ AGENDAMENTOS!"))
        print(input(("Aperte enter para continuar: ")))

    def pega_opcao_paciente_sem_cadastro(self):
        print(self.colorir_erro("PACIENTE NÃO CADASTRADO"))
        print(self.colorir_info("Escolha uma das opções abaixo: "))
        print("1 - Cadastrar paciente")
        print("2 - Retornar a tela principal")
        return self.pegar_opcao("Insira o número da opção escolhida: ", [1, 2])
