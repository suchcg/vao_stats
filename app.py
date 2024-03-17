import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Estadísticas VAO",
                  page_icon=":volleyball:",
                  layout="wide")

df = pd.read_csv("./total_equipo.csv")

#st.dataframe(df)


#--- SIDEBAR ---




#st.dataframe(df_selection)


#--- Mainpage ---
#Info por partido

st.title("Estadísticas por partido :bar_chart:")
partido_ppt=st.selectbox(
    "Selecciona el partido:",
    options=df["Partido"].unique())

df_selection_stadisticas_por_partido = df.query("Partido == @partido_ppt")
st.dataframe(df_selection_stadisticas_por_partido)

#KPI Partido
#ataques
intentos_partido = int(df_selection_stadisticas_por_partido["Intentos"].sum())
puntos_partido = int(df_selection_stadisticas_por_partido["Puntos"].sum())
errores_partido = int(df_selection_stadisticas_por_partido["Errors"].sum())
pe_total = puntos_partido/errores_partido
efectividad_total = puntos_partido/intentos_partido

#recepcion
avg_recepcion = df_selection_stadisticas_por_partido["Puntuacion"].notna().mean()



#Info por Jugador

st.title("Estadísticas por jugador :person_in_manual_wheelchair:")

jugador_ppt=st.selectbox(
    "Selecciona al jugador:",
    options=df["Jugador"].unique())

df_selection_stadisticas_por_jugador = df.query("Jugador == @jugador_ppt")
st.dataframe(df_selection_stadisticas_por_jugador)

#KPIs por jugador
#ataque_jug
intentos_jugador = int(df_selection_stadisticas_por_jugador["Intentos"].sum())
puntos_jugador = int(df_selection_stadisticas_por_jugador["Puntos"].sum())
errores_jugador = int(df_selection_stadisticas_por_jugador["Errors"].sum())
pe_total_jug = round(puntos_jugador/errores_jugador if errores_jugador !=0 else puntos_jugador,2)
efectividad_total_jug = round(puntos_jugador/intentos_jugador,2)

#defensa_jug



# Definir el color del texto basado en el valor
color = "red" if pe_total_jug < 1 else "green"

styled_text = f'<span style="color:{color}">{pe_total_jug}</span>'



left_jug, middle_jug, right_jug = st.columns(3)

with left_jug:
    st.subheader("Ataque:")
    st.write(f"Intentos totales: {intentos_jugador}")
    st.write(f"Puntos totales: {puntos_jugador}")
    st.write(f"Errores totales: {errores_jugador}")
    st.markdown(f"**Puntos por cada Error de ataque:** <span style='color:{color}'>{pe_total_jug}</span>", unsafe_allow_html=True)
    st.write(f"Puntos por intento: {efectividad_total_jug}")

with middle_jug:
    st.subheader("Recepción: (En construcción)")
    st.write(f"Puntuación media de recepción:")



with right_jug:
    st.subheader(f"Saques:(En construcción)")



