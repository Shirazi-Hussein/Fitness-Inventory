# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:39:30 2020

@author: truet
"""
from scrapes import *
from threading import Thread


def ab():
    ab_b = americanbarbell_barbell_e.main()
    ab_p = americanbarbell_plates_e.main()
    
def bos():
    bos_b = ballsofsteel_barbells_e.main()
    bos_p = ballsofsteel_plates_e.main()

def rf():
    rf_b = repfitness_barbells.main()
    rf_p = repfitness_plates_rework.main()

def r():
    r_b = rogue_barbells.main()
    r_p = rogue_plates.main()

def tf():
    tf_b = titanfitness_barbells.main()
    tf_p = titanfitness_plates.main()

def xmf():
    xmf_b = xmarkfitness_barbells.main()
    xmf_p = xmarkfitness_plates.main()

if __name__ == '__main__':
    Thread(target = ab).start()
    Thread(target = bos).start()
    Thread(target = rf).start()
    Thread(target = r).start()
    Thread(target = tf).start()
    Thread(target = xmf).start()