# Bibliotecas importadas para o projeto:
import streamlit as st
import datetime
import pandas as pd
import numpy as np

            
# Distribuição de páginas do site:
st.sidebar.title('Menu')
pagina_selecionada = st.sidebar.selectbox('Opções para realizar o acerto:', ['Dados Empresa', 'Dados da Frota', 'Cadastro Motorista', 'Cadastro Dados Viagem', 'Cadastro Abastecimentos', 'Cadastro Despesas', 'Fechamento do Acerto'])

# Seleções de páginas do site:
if pagina_selecionada == 'Dados Empresa':
    st.title("Acerto de Contas Transportes Gurupi Eirelli")
    st.subheader('CNPJ: 18.042.398/0001-94') 
    st.subheader('Inscrição Estadual: ')     
    st.subheader('Endereço: Rua 1, 45 SALA B.')
    st.subheader('Bairro: Valle dos Igarapés.')  
    st.subheader('Cidade: Igarapé.')  
    st.subheader('UF: Minas Gerais.')  
 
elif pagina_selecionada == 'Dados da Frota':
    st.title('Dados da Frota: ')
    frota = st.text_input("Digite o número da frota: ") 
    placa_cavalo = st.text_input("Digite a placa do cavalo: ")  
    placa_carreta = st.text_input("Digite a placa da carreta: ")  
    enviar_dados_frota = st.button("Enviar")
 
 
    
elif pagina_selecionada == 'Cadastro Motorista':
    st.title('Dados do Motorista: ')
    nome_motorista = st.text_input("Digite o nome do motorista:")  
    cpf_motorista = st.text_input("Digite o CPF do motorista:")  
    data_nascimento_motorista = st.date_input("Selecione a data do nascimento do motorista:", format="DD-MM-YYYY")     
    enviar_dados_motorista = st.button("Enviar")
    
    
    st.write("Nome do Motorista: "  + nome_motorista)
    st.write("CPF do Motorista: "  + cpf_motorista)
    st.write(f"Data do Nascimento do Motorista: {data_nascimento_motorista:%d/%m/%y}")
     
elif pagina_selecionada == 'Cadastro Dados Viagem':
    st.title('Dados da Viagem: ')
    
    numero_contrato = st.number_input("Digite o número do contrato: ")
    valor_frete = st.number_input("Valor do Frete: ")
    
    
    selecao_adiantamento = st.selectbox('Selecione uma opção de adiantamento: ', ['Adiantamento em Cheque', 'Adiantamento Cartão Débito', 'Adiantamento em Folha'])
    
       
    if selecao_adiantamento == 'Adiantamento em Folha':
        sem_adiantamento = (valor_frete * 0)
        st.write(f"Valor do Adiantamento:  R$ {sem_adiantamento:.2f}")

    else:
        adiantamento = (valor_frete * 0.5)
        st.write(f"Valor do Adiantamento:  R$ {adiantamento:.2f}")


    enviar_dados_viagem = st.button("Enviar")
    
    
    
elif pagina_selecionada == 'Cadastro Abastecimentos':
    st.title('Dados dos Abastecimentos: ')
    
    st.write('---')
    
    # Variáveis dos dados dos abastecimentos:
    with st.container():
        st.subheader('Diesel:')
        data_abastecimento = st.date_input("Data do Abastecimento:", format="DD/MM/YYYY")
        litragem_abastecimento_diesel = st.number_input("Litragem do Abastecimento de Diesel:")
        valor_abastecimento_diesel = st.number_input("Valor do Abastecimento de Diesel: ")
 
    st.write('---')   
    
    with st.container():
        st.subheader('Arla32:')
        litragem_abastecimento_arla = st.number_input("Litragem do Arla32: ")
        valor_abastecimento_arla = st.number_input("Valor do Arla32: ")
        enviar_dados_abastecimentos = st.button("Enviar")
    
    
    st.write('---')
    
    # Prints dos dados do abastecimento no site:
    st.subheader('Relatório do Abastecimento: ')
    with st.container():
        st.write(f"Data do Abastecimento:  {data_abastecimento:%d/%m/%y}")
        st.write(f"Litragem do Abastecimento de Diesel: {litragem_abastecimento_diesel:.3f}")
        st.write(f"Valor do Abastecimento de Diesel:  R$ {valor_abastecimento_diesel:.2f}")

        st.write(f"Litragem do Abastecimento de Arla32: {litragem_abastecimento_arla:.3f}")
        st.write(f"Valor do Abastecimento de Arla32:  R$ {valor_abastecimento_arla:.2f}")
        valor_total_abastecimento = (valor_abastecimento_diesel + valor_abastecimento_arla)
        st.write(f"Valor total do Abastecimento: R$ {valor_total_abastecimento:.2f}")

elif pagina_selecionada == 'Cadastro Despesas':
    st.title('Dados das Despesas: ')
    
    # Variáveis dos dados dos abastecimentos:
    chapa = st.number_input("Valor do Chapa: ")
    caixinha = st.number_input("Valor da Caixinha:")
    conferente = st.number_input("Valor do Conferênte: ")
    borracheiro = st.number_input("Valor do Borracheiro: ")
    mecanico = st.number_input("Valor do Mecânico: ")
    demais_despesas = st.number_input("Valor das Demais Despesas: ")
    enviar_dados_despesas = st.button("Enviar")
    
    
    # Cálculos Despesas:
    total_despesas = chapa + caixinha + conferente  + borracheiro + mecanico + demais_despesas

    with st.container():
         st.write(f'A despesa total é:  R$ {total_despesas:.2f}')    
         
         
         
elif pagina_selecionada == 'Fechamento do Acerto':
    st.title('Fechamento do Acerto de Contas: ')