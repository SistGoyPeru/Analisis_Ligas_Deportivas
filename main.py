# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""

import streamlit as st
from clases import Ligas


Liga_española=Ligas("liga_españolaF.xlsm")
Liga_española2=Ligas("liga_española2.xlsm")

Liga_alemana=Ligas("liga_alemana.xlsm")
Liga_Italiana=Ligas("liga_italiana.xlsm")
Liga_Inglesa=Ligas("liga_inglesa.xlsm")



def main():
   
    
    st.sidebar.header("Encuentros")
    local=st.sidebar.selectbox("Equipo Local",Liga_española.equipos_local())
    visita=st.sidebar.selectbox("Equipo Visita",Liga_española.equipos_visita())
    st.markdown("## "+local+" - "+visita)
    
    st.metric(label="Porcentaje Ganador Local",value="{:.2f}".format(Liga_española.PosG_local(local,visita)*100)+"%")
    st.metric(label="Porcentaje Empate",value="{:.2f}".format(Liga_española.Pos_empate(local,visita)*100)+"%")
    st.metric(label="Porcentaje Ganador Visita",value="{:.2f}".format(Liga_española.PosG_visita(local,visita)*100)+"%")
    st.metric(label="Mas 0.5 Goles",value="{:.2f}".format(Liga_española.May05(local,visita)*100)+"%")
    st.metric(label="Mas 1.5 Goles",value="{:.2f}".format(Liga_española.May15(local,visita)*100)+"%")
    st.metric(label="Mas 2.5 Goles",value="{:.2f}".format(Liga_española.May25(local,visita)*100)+"%")
    st.metric(label="Mas 3.5 Goles",value="{:.2f}".format(Liga_española.May35(local,visita)*100)+"%")
    st.metric(label="Mas 4.5 Goles",value="{:.2f}".format(Liga_española.May45(local,visita)*100)+"%")
    st.metric(label="Mas 5.5 Goles",value="{:.2f}".format(Liga_española.May55(local,visita)*100)+"%")



if __name__=='__main__':
    main()
    