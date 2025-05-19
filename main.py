# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""
import matplotlib.pyplot as plt
import streamlit as st
from clases import Ligas
import numpy as np

df=Ligas("Ligas_de_futbol.xlsm")




def main():
    st.sidebar.header("Ligas de Futbol")
    ligas=st.sidebar.selectbox("Liga a Pronosticar",df.equipos_local())
    st.sidebar.header("Encuentros")
    local=st.sidebar.selectbox("Equipo Local",df.equipos_local())
    visita=st.sidebar.selectbox("Equipo Visita",df.equipos_visita())
    st.markdown("## "+local+" - "+visita)
    
    
    
 

if __name__=='__main__':
    main()
    