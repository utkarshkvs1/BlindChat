import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database setup
SQLALCHEMY_DATABASE_URI = 'postgres://bfpxfnoptnjkka:34673f26d35fc1cb5ad131dcd045126bf5d7058a212f8a0319ca0773c8f27588@ec2-54-243-43-72.compute-1.amazonaws.com:5432/dcokktksp4ntae'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook
ACCESS_TOKEN = 'YOUR_FACEBOOK_APP_ACCESS_TOKEN'
VERIFY_TOKEN = 'FACEBOOK_APP_VERIFY_TOKEN'

# App
APP_URL = "https://blindchat9211.herokuapp.com/"

# For analytics purposes
CHATMETRICS_TOKEN = 'CHATMETRICS_TOKEN'

# For debugging
PAGE_ID = 'FACEBOOK_PAGE_PSID'
ADMIN_ID = "ADMIN_PSID"

