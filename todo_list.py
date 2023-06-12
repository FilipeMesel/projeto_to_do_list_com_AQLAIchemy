from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'todo_list'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    concluida = Column(Integer)

def todo_listar():
    # Consultando todos os registros
    todos = session.query(ToDo).all()
    retorno = True
    if len(todos):
        for todo in todos:
            print(f"{todo.id}. {todo.titulo}")
            print(f"Descrição: {todo.descricao}")
            if todo.concluida == 0:
                print("Fazer")
            elif todo.concluida == 1:
                print("Fazendo") 
            elif todo.concluida == 2:
                print("Feito") 
            print("--------------------")
    else:
        retorno = False
    return retorno

def todo_criar(titulo, descricao):
    todo = ToDo(titulo=titulo, descricao=descricao, concluida=0)
    session.add(todo)
    session.commit()

def todo_update_status(id, status):
    # Atualizando um registro
    todo = session.query(ToDo).filter_by(id=id).first()
    todo.concluida = status
    session.commit()

def todo_delete(id):
    # Atualizando um registro
    todo = session.query(ToDo).filter_by(id=id).first()
    session.delete(todo)
    session.commit() 



  

engine = create_engine('sqlite:///meu_banco_de_dados.db')
Base.metadata.create_all(bind=engine)
session = Session(bind=engine)
