# Flask API com MongoDB - Estrutura Modular

API REST simples usando Flask e MongoDB para cadastro e consulta de usuários.

## Estrutura

- `app.py` → inicializa a aplicação e registra blueprints
- `api/` → módulo principal com config, database e rotas

## Instalação

1. Clone o repositório:
```bash
git clone <repo-url>
cd flask_mongo_api
```

2. Crie um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o MongoDB:
- Local: `mongodb://localhost:27017/meubanco`
- Ou defina a variável de ambiente `MONGO_URI`.

5. Rode a API:
```bash
python app.py
```

## Endpoints

### Criar usuário
```
POST /usuarios/
{
    "nome": "Pedro",
    "email": "pedro@email.com",
    "idade": 20
}
```

### Listar todos os usuários
```
GET /usuarios/
```

### Consultar usuário por ID
```
GET /usuarios/<id>
```