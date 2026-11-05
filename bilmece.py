import streamlit as st
st.title('bilmece oyunu')
st.write('Şehirleri gezer ama hiç hareket etmez') 
cevap=st.text_input('bilmece sorusu')
if cevap.lower()=='yol':
 st.success('Tebrikler doğru bildiniz')
elif cevap!='':
 st.error('Tekrar deneyiniz')
