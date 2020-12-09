#!/usr/bin/env python3
"""
This Module is a repository of the different pitch materials used in toy_3.
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

lydian_dictionary = {
    0: 440.0000,
    1: 493.8833,
    2: 554.3653,
    3: 622.2540,
    4: 659.2551,
    5: 739.9888,
    6: 830.6094
}

phrygian_dictionary = {
    0: 329.628,
    1: 349.228,
    2: 391.995,
    3: 440.000,
    4: 493.883,
    5: 523.251,
    6: 587.330
}

phrygian_dictionary2 = {
    0: 329.628 / 2,
    1: 349.228 / 2,
    2: 391.995 / 2,
    3: 440.000 / 2,
    4: 493.883 / 2,
    5: 523.251 / 2,
    6: 587.330 / 2
}

lydian_dictionary2 = {
    0: 440.0000 / 2,
    1: 493.8833 / 2,
    2: 554.3653 / 2,
    3: 622.2540 / 2,
    4: 659.2551 / 2,
    5: 739.9888 / 2,
    6: 830.6094 / 2
}

lydian_list = [lydian_dictionary2[i] for i in lydian_dictionary2.keys()]
phrygian_list = [phrygian_dictionary2[i] for i in phrygian_dictionary2.keys()]
dorian_list = [261.626, 293.665, 331.127, 349.228, 291.995, 440.000, 466.164]
dorian_list_up = [293.665, 329.628, 349.228, 391.995, 440, 493.883, 523.251]
