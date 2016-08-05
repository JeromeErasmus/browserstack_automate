# automate/server/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
#from flask_login import LoginManager
#from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


################
#### config ####
################

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)


app_settings = 'automate.server.config.DevelopmentConfig'#os.getenv('AUTOMATE_APP_SETTINGS', 'automate.server.config.DevelopmentConfig')
app.config.from_object(app_settings)

####################
#### extensions ####
####################
toolbar = DebugToolbarExtension(app)
#bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


###################
### blueprints ####
###################

#from automate.server.user.views import user_blueprint
from automate.server.main.views import main_blueprint
#app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)

#########################
##### error handlers ####
#########################

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500


