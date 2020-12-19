import time
import glob
import importlib

from functools import wraps

from flask_restplus import abort

from store.extensions import api
from store.modules.auth.helper import AuthHelper


def auto_import_model():
    all_dirs = glob.glob("store/modules/*/models/*.py")
    for package in all_dirs:
        package_split = package.split("/")

        class_name = package_split[-2].capitalize()

        model_import_path = '.'.join(package_split)[:-3]
        importlib.import_module(model_import_path, package=class_name)


def auto_import_controller():
    all_dirs = glob.glob("store/modules/*/controller.py")
    for package in all_dirs:
        package_split = package.split("/")
        model_import_path = '.'.join(package_split)[:-3]
        ns = getattr(importlib.import_module(model_import_path), "api")
        api.add_namespace(ns)


def timeit(func):
    def inner1(*args, **kwargs):
        begin = time.time()

        value = func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return value

    return inner1


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_logged_in_user()

        user = data.get('data')
        if not user:
            abort(status, **data)
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthHelper.get_logged_in_user()
        user = data.get('data')
        if not user:
            abort(status, **data)
        if not user['admin']:
            abort(401, 'Admin token required', status='fail')
        return f(*args, **dict(kwargs))

    return decorated
