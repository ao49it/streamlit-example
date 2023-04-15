import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Récupération des données depuis le fichier CSV
url = "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"
data = pd.read_csv(url)

# Affichage de l'interface utilisateur
st.title("Vulnérabilités les plus exploitées")
product = st.selectbox("Produit", data.product.unique())

# Création du graphique
filtered_data = data[data.product == product]
counts = filtered_data.groupby("vulnerability_type").size()
plt.bar(counts.index, counts.values)

# Affichage du graphique
st.pyplot()
