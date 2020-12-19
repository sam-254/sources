import os
import glob
import importlib
from store.core.view import BaseView
from store.extensions import admin, db

from flask_sqlalchemy.model import DefaultMeta


def get_admin_view_class(model):
    class_name = model.__name__ + 'View'
    view_module = '.'.join(model.__module__.split('.')[:-2]) + '.views' + f'.{model.__name__}'.lower()
    view_file_path = os.path.join(*view_module.split('.')) + '.py'
    print(view_file_path)
    if not os.path.exists(view_file_path):
        return BaseView
    return getattr(importlib.import_module(view_module), class_name)


def create_admin():
    for model_class in db.Model._decl_class_registry.values():
        if isinstance(model_class, DefaultMeta):
            model = model_class()
            admin_view = get_admin_view_class(model_class)
            admin.add_view(admin_view(model_class, db.session, category=model.get_category()))
