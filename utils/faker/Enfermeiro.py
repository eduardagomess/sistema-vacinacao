from entidade.enfermeiro import Enfermeiro

__dados_enfermeiro = {
    'nome': 'Ana Silva',
    'telefone': '4833330350',
    'cpf': 11412675944,
    'coren': 89756
}

__dados_enfermeiro2 = {
    'nome': 'Julia Silva',
    'telefone': '48999050687',
    'cpf': 45678936944,
    'coren': 12345
}

__dados_enfermeiro3 = {
    'nome': 'Luiza Medeiros',
    'telefone': '48998476035',
    'cpf': 45696325841,
    'coren': 98745
}

fakeEnfermeiro = Enfermeiro(*__dados_enfermeiro.values())
fakeEnfermeiro2 = Enfermeiro(*__dados_enfermeiro2.values())
fakeEnfermeiro3 = Enfermeiro(*__dados_enfermeiro3.values())
