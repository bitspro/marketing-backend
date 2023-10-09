from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel
from pydantic import ValidationError
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/rizasjpp_marketing'
db = SQLAlchemy(app)



class Services(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(126), nullable=True)
    excerpt = db.Column(db.String(126), nullable=True)
    _services = db.Column("services", db.Text)  # Rename the column for JSON data
    icon = db.Column(db.String(126), nullable=True)
    title = db.Column(db.String(126), nullable=True)

    def __init__(self, description, excerpt, services, icon, title):
        self.description = description
        self.excerpt = excerpt
        self.services = services
        self.icon = icon
        self.title = title

    @classmethod
    def create(cls, description, excerpt, services, icon, title):
        new_service = cls(description, excerpt, services, icon, title)
        db.session.add(new_service)
        db.session.commit()
        return new_service

    @property
    def services(self):
        return json.loads(self._services)

    @services.setter
    def services(self, value):
        self._services = json.dumps(value) if value else "[]"

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'excerpt': self.excerpt,
            'services': self.services,
            'icon': self.icon,
            'title': self.title
        }

    def __repr__(self):
        return f'Portfolio(id={self.id}, title={self.title})'
    
db.create_all()




class RequestservicesCreate(BaseModel):
    description:str
    excerpt: str
    services: list[str]
    icon:str
    title : str




#Get services
@app.route('/services', methods=['GET'])
def get_all_services():
    try:
        services = Services.query.all()
        services_data = []

        for service in services:
            services_item = {
                'id': service.id,
                'description': service.description,
                'excerpt': service.excerpt,
                'services': service.services,
                'icon': service.icon,
                'title': service.title,
            }
            services_data.append(services_item)

        return jsonify({'services': services_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    



#Create Services
@app.route('/services', methods=['POST'])
def create_services():
    try:
        request_data = RequestservicesCreate(**request.json)
        new_services = Services(
            description= request_data.description,
            excerpt = request_data.excerpt,
            services=request_data.services,
            icon = request_data.icon,
            title=request_data.title,
        )
        db.session.add(new_services)
        db.session.commit()  

        return jsonify({'message': 'services entry created successfully!'})
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    




#Update Services
@app.route('/service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        data = request.json

        services = Services.query.get(service_id)

        if services is None:
            return jsonify({'error': 'Portfolio not found'}), 404

        if 'description' in data:
            services.description = data['description']

        if 'excerpt' in data:
            services.excerpt = data['excerpt']
       
        if 'services' in data:
            services.services = data['services']

        if 'icon' in data:
            services.icon = data['icon']

        if 'title' in data:
            services.title = data['title']

        db.session.commit()

        return jsonify({'message': 'services entry updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500





#Delete Services
@app.route('/service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Services.query.get(service_id)

        if service is None:
            return jsonify({'error': 'Service not found'}), 404

        db.session.delete(service)
        db.session.commit()

        return jsonify({'message': 'Service entry deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500