import streamlit as st

st.title ("Notas")

numero = st.number_input("Digite a nota do aluno: ", step=1)
st.button ("Verificar")
st.write (f"A nota do aluno foi: {numero}")
while True:
    if numero > 10 or numero < 0:
        st.error ("Escreva um algoritmo que solicite ao usuario a nota de um aluno!")
        break
    else:
        if numero >= 7:
            st.success ("Aprovado")
            break
        elif numero >= 5:
            st.warning ("Recuperação")
            break
        else:
            st.error ("Reprovado")
            break