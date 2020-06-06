from flask import Blueprint, request
from .responses import response, not_found
from .models.joke import Joke
from .schemas import joke_schema, jokes_schema, params_joke_schema

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")


def set_joke(function):
    def wrapper(*args, **kwargs):
        id = kwargs.get("id", 0)
        joke = Joke.query.filter_by(id=id).first()

        if joke is None:
            return not_found()

        return function(joke)

    wrapper.__name__ = function.__name__
    return wrapper


@api_v1.route("/jokes", methods=["GET"])
def get_jokes():
    page = int(request.args.get("page", 1))  # Dict
    order = request.args.get("order", "desc")

    jokes = Joke.get_by_page(order, page)

    return response(jokes_schema.dump(jokes))


@api_v1.route("/jokes/<id>", methods=["GET"])
@set_joke
def get_joke(joke):
    return response(joke_schema.dump(joke))
