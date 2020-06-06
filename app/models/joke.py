from . import db
from sqlalchemy.event import listen
from sqlalchemy import desc, asc


class Joke(db.Model):
    __tablename__ = "jokes"

    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=db.func.current_timestamp()
    )

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Joke.id) if order == "desc" else asc(Joke.id)
        return Joke.query.order_by(sort).paginate(page, per_page).items

    def __str__(self):
        return self.joke


def insert_jokes(*args, **kwargs):
    db.session.add(
        Joke(
            joke="What is the most loyal tool of a programmer? Git, because of its COMMITment!"
        )
    )
    db.session.commit()  # Persist


listen(Joke.__table__, "after_create", insert_jokes)
