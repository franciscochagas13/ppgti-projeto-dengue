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