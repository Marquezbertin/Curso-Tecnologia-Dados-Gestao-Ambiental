"""
Conteúdo Didático - Apêndices:
- Apêndice A: Glossário Didático Integrado de Tecnologia e Meio Ambiente para Leigos
- Apêndice B: Guia Rápido de Consulta de Comandos Python, Pandas e Folium
- Apêndice C: Resolução Comentada dos Exercícios e Desafios Práticos dos Notebooks
"""

from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether, Image, HRFlowable, Table, TableStyle
from reportlab.lib import colors
from estilos_apostila import criar_box, criar_tabela_codigo, criar_tabela_geral

def obter_apendices(styles):
    story = []
    
    # -------------------------------------------------------------------------
    # APÊNDICE A: GLOSSÁRIO DIDÁTICO
    # -------------------------------------------------------------------------
    story.append(Paragraph("Apêndice A — Glossário Didático Integrado", styles['ModTitle']))
    story.append(Paragraph("<i>Termos fundamentais de tecnologia, ciência de dados e gestão ambiental explicados sem jargões</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    glossario = [
        ("Acurácia", "Proporção de acertos gerais de um modelo de inteligência artificial. Cuidado: pode enganar quando a maioria dos dados pertence a uma única classe."),
        ("Algoritmo", "Sequência finita e ordenada de instruções lógicas que um computador segue para resolver um problema ou realizar um cálculo."),
        ("ANA (Agência Nacional de Águas)", "Órgão federal brasileiro que regula o uso de recursos hídricos e monitora a vazão e a qualidade das bacias hidrográficas nacionais."),
        ("Aprendizado Supervisionado", "Método de inteligência artificial em que o algoritmo aprende analisando dados históricos que já possuem a resposta correta (rótulo)."),
        ("Árvore de Decisão", "Modelo de aprendizado de máquina visual e interpretável que classifica eventos criando uma sequência de perguntas 'SE... ENTÃO'."),
        ("BDQueimadas", "Banco de dados aberto operado pelo INPE que registra diariamente focos de calor detectados por satélites em toda a América do Sul."),
        ("Ciência Cidadã", "Prática científica colaborativa em que estudantes, professores e membros da comunidade participam ativamente da coleta e análise de dados."),
        ("CSV (Comma-Separated Values)", "Formato de arquivo aberto e leve que guarda tabelas de dados como linhas de texto separadas por vírgulas ou pontos e vírgulas."),
        ("DataFrame", "Estrutura do Pandas que armazena uma tabela completa na memória do computador, com linhas indexadas e colunas nomeadas."),
        ("Desmatamento por Corte Raso", "Remoção total e definitiva da cobertura florestal nativa de uma área, convertendo-a em pasto, agricultura ou solo exposto."),
        ("Desvio Padrão", "Medida estatística que indica o quanto os dados se afastam da média. Um desvio alto indica muita instabilidade ou oscilação."),
        ("DETER (INPE)", "Sistema de detecção de desmatamento em tempo quase real do INPE, criado para disparar alertas emergenciais de fiscalização ao IBAMA."),
        ("Falso Negativo (FN)", "Erro em que o modelo afirma que a situação está segura quando, na verdade, ocorreu um evento perigoso (ex: não detectar um fogo real)."),
        ("Falso Positivo (FP)", "Alarme falso emitido pelo modelo quando não havia nenhum perigo real acontecendo."),
        ("Feature (Atributo / Entrada)", "Cada uma das variáveis informadas a um modelo de IA para que ele tente fazer uma previsão (ex: temperatura, vento)."),
        ("Foco de Calor", "Pixel de aproximadamente 1 km² em que a temperatura de brilho no infravermelho termal do satélite ultrapassou o limiar de fogo."),
        ("Folium", "Biblioteca em Python que transforma coordenadas geográficas em mapas digitais interativos e navegáveis no navegador."),
        ("Google Colab", "Plataforma gratuita na nuvem fornecida pelo Google para executar códigos em Python diretamente pelo navegador sem instalação local."),
        ("INMET", "Instituto Nacional de Meteorologia do Brasil, responsável pela rede oficial de estações meteorológicas automáticas e convencionais."),
        ("INPE", "Instituto Nacional de Pesquisas Espaciais, instituição científica pioneira mundial em monitoramento de biomas por sensoriamento remoto."),
        ("Latitude", "Distância em graus em relação à Linha do Equador (-90° no Polo Sul a +90° no Polo Norte). No Brasil é sempre negativa."),
        ("LGPD", "Lei Geral de Proteção de Dados (Lei nº 13.709/2018), que regulamenta a privacidade e o tratamento ético de dados de pessoas físicas."),
        ("Longitude", "Distância em graus em relação ao Meridiano de Greenwich (-180° a Oeste até +180° a Leste). No Brasil é sempre negativa."),
        ("MapBiomas", "Rede colaborativa de ONGs, universidades e empresas que gera mapas anuais de cobertura e uso do solo brasileiro desde 1985."),
        ("Matplotlib", "Principal biblioteca gráfica do ecossistema Python para desenhar figuras científicas, linhas, barras, histogramas e dispersões."),
        ("Matriz de Confusão", "Tabela cruzada que revela com precisão quantos acertos e quantos erros de cada tipo um modelo de classificação cometeu."),
        ("Mediana", "O valor exato que separa a metade superior da metade inferior de uma série de dados ordenados. É imune a valores atípicos."),
        ("Média Aritmética", "Soma de todos os valores de uma amostra dividida pela contagem de elementos. É facilmente distorcida por extremos."),
        ("Outlier (Valor Atípico)", "Observação numérica que se afasta drasticamente do padrão da maioria, podendo ser uma falha de sensor ou um desastre real."),
        ("Pandas", "Biblioteca em Python essencial para carregar, filtrar, agrupar, limpar e manipular tabelas de dados de alta complexidade."),
        ("PRODES (INPE)", "Programa oficial do INPE que calcula a taxa consolidada anual de desmatamento por corte raso nos biomas brasileiros."),
        ("Sensoriamento Remoto", "Obtenção de dados e medições físicas de objetos e fenômenos na superfície terrestre sem que haja contato direto com eles."),
        ("Série Temporal", "Coleção de observações de uma mesma variável organizadas cronologicamente ao longo do tempo (dias, meses ou anos)."),
        ("Target (Alvo / Rótulo)", "A resposta real que um modelo de aprendizado supervisionado é treinado para prever.")
    ]
    
    tabela_glossario = [
        [Paragraph(f"<b>{termo}</b>", styles['TableCellBold']),
         Paragraph(definic, styles['TableCell'])]
        for termo, definic in glossario
    ]
    t_glo = Table(tabela_glossario, colWidths=[120, 385])
    t_glo.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#eaeded')),
    ]))
    story.append(t_glo)
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # APÊNDICE B: GUIA RÁPIDO DE COMANDOS
    # -------------------------------------------------------------------------
    story.append(Paragraph("Apêndice B — Guia Rápido de Comandos Python e Pandas", styles['ModTitle']))
    story.append(Paragraph("<i>Tabela prática de consulta para uso rápido durante aulas e análises de laboratório</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    comandos_rapidos = [
        ["Comando em Python", "O que faz no computador?", "Exemplo de Sintaxe Prática"],
        ["sum(lista)", "Calcula a soma de todos os números contidos na lista.", "total = sum(chuvas)"],
        ["len(objeto)", "Conta a quantidade de elementos de uma lista ou linhas de tabela.", "dias = len(chuvas)"],
        ["max(lista) / min(lista)", "Encontra o maior e o menor valor de uma sequência numérica.", "pico = max(temperaturas)"],
        ["pd.read_csv('arquivo.csv')", "Lê uma planilha em formato CSV e cria um DataFrame na memória.", "df = pd.read_csv('inmet.csv')"],
        ["df.head()", "Exibe as 5 primeiras linhas da tabela para inspeção visual rápida.", "df.head()"],
        ["df.info()", "Mostra nomes das colunas, total de linhas e se há valores nulos.", "df.info()"],
        ["df.describe()", "Gera tabela com média, desvio padrão, mínimo e máximo das colunas.", "df.describe()"],
        ["df.dropna()", "Descarta todas as linhas que contenham algum dado em branco.", "df_limpo = df.dropna()"],
        ["pd.to_datetime(coluna)", "Converte textos de datas em objetos cronológicos reconhecidos.", "df['data'] = pd.to_datetime(df['data'])"],
        ["df[df['col'] > valor]", "Filtra e retorna apenas as linhas que satisfazem a condição.", "criticos = df[df['temp'] >= 35]"],
        ["plt.plot(x, y)", "Desenha um gráfico de linhas conectando os pontos X e Y.", "plt.plot(df['data'], df['temp'])"],
        ["plt.bar(x, y)", "Desenha um gráfico de barras verticais para comparar volumes.", "plt.bar(df['data'], df['chuva'])"],
        ["folium.Map(location=[lat,lon])", "Desenha o mapa interativo centrado nas coordenadas informadas.", "mapa = folium.Map([-22.5, -47.9])"],
        ["folium.Marker([lat,lon]).add_to(m)", "Adiciona um alfinete de localização georreferenciado ao mapa.", "folium.Marker([lat, lon]).add_to(mapa)"],
        ["train_test_split(X, y)", "Sorteia e divide dados em treino e teste com porcentagem definida.", "X_tr, X_te, y_tr, y_te = train_test_split(X, y)"],
        ["modelo.fit(X_treino, y_treino)", "Treina o algoritmo descobrindo os padrões históricos nos dados.", "modelo.fit(X_tr, y_tr)"],
        ["modelo.predict(X_teste)", "Gera previsões para novos dados com base no aprendizado anterior.", "previsoes = modelo.predict(X_te)"]
    ]
    story.append(criar_tabela_geral(comandos_rapidos[0], comandos_rapidos[1:], [135, 185, 185], styles))
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # APÊNDICE C: RESOLUÇÃO COMENTADA DOS EXERCÍCIOS
    # -------------------------------------------------------------------------
    story.append(Paragraph("Apêndice C — Resolução Comentada dos Exercícios", styles['ModTitle']))
    story.append(Paragraph("<i>Gabarito pedagógico detalhado passo a passo das atividades práticas dos notebooks</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph("C.1 Resolução do Exercício 1: Análise de Extremos Climáticos (Notebook 01)", styles['SecTitle']))
    story.append(Paragraph(
        "<b>Enunciado:</b> <i>'Usando a base meteorológica do INMET, filtre os dias em que a temperatura máxima ultrapassou 32°C "
        "e simultaneamente não houve chuva (chuva == 0). Calcule quantos dias críticos foram identificados.'</i>",
        styles['Normal']
    ))
    
    res_ex1 = [
        ("# 1. Aplicação do filtro duplo com operador lógico E (&)\n"
         "condicao_calor = df['temp_max_c'] > 32\n"
         "condicao_seca = df['chuva_mm'] == 0\n"
         "dias_criticos = df[condicao_calor & condicao_seca]\n"
         "\n"
         "# 2. Contagem de ocorrências\n"
         "total_dias = len(dias_criticos)\n"
         "print(f'Total de dias sob risco extremo de estiagem e calor: {total_dias}')",
         "O código cria duas regras lógicas separadas e as combina com o operador '&'. "
         "Em seguida, usa a função len() para contar quantas linhas atenderam a ambos os critérios simultâneos. "
         "Isso permite ao comitê de bacia prever momentos de pico de evaporação e estresse hídrico.")
    ]
    story.append(criar_tabela_codigo(res_ex1, styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("C.2 Resolução do Exercício 2: Mapeamento de Focos Próximos a APAs (Notebook 02)", styles['SecTitle']))
    story.append(Paragraph(
        "<b>Enunciado:</b> <i>'Crie uma camada no mapa Folium com marcadores na cor laranja representando denúncias de descarte de entulho "
        "e adicione um círculo de raio 50 metros ao redor da escola para visualizar a área de influência direta.'</i>",
        styles['Normal']
    ))
    
    res_ex2 = [
        ("# 1. Camada de descarte e círculo escolar\n"
         "camada_descarte = folium.FeatureGroup(name='Pontos de Descarte')\n"
         "folium.Marker([-22.555, -47.905], popup='Entulho na calçada', icon=folium.Icon(color='orange')).add_to(camada_descarte)\n"
         "folium.Circle([-22.550, -47.900], radius=50, color='blue', fill=True, fill_opacity=0.2, popup='Raio Escolar 50m').add_to(mapa)\n"
         "camada_descarte.add_to(mapa)\n"
         "folium.LayerControl().add_to(mapa)",
         "Cria um FeatureGroup próprio para as denúncias com ícone laranja de alerta. "
         "O Circle recebe o raio em metros reais na escala cartográfica, com preenchimento semitransparente (opacity=0.2) "
         "para não tapar as ruas debaixo do mapa.")
    ]
    story.append(criar_tabela_codigo(res_ex2, styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("C.3 Resolução do Exercício 3: Ajuste de Profundidade da Árvore de Decisão (Notebook 03)", styles['SecTitle']))
    story.append(Paragraph(
        "<b>Enunciado:</b> <i>'O que acontece com o modelo de Machine Learning se aumentarmos max_depth para 10? E se reduzirmos para 1? "
        "Qual é a profundidade mais recomendada para um relatório da Secretaria de Meio Ambiente?'</i>",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>Explicação Pedagógica:</b><br/>"
        "• <b>Com max_depth=1 (Subajuste / Underfitting):</b> A árvore faz apenas uma pergunta simples (ex: 'Choveu?'). "
        "O modelo fica excessivamente simplório e não consegue capturar a influência conjunta da temperatura e do vento.<br/>"
        "• <b>Com max_depth=10 (Superajuste / Overfitting):</b> A árvore cria dezenas de ramificações microscópicas, praticamente decorando cada linha da tabela de treino. "
        "Quando colocada para prever dados do próximo ano, ela cometerá erros grotescos porque aprendeu o ruído em vez da tendência física.<br/>"
        "• <b>Profundidade Recomendada (max_depth entre 3 e 4):</b> É o 'ponto de ouro'. Gera entre 4 e 8 regras claras, fáceis de imprimir em um relatório para a Defesa Civil "
        "e mantém excelente capacidade de generalizar em novos eventos climáticos.",
        styles['Normal']
    ))
    
    return story

print("Módulo de apêndices didáticos compilado com sucesso.")
