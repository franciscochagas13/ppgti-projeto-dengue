# Backend em Python de Projeto Cadê a dengue

Este é um projeto Python que realiza a coleta de dados da API de Dengue e armazena esses dados em um banco de dados MongoDB.

## Estrutura do Projeto
- app/: Contém o código principal da aplicação.
- config.py: Arquivo de configuração com variáveis de ambiente.
- requirements.txt: Lista de dependências do Python.
- run.py: Script para iniciar o servidor Flask.

## Requisitos

- Python 3.x
- MongoDB

## Instalação e Execução

1. Crie e ative um ambiente virtual::

```bash
python -m venv venv
source venv/bin/activate
No Windows: venv\Scripts\activate
```

2. Crie e ative um ambiente virtual

```bash
pip install -r requirements.txt
```

3. Configure o arquivo config.py com suas variáveis de ambiente

4. Inicie o servidor Flask
```bash
python run.py
```

## Endpoints da API

A aplicação fornece vários endpoints para consultar dados relacionados à dengue. Abaixo estão as descrições detalhadas de cada um:

### `/data` (GET)

Este endpoint é utilizado para coletar e armazenar dados da API externa de dengue.

**Parâmetros da URL:**

- `ew_start` (obrigatório): Número da semana epidemiológica inicial.
- `ew_end` (obrigatório): Número da semana epidemiológica final.
- `ey_start` (obrigatório): Ano inicial.
- `ey_end` (obrigatório): Ano final.

**Exemplo de Requisição:**
```
http://localhost:5000/data?ew_start=1&ew_end=52&ey_start=2024&ey_end=2024
```

**Respostas:**

- `200 OK`: Dados coletados e armazenados com sucesso.
- `400 Bad Request`: Parâmetros obrigatórios ausentes.
- `500 Internal Server Error`: Erro ao coletar ou armazenar os dados.

### `/api/total-cases` (GET)

Este endpoint retorna o total de casos de dengue no intervalo de datas especificado.

**Parâmetros da URL:**

- `start_date` (obrigatório): Data inicial no formato `YYYY-MM-DD`.
- `end_date` (obrigatório): Data final no formato `YYYY-MM-DD`.

**Exemplo de Requisição:**
```
http://localhost:5000/api/total-cases?start_date=2024-01-01&end_date=2024-06-06
```

**Respostas:**

- `200 OK`: Retorna um JSON com o total de casos.
- `400 Bad Request`: Parâmetros obrigatórios ausentes.
- `500 Internal Server Error`: Erro ao processar a requisição.

### `/api/cases-by-city` (GET)

Este endpoint retorna o total de casos de dengue por cidade no intervalo de datas especificado.

**Parâmetros da URL:**

- `start_date` (obrigatório): Data inicial no formato `YYYY-MM-DD`.
- `end_date` (obrigatório): Data final no formato `YYYY-MM-DD`.

**Exemplo de Requisição:**
```
http://localhost:5000/api/cases-by-city?start_date=2024-01-01&end_date=2024-06-06
```

**Respostas:**

- `200 OK`: Retorna um JSON com o total de casos por cidade.
- `400 Bad Request`: Parâmetros obrigatórios ausentes.
- `500 Internal Server Error`: Erro ao processar a requisição.

### `/api/cases-by-month` (GET)

Este endpoint retorna o total de casos de dengue por mês no intervalo de datas especificado.

**Parâmetros da URL:**

- `start_date` (obrigatório): Data inicial no formato `YYYY-MM-DD`.
- `end_date` (obrigatório): Data final no formato `YYYY-MM-DD`.

**Exemplo de Requisição:**
```
http://localhost:5000/api/cases-by-month?start_date=2024-01-01&end_date=2024-06-06
```

**Respostas:**

- `200 OK`: Retorna um JSON com o total de casos por mês.
- `400 Bad Request`: Parâmetros obrigatórios ausentes.
- `500 Internal Server Error`: Erro ao processar a requisição.

### `/api/scatter-temp-humidity-cases` (GET)

Este endpoint retorna dados para um gráfico de dispersão mostrando a relação entre temperatura, umidade e quantidade de casos de dengue.

**Parâmetros da URL:**

- `start_date` (obrigatório): Data inicial no formato `YYYY-MM-DD`.
- `end_date` (obrigatório): Data final no formato `YYYY-MM-DD`.

**Exemplo de Requisição:**
```
http://localhost:5000/api/scatter-temp-humidity-cases?start_date=2024-01-01&end_date=2024-06-06
```
**Respostas:**

- `200 OK`: Retorna um JSON com dados de temperatura, umidade e casos para o gráfico de dispersão.
- `400 Bad Request`: Parâmetros obrigatórios ausentes.
- `500 Internal Server Error`: Erro ao processar a requisição.
