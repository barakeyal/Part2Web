from flask import Flask
#from flask_fontawesome import FontAwesome

### For using icons FA

#fa = FontAwesome(app)


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

## About
from pages.about.about import about

app.register_blueprint(about)

## Profile
from pages.profile.profile import profile

app.register_blueprint(profile)

## Profile
from pages.menu.menu import menu

app.register_blueprint(menu)

## Catalog
from pages.catalog.catalog import catalog

app.register_blueprint(catalog)

## Contact
from pages.contact.contact import contact

app.register_blueprint(contact)

## Page error handlers
#from pages.page_error_handlers.page_error_handlers import page_error_handlers

#app.register_blueprint(page_error_handlers)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu

app.register_blueprint(main_menu)
