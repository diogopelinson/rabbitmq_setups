# 🐇 RabbitMQ Publisher & Consumer (Python) + venv

Este projeto demonstra como criar um **Publisher** e um **Consumer** simples usando **RabbitMQ** e **Python (pika)**, dentro de um ambiente virtual isolado (**venv**).

---
## Estrutura do Projeto

```
.
├── .venv
├── publisher.py
├── consumer.py
├── consumer_raw.py #Testes Cru sem POO
├── publisher_raw.py #Testes Cru sem POO
└── README.md
```
---

## 📦 Requisitos

- **Python 3.10+**
- **Docker**
- **Biblioteca:** `pika`

---

## 🧩 1. Criar e ativar o ambiente virtual (venv)

### Criar o ambiente:
```bash
python -m venv venv
````

### Ativar:

#### 🪟 No Windows:

```bash
venv\Scripts\activate
```

Exemplo de terminal ativo:

```
(venv) C:\Users\DESKTOP\projeto>
```

#### 🐧 No Linux / WSL / Mac:

```bash
source venv/bin/activate
```

### Desativar:

```bash
deactivate
```

💡 **Dica:** Sempre ative a venv antes de instalar dependências!

---

## ⚙️ 2. Instalar dependências

```bash
pip install pika
```

---

## 🐳 3. Subir o RabbitMQ com Docker

```bash
docker run -d --hostname rmq --name rabbitmq-server \
  -p 8080:15672 -p 5672:5672 rabbitmq:3-management
```

* **Painel Web:** [http://localhost:8080](http://localhost:8080)
* **Usuário/Senha:** `guest / guest`
* **Porta AMQP:** `5672`

---

## 📤 4. Publisher (`publisher.py`)

Envia mensagens para a fila

---

## 📥 5. Consumer (`consumer.py`)

Recebe e imprime mensagens da fila:

---

## ▶️ 6. Executar

1. Inicie o RabbitMQ com Docker
2. Ative sua venv
3. Abra dois terminais:

   * No primeiro:

     ```bash
     python consumer.py
     ```
   * No segundo:

     ```bash
     python publisher.py
     ```

Saída esperada no consumidor:

```
 Ouvindo RabbitMQ na porta 5672...
Mensagem recebida: b'{"Ola": "Mundo"}'
```

---


