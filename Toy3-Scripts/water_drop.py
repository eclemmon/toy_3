#!/usr/bin/env python3
"""
This module is constructs the water droplet class that plays back synthesized water droplets in toy_3
"""
##############################################################
__author__ = "Eric Lemmon"
__copyright__ = "Copyright 2020, Eric Lemmon"
__credits__ = "Eric Lemmon"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Eric Lemmon"
__email__ = "eric.c.lemmon@stonybrook.edu"
__status__ = "Production"

##############################################################

from pyo import *
import os
import time
import random

# Chat Server/Music Handler inserts path to water drop sample here.
water_drop_sf = os.path.abspath(__file__ + "/../../") + "/Toy3-Samples/Water-Drop.wav"


class Water_Drop(object):
    """
    This water drop object acts as a constructor for a simple, text-based granulation and panning object.
    It is designed to be constructed and controlled by messages sent to the chat client.
    """

    def __init__(self, message, soundfile):
        """
        Initializes water drop object.
        :param message: Message from chat server.
        :param soundfile: Sound file to be granulated.
        """
        self.message_len = len(message)
        self.message = message
        self.drop_sound_list = []
        self.fader = Fader(fadein=0.2, fadeout=0.1, mul=1)
        # Builds list of buffers and synthesizes effects.
        for i in range(len(self.message.split())):
            fader = self.fader
            speed = random.uniform(0.25, 1.25)
            drop_sound = SfPlayer(soundfile, speed=speed, loop=False, mul=fader)
            reverb = STRev(drop_sound, inpos=random.random(), revtime=0.5, bal=0.5, roomSize=random.random() * 4,
                           mul=fader)
            self.drop_sound_list.append([fader, drop_sound, reverb, reverb.revtime])
        # print(self.drop_sound_list) # Output for monitoring in terminal.

    def out(self):
        # Plays back buffer list. Sleep to prevent impulse-like clicks.
        for i in range(len(self.drop_sound_list)):
            # print(i, self.drop_sound_list[i], self.drop_sound_list[i][3]) # Output for monitoring in terminal
            self.drop_sound_list[i][1].out()
            self.drop_sound_list[i][0].play()
            time.sleep(self.drop_sound_list[i][3] + .1)
            self.drop_sound_list[i][0].stop()
            time.sleep(.1)
