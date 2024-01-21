from flask import current_app as app, jsonify, request, make_response
from db.models import *
from security_framework import roles_accepted, current_user, auth_token_required
from flask_restful import Resource
from sqlalchemy import or_


class search_theatres(Resource):
    def get(self):
        location = request.args.get('location', '').strip()

        if location:
            theatres = Venue.query.filter(or_(
                Venue.name.ilike(f'%{location}%'),
                Venue.address.ilike(f'%{location}%')
            )).all()
        else:
            theatres = []

        return make_response(jsonify([theatre.search() for theatre in theatres]))
    
class search_shows(Resource):
    def get(self):
        tags = request.args.get('tags', '').strip()
        rating = request.args.get('rating', 0.0)

        if tags:
            shows = Show.query.filter(Show.tags.ilike(f'%{tags}%')).all()
        else:
            shows = []

        # Filter shows by rating
        filtered_shows = [show for show in shows if show.rating >= float(rating)]

        return make_response(jsonify([show.search() for show in filtered_shows]))