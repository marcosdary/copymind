# CopyMind

API para gerar respostas de e-mail com IA, com controle de tom, idioma e variações de resposta.

O projeto foi pensado para portfólio com foco em backend aplicado: arquitetura limpa, validação com Pydantic, integração com modelo LLM e rastreio de uso de tokens.

## Visão do projeto

`CopyMind` resolve um problema simples e real: transformar um e-mail recebido em respostas profissionais prontas para uso.

Entrada:
- conteúdo do e-mail original
- objetivo da resposta
- tom desejado (`formal`, `friendly`, `direct`)
- idioma (`pt-BR`, `en-US`)
- número de variações

Saída:
- lista de respostas geradas
- metadados do modelo
- consumo de tokens (`prompt`, `completion`, `total`)

## Objetivos de portfólio

- Mostrar domínio de integração com LLM em API real.
- Demonstrar design de schemas e contratos de entrada/saída.
- Evidenciar preocupação com custo e observabilidade (usage/tokens).
- Criar base para evoluções de produto (histórico, estilos de marca, score de qualidade).

## Stack

- Python
- FastAPI
- Pydantic
- Groq Client
- Llama (modelo configurado via `settings.LLAMA_VERSATILE`)

## Estrutura atual do projeto

```text
app/
  clients/
    groq_client.py
  config/
    settings.py
  routers/
    v1/
      message_router.py
  schemas/
    chat_completion/
      chat_completion_schema.py
      choice_schema.py
      chat_completion_message_schema.py
      completion_usage_schema.py
  services/
    llama_versatile_ai_service.py
  main.py
```

## Serviço de IA já implementado

Arquivo: [llama_versatile_ai_service.py](/home/matheus-silva-oliveira/Área%20de%20trabalho/copymind/app/services/llama_versatile_ai_service.py)

O serviço `LlamaVersatileAIService` já:
- consome `CLIENT_GROQ`
- usa o modelo definido em `settings.LLAMA_VERSATILE`
- envia `messages` para `chat.completions.create`
- mapeia a resposta para schemas internos:
  - `ChatCompletionSchema`
  - `ChoiceSchema`
  - `ChatCompletionMessageSchema`
  - `CompletionUsageSchema`

Esse mapeamento já entrega uma base ótima para o endpoint de geração de e-mails.

## Projeto sugerido: Email Reply Generator API (MVP)

### Endpoint principal

`POST /v1/email/reply`

### Request (exemplo)

```json
{
  "original_email": "Olá, gostaria de remarcar nossa reunião para sexta às 15h.",
  "goal": "Confirmar novo horário e agradecer a flexibilidade.",
  "tone": "formal",
  "language": "pt-BR",
  "n_variants": 3
}
```

### Response (exemplo)

```json
{
  "request_id": "req_123",
  "model": "llama-3.1-70b-versatile",
  "replies": [
    "Olá, sem problemas. Confirmo a reunião para sexta-feira às 15h. Agradeço a flexibilidade.",
    "Perfeito, reunião remarcada para sexta às 15h. Muito obrigado pela disponibilidade.",
    "Confirmado: sexta-feira, 15h. Obrigado pela flexibilidade no ajuste da agenda."
  ],
  "usage": {
    "prompt_tokens": 120,
    "completion_tokens": 85,
    "total_tokens": 205
  }
}
```

## Fluxo interno do MVP

1. Router recebe e valida payload.
2. Service de e-mail monta prompt com regras de tom/idioma.
3. `LlamaVersatileAIService` gera as respostas.
4. Camada de schema normaliza saída.
5. API retorna respostas + usage.

## Regras de geração recomendadas

- Não inventar dados que não estão no e-mail.
- Manter linguagem profissional e clara.
- Respeitar estritamente o tom e idioma solicitados.
- Retornar exatamente `n_variants`.
- Priorizar respostas curtas a médias (uso prático).

## Próxima estrutura sugerida (incremental)

```text
app/
  routers/v1/email_router.py
  schemas/email/
    reply_request_schema.py
    reply_response_schema.py
  services/
    email_reply_service.py
```

## Critérios de qualidade

- Validação de payload com Pydantic.
- Tratamento de erro do provedor de IA.
- Limite para `n_variants` (ex.: 1 a 3).
- Logs básicos de request e tempo de resposta.
- Exposição de `usage` em todas as respostas bem-sucedidas.

## Evoluções (fase 2)

- Campo `company_style` para voz da marca.
- Endpoint para regenerar variações.
- Histórico por `conversation_id`.
- Métrica por usuário/time (tokens e latência).
- Score simples de qualidade (`clareza`, `cordialidade`, `objetividade`).

## Como apresentar no portfólio

Sugestão de descrição curta:

> API de geração de respostas de e-mail com IA, com controle de tom e idioma, múltiplas variações e rastreio de consumo de tokens. Desenvolvida com FastAPI, Pydantic e integração Groq/Llama.

## Status

Base de integração com LLM implementada.

Próximo passo recomendado:
- implementar o endpoint `POST /v1/email/reply` com schemas dedicados e testes de contrato.
