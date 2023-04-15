import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Récupération des données
url = "https://us-cert.cisa.gov/api/v1/summary"
data = pd.read_json(url)
data = pd.json_normalize(data["data"])

# Affichage de l'interface utilisateur
st.title("Vulnérabilités les plus exploitées")
product = st.selectbox("Produit", data.product.unique())
chart_type = st.selectbox("Type de graphique", ["Barres", "Camembert"])

# Création du graphique
filtered_data = data[data.product == product]
counts = filtered_data.groupby("vulnerability_type").size()
if chart_type == "Barres":
    plt.bar(counts.index, counts.values)
else:
    plt.pie(counts.values, labels=counts.index)

# Affichage du graphique
st.pyplot()
