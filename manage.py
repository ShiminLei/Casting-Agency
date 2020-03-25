from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db, Song, Artist, songs

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    Song(title='Love You', genre='Blue', release_date='2012-1-1').insert()
    Song(title='The World', genre='Jazz', release_date='2019-8-12').insert()
    Song(title='Frozen', genre='Blue', release_date='2011-12-12').insert()

    Artist(name='Edward', age=36, gender='male').insert()
    Artist(name='Mike', age=25, gender='male').insert()
    Artist(name='Jeff', age=35, gender='female').insert()


if __name__ == '__main__':
    manager.run()
