import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.title("""
Choose Your Specs and Predict Your Laptop Price!

This app let user predict their laptop price based on multiple specs preferences.""")

df = pd.read_csv("https://raw.githubusercontent.com/amirahadlina/Checking-Laptop-Price/main/Cleaned_Laptop_data_newest.csv")

X = df['brand','processor','processor_name','ram_GB','ssd','hdd','weight']
Y = df['latest_price']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2, random_state = 999)

laptop = SVC()
laptop.fit(Xtrain, ytrain)
ypred = laptop.predict(Xtest)

st.header('Choose Your Specs Here')

brand = st.selectbox("Choose your brand", ["Lenovo","Avita","HP","acer","ASUS","DELL","RedmiBook","realme","Infinix","MSI","MICROSOFT","SAMSUNG","Vaio","iball","APPLE","ALIENWARE","Nokia","LG","Smartron","Mi"])
processor = st.selectbox("Choose your Processor Brand", ["Intel","AMD","MediaTek","M1","Qualcomm"])
processor_name = st.selectbox("Choose your Processor Name",["Ryzen","Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9","Quad","Dual core","APU Dual","A6-9225","Athlon Dual","Core i3","Core i5","Core i7","Core i9", "Core m3","Genuine Windows","Plentium Silver","Pentium Quad","GeForce RTX","Hexacore","Everscreenpad","Celeron Dual","MediaTek","SnapDragon","M1"])
ram_GB = st.radio("Choose your RAM",["4GB","8GB","16GB","32GB"])
ssd = st.radio("Pick your storage(ssd)",["32GB","128GB","25GB6","512GB","1024GB"])
hdd = st.radio("Pick your storage(hdd)",["512GB","1024GB","2048GB"])
weight = st.radio("Pick your laptop's weight",["Casual","ThiNlight","Gaming"])

if st.button("Submit"):
  Xnew = pd.DataFrame([[brand,processor,processor_name,ram_GB,ssd,hdd,weight]],
                      column = ["brand","processor","processor_name","ram_GB","ssd","hdd","weight"])

  prediction = laptop.predict(Xnew)[0]
  
  st.write(f"Your laptop's price is {predicted}")


clicked = st.button("Submit")
