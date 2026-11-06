# Dicionário de Dados

Definições das variáveis usadas nos exemplos e nas fontes reais. Todo notebook e pôster deve
usar a mesma unidade e o mesmo nome de variável para evitar confusão.

---

## 1. Dados meteorológicos (INMET e exemplo sintético)

| Variável | Nome no arquivo | Unidade | Definição | Cuidado |
|---|---|---|---|---|
| Data | `data` | AAAA-MM-DD | Dia da medição | Usar formato ISO para ordenar |
| Temperatura máxima | `temp_max_c` | °C | Maior temperatura do dia | Pode ocorrer em horário específico |
| Temperatura mínima | `temp_min_c` | °C | Menor temperatura do dia | Mesma observação |
| Chuva | `chuva_mm` | mm | Precipitação acumulada | `0` pode ser ausência ou falha |
| Umidade relativa | `umidade_rel_pct` | % | Umidade do ar | Varia ao longo do dia |
| Vento | `vento_kmh` | km/h | Velocidade do vento | Rajada é diferente de média |

---

## 2. Focos de calor (INPE e exemplo sintético)

| Variável | Nome no arquivo | Unidade | Definição | Cuidado |
|---|---|---|---|---|
| Ano | `ano` | — | Ano de referência | Comparar mesmo período |
| Mês | `mes` | 1–12 | Mês de referência | Sazonalidade afeta a comparação |
| Município | `municipio` | — | Nome do município | Confira a grafia oficial |
| Bioma | `bioma` | — | Bioma predominante | Fronteiras podem variar |
| Focos | `focos` | contagem | Nº de focos detectados | Detecção depende do satélite |

> **Conceito-chave:** foco de calor é uma **detecção por satélite**, não uma certidão de
> queimada. Desmatamento e queimada são fenômenos relacionados, mas não idênticos.

---

## 3. Coleta escolar (exemplo sintético)

| Variável | Nome no arquivo | Unidade | Definição | Cuidado |
|---|---|---|---|---|
| Data | `data` | AAAA-MM-DD | Dia da coleta | Mesmo dia para todos os pontos |
| Ponto | `ponto` | — | Local da medição | Use código, não nome de aluno |
| Variável | `variavel` | — | O que foi medido | Padronize o nome |
| Valor | `valor` | conforme variável | Resultado da medição | Registre a unidade |
| Unidade | `unidade` | L, kWh, °C, kg | Unidade do valor | Não misture unidades |
| Responsável | `responsavel_codigo` | — | Código do grupo | Nunca nome completo |

### Variáveis sugeridas para a escola

| Variável | Como medir | Frequência sugerida | Limitação |
|---|---|---|---|
| Consumo de água | Leitura do hidrômetro | 1×/semana | Não separa uso por atividade |
| Consumo de energia | Leitura do medidor | 1×/semana | Varia com clima e ocupação |
| Temperatura do pátio | Termômetro à sombra | 1×/dia, mesmo horário | Não representa a escola toda |
| Resíduos orgânicos | Pesagem ou contagem | 1×/dia | Depende da balança |
| Área verde | Contagem de árvores / m² | 1× | Critério de "árvore" precisa ser definido |
| Ruído | App de decibel | 3×/dia | Calibração do celular é limitada |

---

## 4. Dados de risco de fogo (exemplo sintético)

| Variável | Nome no arquivo | Unidade | Definição |
|---|---|---|---|
| Temperatura máxima | `temp_max_c` | °C | Entrada do modelo |
| Umidade relativa | `umidade_rel_pct` | % | Entrada do modelo |
| Vento | `vento_kmh` | km/h | Entrada do modelo |
| Chuva | `chuva_mm` | mm | Entrada do modelo |
| Risco de fogo | `risco_fogo` | 0 ou 1 | Rótulo: 0 = sem risco; 1 = risco |

> O rótulo foi gerado por regra didática no arquivo sintético. Em dados reais, o rótulo viria de
> ocorrências confirmadas ou de um índice oficial — e isso muda a interpretação do modelo.

---

## 5. Metadados obrigatórios

Todo conjunto de dados usado no projeto deve registrar:

```
Fonte:
Link:
Responsável pela publicação:
Período:
Abrangência:
Metodologia (resumo):
Unidade:
Limitação declarada:
Data de acesso:
```

Sem metadados, o dado não entra no pôster.
