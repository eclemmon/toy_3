#!/usr/bin/env python3
"""
This Module manages the main backing track for toy_3.
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
import water_drop
import time
import random
import frequency_lists


def introduction(fader_introduction, sine_introduction):
    """
    The introduction of the piece. 10 seconds of music.
    :param sine_introduction: Sine synth object.
    :param fader_introduction: Fader object that controls fades on introduction section.
    """
    # Initialize passed in objects.
    fader_introduction.play()
    # Send sound out from synthesizer.
    sine_introduction.out()
    # Timing Control.
    print('*** introduction ***')  # For monitoring in terminal.
    print('sleep 10')  # For monitoring in terminal.
    time.sleep(10)  # Plays introduction for 10 seconds.


def section_1(fader_introduction, fader_section_1_1, sine_section_1):
    """
    Section 1 of the piece. 52 seconds of music.
    :param fader_section_1_1: Fader object that controls fades.
    :param sine_section_1: Sine Synth.
    :param fader_introduction: Fader object that controls fades in the introduction section.
    """
    # Initialize passed in objects.
    fader_section_1_1.play()
    # Send sound out from synthesizer.
    sine_section_1.out()
    # Timing Control.
    new_note = random.choice(frequency_lists.phrygian_list)  # Used as an interruptive pitch to modulate between modes.
    print('*** section 1 ***')  # For monitoring in terminal.
    print('sleeping 35')  # For monitoring in terminal.
    time.sleep(35)  # Section 1 material generated for 35 seconds.
    sine_section_1.setFreq([new_note / 4, new_note / 4 + 2])  # Sets up modulation.
    time.sleep(5)  # Introduction material and held pivot note play for 5 seconds.
    print('fading intro out and sleeping 12')  # For monitoring in terminal.
    fader_introduction.stop()  # Initiates fade out of introduction material.
    time.sleep(12)


def section_2(fader_section_1, fader_section_2_1, fader_section_2_2, sine_section_2_1, sine_section_2_2):
    """
    Section 2 of the piece. 65 seconds of music.
    :param sine_section_2_1: Sine synth object.
    :param sine_section_2_2: Sine synth object.
    :param fader_section_1: Fader object that controls fades for section 1 music.
    :param fader_section_2_1: Fader object that controls fades for section 2.
    :param fader_section_2_2: Fader object that controls fades for section 2.
    """
    # Initialize passed in objects.
    fader_section_2_1.play()
    fader_section_2_2.play()
    # Send sound out from synthesizer.
    sine_section_2_1.out()
    sine_section_2_2.out()
    # Timing Control.
    print('*** section 2 ***')  # For monitoring in terminal.
    time.sleep(5)
    fader_section_1.stop()
    print('sleeping 45')  # For monitoring in terminal.
    time.sleep(45)  # Play section 2 for 45 Seconds.
    fader_section_2_2.stop()  # Stop one of the sin loops
    time.sleep(15)  # Wait for fade.


def section_3(fader_section_3, sine_section_3_1):
    """
    Section 3 of the piece. 45 seconds of music.
    :param sine_section_3_1: Sine synth object.
    :param fader_section_3: Fader object that controls fades for section 3.
    """
    # time.sleep(15)
    fader_section_3.play()  # Initialize passed in objects.
    # Send sound out from synthesizer.
    sine_section_3_1.out()
    # Timing Control.
    print('*** section 3 ***')  # For monitoring in terminal.
    print('sleeping 40')  # For monitoring in terminal.
    time.sleep(40)  # Play section 3 for 40 Seconds.
    sine_section_3_1.setFreq(random.choice(frequency_lists.dorian_list))  # Sets up modulation.
    time.sleep(5)  # Hold pivot note.


def section_4(fader_section_4_1, fader_section_4_2, fader_section_3_1, fader_section_2_1, sine_section_4_1,
              sine_section_4_2):
    """
    Section 4 of the piece. 60 seconds of music.
    :param sine_section_4_1: Sine synth object.
    :param sine_section_4_2: Sine synth object.
    :param fader_section_4_1: Fader object that controls fades for section 4.
    :param fader_section_4_2: Fader object that controls fades for section 4.
    :param fader_section_3_1: Fader object that controls fades for material started in section 3.
    :param fader_section_2_1: Fader object that controls fades for material started in section 4.
    """
    # Initialize passed in objects.
    fader_section_4_1.play()
    fader_section_4_2.play()
    # Send sound out from synthesizers.
    sine_section_4_1.out()
    sine_section_4_2.out()
    # Timing Control.
    new_note = random.choice(frequency_lists.dorian_list)
    print('***section 4***')  # For monitoring in terminal.
    time.sleep(10)  # Play section 4 for 10 Seconds.
    fader_section_4_1.stop()
    fader_section_3_1.stop()
    print('sleeping 40')  # For monitoring in terminal.
    time.sleep(40)  # Play section 4 for 40 Seconds.
    fader_section_4_2.stop()
    time.sleep(5)
    print('sleeping 10, should hold here')  # For monitoring in terminal.
    fader_section_4_2.play()
    sine_section_4_2.setFreq([new_note / 4, new_note / 4 + 2])  # Sets up modulation.
    sine_section_4_1.setFreq([random.choice(frequency_lists.dorian_list_up),
                              random.choice(frequency_lists.dorian_list_up)])
    fader_section_4_1.play()
    fader_section_2_1.stop()
    time.sleep(5)  # Next transition point.


def section_5(fader_section_5_1, fader_section_5_2, fader_section_5_3, fader_section_5_4,
              fader_section_4_2, fader_section_4_1, fader_section_2_1, sine_section_5_1, sine_section_5_2,
              sine_section_5_4, reverb_section_5_3):
    """
    Section 5 of the piece. 91 seconds of music.
    :param fader_section_5_1: Fader object that controls fades for section 5.
    :param fader_section_5_2: Fader object that controls fades for section 5.
    :param fader_section_5_3: Fader object that controls fades for section 5.
    :param fader_section_5_4: Fader object that controls fades for section 5.
    :param fader_section_4_2: Fader object that controls fades from section 4.
    :param fader_section_4_1: Fader object that controls fades from section 4.
    :param fader_section_2_1: Fader object that controls fades from section 2.
    :param sine_section_5_1: Sine synth object.
    :param sine_section_5_2: Sine synth object.
    :param sine_section_5_4: Sine synth object.
    :param reverb_section_5_3: Sine synth object.
    """
    # Initialize passed in objects.
    fader_section_5_1.play()
    fader_section_5_2.play()
    fader_section_5_4.play()
    # Send sound out from synthesizers.
    sine_section_5_1.out()
    sine_section_5_2.out()
    sine_section_5_4.out()
    # Timing Control.
    print('*** section 5 ***')  # For monitoring in terminal.
    time.sleep(5)
    fader_section_4_2.stop()
    fader_section_5_4.stop()
    time.sleep(5)
    reverb_section_5_3.out()  # Send sound out from reverb object.
    fader_section_5_3.play()
    print('sleeping 40')  # For monitoring in terminal.
    time.sleep(40)
    fader_section_5_2.stop()
    print('sleeping 20')  # For monitoring in terminal.
    time.sleep(20)
    fader_section_5_1.stop()  # Fade out all synths.
    fader_section_5_3.stop()
    fader_section_2_1.stop()
    fader_section_4_1.stop()
    time.sleep(21)


def main_backingtrack(lfo_1, lfo_2):
    """
    Constructs all fade and synthesis objects and initiates control functions.
    :param lfo_1: a simple LFO for the synth objects.
    :param lfo_2: a second simple LFO for the synth objects.
    """

    # Construct necessary objects ### FADERS AND FREQ LISTS ###
    fader_introduction = Fader(fadein=0.1, fadeout=10, dur=0, mul=0.2)
    fader_section_1_1 = Fader(fadein=2, fadeout=0.1, dur=0, mul=.2)
    fader_section_2_1 = Fader(fadein=5, fadeout=10, dur=0, mul=.2)
    fader_section_2_2 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2)
    fader_section_3_1 = Fader(fadein=10, fadeout=10, dur=0, mul=.2)
    fader_section_4_1 = Fader(fadein=4, fadeout=5, dur=0, mul=.2)
    fader_section_4_2 = Fader(fadein=.1, fadeout=0.1, dur=0, mul=.2)
    fader_section_5_1 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2)
    fader_section_5_2 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2)
    fader_section_5_3 = Fader(fadein=10, fadeout=20, dur=0, mul=.1)
    fader_section_5_4 = Fader(fadein=0.1, fadeout=3, dur=0, mul=.2)
    freqs_section_2_1 = frequency_lists.phrygian_list.copy()  # Make a copy so the orig list is not modified in memory.

    # Construct necessary objects ### INTRODUCTION ###
    freqs_introduction = frequency_lists.lydian_list
    rnd_intro = Choice(choice=freqs_introduction, freq=[8, 7])  # Control to choose pitches at 8 & 7 times per sec.
    sine_introduction = SineLoop(freq=rnd_intro, feedback=lfo_1, mul=fader_introduction)  # Synthesizer

    # Construct necessary objects ### SECTION 1 ###
    freqs_section_1 = frequency_lists.lydian_list
    rnd_section_1 = Choice(choice=freqs_section_1, freq=[.1, .3, .2])
    sine_section_1 = SineLoop(freq=[rnd_section_1 / 4, rnd_section_1 / 4 + 2],
                              feedback=lfo_2,
                              mul=fader_section_1_1)  # Synthesizer

    # Construct necessary objects ### SECTION 2 ###
    rnd_section_2_1 = Choice(choice=freqs_section_2_1, freq=[8, 7, 6])
    rnd_section_2_2 = Choice(choice=freqs_section_2_1, freq=[.3, .4, .1])
    sine_section_2_1 = SineLoop(freq=rnd_section_2_1, feedback=lfo_1, mul=fader_section_2_1)  # Synthesizer
    sine_section_2_2 = SineLoop(freq=[rnd_section_2_2 / 4, rnd_section_2_2 / 4 + 2],
                                feedback=lfo_2,
                                mul=fader_section_2_2)  # Synthesizer

    # Construct necessary objects ### SECTION 3 ###
    rnd_section_3_1 = Choice(choice=freqs_section_2_1 * 2, freq=[0.5, 0.7, 1.1, 1.5, 2.0])
    sine_section_3_1 = SineLoop(freq=[rnd_section_3_1 * 2, (rnd_section_3_1 + 2) * 2],
                                feedback=lfo_2,
                                mul=fader_section_3_1)  # Synthesizer

    # Construct necessary objects ### SECTION 4 ###
    freqs_section_4 = frequency_lists.dorian_list
    rnd_section_4_1 = Choice(choice=freqs_section_4, freq=[10, 8])
    rnd_section_4_2 = Choice(choice=freqs_section_4, freq=[1, 2, 3])
    sine_section_4_1 = SineLoop(freq=rnd_section_4_1, feedback=lfo_1, mul=fader_section_4_1)  # Synthesizer
    sine_section_4_2 = SineLoop(freq=[rnd_section_4_2 / 4, rnd_section_4_2 / 4 + 2],
                                feedback=lfo_2,
                                mul=fader_section_4_2)  # Synthesizer

    # Construct necessary objects ### SECTION 5 ###
    rnd_section_5_1 = Choice(choice=frequency_lists.dorian_list_up, freq=[11, 9])
    rnd_section_5_2 = Choice(choice=frequency_lists.dorian_list_up, freq=[1.5, 3, 4.5])
    rnd_section_5_3 = Choice(choice=frequency_lists.dorian_list_up, freq=[5, 7])
    sine_section_5_1 = SineLoop(freq=rnd_section_5_1, feedback=lfo_1, mul=fader_section_5_1)
    sine_section_5_2 = SineLoop(freq=[rnd_section_5_2 / 4, rnd_section_5_2 / 4 + 2], feedback=lfo2,
                                mul=fader_section_5_2)
    sine_section_5_3 = SineLoop(freq=rnd_section_5_3 * 4, feedback=[lfo_1, lfo_2], mul=fader_section_5_3)
    sine_section_5_4 = SineLoop(freq=[random.choice(frequency_lists.dorian_list_up) / 4,
                                      random.choice(frequency_lists.dorian_list_up) / 4 + 2],
                                feedback=0.15, mul=fader_section_5_4)
    reverb_section_5_3 = STRev(sine_section_5_3,
                               inpos=random.random(),
                               revtime=random.random(),
                               bal=random.random(),
                               roomSize=random.random() * 4)

    # INITIALIZE SECTION CONTROL
    introduction(fader_introduction, sine_introduction)
    section_1(fader_introduction, fader_section_1_1, sine_section_1)
    section_2(fader_section_1_1, fader_section_2_1, fader_section_2_2, sine_section_2_1, sine_section_2_2)
    section_3(fader_section_3_1, sine_section_3_1)
    section_4(fader_section_4_1, fader_section_4_2, fader_section_3_1, fader_section_2_1, sine_section_4_1,
              sine_section_4_2)
    section_5(fader_section_5_1, fader_section_5_2, fader_section_5_3, fader_section_5_4, fader_section_4_2,
              fader_section_4_1, fader_section_2_1, sine_section_5_1, sine_section_5_2, sine_section_5_4,
              reverb_section_5_3)


if __name__ == "__main__":
    s = Server(sr=48000, nchnls=8, buffersize=512, duplex=1).boot()
    s.start()

    # Initialize LFOs
    lfo = Sine(.2, 0, .075, .075)
    lfo2 = Sine(.1, 0, .075, .075)

    # Test water drop object.
    # water_drop1 = water_drop.Water_Drop('abc', water_drop.water_drop_sf)
    # water_drop1.out()
    # time.sleep(5)
    # water_drop2 = water_drop.Water_Drop('aaaa sdhjhf sdhjdsu', water_drop.water_drop_sf)
    # water_drop2.out()

    time.sleep(5)  # Some sleep time to the chat server and music handler can switch to their own chat window.
    main_backingtrack(lfo, lfo2)

    s.stop()
    s.shutdown()
