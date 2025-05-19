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

    def ligas_paises(self):
        return self.df_fixture["Liga"].unique()
    
    def equipos_local(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["Local"].unique()
    
    def equipos_visita(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["Visita"].unique()
        
        
    def PgaLG(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["GF"].mean() 
    def PgcLG(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["GC"].mean()
    
    def PgaVG(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["GC"].mean() 
    def PgcVG(self,liga):
        df_liga=self.df_fixture[self.df_fixture["Liga"]==liga]
        return df_liga["GF"].mean()
    
    def PgaL(self,local):
        return self.df_fixture[self.df_fixture['Local']==local].groupby('Local')['GF'].mean().iloc[0]
    def PgcL(self,local):
        return self.df_fixture[self.df_fixture['Local']==local].groupby('Local')['GC'].mean().iloc[0]
    
    def PgaV(self,visita):
        return self.df_fixture[self.df_fixture['Visita']==visita].groupby('Visita')['GC'].mean().iloc[0]
    def PgcV(self,visita):
        return self.df_fixture[self.df_fixture['Visita']==visita].groupby('Visita')['GF'].mean().iloc[0]
    
    def FoL(self,local,liga):
        return self.PgaL(local)/self.PgaLG(liga)
    def FdL(self,local,liga):
        return self.PgcL(local)/self.PgcLG(liga)
    
    def FoV(self,visita,liga):
        return self.PgaV(visita)/self.PgaVG(liga)
    def FdV(self,visita,liga):
        return self.PgcV(visita)/self.PgcVG(liga)
    
    def FpL(self,local,visita,liga):
        return self.FoL(local,liga)*self.FdV(visita,liga)
    def FpV(self,local,visita,liga):
        return self.FoV(visita,liga)*self.FdL(local,liga)
    
    def GeL(self,gol,fpl):
        return poisson.pmf(gol,fpl)
    def GeV(self,gol,fpv):
        return poisson.pmf(gol,fpv)
    
    def Pos_empate(self,local,visita,liga):
        suma=0
        for x in range(11):
            suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(x,self.FpV(local,visita,liga))
        return suma  
    
    def PosG_local(self,local,visita,liga):
        suma=0
        for x in range(1,11):          
            for i in range(10):         
                if x>i:
                    suma=suma+self.GeL(x,self.FpL(local,visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma 
    
    def PosG_visita(self,local,visita,liga):
        suma=0
        for x in range(10):          
            for i in range(1,11):         
                if x<i:
                    suma=suma+self.GeL(x,self.FpL(local,visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma  
    
    def May05(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=1:
                    suma=suma+self.GeL(x,self.FpL(local,visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma
    
    def May15(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=2:
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma
    
    def May25(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=3:
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma 
    
    def May35(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=4:
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma 
    
    def May45(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=5:
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma 
    
    def May55(self,local,visita,liga):
        suma=0
        for x in range(11):          
            for i in range(11):         
                if x+i>=6:
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma
    
    def AmbosMarcan(self,local,visita,liga):
        suma=0
        for x in range(1,11):          
            for i in range(1,11):         
                    suma=suma+self.GeL(x,self.FpL(local, visita,liga))*self.GeV(i,self.FpV(local,visita,liga))
        return suma
   
    
        
    
    
    
    
    