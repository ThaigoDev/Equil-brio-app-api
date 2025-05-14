from flask import Flask, request, jsonify
from database.db_setup import db
from models import User, Mood  
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postup!@localhost:5432/equilibrio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=data['password']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado', 'user_id': user.id}), 201

@app.route('/moods', methods=['POST'])
def create_mood():
    data = request.get_json()
    mood = Mood(
        user_id=data['user_id'],
        mood=data['mood'],
        note=data.get('note')
    )
    db.session.add(mood)
    db.session.commit()
    return jsonify({'message': 'Humor registrado'}), 201

@app.route('/moods/<int:user_id>', methods=['GET'])
def get_moods(user_id):
    moods = Mood.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': m.id,
        'mood': m.mood,
        'note': m.note,
        'recorded_at': m.recorded_at.isoformat()
    } for m in moods])

if __name__ == '__main__':
    app.run(debug=True)
