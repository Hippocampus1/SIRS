from flask import request, jsonify
from utils import logger as log
from central_server import app
from central_server.models.user import User

@app.route("/login/", methods=["POST"])
def login_view():
    response = dict()
    req = request.get_json()

    if request.method == "POST":
        log.debug("[login_view][POST]")
        log.debug("User {}:{} is trying to login".format(req.get('username'), req.get('password')))
        user = User.query.filter_by(username=req.get('username')).first()
        log.debug("{} user found".format(user))
        if user is None:
            response.update({
                'error': "Invalid credentials! Please use an existing account."
            })
        else:
            response.update({
                'email': user.email
            })


    return jsonify(response)

if __name__ == "__main__":
    """Initialize flask app"""
    app.run()
