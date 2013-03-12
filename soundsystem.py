import os
from flask import Flask
app = Flask(__name__)


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
    os.system("sudo aplay rollout.wav")
    return "ROOOOOLLLOUT!"


if __name__ == "__main__":
    app.run()
