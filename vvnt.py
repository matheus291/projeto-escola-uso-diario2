import streamlit as st
st.set_page_config(page_title='Informações sobre a venda de açai')
st.subheader('Digite as informações ao lado')

st.sidebar.header('Informações de quantidade de açai')
t = st.sidebar.number_input('Quantos açais trandicionais',min_value=0, max_value=1000)
ada = st.sidebar.number_input('Quantos Açais adicionais completos vendidos', min_value=0, max_value=1000)
adc = st.sidebar.number_input('Quantos Açais com creme de avelã vendidos', min_value=0, max_value=1000)
adp = st.sidebar.number_input('Quantos Açais com paçoca vendidos?', min_value=0, max_value=1000)
st.write('---')
tf=t*13
adaf = ada * 18
adcf = adc * 16
adpf = adp * 15
valor =  tf+adaf+adcf+adpf
if st.button('Iniciar'):
    st.write(f'o valor constado nas vendas é de R${valor}.')
    st.write(f'A quantidade de açai Tradicional foi de {t} e o valor arrecadado foi de R${tf}')
    st.write(f'A quantidade de açai Adicional completo foi de {ada} e o valor scorecard foi de R${adaf}')
    st.write(f'A quantidade de açai Adicional creme de avelã foi de {adc} e o valor arrecadado foi de R${adcf}')
    st.write(f'A quantidade de açai Adicional com paçoca foi de {adp} e o valor arrecadado foi de R${adpf}')
