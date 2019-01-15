from flask import Blueprint, request, jsonify
from app.api.v1.models.rsvp_models import RsvpModel

v1_rsvp_blueprint = Blueprint('rsvp', __name__, url_prefix='/api/v1')


@v1_rsvp_blueprint.route('/meetups/<int:meetupId>/rsvps', methods=['POST'])
def post_rsvp(meetupId):
    data = request.json
    meetupId = data['meetupId']
    topic = data["topic"]
    status = data["status"]
    if data:
        reserve = RsvpModel().create_rsvp(meetupId, topic, status)
    return jsonify({"status":201, "Meeup rsvp": reserve}), 201