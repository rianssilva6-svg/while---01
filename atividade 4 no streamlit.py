import streamlit as st
st.title ("===login da conta===")

login_salvo = "Rian"
senha_salva = "1234"

st.session_state.setdefault("campos", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input ("Digite o login: ", disabled=st.session_state.campos)
senha = st.text_input ("Digite a senha: ", type="password", disabled=st.session_state.campos)

if st.button ("Verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success ("Seja bem vindo!!")
    else:
        st.session_state.tentativas += 1    
    if st.session_state.tentativas <= 3:
        st.warning (f"Login ou senha inválidos, tentativas: {st.session_state.tentativas}")    
    else:
        st.session_state.campos = True   
        st.error ("limite de tentativas atingidos") 