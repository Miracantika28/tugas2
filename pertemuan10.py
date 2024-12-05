import pandas as pd 
import streamlit as st
import plotly.express as px 
import yfinance as yf

st.title("Pertemuan 10: interaksi streamlit dan Yahoo Finance")
st.write("# Pendahuluan")

kamus_ticker = {
    'GOOGL': 'Google',
    'AAPL' : 'Aplle',
    'SBUX' : 'Starbucks',
    'MCD' : 'McDonals',
    'BBNI' : 'Bank Negara Indonesia (persero) Tbk PT',
    'BMRI' : 'Bank Mandiri (persero) Tbk PT',
    'BBRI' : 'Bank Rakyat Indonesia (persero) Tbk PT'
}
tickerSymbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    kamus_ticker.keys()
)


st.write(f'{kamus_ticker.keys()}')
    
tickerSymbol = 'GOOGL'

st.write(f'Harga saham {tickerSymbol}.')

tickerData = yf.Ticker(tickerSymbol)
pilihan_periode = st.selectbox(
    'pilih periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y']
)

tickerdata = yf.Ticker(tickerSymbol)
tickerDF = tickerdata.history(
    period='1d',
    start='2024-10-01',
    end='2024-11-06'
)
flag_tampil = st.checkbox('Tampilkan tabel')
if flag_tampil:
    st.write(tickerDF.head(10))

flag_grafik = st.checkbox('Tampilkan grafik')
pilihan_atribut = st.multiselect(
    'silahkan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)

grafik = px.line(
    tickerDF,
    title=f'Harga Saham {tickerSymbol}',
    y = pilihan_atribut
)
st.plotly_chart(grafik)
    
    


    