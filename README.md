![teste](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/b4518aaa-0631-4ca4-8292-3d1063e345f0)

<h1 align="center">Modelo de propensão a faturas canceladas <br /> (Python + FAST API + Render + Streamlit)</h1>

### Sumário

1. [Business Background](#1.0-business-background)
   - 1.1 [O Problema de Negócio](#11-o-problema-de-negócio)
   - 1.2 [Objetivo do Projeto](#12-objetivo-do-projeto)
2. [Como Usar o Projeto](#20-como-usar-o-projeto)
3. [Desenvolvimento e Resultados](#30-desenvolvimento-e-resultados)
4. [Deploy do Modelo](#40-deploy-do-modelo)
5. [Conclusão](#50-conclusão)
  
### 1.0 Business background 

O varejista on-line considerado nesse case está sediado no Reino Unido e foi criado em 1981 vendendo principalmente presentes exclusivos para todas as ocasiões. Por questões de segurança, a identidade da empresa não foi revelada durante o compartilhamento de seus dados transacionais no repositório da UCI. 

Durante anos no passado, o comerciante dependia fortemente de catálogos de mala direta, e os pedidos eram atendidos por telefone. Em 2010, a empresa lançou seu próprio site e mudou completamente para a Web. Desde então, tem mantido um ritmo constante e um número saudável de clientes de todas as partes do Reino Unido e da Europa, e acumulou uma enorme quantidade de dados sobre os clientes. Muitos clientes da empresa são atacadistas. Além disso, a companhia também usa Amazon.co.uk para comercializar e vender seus produtos.

O conjunto de dados de transações do cliente mantido pelo comerciante tem 9 variáveis, conforme apresentado na tabela abaixo e contém todas as transações ocorridas entre 12/01/2009 e 12/09/2011. É importante dizer, que esse rol de dados está disponível no repositório da UCI na categoria business com o nome de Online Retail II. Disponível em <https://archive.ics.uci.edu/dataset/352/online+retail>

<div align="center"> <strong>Tabela de variáveis</strong> </div>

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/b9a636ac-8ac8-4fa2-ba88-8cbf6017681f)

### 1.1 O Problema de negócio 

Ao analisar os dados transacionais fornecidos pela empresa, identifiquei que existem registros das transações canceladas, sendo assim, decidi fazer um estudo detalhado das faturas canceladas. 

Em uma análise exploratória identiquei que entre 12/01/2009 e 12/09/2011 a empresa teve 18.345 faturas canceladas, o que representa aproximadante 2,23% do total de faturas. E uma perda de £ 757.642,99, o que representa aproximadante 4,50% do faturamento total.

Embora as métricas de cancelamento não sejam notavelmente altas em geral, uma análise segmentada por país revela um problema localizado no Reino Unido, onde a sede da empresa está situada.

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/2d1943a2-cc64-423b-af74-fd45f4ab3d8b)

Aproximadante 88,30% do valor de venda cancelado pertence ao Reino Unido. 

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/d35670c2-dc7e-433a-984f-e67da917982d)

Aproximadante 74,89% da quantidade de produtos cancelados pertencem ao Reino Unido. 

Portanto, optei por concentrar a análise de cancelamentos exclusivamente no Reino Unido e os resultados obtidos foram os seguintes:

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

Com o intuito de mitigar os cancelamentos de transações no Reino Unido, elaborei um modelo de propensão a faturas canceladas. Esse modelo, uma vez desenvolvido, é caracterizado como um modelo de aprendizado supervisionado. Sua finalidade é realizar uma tarefa de classificação, determinando se uma determinada fatura possui probabilidade de ser cancelada ou não.

Este modelo oferece uma oportunidade para segmentar as faturas em duas categorias distintas: aquelas com potencial de cancelamento e aquelas sem. Isso possibilita que os colaboradores concentrem seus esforços no acompanhamento das faturas que apresentam um perfil de cancelamento após a compra ter sido efetuada. Uma estratégia eficaz seria realizar um acompanhamento mais próximo do processo de compra com os clientes que têm faturas com potencial de cancelamento, visando a redução dessas ocorrências.

O modelo será integrado em uma aplicação web interativa desenvolvida utilizando a plataforma Streamlit. O propósito é tornar o modelo mais envolvente e acessível para os usuários finais, como vendedores ou outros stakeholders interessados em identificar as faturas com maior probabilidade de serem canceladas ou mantidas.

A aplicação web foi construída utilizando uma API desenvolvida com FastAPI e posteriormente hospedada no servidor Render. Para alimentar a aplicação web hospedada no Streamlit, a API pública foi integrada, possibilitando acesso e interação com os dados.

### 2.0 Como usar o projeto 

Para reproduzir o projeto é necessário ter acesso ao seguintes recursos:

➝ Linguagem Python. Neste caso, a análise foi desenvolvida no ambiente de desenvolvimento integrado (IDE) do Jupyter Notebook.

<p>➝ Login no streamlit. Disponível em: https://streamlit.io

Streamlit é uma ferramenta de código aberto em Python usada para criar aplicativos da web interativos para análise de dados e prototipagem rápida. Com o Streamlit, os desenvolvedores podem criar facilmente aplicativos da web com interface de usuário simples e intuitiva, sem a necessidade de conhecimento prévio em desenvolvimento web.

<p>➝ Login no render. Disponível em: https://render.com

Render é uma plataforma de hospedagem de aplicativos e sites que oferece serviços de infraestrutura para implantação e execução de aplicativos da web e API. Ele oferece uma maneira simples e fácil de implantar aplicativos e serviços, sem a necessidade de configuração complexa de servidores ou gerenciamento de infraestrutura.

<p>➝ Todos os 10 arquivos disponíveis neste repositório.
  
### 3.0 Desenvolvimento e resultados 

Para construção do modelo de classificação foi usado o algoritmo CatBoostClassifier que é um algoritmo de aprendizagem supervisionada projetado especificamente para lidar com conjuntos de dados que possuem características categóricas (ou seja, variáveis qualitativas) e é particularmente eficaz em problemas de classificação. O "Cat" em CatBoost refere-se a "categorical" (categórico), e o algoritmo é otimizado para lidar com essas variáveis de forma eficiente. Além disso, o algoritmo usa o processo de boosting que geralmente envolve a construção sequencial de vários classificadores fracos, onde cada novo classificador é treinado para corrigir os erros cometidos pelos classificadores anteriores. Em cada iteração, os exemplos de treinamento que foram classificados incorretamente pelos classificadores anteriores recebem um peso maior, para que o próximo classificador se concentre mais nesses exemplos difíceis. Esse processo é repetido até que um critério de parada seja atendido, como um número máximo de iterações ou quando não há mais ganho significativo.

Para treinar o modelo, o conjunto de dados inicial passou por um pré-processamento com o intuito de obter as variáveis relevantes para tarefa de classificação. Dessa forma, foi criada uma base agrupada a nível de fatura, apenas com os registro do Reino Unido, com as varáveis a seguir:

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/56fbbce7-ebc9-4b74-93e6-ae6899bbcabb)

Para compor o conjunto de dados foram selecionados 13 códigos de estoque referentes aos itens que representam 50% do valor acumulado de vendas canceladas. A presença desses itens na fatura pode ser um indicativo de cancelamento, sendo assim, a base de dados trouxe a quantidade desses itens na fatura. 

Além disso, é importante mencionar que a base não considera os códigos de estoque 'M' e 'AMAZONFEE' pois tratam-se, respectivamente, de cancelamentos realizados de forma manual pela empresa e cancelamentos realizados pela plataforma de venda da Amazon. O objetivo é entender apenas o comportamento dos cancelamentos realizados pelos clientes.

Para treinar o modelo, os dados selecionados foram divididos utilizando o pacote train_test_split. Essa separação foi feita de maneira aleatória para garantir a imparcialidade na seleção dos exemplos para os conjuntos de treinamento e teste. A proporção adotada foi de 70% para o conjunto de treinamento e 30% para o conjunto de teste.

Para reduzir o viés que pode ocorrer quando se utiliza apenas um único conjunto de treinamento e teste, foi utilizada a validação cruzada através da técnica StratifiedKFold. Essa técnica é uma variação do método de validação cruzada k-fold padrão. No método k-fold padrão, o conjunto de dados é dividido em k partes iguais, onde uma parte é usada como conjunto de teste e as restantes são usadas como conjunto de treinamento. Esse processo é repetido k vezes, cada vez utilizando uma parte diferente como conjunto de teste. A diferença principal entre o StratifiedKFold e o k-fold padrão é que o StratifiedKFold mantém a proporção de classes em cada fold. Em problemas de classificação, é importante manter a distribuição das classes em cada conjunto de treinamento e teste para evitar o viés de seleção dos dados. Isso é especialmente importante quando as classes não estão balanceadas no conjunto de dados. O StratifiedKFold garante que cada fold tenha aproximadamente a mesma proporção de cada classe que o conjunto de dados original.

Para otimizar os hiperparâmetros do modelo (iterations, learning_rate e depth) foi utilizado o Grid Search Cross-Validation. A ideia por trás do GridSearchCV é realizar uma busca exaustiva em uma grade de hiperparâmetros especificados, tentando todas as combinações possíveis desses hiperparâmetros. Para cada combinação de hiperparâmetros, o modelo é treinado utilizando validação cruzada (StratifiedKFold) para estimar seu desempenho. No caso específico, o desempenho foi avaliado utilizando a métrica 'roc_auc'. O GridSearchCV foi utilizado principalmente para encontrar a combinação de hiperparâmetros que otimiza o desempenho do modelo de acordo com a métrica escolhida.

Para avaliar a performance do modelo, utilizei as funções classification_report, confusion_matrix e roc_auc_score importadas da biblioteca sklearn.metrics. O foco foi avaliar as principais métricas de classificação: a accuracy, precision, recall e F1 - score. 

Considerando a classe positiva (Sim) como a ocorrência de faturas canceladas e a classe negativa (Não) como faturas não canceladas, obtive os seguintes resultados do modelo:

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/f8ba6ad7-2231-4bda-a66b-e9ccd0e0cb6f)

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/eebce1eb-73ac-4ee3-a7d5-8deffc5dc4aa)

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/05669893-5d4b-4a51-905f-f4d7cc86b888)

Para avaliar o modelo, considerei como métrica principal o recall pois ela busca responder a seguinte pergunta: de todos os exemplos que são positivos, quantos foram classificados corretamente como positivos? Sendo assim, observei que o modelo obteve uma boa performance com o resultado de 84%, isso quer dizer que a cada 100 faturas que são de fato positivas, é esperado que apenas 84 sejam corretamente identificadas como canceladas.

Recall = TP / (TP + FN) = 1686 / (1686 + 329) ≈ 0.84 ou 84%.

As demais métricas (accuracy, precision e f1 - score) também obtiveram uma performance satisfatória acima de 80%, portanto o modelo foi considerado eficaz na tarefa de identificação de faturas canceladas. 

A área sob a curva ROC (AUC — Area Under the Curve ou AUROC — Area Under the Receiver Operating Characteristic curve) também pode ser utilizada como métrica de qualidade de um modelo, dado que quanto mais próxima a curva estiver do canto superior esquerdo, maior será a área sob a curva e melhor será o modelo. Uma vantagem desta métrica é que ela não é sensível ao desbalanço de classes, como ocorre com a acurácia. Por outro lado, a AUROC não é tão facilmente interpretável.

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/e6fc713e-9bfe-4a66-a717-a02ceaa55ce6)

A curva mostrou uma forte inclinação para o canto superior esquerdo, reforçando a confiança de que o modelo está pronto para ser utilizado.

### 4.0 Deploy do modelo

Para fazer o deploy do modelo foram utilizadas três ferramentas: o fast API, o render e o streamlit. 

Todo o processo de deploy foi implementado em 5 etapas:

4.1) A primeira etapa consistiu na serialização do modelo em um arquivo do formato pickle (Sessão 8.0 do Analise_Cancelamento_Vendas.ipybn) e depois o carregamento do novo arquivo (modelo.pkl) no repositório do github;

4.2) A segunda etapa foi a criação do módulo modelo.py onde o objetivo era estruturar 2 funções (carregar_modelo e fazer_predicao): a primeira função para importar o modelo no formato pickle e a segunda função para prever as classes usando o modelo importado.

4.3) A terceira etapa consistiu na criação de uma API com a biblioteca fast API. Consulte o código e a descrição detalhada no módulo fast_api.py.

4.4) A quarta etapa consistiu em tornar a API pública através do seu carregamento no servidor Render. O processo de hospedagem da API no render seguiu o passo a passo disponibilizado no site <https://docs.render.com/deploy-fastapi>. O objetivo foi tornar a API pública para que ela pudesse ser integrada ao streamlit.

4.5) A quinta etapa envolveu a criação de uma aplicação web pública usando o Streamlit. Em resumo, foi desenvolvido um formulário no qual as respostas dos usuários alimentam a API. E a API, cuja função é carregar o modelo e fazer a predição, retorna se a fatura será cancelada ou não. Consulte o código e a descrição detalhada no módulo stream_lit.py. Disponível em: https://casecancelamentovendas-bobjx4pulegbsghod6kx3v.streamlit.app/

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/394c4d73-509f-4747-9721-f1cbdff1a24b)
![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/fe306594-e092-4be9-a280-9a5d621662ef)

Após o preenchimento das informações da fatura, o colaborador terá a previsão de classificação da fatura, ou seja, se ela é uma fatura propensa a ser cancelada ou não.

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/536c255c-43be-44c9-908d-903e5ab25e91)

 Exemplo, caso o formulário seja preenchido com as informações acima, teremos como resposta da API que a fatura será cancelada (Sim).
 
![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/4470bafb-7cd8-4681-a6b5-5d92a75d919a)
### 5.0 Conclusão

A utilização do CatBoostClassifier para construir um modelo de classificação de propensão a faturas canceladas revelou-se uma abordagem eficaz e promissora. Através da análise das características das faturas, o modelo conseguiu aprender padrões e identificar sinais preditivos de cancelamento com precisão.

Os resultados obtidos demonstram a capacidade do CatBoost em lidar com conjuntos de dados desbalanceados e com características categóricas, proporcionando uma classificação robusta e confiável. A interpretação das variáveis mais importantes destacou aspectos significativos relacionados aos padrões de compra, histórico do cliente e outros fatores relevantes para a previsão de cancelamentos de faturas.

Além disso, a flexibilidade do CatBoost em lidar com dados de diferentes tipos e tamanhos possibilitou a construção de um modelo adaptável, capaz de lidar com novos dados e cenários em um ambiente dinâmico.

Em suma, o modelo de classificação baseado em CatBoost apresentou grande potencial para auxiliar na identificação proativa de faturas suscetíveis a cancelamento, permitindo a implementação de estratégias preventivas, além de mitigar possíveis perdas financeiras. Com uma abordagem contínua de refinamento e ajuste, esse modelo pode se tornar uma ferramenta valiosa para melhorar a eficiência operacional e a satisfação do cliente.
