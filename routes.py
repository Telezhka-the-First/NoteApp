from flask import request, jsonify
from database import db_session
from models import Task

def init_routes(app):
    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        new_task = Task(title=data['title'])
        db_session.add(new_task)
        db_session.commit()
        return jsonify({'id': new_task.id, 'title': new_task.title}), 201

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = db_session.query(Task).all()
        return jsonify([{'id': task.id, 'title': task.title} for task in tasks])

    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = db_session.get(Task, task_id)
        if task:
            return jsonify({'id': task.id, 'title': task.title})
        return jsonify({'error': 'Task not found'}), 404

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        data = request.get_json()
        task = db_session.get(Task, task_id)
        if task:
            task.title = data['title']
            db_session.commit()
            return jsonify({'id': task.id, 'title': task.title})
        return jsonify({'error': 'Task not found'}), 404

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = db_session.get(Task, task_id)
        if task:
            db_session.delete(task)
            db_session.commit()
            return jsonify({'result': True})
        return jsonify({'error': 'Task not found'}), 404
