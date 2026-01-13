from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username="Mozelli", password="12345", email="joaomozelli@gmail.com"
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "Mozelli"))

    assert asdict(user) == {
        'id': 1,
        'username': 'Mozelli',
        'password': '12345',
        'email': 'joaomozelli@gmail.com',
        'created_at': time,
        'updated_at': time,
    }
