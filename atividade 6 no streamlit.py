import streamlit as st

st.title ("===Restaurante===")
st.header ("Cardápio")
st.write ("1- Picanha R$ 25,00")
st.write ("2- Lasanha R$ 20,00")
st.write ("3- Strogonoff R$ 18,00")
st.write ("4- Bife Acebolado R$ 15,00")
st.write ("5- Pão com ovo R$ 5,00")

num = st.number_input("Digite o número do prato: ", step=1, min_value=0)

if st.button ("prato desejado"):
    if num == 1:
        st.success("Seu prato foi picanha e o valor é R$25,00")
    if num == 2:
        st.success("Seu prato foi Lasanha e o valor é R$20,00")
    if num == 3:
        st.success("Seu prato foi Strogonoff e o valor é R$18,00")  
    if num == 4:
        st.success("Seu prato foi Bife acebolado e o valor é R$15,00")  
    if num ==5:
        st.success("Seu prato foi Pão com ovo e o valor é R$5,00") 
    else:
        st.error ("Digite o número do prato corretamente!")           

