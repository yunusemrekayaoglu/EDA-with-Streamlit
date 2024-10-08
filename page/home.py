# page/home.py

import streamlit as st
from utils.logger import OperationLogger
from models.data_model import DataModel
from page.data_manager import DataManager  # Import DataManager

class HomePage:
    def __init__(self):
        self.logger = OperationLogger()
        if 'user' not in st.session_state:
            st.session_state.user = ""
        if 'data_model' not in st.session_state:
            st.session_state.data_model = None

    def display(self):
        st.title('Ana Sayfa')

        user_name = st.text_input("Kullanıcı Adınızı Girin:")
        if user_name:
            st.session_state.user = user_name
            st.success(f"Kullanıcı adı '{user_name}' olarak ayarlandı.")
            self.logger.log_operation(user_name, "Kullanıcı adı ayarlandı.")

        uploaded_file = st.file_uploader("Veri dosyasını yükleyin (Parquet formatında)", type=["parquet"])
        if uploaded_file is not None:
            data_manager = DataManager()
            if data_manager.load_data(uploaded_file):
                st.success("Veri seti yüklendi! İçeriğini kontrol etmek için butona tıklayınız.")
                self.logger.log_operation(user_name, "Veri dosyası yüklendi.")
            else:
                st.warning("Veri seti zaten yüklendi.")

        data_model = DataManager().get_data_model()
        if data_model is not None:
            data = data_model.get_data()
            st.write("Veri İçeriği:")
            st.write(data)
            st.write(f"Satır Sayısı: {len(data)}")
            st.write(f"Sütun Sayısı: {len(data.columns)}")
            st.write(f"Sütun İsimleri: {list(data.columns)}")

        with st.expander("Veri seti içeriği için tıklayın"):
            if st.button("Sayısal sütunları görmek için tıklayın"):
                st.write(data_model.numerical_col())
                self.logger.log_operation(user_name, "Sayısal sütunlar gösterildi.")

            if st.button("Kategorik sütunları görmek için tıklayın"):
                st.write(data_model.categorical_col())
                self.logger.log_operation(user_name, "Kategorik sütunlar gösterildi.")

            if st.button("Tarih, Saat sütunları görmek için tıklayın"):
                st.write(data_model.datetime_col())
                self.logger.log_operation(user_name, "Tarih, Saat sütunlar gösterildi.")

            if st.button("İstatistiksel Sonuçlarını görmek için tıklayın"):
                st.write(data_model.numerical_describe())
                self.logger.log_operation(user_name, "İstatistiksel sonuçlar gösterildi.")
