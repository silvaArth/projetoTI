from datetime import datetime

def criar_chamado(dados):
    chamado = {
        "nome": dados["nome"],
        "setor": dados["setor"],
        "problema": dados["problema"],
        "descricao": dados["descricao"],
        "urgencia": dados["urgencia"],
        "status": "Aberto",
        "data_chamado": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    print("Chamado Criado:")
    print(chamado)

    return chamado