import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.title("""
# Choose Your Specs and Predict Your Laptop Price!

This app let's user predict their laptop price based on multiple specs preferences.""")

st.sidebar.header('Choose Your Specs Here')

def spec_input_features():
  
  
