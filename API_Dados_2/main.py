from controlador import controladores
from crud.crud_main import read_dados, insert_dados, delete_dados, update_dados_User, update_dados_Task
from data_models.models import User, Task
#Configurar endpoints
from fastapi import FastAPI
#Levantar API
import uvicorn
from datetime import datetime

app = FastAPI()


#primeiro endpoint mais simples: get
@app.get('/primeiro_endpoint')
def meu_primeiro_endpoint():
    return 'Ola IDP, bora desenvolver na WEB'


@app.get('/Leitura')
def ler_tabela_task(entidade:int):
    if entidade == 1:
        tabela = Task
    if entidade == 2:
        tabela = User
    return read_dados(tabela)

@app.post('/insert_user')
def inserir_user(nome:str, emaill : str):
    usuario = User(name = nome,
                email = emaill, created = datetime.now())
                
    insert_dados(usuario)
    return 'Usuario inserido com sucesso'
                
@app.post('/insert_task')
def inserir_user(task_in:str, priority_in : str, status_in:str, userid_in : int):
    task = Task(created = datetime.now(), updated = datetime.now(),
             task = task_in,
            priority = priority_in, status = status_in, 
            userId = userid_in)
    insert_dados(task)
    return 'Task inserida com sucesso'

@app.delete('/delete')
def delete(id_in : int, Tabela: str):
    if Tabela == 'User':
        Tabela = User
    elif Tabela == 'Task':
        Tabela = Task
    else:
        return 'Tabela inválida!'
    delete_dados(id1 = id_in, Quem=Tabela)
    return 'Usuario deletado com sucesso'

@app.post('/update_user')
def update(id_in : int, nome : str, email: str):
    update_dados_User(id_in, nome, email)
    return 'Usuario atualizado com sucesso'

@app.post('/update_task')
def update(id_in : int, date : datetime, status: str, priority:str, task : str, user: str):
    update_dados_Task(id_in, date, status, priority, task, user)
    return 'Usuario atualizado com sucesso'



#JSON: String formatada, em aspas duplas, com várias chaves e colchetes
#Extração, Transação e carregamento (ETL)
#Swagger : modelo padrão de documentação (OPEN API, versionado)

uvicorn.run(app, host = '0.0.0.0', port = 8888)