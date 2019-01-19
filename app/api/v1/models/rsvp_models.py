

all_rsvps = []

class RsvpModel:
    def __init__(self):
        self.db = all_rsvps
    def create_rsvp(self, topic, status):
        new_rsvp = {
            "meetupId": len(self.db) + 1,
            "topic": topic,
            "status": status
        }
        self.db.append(new_rsvp)
        return new_rsvp

