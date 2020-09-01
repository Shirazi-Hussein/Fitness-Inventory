# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:39:30 2020

@author: truet
"""
from scrapes import *
from threading import Thread
import os

def ab():
    ab_b = americanbarbell_barbell_e.main()
    ab_p = americanbarbell_plates_e.main()
    ab_b.to_csv('data\out1.csv')
    ab_p.to_csv('data\out2.csv')
    
def bos():
    bos_b = ballsofsteel_barbells_e.main()
    bos_p = ballsofsteel_plates_e.main()
    bos_b.to_csv('data\out3.csv')
    bos_p.to_csv('data\out4.csv')

def rf():
    rf_b = repfitness_barbells.main()
    rf_p = repfitness_plates_rework.main()
    rf_b.to_csv('data\out5.csv')
    rf_p.to_csv('data\out6.csv')

def r():
    r_b = rogue_barbells.main()
    r_p = rogue_plates.main()
    r_b.to_csv('data\out7.csv')
    r_p.to_csv('data\out8.csv')

def tf():
    tf_b = titanfitness_barbells.main()
    tf_p = titanfitness_plates.main()
    tf_b.to_csv('data\out9.csv')
    tf_p.to_csv('data\out10.csv')

def xmf():
    xmf_b = xmarkfitness_barbells.main()
    xmf_p = xmarkfitness_plates.main()
    xmf_b.to_csv('data\out11.csv')
    xmf_p.to_csv('data\out12.csv')
    
if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    Thread(target = ab).start()
    Thread(target = bos).start()
    Thread(target = rf).start()
    Thread(target = r).start()
    Thread(target = tf).start()
    Thread(target = xmf).start()