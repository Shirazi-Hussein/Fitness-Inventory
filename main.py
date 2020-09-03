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
    ab_b.to_csv('data\data.csv', 'a+')
    ab_p.to_csv('data\data.csv', 'a+')
    
def bos():
    bos_b = ballsofsteel_barbells_e.results
    bos_p = ballsofsteel_plates_e.results
    bos_b.to_csv('data\data.csv', 'a+')
    bos_p.to_csv('data\data.csv', 'a+')

def rf():
    rf_b = repfitness_barbells.main()
    rf_p = repfitness_plates_rework.main()
    rf_b.to_csv('data\data.csv', 'a+')
    rf_p.to_csv('data\data.csv', 'a+')

def r():
    r_b = rogue_barbells.main()
    r_p = rogue_plates.main()
    r_b.to_csv('data\data.csv', 'a+')
    r_p.to_csv('data\data.csv', 'a+')

def tf():
    tf_b = titanfitness_barbells.main()
    tf_p = titanfitness_plates.main()
    tf_b.to_csv('data\data.csv', 'a+')
    tf_p.to_csv('data\data.csv', 'a+')

def xmf():
    xmf_b = xmarkfitness_barbells.main()
    xmf_p = xmarkfitness_plates.main()
    xmf_b.to_csv('data\data.csv', 'a+')
    xmf_p.to_csv('data\out12.csv', "a+")
    
if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    Thread(target = ab).start()
    Thread(target = bos).start()
    Thread(target = rf).start()
    Thread(target = r).start()
    Thread(target = tf).start()
    Thread(target = xmf).start()
    
    