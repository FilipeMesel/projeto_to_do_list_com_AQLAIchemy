# from database import init_database
from todo_list import todo_listar, todo_criar, todo_update_status, todo_delete

menu =  """
    [l] Listar TODOs
    [c] Criar TODO
    [u] Atualizar TODO
    [d] Delete TODO
=> """


while True:
    opcao = input(menu)

    if opcao == "l": #Ok
        print("Listar TODOs")
        todo_listar()

    elif opcao == "c": #Ok
        print("Criar TODO")
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        todo_criar(titulo, descricao)
        print("TODO Criado")

    elif opcao == "u": #Ok
        print("Atualizar TODO")
        if todo_listar() != False:
            id = input("Digite o id da tarefa: ")
            status = input("Digite o status. \r\nEscolha entre:\r\n0 [Fazer]\r\n1 [Fazendo]\r\n2 [Feito]\r\n")
            todo_update_status(id, status)
            print("TODO Atualizado")
        else:
            print("Lista de tarefas vazias")

    elif opcao == "d": #Ok
        print("Delete TODO")
        if todo_listar() != False:
            id = input("Digite o id da tarefa: ")
            todo_delete(id)
            print("TODO Excluído")
        else:
            print("Lista de tarefas vazias")

    elif opcao == "q": #Ok
        print("Finalizando a operação")
        break;

    else:
        print("opção inválida")