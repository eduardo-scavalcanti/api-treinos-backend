# 🏋️‍♂️ GymTrack API — Gestão de Performance

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092e20.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> API RESTful para controle de rotinas de musculação, focada em segurança JWT, escalabilidade e documentação automatizada.

---

## 🎯 Sobre o Projeto

API robusta desenvolvida para gerenciar treinos e sessões de exercícios. O projeto aplica conceitos avançados de engenharia de software, como autenticação *stateless*, persistência em banco de dados relacional e documentação OpenAPI 3.0.

---

## ✨ Funcionalidades

- **Autenticação JWT (JSON Web Token):** Fluxo de login seguro com tokens de acesso e renovação (*refresh tokens*).
- **Gestão de Templates:** CRUD completo para rotinas de treino personalizadas.
- **Registro de Sessões:** Histórico de execuções vinculado diretamente ao usuário autenticado.
- **Documentação Interativa:** Interface Swagger para visualização e teste imediato de endpoints.

---

## 🧠 Embasamento Técnico

### 🗄️ Modelagem de Dados (ERD)
O banco de dados foi projetado para garantir a integridade referencial. Abaixo, a representação das entidades de Usuários, Templates e Sessões desenvolvida no **dbdiagram.io**.


<img width="908" height="763" alt="Image" src="https://github.com/user-attachments/assets/1143258e-9fc5-4a32-9f35-4fa3d8a74965"/>

### 🔐 Fluxo de Autenticação
A segurança é baseada no padrão Bearer Token, garantindo que o servidor não precise armazenar sessões, facilitando a escalabilidade horizontal.

1.  **Request:** Usuário envia credenciais.
2.  **Validation:** Backend valida e retorna um par de chaves JWT.
3.  **Authorized Access:** Usuário anexa o `Access Token` no header de cada requisição.

---

## 🏗️ Arquitetura e Tech Stack

| Camada | Tecnologia | Papel no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.14 | Core da aplicação. |
| **Framework** | Django 6.0 / DRF | Motor de API e ORM. |
| **Auth** | SimpleJWT | Gestão de tokens de segurança. |
| **Banco** | PostgreSQL | Persistência de dados em produção. |
| **Docs** | drf-spectacular | Geração de documentação OpenAPI. |
| **Infra** | Render / Gunicorn | Hospedagem e servidor de produção. |

---

## 📂 Estrutura de Pastas

```
api-treinos-backend/
├── core/               # Configurações do projeto e variáveis de ambiente
├── treinos/            # App principal (Models, Views, Serializers)
├── static/             # Arquivos estáticos coletados pelo WhiteNoise
├── manage.py           # CLI do Django
├── requirements.txt    # Lista de dependências de produção
└── .env                # Variáveis sensíveis (não commitado)
```

---

## 🚀 Como Rodar Localmente

### 1. Clonar e Instalar
```
git clone [https://github.com/eduardo-scavalcanti/api-treinos-backend](https://github.com/eduardo-scavalcanti/api-treinos-backend)
cd api-treinos-backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurar Ambiente 
Crie um .env com sua SECRET_KEY.
```env
SECRET_KEY=sua_chave_aqui
DEBUG=True
```

### 3. Rodar
```
python manage.py migrate
python manage.py runserver
```
---

## 📊 Deploy e Documentação

A API está publicada e pode ser testada através do Swagger:

🔗 **[Acessar Documentação da API (Swagger)](https://api-treinos-backend.onrender.com/api/docs/)**

<img width="1898" height="907" alt="Image" src="https://github.com/user-attachments/assets/1d2e1d33-891c-4107-928c-2653b60f92d8" />

---
