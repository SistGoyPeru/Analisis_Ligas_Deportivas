# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""

import streamlit as st
from clases import Ligas
import matplotlib.pyplot as plt

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


 

   
    # Crear tres columnas de igual ancho
    col1, col2 = st.columns(2)

    # Colocar elementos en cada columna
    with col1:
        resultados = ['Victoria '+local, 'Empate', 'Victoria '+visita]
        probabilidades = [df.PosG_local(local,visita,ligas)*100, df.Pos_empate(local,visita,ligas)*100, df.PosG_visita(local,visita,ligas)*100]
        colores = ['blue', 'gray', 'green']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad de Resultado del Partido',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)
    
    with col2:

        resultados = ['>0.5', '>1.5', '>2.5','>3.5','>4.5','>5.5']
        probabilidades = [df.May05(local,visita,ligas)*100,df.May15(local,visita,ligas)*100,df.May25(local,visita,ligas)*100,df.May35(local,visita,ligas)*100,df.May45(local,visita,ligas)*100,df.May55(local,visita,ligas)*100, ]
        colores = ['blue', 'gray', 'green']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad de Goles marcados ',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)
        
            
    
        
        


        
        
    


if __name__=='__main__':
    main()
    