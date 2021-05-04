from persistencia.DAO import DAO


class PacienteDAO(DAO):
    def __init__(self):
        super.__init__('paciente.pkl')
