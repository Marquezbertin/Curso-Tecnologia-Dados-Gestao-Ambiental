# Certificado — modelo e critérios

## 1. Critérios de emissão

| Critério | Regra |
|---|---|
| Presença | ≥ 8 de 10 encontros (80%) |
| Entregáveis | ≥ 7 de 9 entregas parciais |
| Projeto | Pôster e apresentação na mostra |
| Ficha de IA | Entregue e revisada |
| Carga horária | 20h |

Quem não atinge o critério **não é reprovado**: recebe plano de recuperação de 2 semanas e conclui
no ciclo seguinte.

---

## 2. Modelo de certificado (texto)

```
CERTIFICADO DE CONCLUSÃO

Certificamos que [NOME DO ALUNO] concluiu o curso livre
"Tecnologia, Dados e IA na Gestão Ambiental",
com carga horária de 20 horas, realizado em [MUNICÍPIO],
no período de [DATA DE INÍCIO] a [DATA DE FIM].

Conteúdo: dados abertos ambientais, planilhas, Python,
mapas, coleta de dados, análise crítica, machine learning
e ética em inteligência artificial.

Projeto final: [TÍTULO DO PROJETO]

[NOME DO PROFESSOR]          [NOME DA COORDENAÇÃO]
[INSTITUIÇÃO]                [INSTITUIÇÃO]

Código de verificação: [CÓDIGO]
Verifique em: [LINK DA PÁGINA DE VERIFICAÇÃO]
```

---

## 3. Código de verificação

Sugestão simples e auditável:

- Prefixo `TDA` (Tecnologia, Dados e Ambiental).
- Ano do curso (4 dígitos).
- Número sequencial do aluno (3 dígitos).
- 2 dígitos de conferência gerados a partir do nome + ano.

Exemplo: `TDA-2026-001-47`.

Registre a lista de códigos em uma planilha de acesso restrito da coordenação, sem publicar nomes.

---

## 4. Página pública de verificação

A página do GitHub Pages pode ter uma seção "Verificar certificado" com:

- campo para digitar o código;
- mensagem "certificado válido" ou "código não encontrado";
- data de emissão e carga horária;
- aviso de que a verificação não expõe dados pessoais.

Implementação simples em JavaScript, sem backend, com uma lista de códigos válidos publicada
apenas se a coordenação autorizar. Caso contrário, a verificação é feita por e-mail.

---

## 5. Certificado para professores e monitores

Professores e monitores recebem certificado de **participação** com a carga horária de formação
(quando houver) e a descrição das atividades. Critérios:

- presença na formação inicial;
- acompanhamento de pelo menos 8 encontros;
- entrega do relatório de observação.

---

## 6. Registro e LGPD

- Nome completo no certificado: sim, com consentimento.
- Nome em lista pública: **não**.
- Código de verificação: sim, sem dados pessoais.
- Retenção do registro: até 2 anos.
- Exclusão a pedido do titular ou responsável: em até 15 dias.
