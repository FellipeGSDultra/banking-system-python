# 🏦 Banking System

Um sistema bancário robusto e modular desenvolvido em Python que simula operações bancárias reais com arquitetura profissional seguindo padrões de mercado, focado na aplicação de boas práticas de desenvolvimento, princípios SOLID e design patterns.

---

## 📋 Visão Geral

O **Banking System** é um projeto educacional que demonstra a evolução de um código monolítico para uma arquitetura modular bem estruturada. O sistema simula operações bancárias como cadastro de clientes, abertura de contas, depósitos, saques e consulta de extratos com validações de entrada e integridade de dados.

Este projeto exemplifica boas práticas de desenvolvimento profissional, incluindo padrões de projeto, princípios SOLID e separação de responsabilidades.

---

## 🛠️ Tecnologias

- **Linguagem**: Python 3.8+
- **Paradigma**: Programação Orientada a Objetos (POO)
- **Padrões Implementados**:
  - Repository Pattern
  - Model-View-Controller (MVC)
  - Encapsulamento com Properties
  - Herança e Polimorfismo

---

## 🏗️ Evolução Técnica

### Modularização e Responsabilidade Única
O sistema foi refatorado de um código monobloco para uma arquitetura modular, onde cada arquivo e pasta possui uma responsabilidade específica. Isso melhora a manutenibilidade, testabilidade e reutilização de código.

### Arquitetura MVC
A separação entre:
- **Models**: Lógica de negócio (Client, Account, Transaction)
- **Views**: Interface com o usuário
- **Controller** (Main): Orquestração do fluxo da aplicação

### Padrões de Projeto Aplicados

#### 🔹 Encapsulamento com Properties
Utilização de atributos privados (`_balance`, `_limit`) com decoradores `@property` e `@setter` para proteger dados sensíveis como saldo e limites de contas, garantindo validações em todas as alterações.

#### 🔹 Herança e Polimorfismo
- **Classe Base `Account`**: Define a estrutura e métodos gerais de contas
- **Classe Especializada `CheckingAccount`**: Sobrescreve comportamentos específicos como regras de saque (limite de $500 e 3 saques diários)

#### 🔹 Validação de Entrada
Implementação da classe `InputValidator` para capturar e tratar erros de entrada do usuário, prevenindo exceções não tratadas e melhorando a experiência.

#### 🔹 Desacoplamento da Camada de Apresentação
Remoção de todos os `print()` das classes de lógica. A classe `HistoryTransaction` apenas formata dados, enquanto `views.py` é responsável pela exibição na interface.

---

## 📚 Estrutura de Pastas

```
Banking_System/
├── README.md                      # Este arquivo
├── main.py                        # Ponto de entrada da aplicação
├── models/
│   ├── __init__.py               # Inicialização do pacote
│   ├── account.py                # Classes Account e CheckingAccount
│   ├── client.py                 # Classe Client (dados de clientes)
│   ├── transaction.py            # Classe Transaction (registro de operações)
│   ├── history_transactions.py   # Classe HistoryTransaction (formatação de extratos)
│   ├── input_validator.py        # Classe InputValidator (validação de entrada)
│   ├── repositories.py           # Repositórios para persistência de dados
│   └── views.py                  # Camada de apresentação (interface com usuário)
```

### Descrição dos Arquivos

| Arquivo | Responsabilidade |
|---------|-------------------|
| `main.py` | Orquestração do fluxo da aplicação e interação com usuário |
| `models/account.py` | Lógica de contas bancárias e operações |
| `models/client.py` | Representação de clientes |
| `models/transaction.py` | Registro de transações |
| `models/history_transactions.py` | Formatação e apresentação de históricos |
| `models/input_validator.py` | Validação e tratamento de entradas |
| `models/repositories.py` | Acesso e persistência de dados |
| `models/views.py` | Interface e exibição de informações |

---

## ✨ Funcionalidades Atuais

✅ **Cadastro de Clientes**
- Criação de perfis de usuário com informações pessoais

✅ **Abertura de Contas Correntes**
- Criação de contas correntes vinculadas a clientes
- Limite de saque: $500 USD
- Limite de transações diárias: 3 saques

✅ **Sistema de Depósitos**
- Depósitos ilimitados com validação de valor
- Atualização automática de saldo

✅ **Sistema de Saques**
- Validação de saldo disponível
- Respeitamento de limite de transações diárias
- Proteção contra saques superiores ao limite configurado

✅ **Extrato Detalhado**
- Visualização formatada do histórico de transações
- Informações completas de cada operação

✅ **Validação Robusta**
- Tratamento de entradas inválidas do usuário
- Prevenção de estados inconsistentes

---

## 📖 Como Executar

### Requisitos
- Python 3.8 ou superior
- Nenhuma dependência externa (usa apenas biblioteca padrão)

### Instalação e Execução

1. **Clone ou baixe o projeto:**
   ```bash
   git clone <seu-repositorio>
   cd Banking_System
   ```

2. **Execute o aplicativo:**
   ```bash
   python main.py
   ```

3. **Interaja com o menu:**
   - Siga as instruções exibidas no console
   - Digite as opções solicitadas conforme indicado

### Exemplo de Uso

```
=== BANKING SYSTEM ===
1. Create Client
2. Open Checking Account
3. Deposit
4. Withdraw
5. Check Statement
6. Exit

Choose an option: 1
Enter client name: João Silva
Client created successfully!
```

---

## 🌍 Inglês no Código: Crescimento Profissional

### Rationale

Todo o código-fonte (variáveis, nomes de métodos, classes e mensagens de retorno técnico) foi desenvolvido em **inglês técnico profissional**, enquanto a documentação permanece em português para facilitar a explicação local.

Esta abordagem deliberada oferece os seguintes benefícios:

#### 🎯 Contexto Global
Ao usar inglês no código, o projeto fica preparado para:
- Colaboração internacional em equipes
- Contribuições de desenvolvedores de diferentes países
- Distribuição e reuso em comunidades globais

#### 📚 Padrão de Mercado
Grandes empresas tech (Google, Microsoft, Meta, etc.) padronizam código em inglês. Este projeto replica esse padrão para simular um ambiente profissional real.

#### 🚀 Desenvolvimento de Carreira
Profissionais que dominam codificação em inglês técnico:
- Têm acesso a oportunidades em empresas internacionais
- Conseguem trabalhar em projetos open-source de renome
- Desenvolvem vocabulário técnico em inglês naturalmente

#### 📝 Documentação Bilíngue
- **Código**: Inglês técnico
- **README e documentação**: Português para acessibilidade local

Esta abordagem oferece o melhor dos dois mundos: profissionalismo técnico global com acessibilidade local.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Este é um projeto educacional destinado a demonstrar boas práticas de desenvolvimento.

Para sugerir melhorias:
1. Identifique a área de melhoria
2. Documente a mudança proposta
3. Respeite os padrões arquiteturais estabelecidos

---

## 📝 Licença

Este projeto é disponibilizado para fins educacionais.

---

## 👨‍💻 Autor

Desenvolvido como demonstração de arquitetura profissional e padrões de projeto em Python.

**Data**: Abril de 2026

---

**⭐ Se este projeto foi útil, considere deixar uma estrela!**