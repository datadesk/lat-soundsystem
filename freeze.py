from flask_frozen import Freezer
from soundsystem import app
freezer = Freezer(app, with_no_argument_rules=False, log_url_for=False)


@freezer.register_generator
def homepage():
    yield {}


if __name__ == '__main__':
    freezer.freeze()
