import streamlit as st

nome = st.text_input("Digite o nome do aluno: ")
n1 = st.number_input("Digite a primeira nota do aluno: ", step=1, min_value=0)
n2 = st.number_input("Digite a segunda nota do aluno: ", step=1, min_value=0)
n3 = st.number_input("Digite a terceira nota do aluno: ", step=1, min_value=0)

media = (n1 + n2 + n3) / 3

while True:
    if media > 7:
     st.success (f"Parabens, sua média foi {media: .1f} e está aprovado!!")
     break
    elif media >= 5 and 6.9:
     st.warning(f"Você está de recuperação, sua média foi {media: .1f}")
     break
    else:
       st.error (f"Está reprovado!! sua média foi {media: .1f}")  
    break