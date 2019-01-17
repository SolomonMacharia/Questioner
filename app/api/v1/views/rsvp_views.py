from flask import Blueprint, request, jsonify
from app.api.v1.models.rsvp_models import RsvpModel
from ..utils.validators import validate

v1_rsvp_blueprint = Blueprint('rsvp', __name__, url_prefix='/api/v1')


@v1_rsvp_blueprint.route('/meetups/<int:meetupId>/rsvps', methods=['POST'])
def post_rsvp(meetupId):
    rsvp_data = request.get_json()
    data = validate(rsvp_data, required_fields=["meetupId", "topic", "status"])
    if type(data) == list:
        return jsonify({"status": 400, "error": data}), 400
    meetupId = data['meetupId']
    topic = data["topic"]
    status = data["status"]

    reserve = RsvpModel().create_rsvp(meetupId, topic, status)
    return jsonify({"status":201, "Meeup rsvp": reserve}), 201