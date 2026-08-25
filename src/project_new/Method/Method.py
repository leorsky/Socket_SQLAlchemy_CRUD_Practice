from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from project_new.src.project_new.Base.Base import Base
from project_new.src.project_new.Table.tasks import Tasks

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)




def method_post(title: str, description: str, completed: bool) -> str:
    with SessionLocal() as session:
        try:
            task1 = Tasks(title=title, description=description, completed=completed)

            session.add(task1)
            session.commit()
            session.refresh(task1)

            print(f'Задача добавлена: {task1.id} - {task1.title} - {task1.description} - {task1.completed} - {task1.created_at}')

            return 'HTTP 201 OK'

        except Exception as e:
            session.rollback()
            print(f'Сбой: {e}')
            return f'HTTP 500 {e}'