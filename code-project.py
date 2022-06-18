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

data = explore_data(my_dataset)


st.header('Choose Your Specs Here')


brand = st.selectbox("Choose your brand", ["Lenovo","Avita","HP","acer","ASUS","DELL","RedmiBook","realme","Infinix","MSI","MICROSOFT","SAMSUNG","Vaio","iball","APPLE","ALIENWARE","Nokia","LG","Smartron","Mi"])
processor = st.selectbox("Choose your Processor Brand", ["Intel","AMD","MediaTek","M1","Qualcomm"])
processor_name = st.selectbox("Choose your Processor Name",["Ryzen","Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9","Quad","Dual core","APU Dual","A6-9225","Athlon Dual","Core i3","Core i5","Core i7","Core i9", "Core m3","Genuine Windows","Plentium Silver","Pentium Quad","GeForce RTX","Hexacore","Everscreenpad","Celeron Dual","MediaTek","SnapDragon","M1"])
ram_GB = st.radio("Choose your RAM",["4GB","8GB","16GB","32GB"])
ssd = st.radio("Pick your storage(ssd)",["32GB","128GB","25GB6","512GB","1024GB"])
hdd = st.radio("Pick your storage(hdd)",["512GB","1024GB","2048GB"])
weight = st.radio("Pick your laptop's weight",["Casual","ThiNlight","Gaming"])

dataset = explore_data
X = pd.df(Cleaned_Laptop_data_newest.dataset, columns = ('brand','processor','processor_name','ram_GB','ssd','hdd','weight'))
Y = pd.df(Cleaned_Laptop_data_newest.target, columns = ['latest_price'])

clicked = st.button("Submit")
