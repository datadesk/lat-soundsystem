import pygame
from flask import Flask
app = Flask(__name__)


def play_sound(filename):
    """
    Play the provided sound file.
    """
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


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
    play_sound("rollout.mp3")
    return "ROOOOOLLLOUT!"


if __name__ == "__main__":
    app.run()
