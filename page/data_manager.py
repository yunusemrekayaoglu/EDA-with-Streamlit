# page/data_manager.py

import streamlit as st
from models.data_model import DataModel

class DataManager:
    def __init__(self):
        if 'data_model' not in st.session_state:
            st.session_state.data_model = None
        if 'data_loaded' not in st.session_state:
            st.session_state.data_loaded = False

    def load_data(self, file):
        if not st.session_state.data_loaded:
            st.session_state.data_model = DataModel(file)
            st.session_state.data_loaded = True
            return True
        return False

    def get_data_model(self):
        return st.session_state.data_model
