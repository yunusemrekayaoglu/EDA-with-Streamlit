# page/eda.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.logger import OperationLogger
from models.data_model import DataModel

class EDA:
    def __init__(self):
        if 'data_model' not in st.session_state:
            st.session_state.data_model = None
        if 'user' not in st.session_state:
            st.session_state.user = ""

        self.logger = OperationLogger()

    def display(self):
        st.title('Exploratory Data Analysis (EDA)')

        if st.session_state.data_model is None:
            st.warning("Veri seti yüklenmedi. Ana sayfadan veri yüklemeyi unutmayın.")
            return

        data = st.session_state.data_model.get_data()

        if data.empty:
            st.warning("Veri seti boş.")
            return

        st.sidebar.header("Sütun Seçimi")
        numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = data.select_dtypes(include=['object', 'bool']).columns.tolist()
        datetime_cols = data.select_dtypes(include=['datetime']).columns.tolist()

        selected_numeric_cols = st.sidebar.multiselect("Sayısal Sütunları Seçin", numeric_cols)
        selected_categorical_cols = st.sidebar.multiselect("Kategorik Sütunları Seçin", categorical_cols)
        selected_datetime_cols = st.sidebar.multiselect("Tarih/Saat Sütunlarını Seçin", datetime_cols)

        if st.checkbox("Veri Seti Özeti Göster"):
            self.show_data_summary(data)
            self.logger.log_operation(st.session_state.user, "Veri Seti Özeti Göster")

        if st.checkbox("Sayısal Sütunların Histogramlarını Göster"):
            self.plot_histograms(data, selected_numeric_cols)
            self.logger.log_operation(st.session_state.user, "Sayısal Sütunların Histogramlarını Göster", selected_numeric_cols)

        if st.checkbox("Kategorik Sütunların Dağılımını Göster"):
            self.plot_categorical_distributions(data, selected_categorical_cols)
            self.logger.log_operation(st.session_state.user, "Kategorik Sütunların Dağılımını Göster", selected_categorical_cols)

        if st.checkbox("Korelasyon Matrisi Göster"):
            self.plot_correlation_matrix(data, selected_numeric_cols)
            self.logger.log_operation(st.session_state.user, "Korelasyon Matrisi Göster", selected_numeric_cols)

        if st.checkbox("Zaman Serisi Analizi Göster"):
            self.plot_time_series(data, selected_datetime_cols)
            self.logger.log_operation(st.session_state.user, "Zaman Serisi Analizi Göster", selected_datetime_cols)

        if st.checkbox("Sayısal Sütunların Boxplotlarını Göster"):
            self.plot_boxplots(data, selected_numeric_cols)
            self.logger.log_operation(st.session_state.user, "Sayısal Sütunların Boxplotlarını Göster", selected_numeric_cols)

    def show_data_summary(self, data):
        st.subheader("Veri Seti Özeti")
        st.write(f"Satır Sayısı: {len(data)}")
        st.write(f"Sütun Sayısı: {len(data.columns)}")
        st.write(f"Sütun İsimleri: {list(data.columns)}")

    def plot_histograms(self, data, columns):
        if columns:
            st.subheader("Sayısal Sütunların Histogramları")
            for col in columns:
                st.write(f"Histogram: {col}")
                st.bar_chart(data[col])
        else:
            st.warning("Seçilen sayısal sütun bulunmuyor.")

    def plot_categorical_distributions(self, data, columns):
        if columns:
            st.subheader("Kategorik Sütunların Dağılımları")
            for col in columns:
                st.write(f"Dağılım: {col}")
                st.bar_chart(data[col].value_counts())
        else:
            st.warning("Seçilen kategorik sütun bulunmuyor.")

    def plot_correlation_matrix(self, data, columns):
        if columns:
            st.subheader("Korelasyon Matrisi")
            corr = data[columns].corr()
            st.write(sns.heatmap(corr, annot=True, cmap='coolwarm'))
            st.pyplot()
        else:
            st.warning("Seçilen sayısal sütun bulunmuyor.")

    def plot_time_series(self, data, columns):
        if columns:
            st.subheader("Zaman Serisi Analizleri")
            for col in columns:
                st.write(f"Zaman Serisi: {col}")

                if data[col].isnull().any():
                    st.warning(f"{col} sütununda eksik veriler bulunuyor. Lütfen eksik verileri doldurun veya temizleyin.")
                    data = data.dropna(subset=[col])

                st.line_chart(data.set_index(col).index)
                st.write("Verinin Tarihsel Dağılımı:")
                data_col = data[col].dropna()
                st.line_chart(data_col.value_counts())
        else:
            st.warning("Seçilen tarih/saat sütunu bulunmuyor.")

    def plot_boxplots(self, data, columns):
        if columns:
            st.subheader("Sayısal Sütunların Boxplotları")
            for col in columns:
                st.write(f"Boxplot: {col}")
                plt.figure(figsize=(10, 4))
                sns.boxplot(data=data, y=col)
                st.pyplot()
        else:
            st.warning("Seçilen sayısal sütun bulunmuyor.")
