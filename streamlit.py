import streamlit as st
st.title("basit hesap makinesi")
sayi1=st.number_input("birinci sayıyı girin")
sayi2=st.number_input("ikinci sayıyı girin")
islem=st.selectbox("bir işlem seçin",["toplama","çıkarma","çarpma","bölme"])
if islem =="toplama":
sonuc=sayi1+sayi2
st.write(sonuc)
