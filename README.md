
1.0 Business background 

O varejista on-line considerado nesse case está sediado no Reino Unido e foi criado em 1981 vendendo principalmente presentes exclusivos para todas as ocasiões. Por questões de segurança, a identidade da empresa não foi revelada durante o compartilhamento de seus dados transacionais no repositório da UCI. 

Durante anos no passado, o comerciante dependia fortemente de catálogos de mala direta, e os pedidos eram atendidos por telefone. Em 2010, a empresa lançou seu próprio site e mudou completamente para a Web. Desde então, tem mantido um ritmo constante e um número saudável de clientes de todas as partes do Reino Unido e da Europa, e acumulou uma enorme quantidade de dados sobre os clientes. Muitos clientes da empresa são atacadistas. Além disso, a companhia também usa Amazon.co.uk para comercializar e vender seus produtos.

O conjunto de dados de transações do cliente mantido pelo comerciante tem 9 variáveis, conforme apresentado na tabela abaixo e contém todas as transações ocorridas entre 12/01/2009 e 12/09/2011. É importante dizer, que esse rol de dados está disponível no repositório da UCI na categoria business com o nome de Online Retail II. Disponível em <https://archive.ics.uci.edu/dataset/352/online+retail>

Tabela de variáveis
![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/b9a636ac-8ac8-4fa2-ba88-8cbf6017681f)

1.1 O Problema de negócio 

Ao analisar os dados transacionais fornecidos pela empresa, identifiquei que existem registros das transações canceladas, sendo assim, decidi fazer um estudo detalhado das faturas canceladas. 

Em uma análise exploratória identiquei que entre 12/01/2009 e 12/09/2011 a empresa teve 18.345 faturas canceladas, o que representa aproximadante 2,23% do total de faturas. E uma perda de £ 757.642,99, o que representa aproximadante 4,50% do faturamento total.

Apesar das métricas de cancelamento não serem tão expressivas, quando se olha essas mesmas métricas em um cenário segmentado por País, observa-se um problema local no Reino Unido, a sede da empresa. 


![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/bc00a23c-388c-4ce0-990f-397fe1126288)

Aproximadante 88,30% do valor de venda cancelado pertence ao Reino Unido. 

![image](https://github.com/letandrade/case_cancelamento_vendas/assets/86376728/e5189949-4c81-40c6-b88c-e5e3ed581e3a)

Aproximadante 74,89% da quantidade de produtos cancelados pertencem ao Reino Unido. 

Sendo assim, resolvi seguir a análise de cancelamentos com foco apenas no Reino Unido e obtive os resultados abaixo:

Total de transações canceladas: 6.730
Proporção de transações canceladas: 16.75%
Qtd de itens cancelados: 360.599
Proporção de itens cancelados: 4.32%
Valor de venda cancelado: £ 669.007,71
Proporção do valor de venda de cancelado: 4.79%
Ticket médio em valor por transação cancelada: £ 99.41
Ticket médio em qtd por transação cancelada: 53.58083209509658
Taket time em valor por transação cancelada: 0.010059674798067724
Taket time em qtd por transação cancelada: 0.018663390636135986
Valor médio de cancelamentos para um cliente por transação: £ 297.87
Quantidade média de cancelamentos para um cliente: 2.99
Quantidade média de itens cancelados para um cliente: 160.55
Quantidade média de itens distintos cancelados para um cliente: 5.84

Além disso, foi verificado que a sexta-feira e o horário da manhã são os mais propensos a cancelamentos de faturas. 

Com o objetivo de reduzir os cancelamentos ocorridos no Reino Unido, desenvolvi um modelo de classificação que identifica se uma fatura é propensa ao cancelamento ou não. 

Esse modelo representa a oportunidade de segmentar as faturas em possíveis de ser canceladas ou não, dessa forma, os calaboradores poderiam focar no acompanhamento das faturas que possuem perfil de cancelamento após a efetuação da compra. Uma boa estratégia seria fazer o acompanhamento do processo de compra junto ao clientes que possuem faturas com potencial de ser canceladas. 


