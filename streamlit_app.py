def main():
    st.title("Détection de l'extinction de l'éclairage public")
    
    src = 'radiance_time_series_interp_9_q90.parquet'
    df = pd.read_parquet(src)

    commune = st.selectbox("Choisir une commune", df['code_insee'].unique())
    
    df_rad_values = df[df['code_insee'] == commune].drop(columns=['code_insee'])

    df_commune = df_rad_values.T.reset_index()
    df_commune.columns= ['date', 'radiance']
    df_commune['date'] = pd.to_datetime(df_commune['date'], format='%Y-%m')
   
    fig_rad = go.Figure()
    fig_rad.add_trace(go.Scatter(x=df_commune['date'], y=df_commune['radiance'], mode='lines', name='Radiance moyenne', yaxis='y1'))
        
    st.plotly_chart(fig_rad)

if __name__ == "__main__":
    main()
