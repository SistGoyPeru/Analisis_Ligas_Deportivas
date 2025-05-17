# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""


from clases import Ligas


Liga_española=Ligas("liga_española.xlsm")
Liga_española2=Ligas("liga_española2.xlsm")

Liga_alemana=Ligas("liga_alemana.xlsm")
Liga_Italiana=Ligas("liga_italiana.xlsm")
Liga_Inglesa=Ligas("liga_inglesa.xlsm")

def main():
   
    print(Liga_española.AmbosMarcan('Real Madrid','Osasuna'))
    
if __name__=='__main__':
    main()
    