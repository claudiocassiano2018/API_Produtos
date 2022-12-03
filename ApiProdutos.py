from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id': 1,
        'Produto': 'Feijão preto',
        'Preço': 'R$ 8.00'
    },
    {
        'id': 2,
        'Produto': 'Arroz',
        'Preço': 'R$ 5.50'
    },
    {
        'id': 3,
        'Produto': 'Macarrão',
        'Preço': 'R$ 3.80'
    },
    {
        'id': 4,
        'Produto': 'carne',
        'Preço': 'R$ 35.00'
    },
    {
        'id': 5,
        'Produto': 'farofa',
        'Preço': 'R$ 12.00'
    },

]

# Consultar(todos)


@app.route('/produtos', methods=['GET'])
def obter_produtos():
    return jsonify(produtos)

# Consultar(id)
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto_por_id(id):
    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)


# Editar
@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto_por_id(id):
    produto_alterado = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)
            return jsonify(produtos[indice])


# Criar
@app.route('/produtos', methods=['POST'])
def incluir_novo_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)

    return jsonify(produtos)


# Excluir
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            del produtos[indice]

    return jsonify(produtos)


app.run(port=5000, host='localhost', debug=True)
