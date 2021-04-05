from tela.tela_abstrata import AbstractTela


class TelaRelatorio(AbstractTela):

    def __init__(self, controlador_agendamento):
        super().__init__()
        self.__controlador_agendamento = controlador_agendamento

    def mostra_relatorio(self, agendamentos):
        print(self.colorir_info("RELATÓRIO DOS AGENDAMENTOS"))
        for agendamento in agendamentos:
            print("\nNome do paciente: ", self.colorir_info(agendamentos[agendamento]["paciente"].nome))
            print("CPF do paciente: ", self.colorir_info(agendamentos[agendamento]["paciente"].cpf))
            print("Telefone do paciente: ", self.colorir_info(agendamentos[agendamento]["paciente"].telefone))
            print("Endereço do paciente: ", self.colorir_info(agendamentos[agendamento]["paciente"].endereco))
            print("Informações do agendamento:  ", self.colorir_info("A vacina está marcada para " +
                                                             agendamentos[agendamento]["agendamento"][0] + " às " +
                                                             agendamentos[agendamento]["agendamento"][1]))
            if agendamentos[agendamento]["paciente"].dose == 0:
                print(self.colorir_erro("Paciente ainda não foi vacinado"))
            elif agendamentos[agendamento]["paciente"].dose == 1:
                print(self.colorir_erro("Paciente já tomou a primeira dose da vacina!"))
                print("Tipo da dose: ", self.colorir_info(agendamentos[agendamento]["paciente"].tipo_dose))
            elif agendamentos[agendamento]["paciente"].dose == 2:
                print("Paciente já recebeu todas as does")
                print("Tipo da dose: ", agendamentos[agendamento]["paciente"].tipo_dose)
            print("Nome do Enfermeiro(a): ", self.colorir_info(agendamentos[agendamento]["enfermeiro"].nome))
            print("COREN do Enfermeiro(a): ", self.colorir_info(agendamentos[agendamento]["enfermeiro"].coren))
        print(input(("\nAperte enter para continuar: ")))