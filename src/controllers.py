__author__ = "Paul Schifferer <paul@schifferers.net>"

# Import flask dependencies
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
)

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db
from app.core import worker

# Import other modules
import json
import logging


# Define the blueprint: 'slack', set its url prefix: app.url/github
discord = Blueprint("discord", __name__, url_prefix="/discord")
