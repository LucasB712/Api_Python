from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_models.models import User, Task

db_engine = create_engine('sqlite:///base_tarefas.db', echo=True)
Session = sessionmaker (bind=db_engine)

#Create
def insert_dados(dados):
    with Session() as session:
        session.add(dados)
        session.commit()

#DELETE
def delete_dados(id1, Quem):
    with Session() as session:
        if Quem == 'User':
            user_to_delete = session.query(User).filter_by(id=id1).first()
        elif Quem == "Task":
            user_to_delete = session.query(User).filter_by(id=id1).first()
        session.delete(user_to_delete)
        session.commit()


#UPDATE
def update_dados_User(id1, names, emails, created):
    with Session() as session:
        user_to_update = session.query(User).filter_by(id=id1).first()

        user_to_update.name = names;
        user_to_update.email = emails;
        user_to_update.created = created;

        session.commit()

def update_dados_Task(id1, date, status,priority, task, user):
    with Session() as session:
        user_to_update = session.query(Task).filter_by(id=id1).first()

        user_to_update.updated = date ;
        user_to_update.priority = priority;
        user_to_update.status = status;
        user_to_update.task = task;
        user_to_update.userId = user;

        session.commit()

#READ
def read_dados_Task(Ide):
    with Session() as session:
        task = session.query(Task).filter(Task.id == Ide).first()
        return task

def read_dados_User(id1):
    with Session() as session:
        task = session.query(User).filter(User.id == id1).first()
        return task


    





