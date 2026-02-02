# SOC Home Lab – Log Analyzer (v2) 🔐

Projeto prático de **Segurança da Informação / Blue Team**, focado na análise de logs Linux (`auth.log`) para identificar eventos de autenticação via SSH.

## Objetivo
Simular atividades de um **SOC (Security Operations Center)** analisando logs e destacando padrões de falhas e acessos legítimos.

## Funcionalidades
- Detecta tentativas de login malsucedidas (`Failed password`)
- Detecta acessos bem-sucedidos (`Accepted password`)
- Conta IPs com maior número de falhas (Top 5)
- Gera relatório no terminal

## Tecnologias
- Python
- Linux (logs)
- Análise de Logs
- Segurança da Informação (Blue Team)

## Como executar
```bash
python analyzer.py
