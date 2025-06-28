import streamlit as st
from funcoes import ler_usuarios, salvar_tarefa, filtrar_tarefas

st.title("Sistema de Tarefas")

menu = st.sidebar.selectbox("Menu", ["Cadastrar tarefa", "Visualizar tarefas"])

usuarios = ler_usuarios()

if menu == "Cadastrar tarefa":
    st.header("Cadastro de Tarefa")

    if not usuarios:
        st.warning("Adicione nomes no arquivo usuarios.txt")
    else:
        nome = st.selectbox("Usuário", usuarios)
        descricao = st.text_input("Descrição da tarefa")
        prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])

        if st.button("Salvar"):
            if descricao.strip():
                salvar_tarefa(nome, descricao, prioridade)
                st.success("Tarefa salva!")
            else:
                st.warning("A descrição não pode estar vazia.")

elif menu == "Visualizar tarefas":
    st.header("Tarefas do Usuário")

    if not usuarios:
        st.warning("Adicione nomes no arquivo usuarios.txt")
    else:
        nome = st.selectbox("Escolha o usuário", usuarios)
        tarefas = filtrar_tarefas(nome)

        if tarefas:
            for usuario, desc, prioridade in tarefas:
                st.write(f"• ({prioridade}) {desc}")
        else:
            st.info("Nenhuma tarefa encontrada.")
