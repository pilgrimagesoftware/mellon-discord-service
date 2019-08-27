__author__ = "Paul Schifferer <paul@schifferers.net>"

from app.common import constants
import os
import logging


class DiscordBot(object):
    client = None
