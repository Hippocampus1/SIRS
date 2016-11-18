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


@app.route("/create-user/", methods=["POST"])
def create_user_view():
    response = dict()
    req = request.get_json()

    if request.method == "POST":
        import pdb; pdb.set_trace()
        user = User(**req)
        user.save()
        response.update({
            'message': "User {} was created successfully".format(repr(user))
        })

        log.debug("[create_user_view][POST]")

    return jsonify(response)


@app.route("/update-user/", methods=["POST"])
def update_user_view():
    response = dict()
    req = request.get_json()

    if request.method == "POST":
        log.debug("[update_user_view][POST]")

    return jsonify(response)


@app.route("/delete-user/", methods=["POST"])
def delete_user_view():
    response = dict()
    req = request.get_json()

    if request.method == "POST":
        log.debug("[delete_user_view][POST]")

    return jsonify(response)


@app.route("/list-users/", methods=["GET"])
def list_users_view():
    response = dict()
    req = request.get_json()

    if request.method == "GET":
        log.debug("[list_users_view][GET]")
        response["objects"] = list()
        for user in User.query.filter():
            response["objects"].append(user.to_dict())


    return jsonify(response)




if __name__ == "__main__":
    """Initialize flask app"""
    app.run()
