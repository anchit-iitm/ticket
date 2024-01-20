from flask import current_app as app, jsonify, request, make_response
from db.models import *
from security_framework import roles_accepted, current_user, auth_token_required
from flask_restful import Resource

class VenueShow(Resource):
    def get(self):
        venues = Venue.query.all()
        shows = Show.query.all()

        venues_data = []
        for venue in venues:
            venue_info = {
                'id': venue.id,
                'name': venue.name,
                'address': venue.address,
                'capacity': venue.capacity,
                'description': venue.description,
                'shows': []
            }
            for show in shows:
                if show.venue_id == venue.id:
                    show_info = {
                        'id': show.id,
                        'name': show.name,
                        'description': show.description,
                        'rating': show.rating,
                        'tags': show.tags,
                        'ticket_price': show.ticket_price,
                        'total_tickets': show.total_tickets,
                        'avialable_tickets': show.avail_ticket,
                    }
                    venue_info['shows'].append(show_info)
            venues_data.append(venue_info)

        return make_response(jsonify(venues_data), 200)