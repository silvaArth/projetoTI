from flask import Flask, render_template, request, redirect, url_for
from services.chamado_service import criar_chamado
from integrations.trello_service import criar_cartao
from database.database import criar_tabela

app = Flask(__name__)

criar_tabela()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/criar", methods=["POST"])
def criar():
    dados = {
        "nome": request.form.get("nome"),
        "setor": request.form.get("secretaria"),
        "problema": request.form.get("problema"),
        "descricao": request.form.get("descricao"),
        "urgencia": request.form.get("urgencia")
    }

    criar_chamado(dados)
    criar_cartao(dados)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
