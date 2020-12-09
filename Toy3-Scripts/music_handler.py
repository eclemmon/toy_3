from pyo import *
from frequency_lists import *
import time
import random

lfo = Sine(.2, 0, .075, .075)
lfo2 = Sine(.1, 0, .075, .075)

def main_backingtrack(lfo, lfo2):

    """
    INTRODUCTION
    """
    print('introduction')

    fader_introduction = Fader(fadein=0.1, fadeout=10, dur=0, mul=.2).play()
    freqs_introduction = lydian_list
    rnd_intro = Choice(choice=freqs_introduction, freq=[8,7])
    sine_introduction = SineLoop(freq=rnd_intro, feedback=lfo, mul=fader_introduction)
    sine_introduction.out()

    print('sleep 10')
    time.sleep(10)

    """
    SECTION 1
    """
    print('***section 1***')

    fader_section_1_1 = Fader(fadein=2, fadeout=0.1, dur=0, mul=.2).play()
    freqs_section_1 = lydian_list
    rnd_section_1 = Choice(choice=freqs_section_1, freq=[.1, .3, .2])
    sine_section_1 = SineLoop(freq=[rnd_section_1/4, rnd_section_1/4+2], feedback=lfo2, mul=fader_section_1_1).out()
    new_note = random.choice(phrygian_list)

    print('sleeping 35')
    time.sleep(35)
    sine_section_1.setFreq([new_note/4, new_note/4+2])
    time.sleep(5)
    print('fading intro out and sleeping 12')
    fader_introduction.stop()
    time.sleep(12)



    """
    SECTION 2
    """
    print('***section 2***')

    fader_section_2_1 = Fader(fadein=5, fadeout=10, dur=0, mul=.2).play()
    fader_section_2_2 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2).play()

    freqs_section_2_1 = phrygian_list.copy()
    rnd_section_2_1 = Choice(choice=freqs_section_2_1, freq=[8,7,6])
    rnd_section_2_2 = Choice(choice=freqs_section_2_1, freq=[.3, .4, .1])
    sine_section_2_1 = SineLoop(freq=rnd_section_2_1, feedback=lfo, mul=fader_section_2_1).out()
    sine_section_2_2 = SineLoop(freq=[rnd_section_2_2/4, rnd_section_2_2/4+2], feedback=lfo2, mul=fader_section_2_2).out()

    time.sleep(5)
    fader_section_1_1.stop()
    print('sleeping 45')
    time.sleep(45)
    fader_section_2_2.stop()

    """
    SECTION 3
    """
    print('***section 3***')

    time.sleep(15)

    fader_section_3_1 = Fader(fadein=10, fadeout=10, dur=0, mul=.2).play()
    rnd_section_3_1 = Choice(choice=freqs_section_2_1*2, freq=[.5, .7, 1.1, 1.5, 2.0])
    sine_section_3_1 = SineLoop(freq=[rnd_section_3_1*2, (rnd_section_3_1+2)*2], feedback=lfo2, mul=fader_section_3_1).out()
    print('sleeping 40')
    time.sleep(40)

    sine_section_3_1.setFreq(random.choice(dorian_list))

    time.sleep(5)


    """
    SECTION 4
    """
    print('***section 4***')

    freqs_section_4 = dorian_list

    fader_section_4_1 = Fader(fadein=4, fadeout=5, dur=0, mul=.2).play()
    fader_section_4_2 = Fader(fadein=.1, fadeout=0.1, dur=0, mul=.2).play()

    rnd_section_4_1 = Choice(choice=freqs_section_4, freq=[10,8])
    rnd_section_4_2 = Choice(choice=freqs_section_4, freq=[1, 2, 3])

    sine_section_4_1 = SineLoop(freq=rnd_section_4_1, feedback=lfo, mul=fader_section_4_1).out()
    sine_section_4_2 = SineLoop(freq=[rnd_section_4_2/4, rnd_section_4_2/4+2], feedback=lfo2, mul=fader_section_4_2).out()

    time.sleep(10)
    fader_section_4_1.stop()
    fader_section_3_1.stop()
    print('sleeping 40')
    time.sleep(40)
    fader_section_4_2.stop()
    time.sleep(5)
    print('sleeping 10, should hold here')
    new_note = random.choice(freqs_section_4)
    fader_section_4_2.play()
    sine_section_4_2.setFreq([new_note/4,new_note/4+2])
    sine_section_4_1.setFreq([random.choice(dorian_list_up), random.choice(dorian_list_up)])
    fader_section_4_1.play()
    fader_section_2_1.stop()
    time.sleep(5)


    """
    SECTION 5
    """
    print('***section 5***')


    fader_section_5_1 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2).play()
    fader_section_5_2 = Fader(fadein=.1, fadeout=10, dur=0, mul=.2).play()
    fader_section_5_3 = Fader(fadein=10, fadeout=20, dur=0, mul=.1)
    fader_section_5_4 = Fader(fadein=0.1, fadeout=3, dur=0, mul=.2).play()

    rnd_section_5_1 = Choice(choice=dorian_list_up, freq=[11,9])
    rnd_section_5_2 = Choice(choice=dorian_list_up, freq=[1.5, 3, 4.5])
    rnd_section_5_3 = Choice(choice=dorian_list_up, freq =[5,7])


    sine_section_5_1 = SineLoop(freq=rnd_section_5_1, feedback=lfo, mul=fader_section_5_1).out()
    sine_section_5_2 = SineLoop(freq=[rnd_section_5_2/4, rnd_section_5_2/4+2], feedback=lfo2, mul=fader_section_5_2).out()
    sine_section_5_3 = SineLoop(freq=rnd_section_5_3*4, feedback=[lfo, lfo2], mul=fader_section_5_3)
    sine_section_5_4 = SineLoop(freq=[random.choice(dorian_list_up)/4, random.choice(dorian_list_up)/4+2], feedback=0.15, mul=fader_section_5_4).out()

    time.sleep(5)
    fader_section_4_2.stop()
    fader_section_5_4.stop()
    time.sleep(5)
    reverb_section_5_3 = STRev(sine_section_5_3, inpos=random.random(), revtime=random.random(), bal=random.random(), roomSize=random.random()*4).out()
    fader_section_5_3.play()
    print('sleeping 40')
    time.sleep(40)
    fader_section_5_2.stop()
    print('sleeping 20')
    time.sleep(20)
    fader_section_5_1.stop()
    fader_section_5_3.stop()
    fader_section_2_1.stop()
    fader_section_4_1.stop()
    time.sleep(21)

if __name__ == "__main__":

    s = Server(sr=48000, nchnls=8, buffersize=512, duplex=1).boot()
    s.start()

#    water_drop1 = Water_Drop('abc', water_drop_sf)
#    water_drop1.out()
##    time.sleep(5)
#    water_drop2 = Water_Drop('aaaa sdhjhf sdhjdsu', water_drop_sf)
#    water_drop2.out()

    time.sleep(5)
    main_backingtrack()

    s.stop()
    s.shutdown()
