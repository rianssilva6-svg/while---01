import streamlit as st

st.title("===login da conta===")

login = st.text_input("Digite o login: ")
senha = st.number_input("Digite a senha: ", step=5)

st.button("Verificar")

while True:
    if login == "Rian" and senha == 1234:
        st.success ("===Seja bem-vindo===")
        break
    else:
        st.error ("Login ou senha inválido!!")
        break
        