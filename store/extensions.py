from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate, MigrateCommand
from flask_restplus import Api
from flask_uploads import UploadSet, IMAGES
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate(db=db)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(version='1.0', title='Store API',
          description='A simple Store API extracted from the original flask-restful example',
          authorizations=authorizations,
          security="apikey"
          )

admin = Admin()
images = UploadSet('images', IMAGES)

cors = CORS(resources={
    r'/*': {
        'origins': '*'
    }
})
