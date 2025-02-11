import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(layout="wide")
    st.title("Visualisation de l'évolution de la radiance nocturne des communes en France")
    
    src = 'radiance_time_series_interp_9_q90.parquet'
    df = pd.read_parquet(src)

    commune = st.selectbox("Choisir une commune", df['code_insee'].unique())
    
    df_rad_values = df[df['code_insee'] == commune].drop(columns=['code_insee'])

    df_commune = df_rad_values.T.reset_index()
    df_commune.columns= ['date', 'radiance']
    df_commune['date'] = pd.to_datetime(df_commune['date'], format='%Y-%m')

    # Calcul des moyennes mobiles sur 6 et 12 mois
    df_commune['MA_6'] = df_commune['radiance'].rolling(window=6, center=True).mean()
    df_commune['MA_12'] = df_commune['radiance'].rolling(window=12, center=True).mean()

   
    fig_rad = go.Figure()
    fig_rad.add_trace(go.Scatter(x=df_commune['date'], y=df_commune['radiance'], mode='lines', name='Radiance moyenne', yaxis='y1'))
    fig_rad.add_trace(go.Scatter(x=df_commune['date'], y=df_commune['MA_6'], mode='lines', name='Moyenne mobile de radiance (6 mois)', line=dict(dash='dash'), yaxis='y1'))
    fig_rad.add_trace(go.Scatter(x=df_commune['date'], y=df_commune['MA_12'], mode='lines', name='Moyenne mobile de radiance (12 mois)', line=dict(dash='dash'), yaxis='y1'))
    
    fig_rad.update_layout(
        title=f"Série temporelle de la moyenne mensuelle de radiance nocturne sur la commune de {commune}",
        xaxis_title='Date',
        yaxis_title='Radiance (nW.sr-1.cm-2)',
        hovermode='x unified')


    st.plotly_chart(fig_rad)

if __name__ == "__main__":
    main()
