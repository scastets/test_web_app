import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    st.title("Détection de l'extinction de l'éclairage public")
    
    src = 'radiance_time_series_interp_9_q90.parquet'
    df = pd.read_parquet(src, index_col=0)

    commune = st.selectbox("Choisir une commune", df['code_insee'].unique())
    
    df_rad_values = df[df['code_insee'] == commune].drop(columns=['code_insee'])
        
    print(df_rad_values)

if __name__ == "__main__":
    main()
