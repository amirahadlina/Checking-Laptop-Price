import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.title("""
# Choose Your Specs and Predict Your Laptop Price!

This app let's user predict their laptop price based on multiple specs preferences.""")

my_dataset = 'Cleaned_Laptop_data_newest.csv'

def explore_data[dataset]:
  df = pd.read_csv("https://raw.githubusercontent.com/amirahadlina/Checking-Laptop-Price/main/Cleaned_Laptop_data_newest.csv")

st.sidebar.header('Choose Your Specs Here')
