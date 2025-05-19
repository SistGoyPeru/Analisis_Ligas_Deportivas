# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""
import matplotlib.pyplot as plt
import streamlit as st
from clases import Ligas
import numpy as np

Liga_española=Ligas("liga_española.xlsm")
Liga_española2=Ligas("liga_española2.xlsm")

Liga_alemana=Ligas("liga_alemana.xlsm")
Liga_Italiana=Ligas("liga_italiana.xlsm")
Liga_Inglesa=Ligas("liga_inglesa.xlsm")



def main():
   
    
    st.sidebar.header("Encuentros")
    local=st.sidebar.selectbox("Equipo Local",Liga_española.equipos_local())
    visita=st.sidebar.selectbox("Equipo Visita",Liga_española.equipos_visita())
    st.markdown("## "+local+" - "+visita)
    
    
    
    resultados = ['Victoria '+local, 'Empate', 'Victoria '+visita]
    probabilidades = [Liga_española.PosG_local(local,visita), Liga_española.Pos_empate(local,visita), Liga_española.PosG_visita(local,visita)]
    colores = ['blue', 'gray', 'green']
    plt.figure(figsize=(8, 5))
    plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
    plt.ylabel('Probabilidad')
    plt.title('Probabilidad de Resultado del Partido')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    st.pyplot(plt)


    goles = np.arange(0,11)
    prob_local = [
                        Liga_española.GeL(goles[0],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[1],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[2],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[3],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[4],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[5],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[6],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[7],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[8],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[9],Liga_española.FpL(local, visita)),
                        Liga_española.GeL(goles[10],Liga_española.FpL(local, visita)),

                    ]
    prob_visita = [
                        Liga_española.GeL(goles[0],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[1],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[2],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[3],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[4],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[5],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[6],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[7],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[8],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[9],Liga_española.FpV(local, visita)),
                        Liga_española.GeL(goles[10],Liga_española.FpV(local, visita)),

                    ]
    cdf_local = np.cumsum(prob_local)
    cdf_visita = np.cumsum(prob_visita)

    plt.figure(figsize=(10, 6))
    plt.plot(goles, cdf_local,marker='o', linestyle='-', color='blue', label=local)
    plt.plot(goles, cdf_visita,marker='o', linestyle='-', color='green', label=visita)
    plt.xlabel('Número de Goles (o menos)')
    plt.ylabel('Probabilidad Acumulada')
    plt.title('Distribución Acumulada de Goles')
    plt.xticks(goles)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    st.pyplot(plt)



if __name__=='__main__':
    main()
    