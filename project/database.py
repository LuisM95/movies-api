import hashlib
from peewee import *
from datetime import datetime

database = MySQLDatabase('fastapi_movies',
                        user='root',
                        password='luismme1995',
                        host='localhost',
                        port=3306)


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.username
    
    class Meta:
        database = database
        table_name = 'users'

    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()
    
    @classmethod
    def authenticate(cls, username, password):
        user = cls.select().where(User.username == username).first()

        if user and user.password == cls.create_password(password):
            return user

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
    class Meta:
        database = database
        table_name = 'movies'

class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie)
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
    
    class Meta:
        database = database
        table_name = 'user_reviews'