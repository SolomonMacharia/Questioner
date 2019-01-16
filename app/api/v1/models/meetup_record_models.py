from flask import jsonify, abort, json
from datetime import datetime
from uuid import uuid4

class MeetupRecord:
    """ Creates the meetup record model """
    def __init__(self):
        self.all_meetup_records = []

    def create_meetup(self, topic, location, images, tags):
        """ Adds a new question to the all_question_records list """
        new_meetup = {
            "meetupId": len(self.all_meetup_records) + 1,
            "topic": topic,
            "images": images,
            "tags": tags,
            "location": location,
            "createdOn": datetime.now(),
            # "happeningOn": json.loads(str(datetime))
        }
        self.all_meetup_records.append(new_meetup)
        return new_meetup

    def fetch_single_meetup(self, meetupId):
        """ Fetches a single meetup based on the meetupId"""
        meetup = [meetup for meetup in self.all_meetup_records if meetup['meetupId'] == meetupId]
        if meetup:
            return meetup
        return abort(404, "Error: Meetup {} does'nt exist.".format(meetupId))

    def delete_meetup(self, meetupId):
        """ Deletes a specific meetup record """
        Meetup = [Meetup for Meetup in self.all_meetup_records if Meetup['meetupId'] == meetupId]
        if Meetup:
            self.all_meetup_records.remove(Meetup[0])
        return abort(400, "Error: meetup {} doesn't exist!".format(meetupId))
        