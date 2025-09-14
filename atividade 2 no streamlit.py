import streamlit as st
st.title ("===média do aluno===")


n1 = st.number_input("Digite a primeira nota do aluno: ", step=1)
n2 = st.number_input("Digite a segunda nota do aluno: ", step=1)
media = (n1 + n2) / 2
    
if st.button("Verificar"):
    st.write (f"A média do aluno foi: {media}")

    while True:
        if media < 0 or media > 10:
            st.error ("Escreva um algoritmo que solicite ao usuario a nota de um aluno!")
            break