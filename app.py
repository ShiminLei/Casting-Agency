import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import db, setup_db, Artist, Song, songs


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    @app.route('/')
    def index():
        return "This is the demo page of Casting Agency." \
            " Feel free to try each endpoint with different roles." + app.config.get('SQLALCHEMY_DATABASE_URI')

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, PUT, POST, DELETE, OPTIONS'
        )
        return response

    # @app.route('/artists')
    # @requires_auth('view:artists')
    @app.route('/artists')
    def get_artists():
        artists = [artist.attributes() for artist in Artist.query.order_by(Artist.id).all()]
        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": 'OK',
            "artists": artists
        })    

    # @app.route('/songs')
    # @requires_auth('view:songs')
    @app.route('/songs')
    def get_songs():
        songs = [song.attributes() for song in Song.query.order_by(Song.id).all()]

        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": 'OK',
            "songs": songs
        })

    @app.route('/artists/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:artists')
    def delete_artists(id):
        target_artist = Artist.query.filter(Artist.id == id).one_or_none()
        if target_artist is None:
            abort(404)
        target_artist.delete()

        return jsonify({"success": True,
                        "status_code": 200,
                        "status_message": 'OK',
                        "id_deleted": id})

    @app.route('/songs/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:songs')
    def delete_songs(id):
        target_song = Song.query.filter(Song.id == id).one_or_none()
        if target_song is None:
            abort(404)
        target_song.delete()

        return jsonify({"success": True,
                        "status_code": 200,
                        "status_message": 'OK',
                        "id_deleted": id})

    @app.route('/artists', methods=['POST'])
    @requires_auth(permission='add:artists')
    def post_artists():

        name = request.json.get("name", None)
        age = request.json.get("age", None)
        gender = request.json.get("gender", None)

        if name is None:
            abort(422)

        new_artist = Artist(name=name, age=age, gender=gender)
        new_artist.insert()

        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": "OK",
            "artist": new_artist.attributes()
        })

    # @app.route('/songs', methods=['POST'])
    # @requires_auth(permission='add:songs')
    @app.route('/songs', methods=['POST'])
    def post_songs():

        title = request.json.get("title", None)
        genre = request.json.get("genre", None)
        release_date = request.json.get("release_date", None)

        if title is None:
            abort(422)

        new_song = Song(title=title, genre=genre, release_date=release_date)
        new_song.insert()

        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": 'OK',
            "song": new_song.attributes()
        })

    @app.route('/artists/<int:id>', methods=['PATCH'])
    @requires_auth(permission='edit:artists')
    def patch_artists(id):
        name = request.json.get("name", None)
        age = title = request.json.get("age", None)
        gender = title = request.json.get("gender", None)
        target_artist = Artist.query.filter(Artist.id == id).one_or_none()
        if target_artist is None:
            abort(404)
        if name is None:
            abort(422)

        target_artist.name = name
        target_artist.age = age
        target_artist.gender = gender
        target_artist.update()

        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": 'OK',
            "artist": target_artist.attributes()
        })

    @app.route('/songs/<int:id>', methods=['PATCH'])
    @requires_auth(permission='edit:songs')
    def patch_songs(id):
        title = request.json.get("title", None)
        genre = request.json.get("genre", None)
        release_date = request.json.get("release_date", None)
        target_song = Song.query.filter(Song.id == id).one_or_none()

        if target_song is None:
            abort(404)

        if title is None:
            abort(422)

        target_song.title = title
        target_song.genre = genre
        target_song.release_date = release_date
        target_song.update()

        return jsonify({
            "success": True,
            "status_code": 200,
            "status_message": 'OK',
            "song": target_song.attributes()
        })

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "status_message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "status_message": "resource Not found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify(error.error), error.status_code

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
