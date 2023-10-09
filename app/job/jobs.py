from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel
from pydantic import ValidationError



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/rizasjpp_marketing'
db = SQLAlchemy(app)




class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    location = db.Column(db.String(256), nullable=True)

    def __init__(self, title, description, location):
        self.title = title
        self.description = description
        self.location = location

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location
        }

    def __repr__(self):
        return f'Job(id={self.id}, title={self.title})'
    
db.create_all()



class RequestJobCreate(BaseModel):
    title: str
    description: str
    location: str




#Get Jobs
@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    try:
        jobs = Job.query.all()
        job_data = []

        for job in jobs:
            job_item = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location
            }
            job_data.append(job_item)

        return jsonify({'jobs': job_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500






#Create Jobs
@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        request_data = RequestJobCreate(**request.json)
        new_job = Job(
            title=request_data.title,
            description=request_data.description,
            location=request_data.location
        )
        db.session.add(new_job)
        db.session.commit()

        return jsonify({'message': 'Job entry created successfully!'})
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    




#Update Jobs
@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        data = request.json

        job = Job.query.get(job_id)

        if job is None:
            return jsonify({'error': 'Job not found'}), 404

        if 'title' in data:
            job.title = data['title']
        if 'description' in data:
            job.description = data['description']
    
        if 'location' in data:
            job.technologies = data['location']

        db.session.commit()

        return jsonify({'message': 'Job entry updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500




#Delete Jobs
@app.route('/job/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    try:
        job = Job.query.get(job_id)

        if job is None:
            return jsonify({'error': 'Job not found'}), 404

        db.session.delete(job)
        db.session.commit()

        return jsonify({'message': 'Job entry deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500