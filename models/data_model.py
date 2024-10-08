# models/data_model.py

import pandas as pd

class DataModel:
    def __init__(self, file):
        self.file = file
        self.data = None
        self.numeric_columns = []
        self.categorical_columns = []
        self.datetime_columns = []
        self.load_data(file)
        self.find_dtypes()
        self.update_dataframes()
        self.numerical_describe()
        self.categorical_describe()
        self.datetime_describe()

    def load_data(self, file):
        try:
            self.data = pd.read_parquet(file)
        except Exception as e:
            print(f"Veri yüklenirken bir hata oluştu: {e}")
            self.data = pd.DataFrame()

    def get_data(self):
        return self.data

    def find_dtypes(self):
        if self.data is None or self.data.empty:
            print("Veri çerçevesi boş veya yüklenmemiş.")
            return
        self.numeric_columns = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        self.categorical_columns = [col for col in self.data.columns if pd.api.types.is_string_dtype(self.data[col]) or pd.api.types.is_bool_dtype(self.data[col])]
        self.datetime_columns = [col for col in self.data.columns if pd.api.types.is_datetime64_any_dtype(self.data[col])]
        self.numeric_columns = [col for col in self.numeric_columns if col not in self.categorical_columns]

    def update_dataframes(self):
        self.numeric_columns_df = self.data[self.numeric_columns] if self.numeric_columns else pd.DataFrame()
        self.categorical_columns_df = self.data[self.categorical_columns] if self.categorical_columns else pd.DataFrame()
        self.datetime_columns_df = self.data[self.datetime_columns] if self.datetime_columns else pd.DataFrame()

    def numerical_col(self):
        return self.numeric_columns if self.numeric_columns else "Sayısal sütun bulunmuyor."

    def categorical_col(self):
        return self.categorical_columns if self.categorical_columns else "Kategorik sütun bulunmuyor."

    def datetime_col(self):
        return self.datetime_columns if self.datetime_columns else "Tarih, saat sütun bulunmuyor."

    def numerical_describe(self):
        if not self.numeric_columns_df.empty:
            description = self.numeric_columns_df.describe().T
            print("Sayısal sütunların özet istatistikleri:")
            print(description)
            return description
        else:
            print("Sayısal sütunlar mevcut değil.")
            return pd.DataFrame()

    def categorical_describe(self):
        if not self.categorical_columns_df.empty:
            description = self.categorical_columns_df.describe(include='all').T
            print("Kategorik sütunların özet istatistikleri:")
            print(description)
            return description
        else:
            print("Kategorik sütunlar mevcut değil.")
            return pd.DataFrame()

    def datetime_describe(self):
        if not self.datetime_columns_df.empty:
            description = self.datetime_columns_df.describe(include='all').T
            print("Tarih ve saat sütunlarının özet istatistikleri:")
            print(description)
            return description
        else:
            print("Tarih ve saat sütunlar mevcut değil.")
            return pd.DataFrame()
