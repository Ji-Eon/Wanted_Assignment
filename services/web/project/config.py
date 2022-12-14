import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    

    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"
    TEMPLATES_FOLDER = f"{os.getenv('APP_FOLDER')}/project/templates"
