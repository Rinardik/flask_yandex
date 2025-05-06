from flask import Blueprint, jsonify, request, abort
from data import db_session
from data.users import User


blueprint = Blueprint('users_api', __name__, url_prefix='/api')


def abort_if_user_not_found(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        abort(404, description=f"Пользователь с ID {user_id} не найден")


@blueprint.route('/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify({
        'users': [user.to_dict() for user in users]
    })


@blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    abort_if_user_not_found(user_id)
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    return jsonify({
        'user': user.to_dict()
    })


@blueprint.route('/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'}), 400

    required_fields = {
        'surname': str,
        'name': str,
        'age': int,
        'position': str,
        'speciality': str,
        'address': str,
        'email': str,
        'hashed_password': str
    }

    for field, field_type in required_fields.items():
        if field not in request.json:
            return jsonify({'error': f'Missing field: {field}'}), 400
        if not isinstance(request.json[field], field_type):
            return jsonify({'error': f'Field {field} must be of type {field_type.__name__}'}), 400

    db_sess = db_session.create_session()

    # Проверяем, нет ли уже пользователя с таким email
    existing_user = db_sess.query(User).filter(User.email == request.json['email']).first()
    if existing_user:
        return jsonify({'error': 'User with this email already exists'}), 400

    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password']
    )

    db_sess.add(user)
    db_sess.commit()

    return jsonify({'id': user.id}), 201


@blueprint.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    abort_if_user_not_found(user_id)

    if not request.json:
        return jsonify({'error': 'Empty request'}), 400

    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)

    allowed_fields = {
        'surname': str,
        'name': str,
        'age': int,
        'position': str,
        'speciality': str,
        'address': str,
        'email': str,
        'hashed_password': str
    }

    for field, field_type in allowed_fields.items():
        if field in request.json:
            if isinstance(request.json[field], field_type):
                setattr(user, field, request.json[field])
            else:
                return jsonify({'error': f'Field {field} must be of type {field_type.__name__}'}), 400

    db_sess.commit()
    return jsonify({'success': 'Пользователь обновлён'})


@blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    abort_if_user_not_found(user_id)
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'Пользователь удалён'})