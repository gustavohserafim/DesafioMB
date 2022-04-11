
## Quero Ser MB - Teste Backend 
## Variações de Médias Móveis Simples
## Sobre 
Esta aplicação entrega os valores de média móvel simples de 20, 50 e 200 dias,
das moedas Bitcoin e Ethereum que são listadas no Mercado Bitcoin.

## Pré requisitos
Docker 20.10.14+ <br>
docker-compose 1.29.2+


## Instalação
Com o docker e docker-compose devidamente instalados basta clonar o repositório e executar o comando
 ```docker-compose up desafiomb```. 
Serão gerados 2 containers docker, contendo a aplicação e o banco de dados populado.




## Rotas
| Rota        | Metodo |
|-------------|--------|
| /{pair}/mms | GET    |

## Parametros
| Parametro | Tipo                  | Default      | Descrição                                                                                  |                                                                
|-----------|-----------------------|--------------|--------------------------------------------------------------------------------------------|
| pair      | GET(url) - string     | -            | Par de moedas da consulta, deve ser ```BRLBTC``` ou ```BRLETH```.                          |
| from      | Unix timestap - float | -            | Periodo de inicio da consulta, não pode ser maior que 365 dias da data atual.              |
| to        | Unix timestap - float | Dia anterior | Periodo de fim da consulta.                                                                |
| range     | int                   | -            | Quantidade de dias de média movel, deve ser um dos valores:```20```, ```50``` ou ```200``` |

## Respostas
| Status code | Descrição                            | body                                                                                    |
|-------------|--------------------------------------|-----------------------------------------------------------------------------------------|
 | 200         | Ok                                   | ```[{ timestamp: int, mms: float}] ```                                                  |
| 400         | Um ou mais parametros são invalidos. | ```{"message": "error message", "errors": {"wrong_param_name": "error description"} ``` |

## População do BD
Script é executado automaticamente ao executar a aplicação. Localizado em scripts/populate.py

## Job de atualização
As incrementações diárias são feitas através de um job que é executado todos os dias pelo crontab. Localizado em scripts/update_job.py

## Testes
Rodar o test/requests_tests.py, se nenhum exception for levantada os testes rodaram com sucesso.