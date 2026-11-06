# Encontro 5 — Mapas e território

**Duração:** 2h · **Fase do projeto:** leitura espacial do problema
**Entregável:** mapa interativo do município com uma camada de dados
**Notebook:** `05-NOTEBOOKS-COLAB/02-mapas-e-territorio.ipynb`

---

## 1. Objetivo

Ao final, o grupo é capaz de localizar o município em um mapa, criar um mapa interativo com
Folium e sobrepor uma camada de dados (pontos ou áreas), explicando o que a camada representa.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **Coordenada** | Par latitude/longitude que localiza um ponto |
| **Ponto** | Local exato (escola, nascente, foco de calor) |
| **Área** | Região delimitada (bairro, fazenda, unidade de conservação) |
| **Camada** | Conjunto de dados desenhado sobre o mapa |
| **Mapa temático** | Mapa que mostra um fenômeno, não só ruas |
| **Escala** | Relação entre o mapa e o território real |

---

## 3. Materiais

- Notebook 02 no Colab.
- Acesso à MapBiomas Plataforma e ao Google Earth (opcional).
- Projetor.
- Mapa impresso do município (plano B offline).

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre CSV, pandas e gráfico.
2. Mostrar duas imagens do mesmo bairro em anos diferentes (Google Earth) e perguntar: "o que
   mudou? como provar?"
3. Objetivo: "colocar o problema no mapa e sobrepor dados".

### Fase 2 — Explorar (20 min)

1. Abrir o Google Maps e localizar a escola; ler latitude e longitude.
2. Abrir a MapBiomas Plataforma e mostrar a camada de uso do solo no município.
3. Perguntar: "que cor representa o quê? qual é o ano? quem produziu esse mapa?"
4. Comparar a área verde em dois anos diferentes.

### Fase 3 — Explicar (15 min)

1. Latitude e longitude: o que são e como ler.
2. `folium.Map()` e `folium.Marker()`.
3. Camadas: pontos, círculos, heatmap.
4. Título, legenda e fonte: um mapa sem legenda não é evidência.
5. Limitação: o mapa mostra o que foi mapeado, não tudo o que existe.

### Fase 4 — Aplicar (60 min)

1. **Criar o mapa base** (10 min) centrado no município.
2. **Adicionar pontos** (20 min): escola, pontos de coleta, focos de calor ou nascentes.
3. **Adicionar uma camada** (15 min): círculos proporcionais ou imagem do MapBiomas.
4. **Escrever a legenda** (10 min): o que cada ponto/cor significa e qual a fonte.
5. **Interpretar** (5 min): o que o mapa revela que a tabela não revelava?

### Fase 5 — Avaliar (15 min)

1. Dois grupos abrem o mapa e explicam a camada.
2. A turma confere: tem legenda? tem fonte? o ponto está no lugar certo?
3. Tarefa da semana: adicionar mais dois pontos ao mapa com foto ou medição.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA para interpretar o mapa, não para gerar coordenadas.

**Prompt sugerido:**

> "Tenho um mapa do município de [nome] com pontos de [tipo de dado] e uma camada de [uso do
> solo/cobertura vegetal] do MapBiomas de [ano]. Quais perguntas eu deveria fazer para
> interpretar esse mapa? Liste 5 perguntas e 3 limitações. Não invente localizações."

**Verificação obrigatória:**

- Confirmar cada coordenada no Google Maps.
- Confirmar a fonte e o ano da camada no site do MapBiomas.
- Registrar: "o que a IA perguntou / o que eu respondi com o mapa".

**Alerta:** a IA pode sugerir coordenadas erradas. Toda coordenada vem de fonte verificável.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Comparar imagens de anos diferentes | Hansen et al. (2013) | Mudança de cobertura é visual e mensurável |
| Mapa temático com legenda | Bertin (1967) | Comunicação cartográfica exige legenda e escala |
| Dados de uso do solo | MapBiomas | Fonte aberta e metodologia pública |
| IA para perguntar, não para localizar | UNESCO (2021) | Verificação humana obrigatória |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Mapa | Não abriu | Mapa base | Com pontos | Com pontos e camada |
| Legenda | Ausente | Parcial | Completa | Completa com fonte |
| Interpretação | Não explica | Descreve | Relaciona com o problema | Aponta limitação e nova pergunta |

---

## 8. Acessibilidade e diferenciação

- Mapa impresso para quem não tem computador.
- Dupla com papéis: quem programa e quem confere as coordenadas.
- Quem termina antes cria um mapa de calor com os pontos.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Latitude e longitude invertidas | Mostrar o exemplo do Google Maps |
| Mapa em branco | Conferir se o notebook rodou a célula do mapa |
| Camada sem fonte | Pedir o link e o ano |
| Ponto fora do município | Comparar com o mapa oficial |

---

## 10. Para o professor

- Teste o Folium no Colab antes da aula (ele funciona sem chave de API).
- Tenha um arquivo com coordenadas da escola e de dois pontos próximos.
- Se a internet cair, use o mapa impresso e peça a legenda no papel.
