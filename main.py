import json


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


# Criando um objeto da classe Produto
produto1 = Produto("Notebook", 3500.00, 10)


# Convertendo os atributos do objeto para um dicionário
dados_produto = {
    "nome": produto1.nome,
    "preco": produto1.preco,
    "quantidade": produto1.quantidade
}


# Serializando e salvando os dados no arquivo JSON
with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_produto, arquivo, indent=4, ensure_ascii=False)


# Lendo o arquivo JSON e recuperando os dados
with open("produto.json", "r", encoding="utf-8") as arquivo:
    dados_recuperados = json.load(arquivo)


# Criando um novo objeto com os dados recuperados
produto2 = Produto(
    dados_recuperados["nome"],
    dados_recuperados["preco"],
    dados_recuperados["quantidade"]
)


# Exibindo os dados do produto reconstruído
print("\nProduto recuperado:")
print(f"Nome: {produto2.nome}")
print(f"Preço: R$ {produto2.preco:.2f}")
print(f"Quantidade: {produto2.quantidade}")
