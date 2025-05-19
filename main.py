# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""

import streamlit as st
from clases import Ligas


df=Ligas("Ligas_de_futbol.xlsm")




def main():
    st.set_page_config(page_title="Ligas de Futbol Pronosticos",layout='wide')

    st.sidebar.image('logo.png',caption="Sistgoy-Pronosticos")
    st.sidebar.header("Ligas de Futbol")
    ligas=st.sidebar.selectbox("Liga a Pronosticar",df.ligas_paises())
    st.sidebar.header("Encuentros")
    local=st.sidebar.selectbox("Equipo Local",df.equipos_local(ligas))
    visita=st.sidebar.selectbox("Equipo Visita",df.equipos_visita(ligas))
    st.subheader("Pronosticos de la "+ligas)
    st.markdown("## "+local+" - "+visita)
   
    st.write(df.FoL(local,ligas))
    st.write(df.FdV(visita,ligas))
    st.write(df.FpL(local,visita,ligas))
    
    
    #Theme
    hide_st_style="""

    <style>
    #MainMenu{visibility:hidden;}
        footer{visibility:hidden;}
        header{visibility:hidden;}
    </style>
    """
 

if __name__=='__main__':
    main()
    