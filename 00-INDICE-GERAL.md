# 🧭 Índice Geral — Tecnologia, Dados e IA na Gestão Ambiental

**Minicurso gratuito** · 10 encontros de 2h (20h) · ensino médio · projeto final em mostra
**Base:** dados abertos brasileiros + Python + mapas + inteligência artificial com verificação

> **A ideia em uma frase:** os alunos investigam um problema ambiental real do seu território e
> usam dados, Python e IA como ferramentas para entendê-lo e propor soluções com evidência.

**Apresentação institucional:** a página para a Secretaria Municipal de Meio Ambiente está em
[`docs/`](docs/) e pode ser publicada no GitHub Pages (veja [`docs/README.md`](docs/README.md)).

---

## 📌 Ficha do curso

| Campo | Descrição |
|---|---|
| **Nome** | Tecnologia, Dados e IA na Gestão Ambiental |
| **Natureza** | Curso livre / minicurso de extensão, gratuito |
| **Público** | Estudantes do ensino médio (14–18 anos), sem pré-requisito de programação |
| **Carga** | 20h — 10 encontros de 2h |
| **Formato** | Aulas práticas em duplas ou trios, notebooks prontos no Google Colab |
| **Produto final** | Projeto em grupo apresentado em mostra de ciências |
| **Plataforma** | Google Colab + Google Sheets/Excel + MapBiomas + navegador |
| **Custo** | R$ 0 para o aluno; todas as ferramentas são gratuitas |
| **Licença** | CC BY-NC-SA 4.0 (conteúdo) e MIT (código) |

---

## 🎯 Por que este curso existe

Três problemas se cruzam:

1. **Dado ambiental existe, mas não chega à escola.** INMET, INPE, MapBiomas e ANA publicam
   dados abertos de qualidade, mas o aluno médio nunca abriu um CSV desses.
2. **"Meio ambiente" costuma ser ensinado como opinião, não como evidência.** Sem dados, o
   debate vira slogan — e o aluno não aprende a distinguir correlação de causalidade, nem a
   reconhecer o limite de uma série histórica.
3. **IA entra na vida do aluno sem critério.** Ele usa chatbot para tudo, mas não sabe verificar
   resposta, avaliar viés, documentar modelo nem perceber quando a IA está errada.

O curso ataca os três ao mesmo tempo: **dado real → análise com Python → IA com verificação →
proposta de ação**.

---

## 🗺️ Mapa do percurso

```
Encontro 1  →  problema e pergunta
Encontro 2  →  planilha e primeiro gráfico
Encontro 3  →  Python básico
Encontro 4  →  pandas e Matplotlib
Encontro 5  →  mapas e território
Encontro 6  →  queimadas e desmatamento
Encontro 7  →  coleta na escola
Encontro 8  →  análise dos dados coletados
Encontro 9  →  IA aplicada ao meio ambiente
Encontro 10 →  solução, pôster e mostra
```

Cada encontro entrega uma peça pequena que alimenta o projeto final. Nada fica "para depois".

---

## 📅 Grade dos 10 encontros

| # | Tema | Conceitos centrais | Entregável | IA |
|---|---|---|---|---|
| 1 | Por que dados e meio ambiente? | Problema, pergunta, variável, fonte | Tema + pergunta de investigação | Assistente organiza mapa mental |
| 2 | Primeiros dados na planilha | Dado, variável, série temporal, gráfico | Gráfico comentado | IA explica o gráfico; aluno confere |
| 3 | Python sem medo — 1 | Colab, célula, variável, lista | Script alterado e rodando | IA como tutora de código |
| 4 | Python sem medo — 2 | CSV, pandas, filtro, média, gráfico | Notebook com análise do tema | IA revisa o código e aponta erros |
| 5 | Mapas e território | Coordenada, ponto, área, camada | Mapa do município com camada | IA interpreta o mapa |
| 6 | Queimadas e desmatamento | Série temporal, comparação, fonte | Comparação entre anos/regiões | IA classifica focos de calor |
| 7 | Coleta de dados na escola | Amostragem, instrumento, frequência | Plano de coleta + registros | IA revisa o desenho amostral |
| 8 | Analisando os dados coletados | Limpeza, estatística, viés, limite | Análise com seção de limitações | IA audita vieses |
| 9 | IA aplicada ao meio ambiente | ML supervisionado, visão computacional, ética | Modelo simples + ficha de modelo | Núcleo do curso |
| 10 | Do dado à solução e mostra | Storytelling, proposta, argumento | Pôster + apresentação | IA ensaia a comunicação |

Planos completos: [`04-ENCONTROS/`](04-ENCONTROS/).

---

## 📂 Mapa dos arquivos

| Arquivo | Para quem | Para que serve |
|---|---|---|
| `README.md` | todos | Apresentação e início rápido |
| `00-INDICE-GERAL.md` | todos | Este mapa |
| `01-PROJETO-PEDAGOGICO.md` | coordenação, escola | Justificativa, BNCC, avaliação, LGPD |
| `02-MATRIZ-CIENTIFICA.md` | professor, coordenação | Evidência científica de cada decisão |
| `03-PLANO-DE-ENSINO.md` | professor | Grade detalhada e materiais por encontro |
| `04-ENCONTROS/` | professor | Aula pronta, minuto a minuto |
| `05-NOTEBOOKS-COLAB/` | professor e aluno | Código executável |
| `06-DADOS/` | professor e aluno | Fontes, dicionário e exemplos |
| `07-AVALIACAO/` | professor | Rubricas e certificado |
| `08-GUIA-DO-PROFESSOR/` | professor | Roteiro, plano B e ética de IA |
| `09-REFERENCIAS/` | todos | Bibliografia científica e normas |
| `10-RECURSOS/` | todos | Ferramentas e links |

---

## ✅ Checklist do professor — antes da primeira aula

- [ ] Li `01-PROJETO-PEDAGOGICO.md` e `02-MATRIZ-CIENTIFICA.md`.
- [ ] Testei o notebook `01-primeiros-dados.ipynb` no Colab com a conta da escola.
- [ ] Escolhi o município e conferi os dados de exemplo do IBGE/INPE/MapBiomas.
- [ ] Preparei o plano B offline (impresso) para o caso de internet cair.
- [ ] Defini as regras de uso de IA da turma (ver `08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md`).
- [ ] Li a política de dados e proteção de menores (seção 7 do projeto pedagógico).
- [ ] Criei o formulário de escolha de tema e o canal oficial da turma.

---

## 🧭 Por onde começar (escolha o seu caminho)

### Se você vai dar a aula
1. `03-PLANO-DE-ENSINO.md` — visão dos 10 encontros.
2. `04-ENCONTROS/01-...` — plano do primeiro encontro.
3. `05-NOTEBOOKS-COLAB/README.md` — como abrir no Colab.
4. `08-GUIA-DO-PROFESSOR/` — roteiro, plano B e ética.

### Se você coordena ou aprova o projeto
1. `01-PROJETO-PEDAGOGICO.md` — justificativa, objetivos e indicadores.
2. `02-MATRIZ-CIENTIFICA.md` — rigor e base da proposta.
3. `09-REFERENCIAS/01-referencias-cientificas.md` — bibliografia.

### Se você é aluno
1. `03-PLANO-DE-ENSINO.md` — o que vamos fazer.
2. `06-DADOS/README.md` — de onde vêm os dados.
3. `05-NOTEBOOKS-COLAB/` — abra o notebook do dia.

---

## 📊 Competências e avaliação

A avaliação é **formativa**: 40% processo, 40% projeto final, 20% apresentação. Não há prova
eliminatória. A rubrica de 4 níveis está em
[`07-AVALIACAO/01-rubrica-avaliacao.md`](07-AVALIACAO/01-rubrica-avaliacao.md).

| Dimensão | O que observa | Peso |
|---|---|---|
| Processo | Entregas parciais e participação | 40% |
| Projeto final | Qualidade da análise, do mapa e da proposta | 40% |
| Apresentação | Clareza e interpretação dos dados | 20% |

---

## 🔗 Links rápidos

- Projeto pedagógico — [`01-PROJETO-PEDAGOGICO.md`](01-PROJETO-PEDAGOGICO.md)
- Matriz científica — [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md)
- Planos de aula — [`04-ENCONTROS/`](04-ENCONTROS/)
- Notebooks — [`05-NOTEBOOKS-COLAB/`](05-NOTEBOOKS-COLAB/)
- Dados — [`06-DADOS/`](06-DADOS/)
- Avaliação — [`07-AVALIACAO/`](07-AVALIACAO/)
- Guia do professor — [`08-GUIA-DO-PROFESSOR/`](08-GUIA-DO-PROFESSOR/)
- Referências — [`09-REFERENCIAS/01-referencias-cientificas.md`](09-REFERENCIAS/01-referencias-cientificas.md)
- Ferramentas — [`10-RECURSOS/01-ferramentas-e-fontes.md`](10-RECURSOS/01-ferramentas-e-fontes.md)
