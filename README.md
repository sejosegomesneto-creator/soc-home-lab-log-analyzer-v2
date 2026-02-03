# Laboratório doméstico SOC – Analisador de logs (v2) 🔐

Projeto prático de **Segurança da Informação / Blue Team**, focado na análise de logs Linux (`auth.log`) para identificação de eventos de autenticação SSH.

## Objetivo
Simular atividades de um **SOC (Security Operations Center)** analisando logs e destacando padrões de falhas e acessos legítimos.

## Funcionalidades
- Detecta tentativas de login malsucedidas (`Failed password`)
- Detecta acessos bem-sucedidos (`Accepted password`)
- Conta IPs com maior número de falhas (Top 5)
- Gera relatório diretamente no terminal

## Tecnologias
- Python
- Linux (logs)
- Análise de Logs
- Segurança da Informação (Blue Team)

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/sejosegomesneto-creator/soc-home-lab-log-analyzer-v2.git
