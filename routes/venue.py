from flask import current_app as app, jsonify, request, make_response
from db.models import *
from security_framework import roles_accepted, current_user, auth_token_required
from flask_restful import Resource

class allvenue(Resource):
    # @roles_accepted('admin')
    # @auth_token_required
    def post(self):
        data = request.get_json()
        name = data['name']
        address = data['address']
        capacity = data['capacity']
        description = data['description']

        try:
            # Create a new venue record in the database
            venue = Venue(name=name, address=address, capacity=capacity, description=description)
            db.session.add(venue)
            db.session.commit()

            return make_response(jsonify({'message': 'Venue created successfully'}), 200)
        except:
            # Handle the case when error
            return make_response(jsonify({'message': 'some error occured.'}), 400)


class singlevenue(Resource):
    def patch(self, id):
        venue = Venue.query.get(id)
        if not venue:
            return make_response(jsonify({'message': 'Venue not found'}), 404)
        data = request.get_json()
        capacity = data.get('capacity')
        description = data.get('description')

        if capacity is not None:
            venue.capacity = capacity
        if description is not None:
            venue.description = description

        db.session.commit()
        return make_response(jsonify({'message': 'Venue updated successfully'}), 200)
    
    def get(self, id):
        venue = Venue.query.get(id)
        if venue:
            venue_info = {
                'id': venue.id,
                'name': venue.name,
                'address': venue.address,
                'capacity': venue.capacity,
                'description': venue.description,
            }
            return make_response(jsonify(venue_info), 200)
        return make_response(jsonify({'message': 'Venue not found'}), 404)