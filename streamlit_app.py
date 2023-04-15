import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Récupération des données depuis l'URL fournie
url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
response = requests.get(url)
data = pd.DataFrame(response.json())

# Affichage de l'interface utilisateur
st.title("Vulnérabilités les plus exploitées")
#product = st.selectbox("Produit", data.product.unique())
product_options = list(data.product.unique())
product = st.sidebar.selectbox("Produit", product_options)

# Création du graphique
filtered_data = data[data.product == product]
counts = filtered_data.groupby("vulnerability_type").size()
plt.bar(counts.index, counts.values)

# Affichage du graphique
st.pyplot()
