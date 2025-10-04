import streamlit as st

phi = 22/7
st.header("Aplikasi Luas Lingkaran")
inputan = st.number_input("Masukkan diameter atau jari jarinya!", 0)
st.write("Pilih salah satu !")
if st.button("Jari-jari") :
	rumus = phi * inputan * inputan
	st.write("Kamu memilih jari jari : ", rumus)
	
if st.button("Diameter") :
	bagi = inputan / 2
	rumus = phi * bagi * bagi 
	st.write("Kamu memilih diameter : ", rumus)