import dweepy
import requests


for dweet in dweepy.listen_for_dweets_from('lat-soundsystem'):
    requests.post("http://localhost/webhook/", json=dweet)
