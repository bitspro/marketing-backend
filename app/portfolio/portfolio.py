from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from pydantic import BaseModel
from pydantic import ValidationError




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/rizasjpp_marketing'
db = SQLAlchemy(app)




class Portfolio(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(db.Integer, primary_key=True)
    _images = db.Column("images", db.Text)  
    title = db.Column(db.String(126), nullable=True)
    description = db.Column(db.String(126), nullable=True)
    _services = db.Column("services", db.Text)  
    _technologies = db.Column("technologies", db.Text)

    def __init__(self, images, title, description, services, technologies):
        self.images = images
        self.title = title
        self.description = description
        self.services = services
        self.technologies = technologies

    @classmethod
    def create(cls, images, title, description, services, technologies):
        new_portfolio = cls(images, title, description, services, technologies)
        db.session.add(new_portfolio)
        db.session.commit()
        return new_portfolio

    @property
    def images(self):
        return json.loads(self._images)

    @images.setter
    def images(self, value):
        self._images = json.dumps(value) if value else "[]"

    @property
    def services(self):
        return json.loads(self._services)

    @services.setter
    def services(self, value):
        self._services = json.dumps(value) if value else "[]"

    @property
    def technologies(self):
        return json.loads(self._technologies)

    @technologies.setter
    def technologies(self, value):
        self._technologies = json.dumps(value) if value else "[]"

    def to_dict(self):
        return {
            'id': self.id,
            'images': self.images,
            'title': self.title,
            'description': self.description,
            'services': self.services,
            'technologies': self.technologies
        }

    def __repr__(self):
        return f'Portfolio(id={self.id}, title={self.title})'
    
db.create_all()





class RequestPortfolioCreate(BaseModel):
    images: list[str]
    title: str
    description: str
    services: list[str]
    technologies: list[str]




#Get Portfolio
@app.route('/portfolio', methods=['GET'])
def get_all_portfolios():
    try:
        portfolios = Portfolio.query.all()
        portfolio_data = []

        for portfolio in portfolios:
            portfolio_item = {
                'id': portfolio.id,
                'images': portfolio.images,
                'title': portfolio.title,
                'description': portfolio.description,
                'services': portfolio.services,
                'technologies': portfolio.technologies
            }
            portfolio_data.append(portfolio_item)

        return jsonify({'portfolios': portfolio_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    



#Create Portfolio
@app.route('/portfolio', methods=['POST'])
def create_portfolio():
    try:
        request_data = RequestPortfolioCreate(**request.json)
        new_portfolio = Portfolio(
            images=request_data.images,
            title=request_data.title,
            description=request_data.description,
            services=request_data.services,
            technologies=request_data.technologies
        )
        db.session.add(new_portfolio)
        db.session.commit()  

        return jsonify({'message': 'Portfolio entry created successfully!'})
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400





#Update Portfolio
@app.route('/portfolio/<int:portfolio_id>', methods=['PUT'])
def update_portfolio(portfolio_id):
    try:
        data = request.json

        portfolio = Portfolio.query.get(portfolio_id)

        if portfolio is None:
            return jsonify({'error': 'Portfolio not found'}), 404

        if 'images' in data:
            portfolio.images = data['images']
        if 'title' in data:
            portfolio.title = data['title']
        if 'description' in data:
            portfolio.description = data['description']
        if 'services' in data:
            portfolio.services = data['services']
        if 'technologies' in data:
            portfolio.technologies = data['technologies']

        db.session.commit()

        return jsonify({'message': 'Portfolio entry updated successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500






#Delete Portfolio
@app.route('/portfolio/<int:portfolio_id>', methods=['DELETE'])
def delete_portfolio(portfolio_id):
    try:
        portfolio = Portfolio.query.get(portfolio_id)

        if portfolio is None:
            return jsonify({'error': 'Portfolio not found'}), 404

        db.session.delete(portfolio)
        db.session.commit()

        return jsonify({'message': 'Portfolio entry deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500