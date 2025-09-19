import streamlit as st
st.title ("Viajar")

nome = st.text_input("Digite seu nome: ")
viagem = st.selectbox('Qual cidade você gostaria de visitar?',['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'])
grana = st.slider ("Qual seu orçamento?:", min_value=0, max_value=10000, step=10)
hotel = st.radio ("Já alugou um apartamento?", ["Sim", "Não"])

if st.button ("Verificar"):
  st.write (f"Seu nome é {nome}")
  st.write (f"Seu destino é {viagem}")
  st.write (f"Seu orçamento é {grana}")
  st.write (f"tem apartamento? {hotel}")

comente = st.chat_input ("Digite como foi a experiencia")
st.write (f"{comente}")