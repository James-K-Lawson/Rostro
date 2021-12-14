from app import db

class RosterForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    roster_name = db.Column(db.String(120))

    def __repr__(self):
        return '<{} Roster>'.format(self.username)