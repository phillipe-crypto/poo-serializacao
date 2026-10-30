# poo-serializacao

# Exercício: Cadastro de produtos
Desenvolva um script em Python utilizando Programação Orientada a Objetos (POO) que represente os produtos de uma loja e permita salvar (serializar) e recuperar (desserializar) seus dados em um arquivo.

# Requisitos:

#### 1. Criar uma classe `Produto` com os atributos `nome`, `preco` e `quantidade`.
#### 2. Criar um objeto da classe `Produto`.
#### 3. Serializar os atributos do objeto para JSON.
#### 4. Salvar os dados em um arquivo chamado `produto.json`.
#### 5. Ler o arquivo e desserializar os dados.
#### 6. Criar um novo objeto `Produto` com os dados recuperados.
#### 7. Exibir os dados do objeto reconstruído.

---

### Questões para responder:
- Qual é a diferença entre serialização e desserialização?

    R: Serialização é o processo de converter os dados de um objeto para um formato que possa ser armazenado ou transmitido, como JSON. Desserialização é o processo inverso, que recupera os dados e permite reconstruir o objeto.

- Qual é a vantagem de salvar os dados em um arquivo?

    R: Permite manter os dados armazenados mesmo após o encerramento do programa, possibilitando recuperá-los posteriormente.

- O objeto recuperado é necessariamente a mesma instância do objeto original? Justifique.

    R: Não. É uma nova instância criada a partir dos dados recuperados do arquivo JSON. Ela possui os mesmos valores dos atributos do objeto original, mas é um objeto diferente na memória.

- Em que situação real uma aplicação precisaria serializar objetos?

    R: Em um sistema de loja virtual, por exemplo, para salvar informações de produtos, como nome, preço e quantidade, em arquivos ou bancos de dados, permitindo recuperá-las posteriormente.
