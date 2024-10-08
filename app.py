import streamlit as st
from page.home import HomePage
from page.eda import EDA

def main():
    st.sidebar.title('Navigasyon')
    page = st.sidebar.radio("Sayfa Seçin", ["Ana Sayfa", "EDA"])

    if page == "Ana Sayfa":
        HomePage().display()
    elif page == "EDA":
        EDA().display()

if __name__ == "__main__":
    main()
