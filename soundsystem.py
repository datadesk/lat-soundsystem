import os
import dweepy
from flask import Flask
from flask import render_template
app = Flask(__name__)

# Settings
THIS_DIR = os.path.dirname(__file__)
DWEEPY_NAME = 'lat-soundsystem'


@app.route("/")
def homepage():
    """
    Homepage.
    """
    object_list = dweepy.get_dweets_for(DWEEPY_NAME)
    return render_template("index.html", object_list=object_list)


@app.route("/rollout/")
def rollout():
    """
    What you got in that bag?
    """
    path = os.path.join(THIS_DIR, 'rollout.wav')
    _play(path)
    return "ROOOOOLLLOUT!"


@app.route("/hampster-dance/")
def hampster_dance():
    """
    The soundtrack of the Internet that once was.
    """
    path = os.path.join(THIS_DIR, 'hampsterdance.wav')
    _play(path)
    return "Dance! Hampster! Dance!"


@app.route("/snap/")
def snap():
    """
    The Addams Family snaps it out.
    """
    path = os.path.join(THIS_DIR, 'snap.wav')
    _play(path)
    return "OH SNAP!"


@app.route("/take-me-to-the-clouds-above/")
def take_me_to_the_clouds_above():
    """
    Let Whitney tell it.
    """
    path = os.path.join(THIS_DIR, 'takemetothecloudsabove.wav')
    _play(path)
    return "Mmmm Hmmm!"


def _play(path):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
            pass


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
