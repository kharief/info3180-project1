from . import db
from werkzeug.security import generate_password_hash


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property_information'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    numrooms= db.Column(db.Integer)
    numbathrooms= db.Column(db.Integer)
    price= db.Column(db.Float)
    propertytype = db.Column(db.String(80))
    location = db.Column(db.String(130))
    filename = db.Column(db.String(100))

    def __init__(self, title, description, numrooms, numbathrooms, price, propertytype, location, filename):
        self.title = title
        self.description = description
        self.numrooms = numrooms
        self.numbathrooms = numbathrooms
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.filename = filename

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support


    def __repr__(self):
        return '<ID %r>' % (self.id)