from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'EXEMPLO.db'  
db = SQLAlchemy(app)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    artist = db.Column(db.String(120), unique=False, nullable=False)

@app.route('/music', methods=['POST'])
def add_music():
    data = request.get_json()
    music = Music(name=data['name'], artist=data['artist'])
    db.session.add(music)
    db.session.commit()
    return jsonify({'message': 'Música adicionada com sucesso!'})

@app.route('/music', methods=['GET'])
def get_music():
    music_list = Music.query.all()
    return jsonify([{'name': music.name, 'artist': music.artist} for music in music_list])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


#Terminal

# Traceback (most recent call last):
#   File "c:\Users\Engu\Desktop\provinha\Questão 3\ORM Spotify.py", line 27, in <module>
#     db.create_all()
#   File "C:\Users\Engu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\flask_sqlalchemy\extension.py", line 900, in create_all
#     self._call_for_binds(bind_key, "create_all")
#   File "C:\Users\Engu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\flask_sqlalchemy\extension.py", line 871, in _call_for_binds
#     engine = self.engines[key]
#              ^^^^^^^^^^^^
#   File "C:\Users\Engu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\flask_sqlalchemy\extension.py", line 687, in engines
#     app = current_app._get_current_object()  # type: ignore[attr-defined]
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Engu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\werkzeug\local.py", line 508, in _get_current_object
#     raise RuntimeError(unbound_message) from None
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# the current application. To solve this, set up an application context
# with app.app_context(). See the documentation for more information.
