from tela.tela_abstrata import AbstractTela


class TelaRelatorio(AbstractTela):

    def __init__(self, controlador_atendimento):
        super().__init__()
        self.__controlador = controlador_atendimento

    def mostra_relatorio(self, agendamentos):
        print(self.info("RELATÓRIO DOS AGENDAMENTOS"))
        for agendamento in agendamentos:
            print("\nNome do paciente: ", self.info(agendamentos[agendamento]["paciente"].nome))
            print("CPF do paciente: ", self.info(agendamentos[agendamento]["paciente"].cpf))
            print("Telefone do paciente: ", self.info(agendamentos[agendamento]["paciente"].telefone))
            print("Endereço do paciente: ", self.info(agendamentos[agendamento]["paciente"].endereco))
            print("Informações do agendamento:  ", self.info("A vacina está marcada para " +
                                                             agendamentos[agendamento]["agendamento"][0] + " às " +
                                                             agendamentos[agendamento]["agendamento"][1]))
            print("Nome do Enfermeiro(a): ", self.info(agendamentos[agendamento]["enfermeiro"].nome))
            print("COREN do Enfermeiro(a): ", self.info(agendamentos[agendamento]["enfermeiro"].coren))
        print(input(("\nAperte enter para continuar: ")))