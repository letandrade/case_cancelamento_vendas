
#bibliotecas
import streamlit as st
import json
import requests


#Titulo
st.title('Modelo de Previsão de Cancelamento de Fatura')

#Subtítulo
st.write('Preencha as informações da sua fatura.\n\n')

#DiaDaSemana
opcao_1 = st.selectbox('Escolha o dia da semana',('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'))

#FaixaHorária
opcao_2 = st.selectbox('Escolha a faixa horária',('Manhã','Tarde','Noite','Madrugada'))

#Mês
st.write('Escolha o mês')
opcao_3 = int(st.slider('Mês', 0, 12, 1))

#ClienteID
opcao_4 = st.text_input('Digite o ClienteID:')

#Qtd_Itens
opcao_5 = st.number_input('Digite a quantidade de itens:', min_value = 0)

#Vendas
opcao_6 =  st.number_input('Digite o valor de vendas:', min_value = 0.0)

#Média_Preço
opcao_7 = st.number_input('Digite a média de preço:', min_value = 0.0)

#Qtd_Itens_Distintos
opcao_8  = st.number_input('Digite a quantidade de itens distintos:', min_value=0)

#produto1
opcao_9  = st.number_input('Digite a quantidade de itens do produto "20971 - PINK BLUE FELT CRAFT TRINKET BOX":', min_value=0)

#produto2
opcao_10  = st.number_input('Digite a quantidade de itens do produto "21108 - FAIRY CAKE FLANNEL ASSORTED COLOUR":', min_value=0)

#produto3
opcao_11  = st.number_input('Digite a quantidade de itens do produto "22423 - REGENCY CAKESTAND 3 TIER":', min_value=0)

#produto4
opcao_12  = st.number_input('Digite a quantidade de itens do produto "23113 - PANTRY CHOPPING BOARD":', min_value=0)

#produto5
opcao_13  = st.number_input('Digite a quantidade de itens do produto "23166 - MEDIUM CERAMIC TOP STORAGE JAR":', min_value=0)

#produto6
opcao_14  = st.number_input('Digite a quantidade de itens do produto "23843 - PAPER CRAFT,LITTLE BIRDIE":', min_value=0)

#produto7
opcao_15  = st.number_input('Digite a quantidade de itens do produto "47566B - TEA TIME PARTY BUNTING":', min_value=0)

#produto8
opcao_16  = st.number_input('Digite a quantidade de itens do produto "48185 - DOORMAT FAIRY CAKE":', min_value=0)

#produto9
opcao_17 = st.number_input('Digite a quantidade de itens do produto "71477 - COLOUR GLASS. STAR T-LIGHT HOLDER":', min_value=0)

#produto10
opcao_18  = st.number_input('Digite a quantidade de itens do produto "79323P - PINK CHERRY LIGHTS":', min_value=0)

#produto11
opcao_19  = st.number_input('Digite a quantidade de itens do produto "79323W - WHITE CHERRY LIGHTS":', min_value=0)

#produto12
opcao_20  = st.number_input('Digite a quantidade de itens do produto "84078A - SET/4 WHITE RETRO STORAGE CUBES":', min_value=0)
 
#produto13
opcao_21  = st.number_input('Digite a quantidade de itens do produto "85123A - WHITE HANGING HEART T-LIGHT HOLDER":', min_value=0)


entradas = {"DiaSemana": opcao_1, "FaixaHora": opcao_2, "Mes": opcao_3, "ClienteID": opcao_4, "QuantidadeItens": opcao_5,
            "Vendas": opcao_6, "MediaPreco":opcao_7, "QtdItensDistintos": opcao_8, "QtdProduto1": opcao_9,
            "QtdProduto2": opcao_10,"QtdProduto3": opcao_11, "QtdProduto4": opcao_12,"QtdProduto5": opcao_13,
            "QtdProduto6": opcao_14,"QtdProduto7": opcao_15,"QtdProduto8": opcao_16, "QtdProduto9": opcao_17, 
            "QtdProduto10": opcao_18,"QtdProduto11": opcao_19,"QtdProduto12": opcao_20,"QtdProduto13": opcao_21}


if st.button('Gerar previsão'):
    res = requests.post(url='https://case-cancelamento-vendas.onrender.com/fazer-predicao', json = entradas)

    # Verificar se a solicitação foi bem-sucedida (código 200)
    if res.status_code == 200:
        resposta_json = res.json()
        st.subheader(f"Resposta da API foi = {resposta_json}")
    else:
        st.subheader(f"Falha na solicitação. Código de status = {res.status_code}")    
    


