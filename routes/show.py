from flask import current_app as app, jsonify, request, make_response
from db.models import *
from security_framework import roles_accepted, current_user, auth_token_required
from flask_restful import Resource

class eachshow(Resource):
    def get(self, show_id, venue_id):
        show = Show.query.filter_by(id=show_id, venue_id=venue_id).first()

        if not show:
            return jsonify({'message': 'Show not found'}), 404
        
        if request.method == 'GET':
            show_info = {
                'id': show.id,
                'name': show.name,
                'description': show.description,
                'rating': show.rating,
                'tags': show.tags,
                'ticket_price': show.ticket_price,
                'venue_id': show.venue_id,
                'total_tickets': show.total_tickets
            }
            return make_response(jsonify(show_info), 200)
        
    def put(self, show_id, venue_id):
        show = Show.query.filter_by(id=show_id, venue_id=venue_id).first()
        data = request.get_json()
        description = data.get('description')
        rating = data.get('rating')
        tags = data.get('tags')
        ticket_price = data.get('ticket_price')
        total_tickets = data.get('total_tickets')

        if rating is not None:
            show.rating = rating
        if tags is not None:
            show.tags = tags
        if ticket_price is not None:
            show.ticket_price = ticket_price
        if total_tickets is not None:
            show.total_tickets = total_tickets
            show.avail_ticket = total_tickets
        if description is not None:
            show.description = description
        
        # show.name = show.name
        # show.venue_id = show.venue_id

        try:
            db.session.commit()
            return make_response(jsonify({'message': 'Show modified successfully'}), 200)
        except:
            db.session.rollback()
            return make_response(jsonify({'message': 'Error modifying show'}), 500)
        
    def delete(self, show_id, venue_id):
        show = Show.query.filter_by(id=show_id, venue_id=venue_id).first()

        if not show:
            return make_response(jsonify({'message': 'Show not found'}), 404)

        try:
            db.session.delete(show)
            db.session.commit()
            return make_response(jsonify({'message': 'Show deleted successfully'}), 200)
        except:
            db.session.rollback()
            return make_response(jsonify({'message': 'Error deleting show'}), 500)
        
class show(Resource):
    def post(self):
        data = request.get_json()
        name = data['name']
        description = data['description']
        rating = data['rating']
        tags = data['tags']
        ticket_price = data['ticket_price']
        total_tickets = data['total_tickets']
        venue_id = data['venue_id']
        try:
            new_show = Show(name=name, rating=rating, tags=tags, ticket_price=ticket_price, venue_id=venue_id, total_tickets=total_tickets, avail_ticket=total_tickets, description=description)
            db.session.add(new_show)
            db.session.commit()
            return make_response(jsonify({'message': 'Show has been created successfully'}), 200)
        except Exception as e:
            # print(e)
            db.session.rollback()
            # Handle any error that may occur during show creation
            return make_response(jsonify({'message' : 'Error creating show'}), 500)