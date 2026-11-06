# 🌎 Tecnologia, Dados e IA na Gestão Ambiental

Minicurso **gratuito, aberto e pronto para usar em sala** — 10 encontros de 2h (20h) para o
ensino médio, construído sobre **evidência científica** e com **inteligência artificial**
como ferramenta de investigação, não como atalho.

> **A ideia em uma frase:** cada grupo investiga um problema ambiental real do seu território,
> aprende a ler os dados abertos que já existem, coleta os seus próprios dados e usa Python,
> mapas e IA para transformar evidência em uma proposta de ação apresentada à comunidade.

**Apresentação para a Secretaria de Meio Ambiente:** o site do projeto está em
[`docs/`](docs/) e pode ser publicado no GitHub Pages (instruções em [`docs/README.md`](docs/README.md)).

---

## 🎯 O que o aluno sai sabendo fazer

| # | Competência | Evidência de aprendizagem |
|---|---|---|
| 1 | Localizar e ler dados ambientais abertos (INMET, INPE, MapBiomas, ANA) | Ficha de fonte com data, variável, limitação |
| 2 | Organizar, limpar e visualizar dados em planilha e em Python | Notebook comentado com gráfico |
| 3 | Criar mapas simples do município | Mapa interativo com uma camada de dados |
| 4 | Planejar e executar coleta de dados na escola | Plano de coleta + planilha de registros |
| 5 | Interpretar dados criticamente (fonte, erro, viés, limite) | Análise com seção "o que os dados não mostram" |
| 6 | Usar IA generativa e machine learning com verificação humana | Prompt documentado + modelo avaliado |
| 7 | Comunicar resultados e propor ações baseadas em evidência | Pôster e apresentação na mostra |

---

## 🗂️ Organização do repositório

| Pasta / arquivo | Conteúdo |
|---|---|
| [`00-INDICE-GERAL.md`](00-INDICE-GERAL.md) | Visão geral, grade dos 10 encontros e por onde começar |
| [`01-PROJETO-PEDAGOGICO.md`](01-PROJETO-PEDAGOGICO.md) | Justificativa, objetivos, BNCC, metodologia, avaliação, LGPD e cronograma |
| [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md) | Cada decisão didática ligada a uma evidência científica |
| [`03-PLANO-DE-ENSINO.md`](03-PLANO-DE-ENSINO.md) | Plano dos 10 encontros com entregáveis e materiais |
| [`04-ENCONTROS/`](04-ENCONTROS/) | 10 planos de aula completos, minuto a minuto |
| [`05-NOTEBOOKS-COLAB/`](05-NOTEBOOKS-COLAB/) | Notebooks Python prontos para Google Colab |
| [`06-DADOS/`](06-DADOS/) | Fontes de dados, dicionário de dados e exemplos didáticos |
| [`07-AVALIACAO/`](07-AVALIACAO/) | Rubricas de 4 níveis, avaliação por encontro e certificado |
| [`08-GUIA-DO-PROFESSOR/`](08-GUIA-DO-PROFESSOR/) | Roteiro, plano B offline, ética e segurança de IA |
| [`09-REFERENCIAS/`](09-REFERENCIAS/) | Referências científicas e normativas completas |
| [`10-RECURSOS/`](10-RECURSOS/) | Ferramentas gratuitas, fontes de dados e links |

---

## 🧭 Os 10 encontros

| # | Encontro | Entregável | IA no encontro |
|---|---|---|---|
| 1 | Por que dados e meio ambiente? | Tema + pergunta de investigação | Mapa mental com assistente de IA |
| 2 | Primeiros dados na planilha | Gráfico comentado | IA para explicar o gráfico (com conferência) |
| 3 | Python sem medo — parte 1 | Script alterado e rodando | IA como tutora de código |
| 4 | Python sem medo — parte 2 | Notebook com análise | IA para revisar e apontar erros |
| 5 | Mapas e território | Mapa do município com camada | IA para interpretar o mapa |
| 6 | Queimadas e desmatamento | Comparação entre anos/regiões | IA para classificar focos de calor |
| 7 | Coleta de dados na escola | Plano de coleta + registros | IA para revisar o desenho amostral |
| 8 | Analisando os dados coletados | Análise com limitações | IA para auditar vieses |
| 9 | IA aplicada ao meio ambiente | Modelo simples + ficha de modelo | Machine learning + visão computacional |
| 10 | Do dado à solução e mostra | Pôster + apresentação | IA para ensaiar a comunicação |

Planos detalhados em [`03-PLANO-DE-ENSINO.md`](03-PLANO-DE-ENSINO.md) e em
[`04-ENCONTROS/`](04-ENCONTROS/).

---

## 🧪 Base científica em uma página

O curso não foi desenhado "por intuição". Cada escolha tem uma razão declarada:

| Decisão | Base científica | Onde ver |
|---|---|---|
| 2/3 da aula é prática, não exposição | Freeman et al. (2014), *PNAS* | [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md) |
| Quiz de recuperação no início de cada aula | Karpicke & Roediger (2008); Karpicke (2012) | [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md) |
| Ciclo de 5 fases (Engajar → Explorar → Explicar → Aplicar → Avaliar) | Bybee et al. (2006), modelo BSCS 5E | [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md) |
| Projeto desde a primeira semana | Papert (1980); Resnick (2017) | [`01-PROJETO-PEDAGOGICO.md`](01-PROJETO-PEDAGOGICO.md) |
| Leitura lateral e teste CRAAP para fontes | Wineburg & McGrew (2019); Blakeslee (2004) | [`04-ENCONTROS/06-queimadas-e-desmatamento.md`](04-ENCONTROS/06-queimadas-e-desmatamento.md) |
| IA com verificação, ficha de modelo e revisão humana | Mitchell et al. (2019); Gebru et al. (2021); UNESCO (2021) | [`08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md`](08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md) |
| Dados de satélite e machine learning aplicados ao território | Reichstein et al. (2019); Rolnick et al. (2022); Gorelick et al. (2017) | [`06-DADOS/README.md`](06-DADOS/README.md) |

A matriz completa, com a aplicação prática de cada evidência, está em
[`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md).

---

## 🧰 Ferramentas — todas gratuitas

| Ferramenta | Para quê | Link |
|---|---|---|
| Google Colab | Python no navegador, sem instalar | https://colab.research.google.com/ |
| Google Sheets / Excel | Primeiros dados e gráficos | https://sheets.google.com/ |
| Python: pandas, Matplotlib, Folium, scikit-learn | Análise, gráficos, mapas e ML | https://pandas.pydata.org/ |
| MapBiomas Plataforma | Uso do solo e cobertura vegetal | https://plataforma.mapbiomas.org/ |
| Google Earth Engine | Imagens de satélite em escala | https://earthengine.google.com/ |
| INMET | Temperatura e chuva | https://portal.inmet.gov.br/ |
| INPE (PRODES, DETER, Queimadas) | Desmatamento e focos de calor | https://terrabrasilis.dpi.inpe.br/ |
| ANA | Qualidade e quantidade de água | https://www.snirh.gov.br/ |
| Teachable Machine | Visão computacional sem código | https://teachablemachine.withgoogle.com/ |
| Chatbot de IA (Gemini, ChatGPT, etc.) | Assistente de análise e código | conta gratuita do professor |

> ⚠️ Nada aqui exige cartão de crédito ou licença paga. Se um passo pedir pagamento, é o passo
> errado.

---

## 🚀 Começando em 5 minutos

1. Leia [`00-INDICE-GERAL.md`](00-INDICE-GERAL.md) para entender o percurso.
2. Abra [`03-PLANO-DE-ENSINO.md`](03-PLANO-DE-ENSINO.md) e escolha o encontro 1.
3. Leia o plano do encontro em [`04-ENCONTROS/01-por-que-dados-e-meio-ambiente.md`](04-ENCONTROS/01-por-que-dados-e-meio-ambiente.md).
4. Abra o notebook [`05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb`](05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb) no Colab.
5. Aplique a rubrica de [`07-AVALIACAO/01-rubrica-avaliacao.md`](07-AVALIACAO/01-rubrica-avaliacao.md).

---

## 🧑‍🏫 Para quem é

- **Professor do ensino médio** que quer trabalhar dados e meio ambiente com projeto real.
- **Projeto social ou escola pública** que precisa de material gratuito e de baixo custo.
- **Autodidata** que quer aprender ciência de dados aplicada a uma causa concreta.

Não exige experiência prévia em programação — nem do aluno, nem do professor. O plano B offline
está em [`08-GUIA-DO-PROFESSOR/02-plano-b-offline.md`](08-GUIA-DO-PROFESSOR/02-plano-b-offline.md).

---

## 🔐 Ética, dados e proteção de menores

- Nenhum dado pessoal de aluno em repositório público.
- Dados ambientais da escola são **agregados** e identificados por código, não por nome.
- Uso de IA sempre com **verificação humana** e registro do prompt.
- Chaves de API ficam na conta do professor, nunca no navegador do aluno.
- Detalhes em [`08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md`](08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md).

---

## 📄 Licença e atribuição

- **Conteúdo didático** (textos, atividades, planos): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt-br).
- **Código dos notebooks**: MIT — use, adapte e compartilhe mantendo o crédito.
- **Dados de exemplo**: sintéticos e didáticos, marcados como tal; não representam medições reais.
- **Dados públicos** (INMET, INPE, MapBiomas, ANA): mantêm as licenças e os termos dos provedores.
- Material alinhado ao ecossistema aberto de [Marquez Bertin](https://github.com/Marquezbertin)
  e do [Laboratório Tech Social](https://marquezbertin.github.io/laboratorio-tech-social/).

---

## 🤝 Como contribuir

1. Abra uma *issue* com a melhoria (encontro, notebook, dado ou correção).
2. Faça um *fork*, crie uma branch (`docs/melhora-encontro-x`) e envie um pull request.
3. Toda contribuição passa por revisão: clareza, adequação ao ensino médio, rigor da fonte,
   acentuação e links funcionando.

**Encontrou um erro científico ou um link quebrado?** Corrija e envie — material didático
melhora com uso real.
