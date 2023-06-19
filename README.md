<h1 align='center'>  HEALTH INSURANCE CROSS SELL PREDICTION <br> [projeto em andamento] </h1>

<div align=center>

![Healthin](images/healthin.png 'aaa')
</div>

<p align="justify"><i>Esse é um problema de negócio fictício, porém a empresa e os dados são reais assim como a solução do problema também é feita seguindo os passos que um projeto real seguiria.</i></p>

<p align="justify"><i>Este README apresenta um apanhado dos métodos utilizados e dos principais resultados obtidos. Você pode obter mais detalhes visitando o 
<a href="">Jupyter Notebook</a> do projeto.</i></p>

# 1.0 - **Problema de negócio**

## 1.1 - **Descrição do problema**

<p align="justify"> Uma apólice de seguro é um acordo pelo qual uma empresa se compromete a fornecer uma garantia de compensação por perdas, danos, doenças ou morte especificados em troca do pagamento de um prêmio especificado. Um prêmio é uma quantia em dinheiro que o cliente precisa pagar regularmente a uma companhia de seguros por essa garantia. </p>

<p align="justify"> Uma companhia de seguros que fornece diferentes tipos de seguros a seus clientes precisa construir de um modelo para prever se os segurados (clientes) que adquiriram seguro de saúde no ano anterior também estariam interessados no seguro de veículo fornecido pela empresa. </p>

<p align="justify"> Construir um modelo para prever se um cliente estaria interessado em Seguro de Veículo é extremamente útil para a empresa, pois ela pode planejar sua estratégia de comunicação para alcançar esses clientes e otimizar seu modelo de negócios e receita.</p>


## 1.2 - **Objetivos**

<p align="justify">Como cientista de dados foi nos dado a tarefa de prever os potenciais clientes com base nos dados disponíveis da empresa sobre seus clientes. Além disso, para que o time de Marketing tenha fácil acesso à esses clientes, foi solicitado que esses resultados possam ser consultados em uma tabela no Google Sheets .</p>

## 1.3 - **Visão geral dos dados**

<p align="justify"> Os dados foram obtidos através da plataforma <a href="https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-predictions">Kaggle</a>. Neles temos informações gerais sobre os clientes que já adquiriram o seguro de saúde oferecido pela seguradora. O dataset original contém as seguintes informações:</p>

<details><summary><strong> Descrição dos dados disponibilizados</strong> </summary>

| Variável            | Descrição                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------|
| id                  | ID único do cliente                                                                                 |
| Gender              | Gênero do cliente                                                                                   |
| Age                 | Idade do cliente                                                                                    |
| Driving_License     | 0: Cliente não possui CNH, 1: Cliente já possui CNH                                                 |
| Region_Code         | Código único para a região do cliente                                                               |
| Previously_Insured  | 1: Cliente já possui Seguro de Veículo, 0: Cliente não possui Seguro de Veículo                     |
| Vehicle_Age         | Idade do Veículo                                                                                    |
| Vehicle_Damage      | 1: Cliente teve seu veículo danificado no passado, 0: Cliente não teve seu veículo danificado      |
| Annual_Premium      | O valor que o cliente precisa pagar como prêmio anual                                              |
| Policy_Sales_Channel| Código anonimizado para o canal de abordagem ao cliente                                             |
| Vintage             | Número de dias que o cliente está associado à empresa                                              |
| Response            | 1: Cliente está interessado, 0: Cliente não está interessado                                       |

</details>
