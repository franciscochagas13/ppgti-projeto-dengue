### Dump MongoDB
- **dengue_db.agz:** Arquivo de dump do MongoDB que contém o banco de dados `dengue_db` com dados dos casos de dengue.

# Tutorial: Como Importar um Dump do MongoDB

## Importar o Dump em um Container Docker

### Passo 1: Copiar o Dump para o Container

1. **Identifique o nome ou ID do container MongoDB**:
    ```sh
    docker ps
    ```
2. **Copie o dump para o container**:
    ```sh
    docker cp /path/to/dump <container_name_or_id>:/data/db/dump
    ```

### Passo 2: Executar o `mongorestore` dentro do Container

1. **Acesse o container**:
    ```sh
    docker exec -it <container_name_or_id> /bin/bash
    ```
2. **Execute o comando `mongorestore`**:
    ```sh
    mongorestore --db dengue_db /data/db/dump/dengue_db
    ```

**Exemplo Completo**:
```sh
docker cp /path/to/dump mongo_container:/data/db/dump
docker exec -it mongo_container /bin/bash
mongorestore --db dengue_db /data/db/dump/dengue_db
```

## Importar o Dump em uma Instância MongoDB Fora do Docker

### Passo 1: Localize o Dump

Certifique-se de que o dump do banco de dados está acessível no seu sistema, por exemplo, `/path/to/dump/dengue_db`.

### Passo 2: Usar o `mongorestore` para Importar o Dump

Execute o comando `mongorestore`:
```sh
mongorestore --db dengue_db /path/to/dump/dengue_db
```
### Dica: Conexão com Autenticação

Se a sua instância MongoDB requer autenticação, use:

```sh
mongorestore --db dengue_db --username <username> --password <password> --authenticationDatabase admin /path/to/dump/dengue_db
```

### Conexão a um Servidor MongoDB Remoto
Se estiver conectando a um servidor MongoDB remoto, use:

```sh

mongorestore --uri="mongodb://<username>:<password>@<host>:<port>/dengue_db" /path/to/dump/dengue_db
```
