from app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(50), nullable=False)
    tahun_rilis = db.Column(db.Integer, nullable=False)
    sutradara = db.Column(db.String(50), nullable=False)
    pemain = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.judul
