# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:39:30 2020

@author: truet
"""
from scrapes import *
from threading import Thread
import os
import glob
import pandas as pd


def ab():
    ab_b = americanbarbell_barbell_e.main()
    ab_p = americanbarbell_plates_e.main()
    ab_b.to_csv('out1.csv')
    ab_p.to_csv('out2.csv')
    
def bos():
    bos_b = ballsofsteel_barbells_e.results
    bos_p = ballsofsteel_plates_e.results
    bos_b.to_csv('out3.csv')
    bos_p.to_csv('out4.csv')

def rf():
    rf_b = repfitness_barbells.main()
    rf_p = repfitness_plates_rework.main()
    rf_b.to_csv('out5.csv')
    rf_p.to_csv('out6.csv')

def r():
    r_b = rogue_barbells.main()
    r_p = rogue_plates.main()
    r_b.to_csv('out7.csv')
    r_p.to_csv('out8.csv')

def tf():
    tf_b = titanfitness_barbells.main()
    tf_p = titanfitness_plates.main()
    tf_b.to_csv('out9.csv')
    tf_p.to_csv('out10.csv')

def xmf():
    xmf_b = xmarkfitness_barbells.main()
    xmf_p = xmarkfitness_plates.main()
    xmf_b.to_csv('out11.csv')
    xmf_p.to_csv('out12.csv')
    
if __name__ == '__main__':
    threads = [Thread(target=t) for t in (ab, bos, rf, r, tf, xmf)]
    os.chdir("data")
    for thread in threads:
        thread.start()
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    for thread in threads:
        thread.join()
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    
    
    