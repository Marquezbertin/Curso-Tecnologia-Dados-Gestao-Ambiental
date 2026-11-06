# Dados do curso

Esta pasta reúne as **fontes de dados abertos** usadas no curso, o **dicionário de dados** e os
**arquivos de exemplo** (sintéticos) para quem não conseguir baixar dados reais na hora da aula.

---

## 1. Fontes oficiais (dados reais)

| Fonte | O que oferece | Onde acessar | Cuidado |
|---|---|---|---|
| **INMET** | Temperatura, chuva, umidade, vento de estações automáticas | https://portal.inmet.gov.br/ | Estação pode ter falhas (`-9999`) |
| **INPE — Queimadas** | Focos de calor detectados por satélite | https://terrabrasilis.dpi.inpe.br/ | Foco não é sinônimo de desmatamento |
| **INPE — PRODES** | Desmatamento por corte raso (Amazônia e outros biomas) | https://terrabrasilis.dpi.inpe.br/ | Metodologia e ano de referência |
| **INPE — DETER** | Alertas de desmatamento e degradação | https://terrabrasilis.dpi.inpe.br/ | Alerta não é dado consolidado |
| **MapBiomas** | Uso do solo e cobertura vegetal (série histórica) | https://plataforma.mapbiomas.org/ | Confira a coleção e o ano |
| **ANA / SNIRH** | Qualidade e quantidade de água | https://www.snirh.gov.br/ | Cobertura varia por município |
| **IBGE** | População, território, Censo | https://www.ibge.gov.br/ | Use a data de referência |
| **Google Earth Engine** | Imagens de satélite e análise em escala | https://earthengine.google.com/ | Requer conta e noções de código |

---

## 2. Arquivos de exemplo (sintéticos)

> **Atenção:** os arquivos abaixo são **didáticos e sintéticos**. Eles imitam a estrutura de dados
> reais, mas **não representam medições verdadeiras**. Servem para a aula rodar mesmo sem
> internet ou sem download.

| Arquivo | Colunas | Uso |
|---|---|---|
| [`exemplos/exemplo-inmet-sintetico.csv`](exemplos/exemplo-inmet-sintetico.csv) | `data, temp_max_c, temp_min_c, chuva_mm` | Encontros 2, 3, 4 e 8 |
| [`exemplos/exemplo-focos-calor-sintetico.csv`](exemplos/exemplo-focos-calor-sintetico.csv) | `ano, mes, municipio, bioma, focos` | Encontro 6 |
| [`exemplos/exemplo-escola-sintetico.csv`](exemplos/exemplo-escola-sintetico.csv) | `data, ponto, variavel, valor, unidade, responsavel_codigo` | Encontros 7 e 8 |
| [`exemplos/exemplo-risco-fogo-sintetico.csv`](exemplos/exemplo-risco-fogo-sintetico.csv) | `temp_max_c, umidade_rel_pct, vento_kmh, chuva_mm, risco_fogo` | Encontro 9 |

---

## 3. Como baixar dados reais do INMET (passo a passo)

1. Abra https://portal.inmet.gov.br/
2. Vá em **Dados históricos** ou **Estações automáticas**.
3. Escolha o estado e o município mais próximo.
4. Selecione o período (ex.: últimos 12 meses).
5. Baixe o CSV e abra no Colab ou na planilha.
6. Anote no notebook: **estação, período, fonte e limitação**.

### Códigos de falha comuns

| Código | Significado |
|---|---|
| `-9999` | Falha de medição ou dado ausente |
| vazio | Sem registro no período |
| `0.0` em chuva | Pode ser ausência real de chuva ou falha; confira o contexto |

---

## 4. Como baixar focos de calor do INPE

1. Abra https://terrabrasilis.dpi.inpe.br/
2. Entre em **Queimadas**.
3. Escolha o estado, o município e o período.
4. Baixe o CSV.
5. Confira a **metodologia** e o **satélite** usado.
6. Registre a fonte e a limitação no notebook.

---

## 5. Ética e proteção de dados

- Dados ambientais da escola são **agregados** e identificados por código (`Ponto A`, `G1`).
- Nunca inclua nome, rosto, endereço ou telefone de aluno.
- Ao usar IA, não cole dados pessoais no prompt.
- Ao publicar no GitHub, confira se não há dado identificável.
- Siga a LGPD (Lei 13.709/2018) e o ECA (Lei 8.069/1990).

---

## 6. Como citar os dados no pôster

Use o formato:

> FONTE: INMET. Estação [nome], período [mês/ano a mês/ano]. Disponível em: [link]. Acesso em:
> [data]. Limitação: [ex.: série com falhas em dias de chuva intensa].

Para MapBiomas:

> FONTE: MAPBIOMAS. Coleção [número], classe [nome], ano [ano]. Disponível em:
> https://plataforma.mapbiomas.org/. Acesso em: [data].

Para INPE:

> FONTE: INPE. [PRODES/DETER/Queimadas], [município/estado], [período]. Disponível em:
> https://terrabrasilis.dpi.inpe.br/. Acesso em: [data].

---

## 7. Dicionário de dados

O dicionário completo está em [`dicionario-de-dados.md`](dicionario-de-dados.md).
