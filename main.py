# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:21:30 2025

@author: Alex

"""
import numpy as np
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
        resultados = ['1', 'X', '2']
        probabilidades = [df.PosG_local(local,visita,ligas)*100, df.Pos_empate(local,visita,ligas)*100, df.PosG_visita(local,visita,ligas)*100]
        colores = ['green', 'Yellow', 'red']
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

        resultados = ['>0.5', '>1.5', '>2.5','>3.5','>4.5','>5.5']
        probabilidades = [df.May05(local,visita,ligas)*100,df.May15(local,visita,ligas)*100,df.May25(local,visita,ligas)*100,df.May35(local,visita,ligas)*100,df.May45(local,visita,ligas)*100,df.May55(local,visita,ligas)*100, ]
        colores = ['#28b463', '#2ecc71', '#58d68d','#82e0aa', '#abebc6', '#d5f5e3']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad Mas de Goles ',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)


        resultados = ['SI','NO']
        probabilidades = [df.AmbosMarcan(local,visita,ligas)*100,(1-df.AmbosMarcan(local,visita,ligas))*100]
        colores = ['green','red']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad que Ambos marcan',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)
    
    with col2:

        resultados = ['1X', '12', 'X2']
        probabilidades = [df.PosG_local(local,visita,ligas)*100+df.Pos_empate(local,visita,ligas)*100,df.PosG_local(local,visita,ligas)*100+df.PosG_visita(local,visita,ligas)*100,df.Pos_empate(local,visita,ligas)*100+df.PosG_visita(local,visita,ligas)*100]
        colores = ['green', 'Yellow', 'red']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad Doble Oportunidad',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)

        resultados = ['<0.5', '<1.5', '<2.5','<3.5','<4.5','<5.5']
        probabilidades = [(1-df.May05(local,visita,ligas))*100,(1-df.May15(local,visita,ligas))*100,(1-df.May25(local,visita,ligas))*100,(1-df.May35(local,visita,ligas))*100,(1-df.May45(local,visita,ligas))*100,(1-df.May55(local,visita,ligas))*100, ]
        colores = ['#d5f5e3', '#abebc6', '#82e0aa','#58d68d', '#2ecc71', '#28b463']
        plt.figure(figsize=(12, 8))
        bars=plt.bar(resultados, probabilidades, color=colores, alpha=0.7)
        plt.ylabel('Probabilidad (%)',fontsize=20)
        plt.title('Probabilidad Menos de Goles ',fontsize=20)
        plt.grid(axis='y', linestyle='--',)
        plt.bar_label(bars, padding=3,fmt='%.2f%%',fontsize=20)
        plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)],fontsize=20)
        plt.xticks(fontsize=16)
        plt.tight_layout()
        st.pyplot(plt)

        goles = np.arange(0,11)
        prob_local = [
                            df.GeL(goles[0],df.FpL(local, visita,ligas)),
                            df.GeL(goles[1],df.FpL(local, visita,ligas)),
                            df.GeL(goles[2],df.FpL(local, visita,ligas)),
                            df.GeL(goles[3],df.FpL(local, visita,ligas)),
                            df.GeL(goles[4],df.FpL(local, visita,ligas)),
                            df.GeL(goles[5],df.FpL(local, visita,ligas)),
                            df.GeL(goles[6],df.FpL(local, visita,ligas)),
                            df.GeL(goles[7],df.FpL(local, visita,ligas)),
                            df.GeL(goles[8],df.FpL(local, visita,ligas)),
                            df.GeL(goles[9],df.FpL(local, visita,ligas)),
                            df.GeL(goles[10],df.FpL(local, visita,ligas)),

                        ]
        prob_visita = [
                            df.GeL(goles[0],df.FpV(local, visita,ligas)),
                            df.GeL(goles[1],df.FpV(local, visita,ligas)),
                            df.GeL(goles[2],df.FpV(local, visita,ligas)),
                            df.GeL(goles[3],df.FpV(local, visita,ligas)),
                            df.GeL(goles[4],df.FpV(local, visita,ligas)),
                            df.GeL(goles[5],df.FpV(local, visita,ligas)),
                            df.GeL(goles[6],df.FpV(local, visita,ligas)),
                            df.GeL(goles[7],df.FpV(local, visita,ligas)),
                            df.GeL(goles[8],df.FpV(local, visita,ligas)),
                            df.GeL(goles[9],df.FpV(local, visita,ligas)),
                            df.GeL(goles[10],df.FpV(local, visita,ligas)),

                        ]
        cdf_local = np.cumsum(prob_local)
        cdf_visita = np.cumsum(prob_visita)

        plt.figure(figsize=(12, 8))
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
    