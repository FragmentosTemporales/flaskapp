from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
migrate = Migrate()

class Base(db.Model):
    """ Model that contains base database models. """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save_to_db(self):
        """ Saving into db """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, **kwargs):
        """  Updating into db """
        for key, value in kwargs.items():
            setattr(self, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_from_db(self):
        """ Deleting from database """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        """ Find by id """
        return cls.query.filter_by(id=id).first()

class User(Base):
    __tablename__ = 'user'
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_disabled = db.Column(db.Boolean, default=False)

    def serialize(self):
        """ Return the user data """
        return {
            "id": self.id,
            "email": self.email,
            "is_disabled": self.is_disabled,
        }

    def set_password(self, password):
        """ Setting password for user """
        self.password = generate_password_hash(password)

    def set_email_lower(self, email):
        """Setting the lowercase email"""
        self.email = email.lower()

    def check_password(self, password):
        """ Checking password for user """
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_email(cls, email):
        """ Find user by email address """
        email_lower = email.lower()
        return cls.query.filter_by(email=email_lower).first()

    @staticmethod
    def exists(email):
        """ Check if user exists """
        email_lower = email.lower()
        user = User.find_by_email(email_lower)
        if user:
            return True
        return False