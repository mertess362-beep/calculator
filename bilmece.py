import streamlit as st
st.title('bilmece oyunu')
cevap=st.text_input('bilmece sorusu')
if cevap.lower()=='yol':
 st.success('Tebrikler doğru bildiniz')
elif cevap!='':
 st.error('Tekrar deneyiniz')
