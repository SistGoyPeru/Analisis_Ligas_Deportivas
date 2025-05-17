# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:44:31 2025

@author: Alex Goyzueta Delgado
"""


from scipy.stats import poisson
from pathlib import Path
from openpyxl import load_workbook
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')


class Ligas:
    def __init__(self,archivo):
        self.archivo=archivo
        self.df_fixture=pd.read_excel(Path(__file__).resolve().parent / self.archivo)
        
    def PgaLG(self):
        return self.df_fixture["GF"].mean() 
    def PgcLG(self):
        return self.df_fixture["GC"].mean()
    
    def PgaVG(self):
        return self.df_fixture["GC"].mean() 
    def PgcVG(self):
        return self.df_fixture["GF"].mean()
    
    def PgaL(self,local):
        return self.df_fixture[self.df_fixture['Local']==local].groupby('Local')['GF'].mean().iloc[0]
    def PgcL(self,local):
        return self.df_fixture[self.df_fixture['Local']==local].groupby('Local')['GC'].mean().iloc[0]
    
    def PgaV(self,visita):
        return self.df_fixture[self.df_fixture['Visita']==visita].groupby('Visita')['GC'].mean().iloc[0]
    def PgcV(self,visita):
        return self.df_fixture[self.df_fixture['Visita']==visita].groupby('Visita')['GF'].mean().iloc[0]
    
    def FoL(self,local):
        return self.PgaL(local)/self.PgaLG()
    def FdL(self,local):
        return self.PgcL(local)/self.PgcLG()
    
    def FoV(self,visita):
        return self.PgaV(visita)/self.PgaVG()
    def FdV(self,visita):
        return self.PgcV(visita)/self.PgcVG()
    
    def FpL(self,local,visita):
        return self.FoL(local)*self.FdV(visita)
    def FpV(self,local,visita):
        return self.FoV(visita)*self.FdL(local)
    
    def GeL(self,gol,fpl):
        return poisson.pmf(gol,fpl)
    def GeV(self,gol,fpv):
        return poisson.pmf(gol,fpv)
    
    def Pos_empate(self,local,visita):
        suma=0
        for x in range(11):
            suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(x,self.FpV(local,visita))
        return suma  
    
    def PosG_local(self,local,visita):
        suma=0
        for x in range(1,11):          
            for i in range(10):         
                if x>i:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma 
    
    def PosG_visita(self,local,visita):
        suma=0
        for x in range(10):          
            for i in range(1,11):         
                if x<i:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma  
    
    def May05(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=1:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma
    
    def May15(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=2:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma
    
    def May25(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=3:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma 
    
    def May35(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=4:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma 
    
    def May45(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=5:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma 
    
    def May55(self,local,visita):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=6:
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma
    
    def AmbosMarcan(self,local,visita):
        suma=0
        for x in range(1,11):          
            for i in range(1,11):         
                    suma=suma+self.GeL(x,self.FpL(local, visita))*self.GeV(i,self.FpV(local,visita))
        return suma
   
    
        
    
    
    
    
    