from App import app, db
from App.models import User

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицы
        if User.query.count() == 0:  # Если нет пользователей, добавим одного
            user = User(name='Default User', email='user@example.com', password='password')
            db.session.add(user)
            db.session.commit()
    app.run(debug=True)

