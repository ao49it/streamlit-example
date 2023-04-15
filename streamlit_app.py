import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import schedule
import time

# Fonction pour récupérer les données et les stocker dans un fichier CSV
def get_data():
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    data = pd.read_json(url)
    data.to_csv("data.csv", index=False)

# Planifier la récupération des données chaque jour à 8h
schedule.every().day.at("08:00").do(get_data)

# Attendre jusqu'à 8h pour récupérer les données pour la première fois
while True:
    if time.strftime("%H:%M:%S") == "08:00:00":
        get_data()
        break
    time.sleep(1)

# Récupération des données depuis le fichier CSV
data = pd.read_csv("data.csv")

# Affichage de l'interface utilisateur
st.title("Vulnérabilités les plus exploitées")
product = st.selectbox("Produit", data.product.unique())

# Création du graphique
filtered_data = data[data.product == product]
counts = filtered_data.groupby("vulnerability_type").size()
plt.bar(counts.index, counts.values)

# Affichage du graphique
st.pyplot()
