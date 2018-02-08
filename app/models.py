__author__ = 'Bing'

from datetime import datetime
from app import db


class Domain(db.Model):
    __tablename__ = 'domains'
    id = db.Column(db.Integer, primary_key=True)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(20), index=True, unique=True)
    description = db.Column(db.Text)
    type = db.Column(db.String(30))
    registry = db.Column(db.String(100))
    status = db.Column(db.String(20))
    cate = db.Column(db.String(30))
    popular = db.Column(db.Integer)
    restrictions = db.Column(db.String(200))
    sources = db.Column(db.Text)

    prices = db.relationship('Price', backref='domain')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Domain %r>' % self.name


class Registrar(db.Model):
    __tablename__ = 'registrars'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), index=True, unique=True)
    name = db.Column(db.String(30), unique=True)
    url = db.Column(db.String(30))
    rating = db.Column(db.Float)

    prices = db.relationship('Price', backref='registrar')


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Name %r' % self.name


class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    register = db.Column(db.Float)
    renewal = db.Column(db.Float)
    transfer = db.Column(db.Float)
    whois = db.Column(db.Float)

    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'))
    registrar_id = db.Column(db.Integer, db.ForeignKey('registrars.id'))


class Cheapest(db.Model):
    __tablename__ = 'cheapest'
    id = db.Column(db.Integer, primary_key=True)
    extension = db.Column(db.String(20))
    reg_registrar = db.Column(db.String(20))
    reg_price = db.Column(db.Float)
    renew_registrar = db.Column(db.String(20))
    renew_price = db.Column(db.Float)
    tran_registrar = db.Column(db.String(20))
    tran_price = db.Column(db.Float)
    popularity = db.Column(db.Integer)


    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()

        for i in range(count):
            u = Cheapest(extension=forgery_py.lorem_ipsum.word(),
                         reg_registrar=forgery_py.lorem_ipsum.word(),
                         reg_price=float(forgery_py.monetary.formatted_money()),
                         renew_registrar=forgery_py.lorem_ipsum.word(),
                         renew_price=float(forgery_py.monetary.formatted_money()),
                         tran_registrar=forgery_py.lorem_ipsum.word(),
                         tran_price=float(forgery_py.monetary.formatted_money()),
                         popularity=int(forgery_py.basic.number())
            )

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py
        seed()

        for i in range(count):
            u = User(username=forgery_py.name.full_name(),
                     email=forgery_py.email.address(),
                     password=forgery_py.basic.password())

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
