import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre du dashboard
st.title("Dashboard interactif avec Streamlit")

# Création d'un slider pour modifier la fréquence de la sinusoïde
freq = st.slider("Choisissez une fréquence", min_value=1, max_value=20, value=5)

# Génération des données
x = np.linspace(0, 10, 100)
y = np.sin(freq * x)

# Affichage du graphique
fig, ax = plt.subplots()
ax.plot(x, y, label=f"Sinus {freq} Hz")
ax.legend()
st.pyplot(fig)
