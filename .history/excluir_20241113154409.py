import streamlit as st
import requests

# Configuração básica da página
st.title("Confirmação e Exclusão de Dados")
st.write("Preencha os campos abaixo para confirmar seus dados e solicitar a exclusão no banco de dados.")

# Campos de entrada
email = st.text_input("E-mail")
data_nascimento = st.text_input("Data de Nascimento (dd/mm/aaaa)")
nome_completo = st.text_input("Nome Completo")

# # Botão para confirmação e exclusão
# if st.button("Confirmar e Excluir Dados"):
#     # Verificação básica de preenchimento
#     if not email or not data_nascimento or not nome_completo:
#         st.error("Por favor, preencha todos os campos.")
#     else:
#         # Dados do corpo da requisição
#         payload = {
#             "email": email,
#             "data_nascimento": data_nascimento,
#             "nome_completo": nome_completo
#         }

#         # Substitua pela URL do seu endpoint no Parse do Back4App
#         url = "https://YOUR_PARSE_API_URL/classes/YourClassName"

#         # Cabeçalhos para autenticação do Parse (substitua com suas chaves)
#         headers = {
#             "X-Parse-Application-Id": "YOUR_APP_ID",
#             "X-Parse-REST-API-Key": "YOUR_REST_API_KEY",
#             "Content-Type": "application/json"
#         }

#         # Envio da requisição
#         response = requests.post(url, json=payload, headers=headers)

#         # Análise da resposta
#         if response.status_code == 200:
#             st.success("Os dados foram confirmados e excluídos com sucesso.")
#         else:
#             st.error(f"Falha ao confirmar e excluir os dados. Código de status: {response.status_code}")
