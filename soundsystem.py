import os
from flask import Flask
app = Flask(__name__)
THIS_DIR = os.path.dirname(__file__)

@app.route("/")
def homepage():
    """
    Homepage.
    """
    return "Welcome to the LAT Soundsystem"


@app.route("/rollout/")
def rollout():
    """
    Play a snippet from Ludacris' "Rollout (My Business)"
    """
    path = os.path.join(THIS_DIR, 'rollout.wav')
    os.system("sudo aplay %s" % path)
    return "ROOOOOLLLOUT!"


@app.route("/hampster-dance/")
def rollout():
    """
    Play the theme song from hampsterdance.com
    """
    path = os.path.join(THIS_DIR, 'hampsterdance.wav')
    os.system("sudo aplay %s" % path)
    return "Dance! Hampster! Dance!"


if __name__ == "__main__":
    app.run()
