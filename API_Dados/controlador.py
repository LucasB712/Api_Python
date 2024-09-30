from crud.crud_main import insert_dados, delete_dados, read_dados_Task, read_dados_User, update_dados_User, update_dados_Task
from data_models.models import User, Task
from datetime import datetime


def controladores(): 
    User2 = User(id = 10, name = "Pedro", email = "pedro@idp.edu.br", created = datetime.now())

    Task2 = Task(id = 10, created = datetime.now(), updated = datetime.now(), task = "Trabalho IN", priority = "Estruturar tabelas", status = "Em andamento", userId = 5)

    #INSERT
    insert_dados(User2)
    insert_dados(Task2)


    #DELETE 
    delete_dados(3, 'User')
    delete_dados(4, 'Task')


    #UPDATE
    update_dados_User(1, 'marcos', 'marquinhos@exemplo.com', datetime.now());
    update_dados_Task(2, datetime.now(), 'Em andamento', 'Rigida', 'trabalhar', 5);


    #READ
    user = read_dados_User(1)
    if user:
        print(f"Usuário encontrado: {user.name}, {user.email}, {user.created}")
    else:
        print("Nenhum usuário encontrado.")

    task = read_dados_Task(2)
    if task: 
        print(f'Usuario encontrado: {task.task}, {task.created}', {task.id}, {task.priority}, {task.updated}, {task.userId}, {task.status})
    else:
        print("Nenhum usuário encontrado.")