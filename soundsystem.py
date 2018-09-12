import os
import dweepy
import pygame
from flask import Flask
from flask import jsonify
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
    return render_template("index.html")


@app.route("/dweets/")
def dweet_list():
    """
    Latest dweets
    """
    object_list = dweepy.get_dweets_for(DWEEPY_NAME)
    return render_template("dweet_list.html", object_list=object_list)


@app.route("/rollout/")
def rollout():
    """
    What you got in that bag?
    """
    _play('rollout.wav')
    return jsonify("ROOOOOLLLOUT!")


@app.route("/hampster-dance/")
def hampster_dance():
    """
    The soundtrack of the Internet that once was.
    """
    _play('hampsterdance.wav')
    return jsonify("Dance! Hampster! Dance!")


@app.route("/snap/")
def snap():
    """
    The Addams Family snaps it out.
    """
    _play('snap.wav')
    return jsonify("OH SNAP!")


@app.route("/take-me-to-the-clouds-above/")
def take_me_to_the_clouds_above():
    """
    Let Whitney tell it.
    """
    _play('take-me-to-the-clouds-above.wav')
    return jsonify("Mmmm Hmmm!")


def _play(name):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(THIS_DIR, 'static', name))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
            pass


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
