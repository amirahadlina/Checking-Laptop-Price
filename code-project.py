import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.title("""
Choose Your Specs and Predict Your Laptop Price!

This app let user predict their laptop price based on multiple specs preferences.""")

df = pd.read_csv("https://raw.githubusercontent.com/amirahadlina/Checking-Laptop-Price/main/Cleaned_Laptop_data_newest.csv")
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
df['brand'] = labelencoder.fit_transform(df['brand'])
df['processor_brand'] = labelencoder.fit_transform(df['processor_brand'])
df['processor_name'] = labelencoder.fit_transform(df['processor_name'])
df['weight'] = labelencoder.fit_transform(df['weight'])

X = df[['brand','processor_brand','processor_name','ram_gb','ssd','hdd','weight']]
y = df['latest_price']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2, random_state = 999)

from sklearn.svm import SVC
laptop = SVC()
laptop.fit(Xtrain, ytrain)
ypred = laptop.predict(Xtest)

st.header('Choose Your Specs Here')

brand = st.selectbox("Choose your brand", ["Lenovo","Avita","HP","acer","ASUS","DELL","RedmiBook","realme","Infinix","MSI","MICROSOFT","SAMSUNG","Vaio","iball","APPLE","ALIENWARE","Nokia","LG","Smartron","Mi"])
processor_brand = st.selectbox("Choose your Processor Brand", ["Intel","AMD","MediaTek","M1","Qualcomm"])
processor_name = st.selectbox("Choose your Processor Name",["Ryzen","Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9","Quad","Dual core","APU Dual","A6-9225","Athlon Dual","Core i3","Core i5","Core i7","Core i9", "Core m3","Genuine Windows","Plentium Silver","Pentium Quad","GeForce RTX","Hexacore","Everscreenpad","Celeron Dual","MediaTek","SnapDragon","M1"])
ram_gb = st.radio("Choose your RAM",["4","8","16","32"])
ssd = st.radio("Pick your storage(ssd)",["32","128","256","512","1024"])
hdd = st.radio("Pick your storage(hdd)",["512","1024","2048"])
weight = st.radio("Pick your laptop's weight",["Casual","ThiNlight","Gaming"])

if st.button("Submit"):
  Xnew = pd.DataFrame([[brand,processor_brand,processor_name,ram_gb,ssd,hdd,weight]],
                      column = ["brand","processor_brand","processor_name","ram_gb","ssd","hdd","weight"])

  prediction = laptop.predict(Xnew)[0]
  
  st.write(f"Your laptop's price is {predicted}")
