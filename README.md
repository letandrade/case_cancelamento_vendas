# Modelo de Classificação de Faturas Canceladas (Python + FAST API + Streamlit + Render)

### 1.0 Business background 

O varejista on-line considerado nesse case está sediado no Reino Unido e foi criado em 1981 vendendo principalmente presentes exclusivos para todas as ocasiões. Por questões de segurança, a identidade da empresa não foi revelada durante o compartilhamento de seus dados transacionais no repositório da UCI. 

Durante anos no passado, o comerciante dependia fortemente de catálogos de mala direta, e os pedidos eram atendidos por telefone. Em 2010, a empresa lançou seu próprio site e mudou completamente para a Web. Desde então, tem mantido um ritmo constante e um número saudável de clientes de todas as partes do Reino Unido e da Europa, e acumulou uma enorme quantidade de dados sobre os clientes. Muitos clientes da empresa são atacadistas. Além disso, a companhia também usa Amazon.co.uk para comercializar e vender seus produtos.

O conjunto de dados de transações do cliente mantido pelo comerciante tem 9 variáveis, conforme apresentado na tabela abaixo e contém todas as transações ocorridas entre 12/01/2009 e 12/09/2011. É importante dizer, que esse rol de dados está disponível no repositório da UCI na categoria business com o nome de Online Retail II. Disponível em <https://archive.ics.uci.edu/dataset/352/online+retail>

Tabela de variáveis
![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/b9a636ac-8ac8-4fa2-ba88-8cbf6017681f)

### 1.1 O Problema de negócio 

Ao analisar os dados transacionais fornecidos pela empresa, identifiquei que existem registros das transações canceladas, sendo assim, decidi fazer um estudo detalhado das faturas canceladas. 

Em uma análise exploratória identiquei que entre 12/01/2009 e 12/09/2011 a empresa teve 18.345 faturas canceladas, o que representa aproximadante 2,23% do total de faturas. E uma perda de £ 757.642,99, o que representa aproximadante 4,50% do faturamento total.

Apesar das métricas de cancelamento não serem tão expressivas, quando se olha essas mesmas métricas em um cenário segmentado por País, observa-se um problema local no Reino Unido, a sede da empresa. 


![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/bc00a23c-388c-4ce0-990f-397fe1126288)

Aproximadante 88,30% do valor de venda cancelado pertence ao Reino Unido. 

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/e5189949-4c81-40c6-b88c-e5e3ed581e3a)

Aproximadante 74,89% da quantidade de produtos cancelados pertencem ao Reino Unido. 

Sendo assim, resolvi seguir a análise de cancelamentos com foco apenas no Reino Unido e obtive os resultados abaixo:

Total de transações canceladas: 6.730
<p>Proporção de transações canceladas: 16.75%
<p>Qtd de itens cancelados: 360.599
<p>Proporção de itens cancelados: 4.32%
<p>Valor de venda cancelado: £ 669.007,71
<p>Proporção do valor de venda de cancelado: 4.79%
<p>Ticket médio em valor por transação cancelada: £ 99.41
<p>Ticket médio em qtd por transação cancelada: 53.58083209509658
<p>Taket time em valor por transação cancelada: 0.010059674798067724
<p>Taket time em qtd por transação cancelada: 0.018663390636135986
<p>Valor médio de cancelamentos para um cliente por transação: £ 297.87
<p>Quantidade média de cancelamentos para um cliente: 2.99
<p>Quantidade média de itens cancelados para um cliente: 160.55
<p>Quantidade média de itens distintos cancelados para um cliente: 5.84

Além disso, foi verificado que a sexta-feira e o horário da manhã são os mais propensos a cancelamentos de faturas. 

### 1.2 Objetivo do projeto

Com o objetivo de reduzir os cancelamentos ocorridos no Reino Unido, desenvolvi um modelo de classificação que identifica se uma fatura é propensa ao cancelamento ou não. 

Esse modelo representa a oportunidade de segmentar as faturas em possíveis de ser canceladas ou não, dessa forma, os calaboradores poderiam focar no acompanhamento das faturas que possuem perfil de cancelamento após a efetuação da compra. Uma boa estratégia seria fazer o acompanhamento do processo de compra junto ao clientes que possuem faturas com potencial de ser canceladas. 

### 2.0 Como usar o projeto 

Para reproduzir o projeto é necessário ter acesso ao seguintes recursos:

➝ Linguagem Python com Jupyter notebook.
<p>➝ Login no streamlit. Disponível em: <https://streamlit.io>
<p>➝ Login no render. Disponível em: <https://render.com>
  
### 3.0 Desenvolvimento e resultados 

Para construção do modelo de classificação foi usado o algoritmo CatBoostClassifier que é um algoritmo de aprendizagem supervisionada projetado especificamente para lidar com conjuntos de dados que possuem características categóricas (ou seja, variáveis qualitativas) e é particularmente eficaz em problemas de classificação. O "Cat" em CatBoost refere-se a "categorical" (categórico), e o algoritmo é otimizado para lidar com essas variáveis de forma eficiente. Além disso, o algoritmo usa o processo de boosting que geralmente envolve a construção sequencial de vários classificadores fracos, onde cada novo classificador é treinado para corrigir os erros cometidos pelos classificadores anteriores. Em cada iteração, os exemplos de treinamento que foram classificados incorretamente pelos classificadores anteriores recebem um peso maior, para que o próximo classificador se concentre mais nesses exemplos difíceis. Esse processo é repetido até que um critério de parada seja atendido, como um número máximo de iterações ou quando não há mais ganho significativo.

Para treinar o modelo, o conjunto de dados inicial passou por um pré-processamento com o intuito de obter as variáveis relevantes para tarefa de classificação. Dessa forma, foi criada uma base a nível de fatura com as varáveis abaixo:

Para treinar o modelo foi feita uma separação do conjunto de dados selecionado utilizando o pacote train_test_split. A segmentação é realizada de forma aleatória, isso significa que os dados são divididos em conjuntos de treinamento e teste de maneira aleatória, garantindo que não haja viés na seleção dos exemplos para cada conjunto.
Além disso, foi considerada a proporção de 70%/30% para divisão, respectivamente, em conjuntos de treinamento e teste.

### 4.0 Deploy do modelo

### 5.0 Conclusão
