from flask import jsonify


def response(data):
    return jsonify({"success": True, "data": data}), 200


def not_found():
    return (
        jsonify(
            {
                "success": False,
                "data": {},
                "message": "Joke not found (literally)",
                "code": 404,
            }
        ),
        404,
    )
