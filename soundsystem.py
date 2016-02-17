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
def hampster_dance():
    """
    The soundtrack of the Internet that once was.
    """
    path = os.path.join(THIS_DIR, 'hampsterdance.wav')
    os.system("sudo aplay %s" % path)
    return "Dance! Hampster! Dance!"


@app.route("/snap/")
def snap():
    """
    Play a of the Addams Family theme
    """
    path = os.path.join(THIS_DIR, 'snap.wav')
    os.system("sudo aplay %s" % path)
    return "OH SNAP!"


if __name__ == "__main__":
    app.run()
