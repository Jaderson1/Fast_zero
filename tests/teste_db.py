from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def teste_creat_user():
    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username='jaderson', email='jaderson@gmail.com', password='senha'
        )

        session.add(user)
        session.commit()
        session.refresh(user)

    assert user.id == 1
