# Copyright (c) 2019 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from . import SentryLogger


def getMetaData():
    return {}


def register(app):
    return { "logger": SentryLogger.SentryLogger() }
