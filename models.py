from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/castingagency'#os.getenv('DATABASE_URI')
db = SQLAlchemy()


def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


# Helper table
songs = db.Table('songs',
                  db.Column('artist_id',
                            db.Integer,
                            db.ForeignKey('artist.id'),
                            primary_key=True),
                  db.Column('song_id',
                            db.Integer,
                            db.ForeignKey('song.id'),
                            primary_key=True))

# Artist

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    songs = db.relationship('Song', secondary=songs,
                             lazy='dynamic', backref=db.backref('artists'))

    def attributes(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


# Song

class Song(db.Model):
    __tablename = 'song'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    release_date = db.Column(db.DateTime())

    def attributes(self):
        return {
            'id': self.id,
            'title': self.title,
            'gente': self.genre,
            'release_date': self.release_date,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
