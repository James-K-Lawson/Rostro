import os
basedir = os.path.abspath(os.path.dirname(__file__))

os.environ['AWS_ACCESS_KEY_ID'] = "AKIAQ6WALA44IUBOTRXV"
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'OSTER0'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'tmp'
    ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    AWS_ACCESS_KEY_ID = os.environ.get('S3_BUCKET') or "AKIAQ6WALA44IUBOTRXV"
    AWS_SECRET_ACCESS_KEY = os.environ.get('S3_BUCKET') or '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'
    S3_BUCKET = os.environ.get('S3_BUCKET') or 'rostrobucket'