# b2bflow-desafio

Este projeto é uma solução em Python que lê contatos salvos no Supabase e envia mensagens personalizadas via Z-API.

## Clonando o Repositório
Para começar, clone o repositório para sua máquina local com o seguinte comando:
```bash
git clone https://github.com/Guilherme-Pelissari/b2bflow-desafio.git
cd b2bflow-desafio
```

## Passos de Setup

### 1. Configuração no Supabase
- Crie uma conta no [Supabase](https://supabase.com).
- Crie um novo projeto e anote o `SUPABASE_URL` e `SUPABASE_KEY` no dashboard.
- No SQL Editor, crie a tabela `contatos` com o seguinte comando:
  ```sql
  CREATE TABLE contatos (
      id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
      nome TEXT NOT NULL,
      telefone TEXT NOT NULL
  );
  ```
- Insira pelo menos 1 a 3 contatos (exemplo):
  ```sql
  INSERT INTO contatos (nome, telefone) VALUES ('Guilherme', '5511999999999');
  ```

### 2. Configuração no Z-API
- Crie uma conta no [Z-API](https://z-api.io).
- Gere uma nova instância e anote o `ZAPI_INSTANCE_ID` e `ZAPI_TOKEN`.
- Configure o `Client-Token` na seção de segurança.

### 3. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:
```
SUPABASE_URL=https://your-supabase-project-url.supabase.co
SUPABASE_KEY=your-supabase-key
ZAPI_INSTANCE_ID=your-zapi-instance-id
ZAPI_TOKEN=your-zapi-token
ZAPI_CLIENT_TOKEN=your-zapi-client-token
```

## Como Rodar
1. Instale as dependências:
   ```bash
   pip install supabase requests python-dotenv
   ```
2. Configure o arquivo `.env` com suas chaves.
3. Execute o script:
   ```bash
   python main.py
   ```
O script buscará até 3 contatos no Supabase e enviará a mensagem "Olá {{nome_contato}}, tudo bem com você?" para cada um.

## Estrutura do Projeto
- `main.py`: Contém a lógica principal de conexão com Supabase e envio via Z-API.
- `.env`: Armazena as chaves sensíveis.

