from entidade.paciente import Paciente

__dados_paciente = {
    'nome': 'Eduarda Oliveira Gomes',
    'telefone': '48998477220',
    'cpf': 11412675944,
    'bairro': 'agronomica',
    'rua': 'delminda silveira',
    'numero': '729',
    'complemento': 'bloco H apto 406',
    'data': "04/09/1999",
}

__dados_paciente2 = {
    'nome': 'Fernanda Oliveira Gomes',
    'telefone': '48999050489',
    'cpf': 12345678944,
    'bairro': 'corrego grande',
    'rua': 'joao pinto',
    'numero': '72',
    'complemento': 'apto 505',
    'data': "05/08/1994",
}

__dados_paciente3 = {
    'nome': 'Iara Goretti Ivanov',
    'telefone': '48996229635',
    'cpf': 37648292904,
    'bairro': 'corrego grande',
    'rua': 'joao rosa',
    'numero': '78',
    'complemento': 'apto 55',
    'data': "26/05/1960",
}

fakePaciente = Paciente(*__dados_paciente.values())
fakePaciente2 = Paciente(*__dados_paciente2.values())
fakePaciente3 = Paciente(*__dados_paciente3.values())
