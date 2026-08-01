from random import choice
places=["Yes!","No!","Reply hazy","Sorry, what?"]
def give():
    """Return random fast food place"""
    return choice(places)