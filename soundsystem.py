import os
import time
import dweepy
import pygame
import subprocess
from flask import abort
from flask import Flask
from flask import request
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


@app.route("/webhook/", methods=["POST"])
def webhook():
    """
    Parse and process webhooks from the outside world.
    """
    # Get the POST data
    data = request.get_json()

    # Make sure it's the right structure
    try:
        hook_name = data['content']['hook']
    except KeyError:
        abort(400)

    # Get the hook, provided it exists
    hooks_dict = {
        "rollout": rollout,
        "hampster_dance": hampster_dance,
        "snap": snap,
        "take_me_to_the_clouds_above": take_me_to_the_clouds_above
    }
    try:
        hook = hooks_dict[hook_name]
    except KeyError:
        abort(400)

    print("Running hook: {}".format(hook_name))

    # Run the hook
    return hook()


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
    # _open("rollout.html")
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
    _play('take_me_to_the_clouds_above.wav')
    return jsonify("Mmmm Hmmm!")


def _open(name):
    """
    Open the provided HTML file.
    """
    path = os.path.join(THIS_DIR, 'templates', 'webhooks', name)
    p = subprocess.Popen(["chromium-browser", path])
    time.sleep(5)
    p.kill()


def _play(name):
    """
    Play the provided sound file.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(THIS_DIR, 'static', name))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
