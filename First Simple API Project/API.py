import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()


def check_auth(func):
    def wrapper_auth(*args, **kwargs):
        headers = request.headers
        if headers.get("Authorization") is None or headers.get("Authorization") != os.getenv('_FIRST_API_KEY'):
            return jsonify({'error': 'Unauthorized'}), 401
        return func(*args, **kwargs)

    return wrapper_auth


def check_post(func):
    def wrapper_post(*args, **kwargs):
        data = request.json
        if data is None or len(data) < 2:
            return jsonify({'error': 'missing parameters'}), 400
        for key, value in data.items():
            if not isinstance(value, (int, float)):
                return jsonify({'error': f'invalid parameter {key}, only int or float values'}), 400
        return func(*args, **kwargs)

    return wrapper_post


def check_auth_and_post(func):
    decorated_func = check_post(check_auth(func))

    def wrapper(*args, **kwargs):
        return decorated_func(*args, **kwargs)

    return wrapper


def check_auth_multi(func):
    decorated_func = check_post(check_auth(func))

    def wrapper__(*args, **kwargs):
        return decorated_func(*args, **kwargs)

    return wrapper__


def check_auth_and_post(func):
    decorated_func = check_post(check_auth(func))

    def wrapper(*args, **kwargs):
        return decorated_func(*args, **kwargs)

    return wrapper


class CalculatorApi:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = os.getenv('_SECRET_KEY')
        self.__API_KEY = os.getenv('_FIRST_API_KEY')
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/add', view_func=self.sum_route, methods=['POST'])
        self.app.add_url_rule('/subtract', view_func=self.subtr_routes, methods=['POST'])
        self.app.add_url_rule('/multiply', view_func=self.multiplly_routes, methods=['POST'])

    @check_auth_and_post
    def sum_route(self):
        data = request.json
        total = None
        for key, value in data.items():
            if total is None:
                total = value
            else:
                total += value

        return jsonify({'sum': total}), 200

    @check_auth
    @check_post
    def subtr_routes(self):
        data = request.json
        total = None
        for key, value in data.items():
            if total is None:
                total = value
            else:
                total -= value

        return jsonify({'sub': f'total of subtraction is {total}'}), 200

    @check_auth_multi
    def multiplly_routes(self):
        deta = request.json
        total = None
        for key, value in deta.items():
            if total is None:
                total = value
            else:
                total *= value

        return jsonify({'multiply': total}), 200


if __name__ == '__main__':
    app = CalculatorApi()
    app.app.run(debug=True)
