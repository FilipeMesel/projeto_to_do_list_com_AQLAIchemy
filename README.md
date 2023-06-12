# Sistema Bancário em Python

Este repositório contém um código em Python que busca elaborar um sistema de criar, atualizar e deletar tarefas a partir de uma lista presente em um banco de dados SQL usando a biblioteca "AQLAIchemy"

## Funcionalidades

O código apresenta um menu com as seguintes opções:

 - [l] Listar TODOs
 - [c] Criar TODO
 - [u] Atualizar TODO
 - [d] Delete TODO

## Dependências

Este projeto não possui nenhuma dependência externa. A única dependência necessária é o Python 3 e a biblioteca "AQLAIchemy". que deve ser instalada digitando no "cmd":

 - pip install SQLAlchemy

Sinta-se à vontade para clonar este repositório, explorar o código e adaptá-lo conforme necessário para atender às suas necessidades.

## Arquivos

O arquivo "todo_list.py" apresenta o Objeto que representa a tabela de TODOs a qual apresenta as colunas:

 - id = Column(Integer, primary_key=True)
 - titulo = Column(String)
 - descricao = Column(String)
 - concluida = Column(Integer)

Além de apresentar as funções:
 - todo_listar(): Apresenta no terminal todas as tarefas criadas
 - todo_criar(titulo, descricao): Função para criar um novo TODO a partir de um título e de uma descrição
 - todo_update_status(id, status): Função que atualiza o status da tarefa usando 0 [Fazer], 1 [Fazendo] e 2 [Feito]
 - todo_delete(id): Função para excluir do banco de dados um TODO

## Como utilizar

Qualquer pessoa é livre para clonar este repositório e executar o código localmente. Para isso, siga as instruções abaixo:

1. Certifique-se de ter o Python 3 e "SQLAlchemy" instalados em seu sistema.
2. Clone este repositório para o seu ambiente local.

3. Navegue até o diretório do projeto.

4. Execute o código Python.

$ python application.py