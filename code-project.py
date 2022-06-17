import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Prediction App for Laptop Price Range
This app lets user choose a few classification methods to predict laptop price ranges based on multiple predictors.""")
st.write("""Dataset of this laptop price range can get from here([https://www.kaggle.com/datasets/kuchhbhi/latest-laptop-price-list])
