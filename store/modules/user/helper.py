from geolite2 import geolite2

from flask import request
from flask_restplus import abort

from store.modules.user.models.user import User


def register():
    payload = request.json

    name = payload.get("name")
    email = payload.get('email')
    age = payload.get('age')
    password = payload.get('password')
    # ip = str(request.remote_addr)
    # geolocation = geolocation_by_ip(ip)

    user = User.get_by_email(email)
    if user:
        abort(401, 'User already exists.', status='fail')

    user = User()
    user.name = name
    user.email = email
    user.age = age
    user.password = password
    # user.geolocation = geolocation
    # user.ip = ip
    # print("user ip", user.ip)
    user.save()

    response_object = {
        'status': 'success',
        'message': 'You registered successfully.'
    }

    return response_object, 201


def geolocation_by_ip(ip):
    reader = geolite2.reader()
    geo_data = reader.get(ip)
    if geo_data:
        return str(geo_data["country"]["iso_code"])
