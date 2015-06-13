"""Written by - Rafal Kowalski"""
import sys
import logging

from flask import Flask, render_template, jsonify, url_for
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from open_event.models import db
import open_event.models.event_listeners
from open_event.views.admin.admin import AdminView
from flask.ext.cors import CORS

app = Flask(__name__)
from views import views
migrate = Migrate(app, db)
db.init_app(app)
cors = CORS(app)
app.secret_key = 'super secret key'
app.config.from_object('config')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

with app.app_context():
    AdminView(app, "Open Event").init()

