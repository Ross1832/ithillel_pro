
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from a.config import Config

app = Flask(__name__)
app.config.from_object(Config)

conv = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = MetaData(naming_convention=conv)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db, render_as_bach=True)

from a.application import views
from a.application import models