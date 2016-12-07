from flask import request, jsonify
from flask_login import login_user, logout_user
from utils import logger as log
from central_server import app
from central_server.models.user import User
from central_server.decorators import login_required, admin_required


@app.route("/error/")
def error_view():
    params = request.args.to_dict()
    response = {
        "error": params.get("message")
    }
    return jsonify(response)


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
            login_user(user)
            response.update(user.to_dict())

    return jsonify(response)


@app.route("/logout/", methods=["POST"])
@login_required
def logout_view():
    response = dict()
    if request.method == "POST":
        log.debug("[logout_view][POST]")
        logout_user()
    return jsonify(response)


@app.route("/create-user/", methods=["POST"])
def create_user_view():
    response = dict()
    req = request.get_json()

    if request.method == "POST":
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



# DON'T PUT ANYTHING BELOW THIS COMMENT
"""Initialize flask app"""
app.run()
