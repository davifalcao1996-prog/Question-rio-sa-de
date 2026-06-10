import streamlit as st

st.title("Questionário de Saúde")

nome = st.text_input("Qual é o seu nome?")
idade = st.text_input("Qual é a sua idade?")
peso = st.text_input("Qual é o seu peso?")
horario = st.text_input("Qual é o horário que você acorda diariamente?")
comer = st.text_input("O que come pela manhã?")
sono = st.text_input("Qual horário você dorme diariamente?")
comida = st.text_input("Qual comida não pode faltar no seu cardápio?")
banheiro = st.text_input("Quantas vezes vai ao banheiro por dia?")
refeicoes = st.text_input("Quantas refeições você faz ao dia?")
atividade = st.text_input("Pratica alguma atividade física?")
doenca = st.text_input("Tem algum tipo de doença crônica?")

if st.button("Enviar"):
    st.success("Questionário enviado!")
    st.write({
        "Nome": nome,
        "Idade": idade,
        "Peso": peso,
        "Acorda": horario,
        "Café da manhã": comer,
        "Sono": sono,
        "Comida": comida,
        "Banheiro": banheiro,
        "Refeições": refeicoes,
        "Atividade": atividade,
        "Doença": doenca
    })
