from flask import Blueprint, jsonify, request, abort
from data import db_session
from data.jobs import Job


blueprint = Blueprint('jobs_api', __name__, url_prefix='/api')


def abort_if_job_not_found(job_id):
    db_sess = db_session.create_session()
    job = db_sess.get(Job, job_id)
    if not job:
        abort(404, description=f"Работа с ID {job_id} не найдена")


@blueprint.route('/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify({
        'jobs': [job.to_dict() for job in jobs]
    })


@blueprint.route('/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    abort_if_job_not_found(job_id)
    db_sess = db_session.create_session()
    job = db_sess.get(Job, job_id)
    return jsonify({
        'job': job.to_dict()
    })


@blueprint.route('/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'}), 400

    required_fields = {
        'job_title': str,
        'team_leader_id': int,
        'work_size': int,
        'collaborators': str,
        'is_finished': bool,
        'hazard_category_id': int
    }

    for field, field_type in required_fields.items():
        if field not in request.json:
            return jsonify({'error': f'Missing field: {field}'}), 400
        if not isinstance(request.json[field], field_type):
            return jsonify({'error': f'Field {field} must be of type {field_type.__name__}'}), 400

    db_sess = db_session.create_session()

    job = Job(
        job_title=request.json['job_title'],
        team_leader_id=request.json['team_leader_id'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        hazard_category_id=request.json['hazard_category_id']
    )

    db_sess.add(job)
    db_sess.commit()

    return jsonify({'id': job.id}), 201


@blueprint.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    abort_if_job_not_found(job_id)
    db_sess = db_session.create_session()
    job = db_sess.get(Job, job_id)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'Работа успешно удалена'})


@blueprint.route('/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    abort_if_job_not_found(job_id)

    if not request.json:
        return jsonify({'error': 'Empty request'}), 400

    db_sess = db_session.create_session()
    job = db_sess.get(Job, job_id)

    update_fields = {
        'job_title': str,
        'team_leader_id': int,
        'work_size': int,
        'collaborators': str,
        'is_finished': bool,
        'hazard_category_id': int
    }

    for field, field_type in update_fields.items():
        if field in request.json:
            if isinstance(request.json[field], field_type):
                setattr(job, field, request.json[field])
            else:
                return jsonify({'error': f'Field {field} must be of type {field_type.__name__}'}), 400

    db_sess.commit()
    return jsonify({'success': 'Работа обновлена'})