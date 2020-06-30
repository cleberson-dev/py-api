# Python REST API

API REST simples escrita em Python com o uso de FastAPI.



## Uso

Assegure que tenha [Python 3](https://www.python.org/downloads/) (>=3.4) instalado em sua máquina, bem como um banco de dados PostgreSQL instalado, [configurado](#config-bd) e em execução.

Para usar a aplicação:

- Faça download do repositório em sua máquina:

  - Baixando e extraindo o ZIP clicando no botão verde ""

  - Ou clonando o repositório usando linha de comando:

    ``````bash
    git clone https://github.com/cleberson-dev/py-api
    ``````

- Instale as dependências necessárias:

  ```bash
  python -m pip install -r requirements.txt # python ou python3
  ```

- Execute a aplicação:

  ``````bash
  uvicorn main:app --reload
  ``````

Servidor estará esperando por requisições no endereço `http://localhost:8000`

> FastAPI gera uma documentação interativa para a API fora da caixa, graças ao Swagger, disponível em `http://localhost:8000/docs`



## Configuração

<h3 id="config-bd"></h3>

### Banco de dados

O banco de dados usado na aplicação é local (`localhost`) e gerenciado por PostgreSQL, portanto é necessário definir algumas variáveis de ambiente antes da execução da aplicação sendo elas:

- `POSTGRES_DB`: Nome do banco de dados
- `POSTGRES_USER`: Nome de usuário usado no banco de dados
- `POSTGRES_PASSWORD`: Senha usada para logar-se no banco.



## Rotas

- GET `/`: Obter um 'Olá mundinho' em JSON: `{ "Olá": "Mundinho" }`
- GET `/posts`:  Adquirir todos as postagens armazenadas no banco de dados no formato: `{ id: number, title: string, content: string }`
- POST `/posts`: Criar uma nova postagem, passando informações da publicação no formato`{ title: string, content: string }`, retornando a postagem com o id na resposta.



## Tecnologias

- [**Python**](https://www.python.org/): Linguagem de programação multi-paradigmas voltado para scripting.
- [**FastAPI**](https://fastapi.tiangolo.com/): Framework para construção de APIs REST de alta performance, com fácil aprendizado e pronta para produção.
- [**PostgreSQL**](http://postgresql.org/): Banco de dados SQL (relacional)
- [**SQLAlchemy**](https://www.sqlalchemy.org/): Biblioteca capaz de mapear relações de bancos de dados relacionais em objetos de programação orientada a objetos (ou seja, ORM).
- [**Pydantic**](https://pydantic-docs.helpmanual.io/): Biblioteca para validação de dados, usando anotações em Python.