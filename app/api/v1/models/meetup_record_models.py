from flask import jsonify, abort
from datetime import datetime
from uuid import uuid4

class MeetupRecord:
    """ Creates the meetup record model """
    def __init__(self, *args):
        self.all_meetup_records = []

    def create_meetup(self, meetupId, createdOn, location, images, happeningOn, tags):
        """ Adds a new question to the all_question_records list """
        self.meetupId = meetupId
        self.createdOn = datetime.now()
        self.location = location
        self.images = images
        self.happeningOn = happeningOn
        self.tags = tags

        new_meetup = {
        "status": 201,
        "data": [{
            "id": uuid4().int,
            "topic": "The topic",
            "location": "The venue",
            "happeningOn": "The meetup date.",
            "tags": ["tag1", "tag2", "tag3"]
        }]
    }
        self.all_meetup_records.append(new_meetup)

    def fetch_single_meetup(self, meetupId):
        """ Fetches a single meetup based on the meetupId"""
        for meetup in self.all_meetup_records:
            if meetupId == int(meetupId):
                return meetup
        return abort(404, "Error: Meetup {} does'nt exist.".format(meetupId))
