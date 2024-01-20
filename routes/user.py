from flask import current_app as app, jsonify, request, make_response
from db.models import *
from security_framework import roles_accepted, current_user, auth_token_required
from flask_restful import Resource

class list_venues(Resource):
    def get(self):
        def extract_venue_data(venue):
            return {
                'id': venue.id,
                'name': venue.name,
                'address': venue.address,
                'description': venue.description,
            }

        def extract_shows_for_venue(venue):
            shows = Show.query.filter_by(venue_id=venue.id).all()
            return [
                {
                    'id': show.id,
                    'name': show.name,
                    'description': show.description,
                    'rating': show.rating,
                    'tags': show.tags,
                    'ticket_price': show.ticket_price,
                    'total_tickets': show.avail_ticket,
                }
                for show in shows
            ]
        try:
            venues = Venue.query.all()
            venues_data = []

            for venue in venues:
                venue_data = extract_venue_data(venue)
                venue_data['shows'] = extract_shows_for_venue(venue)
                venues_data.append(venue_data)

            return make_response(jsonify(venues_data), 200)

        except Exception as e:
            return make_response(jsonify({'message': 'An error occurred while fetching venues'}), 500)
        
class list_show(Resource):
    def get(self, show_id):
        show = db.session.get(Show, show_id)
        if not show:
            return make_response(jsonify({'message': 'Show not found'}), 404)
        try:
            show_data = {
                'id': show.id,
                'name': show.name,
                'description': show.description,
                'rating': show.rating,
                'tags': show.tags,
                'ticket_price': show.ticket_price,
                'total_tickets': show.avail_ticket,
            }
            return make_response(jsonify(show_data), 200)
        except Exception as e:
            return make_response(jsonify({'message': 'An error occurred while fetching show'}), 500)
        
class create_booking(Resource):
    def post(self):
        data = request.get_json()
        show_id = data.get('show_id')
        num_tickets = int(data['number_of_tickets'])
        userid = data.get('uid')
        # print(current_user.id)
        # show = Show.query.get(show_id)
        show = db.session.get(Show, show_id)

        if not show:
            return make_response(jsonify({'message': 'Show not found'}), 404)

        if show.total_tickets < num_tickets:
            return make_response(jsonify({'message': 'Not enough available tickets'}), 400)

        try:
            total_amount = show.ticket_price * num_tickets
            new_booking = Booking(user_id=userid, show_id=show_id, number_of_tickets=num_tickets, total_amount=total_amount, booking_date=datetime.now())
            show.avail_ticket -= num_tickets  # Update the available tickets for the show
            db.session.add(new_booking)
            activity = UserActivity(user_id=userid, activity_type='booking')
            db.session.add(activity)
            db.session.commit()
            return make_response(jsonify({'message': 'Ticket booked successfully'}), 200)
        except:
            db.session.rollback()
            return make_response(jsonify({'message': 'An error occurred while booking the ticket'}), 500)