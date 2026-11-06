# Projeto Pedagógico — Tecnologia, Dados e IA na Gestão Ambiental

**Versão:** 1.0 · **Carga:** 20h (10 encontros de 2h) · **Público:** ensino médio (14–18 anos)
**Formato:** curso livre, gratuito, presencial ou híbrido, com notebooks no Google Colab
**Proponente:** Laboratório Tech Social / Marquez Bertin
**Parceiro institucional pretendido:** Secretaria Municipal de Meio Ambiente (com articulação
com a Secretaria de Educação)
**Documentos irmãos:** `00-INDICE-GERAL.md`, `02-MATRIZ-CIENTIFICA.md`,
`03-PLANO-DE-ENSINO.md`, `04-ENCONTROS/`, `07-AVALIACAO/`, `08-GUIA-DO-PROFESSOR/`

---

## Sumário

1. [Resumo executivo](#1-resumo-executivo)
2. [Identificação do projeto](#2-identificação-do-projeto)
3. [Justificativa](#3-justificativa)
4. [Marco legal e referências curriculares](#4-marco-legal-e-referências-curriculares)
5. [Objetivos](#5-objetivos)
6. [Público-alvo e critérios de participação](#6-público-alvo-e-critérios-de-participação)
7. [Metodologia com base científica](#7-metodologia-com-base-científica)
8. [Estrutura curricular e IA](#8-estrutura-curricular-e-ia)
9. [Avaliação e certificação](#9-avaliação-e-certificação)
10. [Acessibilidade, inclusão e proteção de dados](#10-acessibilidade-inclusão-e-proteção-de-dados)
11. [O que a Secretaria recebe](#11-o-que-a-secretaria-recebe)
12. [O que pedimos à Secretaria](#12-o-que-pedimos-à-secretaria)
13. [Indicadores e monitoramento](#13-indicadores-e-monitoramento)
14. [Riscos e plano de contingência](#14-riscos-e-plano-de-contingência)
15. [Cronograma de implantação](#15-cronograma-de-implantação)
16. [Orçamento](#16-orçamento)
17. [Sustentabilidade e continuidade](#17-sustentabilidade-e-continuidade)
18. [Referências](#18-referências)

---

## 1. Resumo executivo

O município já produz e recebe **dados ambientais** — qualidade do ar, focos de calor,
desmatamento, chuva, temperatura, recursos hídricos, resíduos, uso do solo. Esses dados, porém,
raramente chegam à escola e quase nunca viram **decisão pública** compreensível pela população.

O minicurso **Tecnologia, Dados e IA na Gestão Ambiental** resolve essa lacuna com uma proposta
simples e de custo zero para o aluno:

- **10 encontros de 2h** (20h), em duplas ou trios, com notebooks prontos no Google Colab.
- O aluno investiga um **problema ambiental real do território** e produz uma **proposta de ação
  baseada em evidência**, apresentada em mostra pública.
- A **inteligência artificial** entra como ferramenta de análise, de programação e de
  comunicação — sempre com verificação humana, ficha de modelo e registro de uso.
- Todo o material é **aberto, gratuito e reaplicável** por qualquer escola da rede.

**Resultado esperado na primeira turma:** 20 a 30 alunos formados, 6 a 10 projetos apresentados,
100% de conclusão entre quem cumpre presença mínima, e um **banco de diagnósticos locais** que a
Secretaria pode usar como insumo de educação ambiental e de planejamento.

**Custo para o aluno:** R$ 0. **Custo para a Secretaria:** R$ 0 a R$ 3.500 (somente conforto e
divulgação, conforme cenário na seção 16).

---

## 2. Identificação do projeto

| Campo | Descrição |
|---|---|
| **Nome** | Tecnologia, Dados e IA na Gestão Ambiental |
| **Natureza** | Curso livre de extensão, gratuito, sem fins lucrativos |
| **Modalidade** | Presencial, híbrido ou online ao vivo (a definir com a Secretaria) |
| **Público** | Estudantes do ensino médio (14–18 anos) da rede pública e comunidade |
| **Carga horária** | 20h — 10 encontros de 2h |
| **Turmas** | 1 turma piloto de até 30 alunos; 2º ciclo com até 2 turmas |
| **Equipe mínima** | 1 professor titular + 1 monitor/voluntário por turma |
| **Plataforma** | Google Colab, Google Sheets/Excel, MapBiomas, navegador |
| **Certificação** | certificado de curso livre com carga horária e código de verificação |
| **Idioma** | português do Brasil |
| **Licença** | CC BY-NC-SA 4.0 (conteúdo) e MIT (código) |
| **Custo do aluno** | R$ 0 (zero) |

---

## 3. Justificativa

### 3.1 O problema ambiental como problema de informação

A gestão ambiental municipal depende de informação confiável: onde está o foco de calor, qual
bairro tem menos área verde, como evoluiu o uso do solo, quanto choveu acima da média, onde há
descarte irregular. Os dados existem, mas há três gargalos:

1. **Gargalo de acesso:** os dados estão em portais técnicos (INPE, INMET, MapBiomas, ANA) que
   o cidadão comum não sabe navegar.
2. **Gargalo de interpretação:** sem formação em leitura de dados, o número vira manchete e a
   correlação vira causa.
3. **Gargalo de participação:** a população recebe a decisão pronta; não participa do diagnóstico
   nem acompanha o resultado.

### 3.2 O problema educacional

A BNCC e a Política Nacional de Educação Digital pedem cultura digital e pensamento
computacional, mas a escola média ainda ensina tecnologia de forma instrumental (usar o
aplicativo), não investigativa (usar o dado para perguntar e decidir). Ao mesmo tempo, a IA
generativa chegou ao celular do aluno sem que ele tenha critérios para verificar respostas,
reconhecer viés ou documentar o que usou.

### 3.3 A resposta do curso

| Problema | Resposta didática |
|---|---|
| Dado existe, mas não chega à escola | Aulas com dados abertos reais de INMET, INPE, MapBiomas e ANA |
| Número vira opinião | Trilha de leitura crítica: fonte, variável, período, limite |
| Aluno não programa | Colab com notebooks guiados; começa alterando parâmetro, não digitando do zero |
| IA sem critério | Uso com verificação, prompt documentado, ficha de modelo e revisão humana |
| Diagnóstico fica na gaveta | Mostra pública + entrega de relatório agregado à Secretaria |
| Curso custa caro | Ferramentas gratuitas, material aberto, custo zero para o aluno |

### 3.4 Por que um curso de dados ambientais no ensino médio

A adolescência é a fase em que o jovem escolhe caminho (técnico, trabalho, universidade) e em
que a participação cidadã começa a ganhar forma. Um curso que une **dados + meio ambiente + IA**
oferece três saídas concretas:

- **formação cidadã:** o aluno aprende a exigir e entender política pública com evidência;
- **formação técnica:** portfólio com Python, mapas e modelo de machine learning;
- **formação científica:** hipótese, coleta, análise, limitação e comunicação.

---

## 4. Marco legal e referências curriculares

### 4.1 Legislação e normas

| Norma | O que garante ou orienta |
|---|---|
| **Lei 9.795/1999** — Política Nacional de Educação Ambiental | Educação ambiental como componente essencial e permanente |
| **Lei 9.394/1996** — LDB | Educação como direito; cursos livres e extensão |
| **Lei 13.709/2018** — LGPD | Tratamento de dados pessoais; art. 14 trata de crianças e adolescentes |
| **Lei 8.069/1990** — ECA | Proteção integral de crianças e adolescentes |
| **Lei 12.965/2014** — Marco Civil da Internet | Direitos e deveres no uso da internet |
| **Lei 14.533/2023** — PNED | Política Nacional de Educação Digital |
| **Lei 13.146/2015** — LBI | Acessibilidade e inclusão |
| **BNCC (2018)** | Competências gerais, Ciências da Natureza, Matemática, Geografia e Cultura Digital |
| **Resolução CNE/CEB 1/2022** | Computação na educação básica: pensamento computacional, mundo digital e cultura digital |
| **Agenda 2030 / ODS** | ODS 4 (educação), 6 (água), 11 (cidades), 13 (clima) e 15 (vida terrestre) |
| **UNESCO (2021)** | Recomendação sobre a ética da inteligência artificial |

### 4.2 BNCC — competências gerais mobilizadas

| # | Competência | Como aparece |
|---|---|---|
| 1 | Conhecimento | Conceitos de clima, território, dados e IA com exemplos locais |
| 2 | Pensamento científico, crítico e criativo | Pergunta, hipótese, coleta, análise, conclusão e limite |
| 3 | Repertório cultural | Território, comunidade e história ambiental local |
| 4 | Comunicação | Gráfico, mapa, pôster e apresentação na mostra |
| 5 | Cultura digital | Uso crítico, ético e produtivo de dados e IA |
| 6 | Trabalho e projeto de vida | Portfólio com Python, mapas e modelo de ML |
| 7 | Argumentação | Defender uma proposta com evidência e responder perguntas |
| 8 | Autoconhecimento e autocuidado | Ergonomia, pausas, uso saudável de telas |
| 9 | Empatia e cooperação | Duplas, trios e revisão por pares |
| 10 | Responsabilidade e cidadania | Proposta de ação ambiental e compromisso público |

### 4.3 Computação na BNCC (Resolução CNE/CEB 1/2022)

| Eixo | Como aparece no curso |
|---|---|
| **Pensamento computacional** | Decomposição do problema, algoritmo, código em Python, automação |
| **Mundo digital** | Dados, planilhas, CSV, mapas, modelos de machine learning |
| **Cultura digital** | Ética de dados, viés algorítmico, privacidade, verificação de IA |

### 4.4 Educação ambiental (Lei 9.795/1999)

O curso adota a educação ambiental **crítica, participativa e transversal**, não apenas
conservacionista: o aluno investiga o território em que vive, reconhece conflitos ambientais e
propõe ação com base em evidência. A mostra final é, ao mesmo tempo, avaliação e devolutiva à
comunidade.

---

## 5. Objetivos

### 5.1 Objetivo geral

Formar jovens capazes de **investigar problemas ambientais do seu território com dados abertos,
Python e inteligência artificial**, comunicando conclusões e propondo ações baseadas em
evidência.

### 5.2 Objetivos específicos

1. Localizar, baixar e ler dados ambientais abertos de fontes brasileiras.
2. Organizar e visualizar dados em planilha e em Python.
3. Construir mapas simples do município com uma camada de dados.
4. Planejar e executar uma coleta de dados na escola, com critério de amostragem.
5. Interpretar dados criticamente, identificando fonte, erro, viés e limite.
6. Usar IA generativa e machine learning com verificação humana e documentação.
7. Comunicar resultados em pôster e apresentação de 5 a 8 minutos.
8. Entregar à comunidade e à Secretaria um diagnóstico agregado do território.

### 5.3 Objetivos de aprendizagem — ao final, o aluno é capaz de

- explicar a diferença entre dado, informação e evidência;
- descrever uma série temporal e identificar tendência, sazonalidade e valor atípico;
- ler um CSV e produzir um gráfico comentado em Python;
- criar um mapa interativo com pontos ou áreas do município;
- comparar focos de calor e desmatamento entre anos e regiões;
- planejar uma coleta com frequência, instrumento e responsável;
- treinar um modelo simples de classificação e interpretar seus erros;
- avaliar uma resposta de IA e registrar o prompt usado;
- apresentar uma proposta ambiental com evidência e limitações.

---

## 6. Público-alvo e critérios de participação

### 6.1 Público

| Perfil | Descrição | Pré-requisito |
|---|---|---|
| **Estudantes do ensino médio** | Rede pública municipal/estadual, 14–18 anos | Saber ler e escrever; nenhum conhecimento de programação |
| **Jovens da comunidade** | 14–18 anos, projetos sociais, EJA | Nenhum |
| **Professores da rede** | Podem participar como formação continuada | Nenhum |

### 6.2 Critérios de prioridade (não de exclusão)

Quando a procura superar as vagas:

1. Estudante da rede pública do município.
2. Família com renda elegível ao CadÚnico.
3. Meninas e jovens mulheres (meta de equidade: 50%).
4. Pessoa com deficiência ou neurodivergente, com apoio de acessibilidade.
5. Morador de bairro rural ou periférico.
6. Participante da EJA.
7. Demais interessados, por ordem de inscrição.

**Nunca são critérios de exclusão:** nota, histórico escolar, saber inglês, ter computador,
morar no centro.

### 6.3 Gratuidade

O curso é **gratuito para todos os alunos**: sem mensalidade, sem taxa de material, sem venda de
curso ao final. O material é aberto e as ferramentas são gratuitas. A gratuidade é um princípio
do projeto, não uma promoção.

### 6.4 Acessibilidade

- Material em Markdown e PDF com texto selecionável e contraste mínimo 4,5:1.
- Toda atividade tem versão que roda no celular ou no papel.
- Intérprete de Libras sob demanda, com antecedência.
- Tempo extra de 50% quando solicitado; entrega por áudio ou vídeo aceita.
- Nenhum aluno é obrigado a ligar câmera ou expor a tela.

---

## 7. Metodologia com base científica

O curso segue o ciclo de 5 fases do modelo **BSCS 5E** (Bybee et al., 2006), adaptado à realidade
brasileira e à duração de 2h:

```
Engajar  →  Explorar  →  Explicar  →  Aplicar  →  Avaliar
(problema)  (dados)     (conceito)   (projeto)   (mostra)
```

### 7.1 Princípios didáticos e evidência

| Princípio | Evidência | Aplicação concreta |
|---|---|---|
| **Aprendizagem ativa** | Freeman et al. (2014), *PNAS* | No máximo 1/3 de exposição; 2/3 de prática guiada |
| **Recuperação ativa** | Karpicke & Roediger (2008); Karpicke (2012) | Quiz de recuperação de 5 min no início de toda aula |
| **Prática espaçada** | Karpicke (2012) | Cada conceito reaparece nos encontros seguintes, não em bloco único |
| **Construcionismo** | Papert (1980); Resnick (2017) | Toda aula termina com algo construído e compartilhável |
| **Ciclo 5E** | Bybee et al. (2006) | Estrutura fixa de 5 fases em todos os encontros |
| **Desenho reverso** | Wiggins & McTighe (2005) | Primeiro o entregável e a rubrica; depois a atividade |
| **Aprendizagem experiencial** | Kolb (1984) | Problema real → experiência → reflexão → conceito → nova aplicação |
| **Zona de desenvolvimento proximal** | Vygotsky (1978) | Duplas estratégicas e monitor que dá dica de 30 s, não a resposta |
| **Alfabetização midiática** | Wineburg & McGrew (2019); Blakeslee (2004) | Leitura lateral e teste CRAAP para toda fonte de dados |
| **Letramento crítico de dados** | D'Ignazio & Klein (2020); O'Neil (2016) | Seção obrigatória "o que os dados não mostram" em toda análise |
| **IA responsável** | Mitchell et al. (2019); Gebru et al. (2021); UNESCO (2021) | Ficha de modelo, datasheet e revisão humana registrada |

A matriz completa, decisão por decisão, está em [`02-MATRIZ-CIENTIFICA.md`](02-MATRIZ-CIENTIFICA.md).

### 7.2 Estrutura de um encontro de 2h

| Fase | Tempo | O que acontece |
|---|---|---|
| **1. Engajar** | 10 min | Recuperação da aula anterior + problema do dia |
| **2. Explorar** | 20 min | Dados reais, pergunta, hipótese em grupo |
| **3. Explicar** | 15 min | Conceito necessário, com exemplo do território |
| **4. Aplicar** | 60 min | Mão na massa no notebook + projeto do grupo |
| **5. Avaliar** | 15 min | Mostra rápida, feedback e tarefa da semana |

### 7.3 Papel do professor e do monitor

- O professor **não entrega a resposta**: dá dica de 30 s e devolve a pergunta ao grupo.
- O monitor circula, registra quem travou e ajuda a dupla a ler a mensagem de erro.
- Toda dúvida técnica vira oportunidade de leitura de erro: "o que o computador está dizendo?"
- O erro é tratado como **evidência de aprendizagem**, não como fracasso.

### 7.4 IA como ferramenta pedagógica, não como substituta

| Uso da IA | Como é feito | Verificação obrigatória |
|---|---|---|
| Explicar um conceito | Aluno pergunta ao chatbot e reescreve com as próprias palavras | Comparar com o material e com o professor |
| Ajudar no código | Aluno pede explicação de erro, não a resposta pronta | Rodar o código e explicar cada linha alterada |
| Analisar dados | IA sugere hipótese e gráfico | Aluno confere no notebook e cita a fonte |
| Comunicar | IA ajuda a revisar o texto do pôster | Aluno confirma cada número com a planilha |
| Documentar | Aluno preenche ficha de modelo e registro de prompt | Professor revisa antes da mostra |

Regras completas em [`08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md`](08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md).

---

## 8. Estrutura curricular e IA

### 8.1 Visão geral

| # | Encontro | Foco | Entregável | IA |
|---|---|---|---|---|
| 1 | Por que dados e meio ambiente? | Problema e pergunta | Tema + pergunta | Mapa mental com assistente |
| 2 | Primeiros dados na planilha | Série temporal | Gráfico comentado | IA explica o gráfico |
| 3 | Python sem medo — 1 | Lógica e código | Script alterado | IA como tutora |
| 4 | Python sem medo — 2 | pandas e gráficos | Notebook com análise | IA revisa o código |
| 5 | Mapas e território | Geografia e camadas | Mapa com camada | IA interpreta o mapa |
| 6 | Queimadas e desmatamento | Comparação e crítica | Comparação entre anos | IA classifica focos |
| 7 | Coleta na escola | Amostragem | Plano de coleta | IA revisa o desenho |
| 8 | Análise dos dados | Estatística e viés | Análise com limitações | IA audita vieses |
| 9 | IA aplicada ao meio ambiente | ML e visão computacional | Modelo + ficha | Núcleo do curso |
| 10 | Do dado à solução e mostra | Comunicação | Pôster + apresentação | IA ensaia a fala |

### 8.2 Progressão de competências

| Bloco | Encontros | Competência | Evidência |
|---|---|---|---|
| **Fundamentos** | 1–2 | Ler dado e fonte | Ficha de fonte + gráfico |
| **Programação** | 3–4 | Analisar com Python | Notebook comentado |
| **Território** | 5–6 | Ler mapa e série histórica | Mapa + comparação |
| **Método** | 7–8 | Coletar e interpretar | Plano + análise com limite |
| **IA** | 9 | Treinar e avaliar modelo | Modelo + ficha de modelo |
| **Comunicação** | 10 | Propor com evidência | Pôster + apresentação |

### 8.3 Como a IA é ensinada (e não apenas usada)

O curso separa três camadas, para o aluno não confundir "usar chatbot" com "fazer IA":

1. **IA generativa como assistente** (encontros 1–8): o aluno usa chatbot para explicar, revisar e
   organizar — sempre com verificação e registro do prompt.
2. **Machine learning supervisionado** (encontro 9): o aluno treina um modelo simples de
   classificação (ex.: prever risco de foco de calor a partir de variáveis climáticas) e aprende
   a medir acurácia, matriz de confusão e viés.
3. **Visão computacional** (encontro 9): o aluno usa uma ferramenta de treino de imagens
   (Teachable Machine) ou um modelo pré-treinado para classificar imagens de satélite ou do
   pátio da escola, discutindo o que o modelo erra e por quê.

O aluno sai sabendo que **IA não é oráculo**: é um modelo treinado em dados, com erro, viés e
limite — e que a decisão final é humana.

---

## 9. Avaliação e certificação

### 9.1 Princípios

- **Formativa e criterial:** compara o aluno com o critério, não com o colega.
- **Sem prova eliminatória.**
- **Transparente:** o aluno conhece a rubrica antes da tarefa.
- **Múltiplos instrumentos:** entrega, observação, autoavaliação e apresentação.

### 9.2 Composição da nota

| Dimensão | Peso | O que observa |
|---|---|---|
| Processo | 40% | Entregas parciais e participação nas atividades |
| Projeto final | 40% | Qualidade da análise, do mapa e da proposta |
| Apresentação | 20% | Clareza e capacidade de interpretar os dados |

### 9.3 Rubrica resumida (4 níveis)

| Critério | Iniciante | Em desenvolvimento | Proficiente | Avançado |
|---|---|---|---|---|
| Pergunta e problema | Vago | Parcial | Claro | Claro, relevante e delimitado |
| Fonte e dado | Não identifica | Identifica com ajuda | Identifica e cita | Compara fontes e aponta limite |
| Análise | Copia gráfico | Lê o gráfico | Interpreta e relaciona | Explica tendência, erro e viés |
| Mapa | Não produz | Produz com ajuda | Produz com camada | Produz com legenda e crítica |
| IA | Usa sem verificar | Verifica às vezes | Verifica e registra | Documenta modelo e limite |
| Comunicação | Não apresenta | Apresenta com apoio | Apresenta com clareza | Convence e responde perguntas |

Rubrica completa em [`07-AVALIACAO/01-rubrica-avaliacao.md`](07-AVALIACAO/01-rubrica-avaliacao.md).

### 9.4 Certificação

| Critério | Regra |
|---|---|
| Presença | ≥ 8 de 10 encontros (80%) |
| Entrega | Projeto final apresentado na mostra |
| Carga certificada | 20h |
| Recuperação | Quem não atinge o critério recebe plano de 2 semanas e conclui no ciclo seguinte |

O certificado tem código de verificação e pode ser conferido na página pública do projeto.

---

## 10. Acessibilidade, inclusão e proteção de dados

### 10.1 Acessibilidade

- Material com contraste mínimo 4,5:1, fonte mínima 16 px e texto alternativo em imagens.
- Toda atividade tem versão no celular e versão em papel.
- Intérprete de Libras sob demanda (15 dias de antecedência).
- Instruções curtas, uma por vez; pausas programadas.
- Nenhuma atividade exige deslocamento ou aparelho próprio.

### 10.2 Proteção de dados (LGPD e ECA)

| Dado | Para quê | Base legal | Retenção |
|---|---|---|---|
| Nome e apelido | Identificação e certificado | Consentimento / execução | Até 1 ano |
| Idade e faixa | Encaixe e proteção | Consentimento do responsável | Até 1 ano |
| Contato do responsável | Comunicação | Consentimento | Até 1 ano |
| Escola e bairro | Relatório agregado | Consentimento | Agregado, sem nome |
| Presença e entregas | Certificação | Execução do curso | Até 2 anos |
| Imagem e voz | Mostra e divulgação | Consentimento específico e revogável | Até 2 anos |

**Não coletamos:** CPF de menor, endereço completo, foto de documento, diagnóstico médico,
religião, orientação sexual, dados bancários.

**Dados ambientais da escola:** registrados de forma agregada e identificados por código
(ex.: "Escola A", "Ponto 3"), nunca por nome de aluno.

### 10.3 Regras de ouro

- Dois adultos presentes em qualquer atividade com menores.
- Canal oficial de comunicação; nunca conversa privada com aluno.
- Nenhum dado de aluno em repositório público.
- Chaves de API e contas de IA ficam com o professor, nunca no navegador do aluno.
- Uso de IA registrado em ficha simples (prompt, finalidade, verificação).
- Suspeita de risco: acolher, não investigar, registrar e acionar a coordenação no mesmo dia.

---

## 11. O que a Secretaria recebe

| Entrega | Descrição | Quando |
|---|---|---|
| **Curso completo** | 10 planos de aula, notebooks, dados, rubricas e certificados | Antes da 1ª aula |
| **Turma formada** | 20 a 30 jovens com competência em dados ambientais | Ao fim do ciclo |
| **Mostra pública** | Apresentação dos projetos à comunidade e à imprensa local | Encontro 10 |
| **Relatório agregado** | Diagnósticos do território produzidos pelos alunos, sem dados pessoais | Até 30 dias após a mostra |
| **Banco de projetos** | Pôsteres e notebooks publicados no GitHub Pages | Contínuo |
| **Material reaplicável** | Todo o kit aberto para a rede municipal usar de novo | Imediato |
| **Formação de professores** | Professores da rede podem participar como observadores | Durante o curso |
| **Indicadores** | Presença, conclusão, satisfação e projetos publicados | Mensal |

### 11.1 Como os dados dos alunos ajudam a gestão municipal

- Mapa de pontos de descarte irregular, áreas verdes e temperatura do pátio.
- Série de consumo de água e energia da escola.
- Diagnóstico de percepção ambiental do bairro.
- Comparação entre dados locais e dados de satélite (INPE/MapBiomas).
- Subsídio para ações de educação ambiental, arborização, drenagem e resíduos.

---

## 12. O que pedimos à Secretaria

| Pedido | Por quê | Custo |
|---|---|---|
| **Apoio institucional** | Divulgação nas escolas e legitimidade do curso | R$ 0 |
| **Espaço com internet** (ou laboratório) | Aulas presenciais ou híbridas | R$ 0 (cedido) |
| **Divulgação** | Cartaz, redes da Prefeitura e escolas | R$ 0 a R$ 500 |
| **Indicação de 1 ponto focal** | Articulação com escolas e comunidade | R$ 0 |
| **Dados municipais agregados** (opcional) | Enriquecer os projetos com dados locais | R$ 0 |
| **Certificação institucional** (opcional) | Assinatura conjunta do certificado | R$ 0 |
| **Coffee break e impressão da mostra** (opcional) | Conforto e registro do evento | R$ 0 a R$ 3.000 |

**Não pedimos:** pagamento de professor, compra de software, licença de plataforma ou
mensalidade do aluno. O curso funciona com R$ 0; o cenário com custo melhora a experiência, não
a viabiliza.

---

## 13. Indicadores e monitoramento

| Indicador | Fórmula | Meta | Frequência |
|---|---|---|---|
| Alunos atendidos | matrículas confirmadas | 20–30 | por turma |
| Taxa de conclusão | concluintes / matriculados | ≥ 80% | por turma |
| Presença média | presenças / aulas × alunos | ≥ 80% | semanal |
| Satisfação do aluno | nota 1–5 | ≥ 4,5 | ao fim |
| Projetos apresentados | projetos na mostra | ≥ 6 | por turma |
| Projetos publicados | no ar 30 dias depois | ≥ 60% | por turma |
| Equidade de gênero | meninas / total | ≥ 50% | por turma |
| Inclusão de renda | CadÚnico / total | ≥ 30% | por turma |
| Entrega de relatório | relatório à Secretaria | 100% | por turma |
| Incidentes de dados | confirmados | 0 | contínuo |

Monitoramento: planilha única de presença (acesso restrito), formulário de 5 linhas por aula e
relatório mensal de 1 página para a Secretaria.

---

## 14. Riscos e plano de contingência

| Risco | Probabilidade | Impacto | Prevenção | Resposta |
|---|---|---|---|---|
| Internet do aluno cai | alta | médio | material em PDF e atividade no papel | tarefa por WhatsApp + notebook compartilhado |
| Laboratório indisponível | média | alto | versão híbrida e celular | aula na sala comum com planilha |
| Evasão por trabalho | média | alto | horário no contraturno e gravação | mensagem de retomada + reposição |
| Aluno sem aparelho | alta | médio | duplas e empréstimo | kit impresso + biblioteca/escola |
| Incidente com menor | baixa | muito alto | dois adultos e canal oficial | protocolo e acionamento da coordenação |
| Vazamento de dados | baixa | alto | minimização e acesso restrito | conter, registrar e avaliar comunicação à ANPD |
| Uso indevido de IA | média | médio | regras e ficha de registro | revisão humana obrigatória |
| Calendário escolar conflita | média | médio | planejar com a Secretaria | aula gravada + reposição |

---

## 15. Cronograma de implantação

| Período | Ação |
|---|---|
| **Mês -2** | Apresentação à Secretaria; definição de espaço, horário e ponto focal |
| **Mês -1** | Divulgação nas escolas; inscrições; formação do professor e do monitor |
| **Semana 0** | Acolhimento, teste técnico e contrato de convivência |
| **Semanas 1–9** | Encontros 1 a 9 (1 por semana, 2h) |
| **Semana 10** | Mostra pública, feedback e certificação |
| **Até 30 dias depois** | Relatório agregado à Secretaria e publicação dos projetos |
| **Ciclo seguinte** | Oferta de nova turma e formação de professores da rede |

---

## 16. Orçamento

### 16.1 Cenário de custo zero (viável)

| Item | Custo | Como |
|---|---|---|
| Plataforma | R$ 0 | Google Colab e Google Sheets |
| Material didático | R$ 0 | kit aberto já pronto |
| Ferramentas | R$ 0 | Python, Folium, scikit-learn, MapBiomas |
| Espaço e internet | R$ 0 | cedidos pela escola/Secretaria |
| Equipe | R$ 0 | voluntariado e cedência |
| Divulgação | R$ 0 | escolas, redes da Prefeitura e boca a boca |
| **Total** | **R$ 0** | |

### 16.2 Cenário com qualidade (recomendado)

| Item | Quantidade | Custo unitário | Total |
|---|---|---|---|
| Impressão de fichas e pôsteres | 30 kits | R$ 10 | R$ 300 |
| Certificados impressos (opcional) | 30 | R$ 4 | R$ 120 |
| Coffee break da mostra | 1 evento | R$ 400 | R$ 400 |
| Divulgação impressa | 1 lote | R$ 500 | R$ 500 |
| Reserva para imprevisto | — | — | R$ 300 |
| **Total** | | | **R$ 1.620** |

> O curso funciona com R$ 0. O cenário de R$ 1.620 melhora conforto e alcance, não viabiliza — e
> pode ser coberto por parceria, edital ou doação.

---

## 17. Sustentabilidade e continuidade

- **Material aberto:** qualquer escola da rede pode reaplicar o curso sem custo.
- **Formação de professores:** docentes da rede participam como observadores e podem conduzir a
  turma seguinte.
- **Banco de projetos:** os notebooks e pôsteres ficam publicados e servem de exemplo.
- **Parceria com a Secretaria:** os diagnósticos alimentam ações de educação ambiental.
- **Continuidade:** alunos formados podem atuar como monitores no ciclo seguinte.
- **Diversificação:** editais de educação digital e meio ambiente, universidades e empresas
  locais podem apoiar o cenário com qualidade.

---

## 18. Referências

### 18.1 Legislação e normas

- BRASIL. **Lei 9.795/1999** — Política Nacional de Educação Ambiental.
- BRASIL. **Lei 9.394/1996** — Diretrizes e Bases da Educação Nacional.
- BRASIL. **Lei 13.709/2018** — Lei Geral de Proteção de Dados Pessoais.
- BRASIL. **Lei 8.069/1990** — Estatuto da Criança e do Adolescente.
- BRASIL. **Lei 12.965/2014** — Marco Civil da Internet.
- BRASIL. **Lei 14.533/2023** — Política Nacional de Educação Digital.
- BRASIL. **Lei 13.146/2015** — Lei Brasileira de Inclusão.
- BRASIL. **BNCC** — Base Nacional Comum Curricular (2018).
- CNE. **Resolução CNE/CEB 1/2022** — Computação na educação básica.
- UNESCO. **Recommendation on the Ethics of Artificial Intelligence** (2021).

### 18.2 Referenciais pedagógicos e científicos

- BYBEE, R. W. et al. *The BSCS 5E Instructional Model: Origins and Effectiveness*. BSCS, 2006.
- FREEMAN, S. et al. Active learning increases student performance in science, engineering, and
  mathematics. *PNAS*, v. 111, n. 23, p. 8410–8415, 2014.
- KARPICKE, J. D.; ROEDIGER, H. L. The critical importance of retrieval for learning.
  *Science*, v. 319, n. 5865, p. 966–968, 2008.
- KARPICKE, J. D. Retrieval-based learning: Active retrieval promotes meaningful learning.
  *Current Directions in Psychological Science*, v. 21, n. 3, p. 157–163, 2012.
- KOLB, D. A. *Experiential Learning*. Prentice-Hall, 1984.
- PAPERT, S. *Mindstorms: Children, Computers, and Powerful Ideas*. Basic Books, 1980.
- RESNICK, M. *Lifelong Kindergarten*. MIT Press, 2017.
- VYGOTSKY, L. S. *Mind in Society*. Harvard University Press, 1978.
- WIGGINS, G.; McTIGHE, J. *Understanding by Design*. 2. ed. ASCD, 2005.
- BLAKESLEE, S. The CRAAP test. *LOEX Quarterly*, v. 31, n. 3, p. 6–7, 2004.
- WINEBURG, S.; McGREW, S. Lateral reading and the nature of expertise. *Teachers College
  Record*, v. 121, n. 11, p. 1–40, 2019.
- D'IGNAZIO, C.; KLEIN, L. F. *Data Feminism*. MIT Press, 2020.
- O'NEIL, C. *Weapons of Math Destruction*. Crown, 2016.

### 18.3 Dados, meio ambiente e IA

- IPCC. *Sixth Assessment Report (AR6)*. 2021–2023.
- REICHSTEIN, M. et al. Deep learning and process understanding for data-driven Earth system
  science. *Nature*, v. 566, p. 195–204, 2019.
- ROLNICK, D. et al. Tackling Climate Change with Machine Learning. *ACM Computing Surveys*,
  v. 55, n. 2, p. 1–96, 2022.
- ZHU, X. X. et al. Deep learning in remote sensing: A comprehensive review and list of
  resources. *IEEE Geoscience and Remote Sensing Magazine*, v. 5, n. 4, p. 8–36, 2017.
- GORELICK, N. et al. Google Earth Engine: Planetary-scale geospatial analysis for everyone.
  *Remote Sensing of Environment*, v. 202, p. 18–27, 2017.
- HANSEN, M. C. et al. High-resolution global maps of 21st-century forest cover change.
  *Science*, v. 342, n. 6160, p. 850–853, 2013.
- MITCHELL, M. et al. Model Cards for Model Reporting. *FAT* '19*, 2019.
- GEBRU, T. et al. Datasheets for Datasets. *Communications of the ACM*, v. 64, n. 12,
  p. 86–92, 2021.
- MAPBIOMAS. *Plataforma MapBiomas* — https://plataforma.mapbiomas.org/
- INPE. *PRODES, DETER e Queimadas* — https://terrabrasilis.dpi.inpe.br/
- INMET. *Portal de dados meteorológicos* — https://portal.inmet.gov.br/
- ANA. *Sistema Nacional de Informações sobre Recursos Hídricos* — https://www.snirh.gov.br/

A bibliografia completa e comentada está em
[`09-REFERENCIAS/01-referencias-cientificas.md`](09-REFERENCIAS/01-referencias-cientificas.md).
