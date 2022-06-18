import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.title("""
Choose Your Specs and Predict Your Laptop Price!

This app let user predict their laptop price based on multiple specs preferences.""")

my_dataset = 'Cleaned_Laptop_data_newest.csv'

def explore_data(dataset):
  df = pd.read_csv("https://raw.githubusercontent.com/amirahadlina/Checking-Laptop-Price/main/Cleaned_Laptop_data_newest.csv")
  return df

st.header('Choose Your Specs Here')
brand = st.selectbox("Choose your brand", ["Lenovo","Avita","HP","acer","ASUS","DELL","RedmiBook","realme","Infinix","MSI","MICROSOFT","SAMSUNG","Vaio","iball","APPLE","ALIENWARE","Nokia","LG","Smartron","Mi"])

st.header('Choose Your Processor Brand')
processor = st.selectbox("Choose your Processor Brand", ["Intel","AMD","MediaTek","M1","Qualcomm"])
