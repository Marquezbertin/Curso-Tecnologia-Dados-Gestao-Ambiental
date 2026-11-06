"""
Conteúdo Didático Parte 1:
- Capa e Apresentação Institucional
- Sumário Geral
- Módulo 1: O Papel dos Dados na Gestão Ambiental
- Módulo 2: Do Caos à Clareza — Organização e Planilhas Ambientais
- Módulo 3: Python sem Medo (Parte 1: Fundamentos para Leigos)
"""

from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether, Image, HRFlowable, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
import os
from estilos_apostila import criar_box, criar_tabela_codigo, criar_tabela_geral

def obter_capa_e_abertura(styles, img_dir):
    story = []
    
    # Espaçamento de topo
    story.append(Spacer(1, 40))
    
    # Tarja superior
    story.append(Paragraph("<b>MINICURSO LIVRE E GRATUITO · MATERIAL DIDÁTICO OFICIAL</b>", ParagraphStyle(
        'CoverHeader', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=colors.HexColor('#27ae60'), alignment=1
    )))
    story.append(Spacer(1, 15))
    
    # Título Principal
    story.append(Paragraph("Tecnologia, Dados e Inteligência Artificial<br/>na Gestão Ambiental", styles['CoverTitle']))
    
    # Subtítulo Didático
    story.append(Paragraph(
        "Um Guia Prático, Passo a Passo e Descomplicado para Leigos:<br/>"
        "Investigando o Território, Decodificando Códigos e Tomando Decisões Baseadas em Evidências",
        styles['CoverSubtitle']
    ))
    story.append(Spacer(1, 20))
    
    # Linha elegante
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor('#145a32'), spaceBefore=5, spaceAfter=25))
    
    # Caixa de Destaque da Metodologia
    resumo_texto = [
        "<b>Para quem é este material?</b> Esta apostila foi desenhada especificamente para pessoas que <b>nunca programaram</b> e que desejam entender como computadores, dados abertos e inteligência artificial podem proteger rios, florestas e cidades.",
        "<b>Filosofia Didática:</b> Você não precisa ser um programador profissional para usar a tecnologia a favor do meio ambiente. O objetivo central é compreender <b>o que cada instrução está fazendo</b>, transformar números brutos em argumentos científicos sólidos e evitar decisões ambientais baseadas em achismos ou desinformação.",
        "<b>Pilares do Curso:</b> Dados Públicos Oficiais (INMET, INPE, MapBiomas) ➔ Processamento Acessível em Nuvem (Google Colab & Python) ➔ Cartografia Digital (Mapas Folium) ➔ Inteligência Artificial Auditável ➔ Soluções para Políticas Públicas."
    ]
    story.append(criar_box("BEM-VINDO À JORNADA DOS DADOS AMBIENTAIS", resumo_texto, tipo="didatico", styles=styles))
    story.append(Spacer(1, 40))
    
    # Metadados de Publicação
    story.append(Paragraph("<b>Desenvolvimento Pedagógico & Científico:</b> Projeto Tecnologia e Gestão Ambiental", styles['CoverMeta']))
    story.append(Paragraph("<b>Compatibilidade:</b> Google Colab, Python 3, Pandas, Matplotlib, Folium e Scikit-Learn", styles['CoverMeta']))
    story.append(Paragraph("<b>Licenciamento Aberto:</b> Creative Commons Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional (CC BY-NC-SA 4.0)", styles['CoverMeta']))
    story.append(Paragraph("<b>Repositório Oficial:</b> github.com/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental", styles['CoverMeta']))
    
    story.append(PageBreak())
    
    # -------------------------------------------------------------------------
    # SUMÁRIO GERAL DA APOSTILA
    # -------------------------------------------------------------------------
    story.append(Paragraph("Sumário Geral da Apostila", styles['ModTitle']))
    story.append(Paragraph("<i>Uma visão panorâmica do percurso formativo em 10 módulos integrados</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1b4f72'), spaceBefore=4, spaceAfter=14))
    
    modulos_sumario = [
        ("Módulo 1", "O Papel dos Dados na Gestão Ambiental Moderna: Da Opinião à Evidência", "Fundamentos de dados, formulação de perguntas territoriais e portais abertos."),
        ("Módulo 2", "Do Caos à Clareza: Organização de Dados Ambientais em Planilhas", "Estrutura tabular, séries temporais, sazonalidade, médias e outliers."),
        ("Módulo 3", "Python sem Medo (Parte 1): Primeiros Passos na Programação para Leigos", "Google Colab, variáveis, tipos de dados, listas e anatomia dos erros."),
        ("Módulo 4", "Python sem Medo (Parte 2): Análise e Gráficos com Pandas e Matplotlib", "DataFrames, leitura de CSV, filtros ambientais e construção de gráficos."),
        ("Módulo 5", "Geotecnologias e Cartografia Digital: Mapeando o Território com Folium", "Coordenadas geográficas, camadas SIG, pontos críticos e mapas interativos."),
        ("Módulo 6", "Monitoramento por Satélite: Focos de Calor, Queimadas e Desmatamento", "Sensoriamento remoto, INPE/BDQueimadas, PRODES vs DETER e vieses de nuvem."),
        ("Módulo 7", "Ciência Cidadã e Coleta de Dados de Campo na Escola e Comunidade", "Desenho amostral, instrumentos de baixo custo, protocolos éticos e LGPD."),
        ("Módulo 8", "Tratamento Estatístico e Análise Crítica dos Dados Coletados", "Saneamento de dados imperfeitos, média vs mediana, dispersão e limitações."),
        ("Módulo 9", "Inteligência Artificial e Aprendizado de Máquina na Gestão Ambiental", "IA preditiva vs generativa, Árvores de Decisão, matriz de confusão e ética."),
        ("Módulo 10", "Do Dado à Solução: Storytelling, Políticas Públicas e Mostra Científica", "Construção de narrativas com dados, elaboração de pôster e pitch executivo."),
        ("Apêndice A", "Glossário Didático Integrado de Tecnologia e Meio Ambiente", "Mais de 40 termos técnicos explicados em linguagem simples e acessível."),
        ("Apêndice B", "Guia de Consulta Rápida de Comandos Python, Pandas e Folium", "Tabela sintética de instruções para consulta rápida em aula e laboratório."),
        ("Apêndice C", "Caderno de Resolução Comentada de Exercícios e Desafios", "Gabarito detalhado passo a passo de todas as atividades práticas propostas.")
    ]
    
    tabela_sumario_dados = [
        [Paragraph(f"<b>{m[0]}</b>", styles['TableCellBold']),
         Paragraph(f"<b>{m[1]}</b><br/><font color='#555555'>{m[2]}</font>", styles['TableCell'])]
        for m in modulos_sumario
    ]
    t_sumario = Table(tabela_sumario_dados, colWidths=[80, 425])
    t_sumario.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#eaeded')),
    ]))
    story.append(t_sumario)
    story.append(Spacer(1, 15))
    
    story.append(criar_box(
        "COMO APROVEITAR ESTE MATERIAL AO MÁXIMO",
        ["Leia o texto no seu próprio ritmo. Sempre que encontrar um bloco de código, <b>não tente decorá-lo</b>.",
         "Consulte as caixas verdes e azuis: elas traduzem exatamente o que cada linha de código está mandando o computador fazer.",
         "A tecnologia aqui é apenas um meio; o objetivo final é entender e transformar a realidade ambiental da sua comunidade."],
        tipo="ambiental",
        styles=styles
    ))
    
    story.append(PageBreak())
    return story

def obter_modulo_1(styles):
    story = []
    story.append(Paragraph("Módulo 1 — O Papel dos Dados na Gestão Ambiental", styles['ModTitle']))
    story.append(Paragraph("<i>Como transformar incômodos locais em investigações científicas fundamentadas</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Durante décadas, os debates e as decisões sobre preservação ambiental no Brasil foram conduzidos com base em impressões genéricas, "
        "intuições ou discursos polarizados. Frases como <i>'parece que está fazendo mais calor este ano'</i> ou <i>'antigamente chovia muito mais'</i> "
        "fazem parte do senso comum, mas não têm peso suficiente para orientar a construção de uma política pública municipal, "
        "uma drenagem urbana eficiente ou a mobilização de brigadistas contra incêndios florestais. Para agir com precisão, precisamos de <b>evidências</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("1.1 A Escada do Conhecimento: Dado, Informação e Evidência", styles['SecTitle']))
    story.append(Paragraph(
        "Para quem está começando na área técnica ou ambiental, esses três termos parecem sinônimos, mas representam etapas completamente diferentes:",
        styles['Normal']
    ))
    
    dados_escada = [
        ["Nível", "Conceito Chave", "Exemplo no Cotidiano", "Papel na Gestão"],
        ["1. Dado", "Registro bruto de uma medição física ou observação sem contexto.", "'85 mm'", "Inútil isoladamente. Não sabemos se é muito ou pouco."],
        ["2. Informação", "O dado processado, organizado e contextualizado em tempo e espaço.", "'85 mm de chuva em 24h em Campinas no mês de março.'", "Permite comparar com a média histórica e notar anomalias."],
        ["3. Evidência", "A informação associada a uma hipótese causal para orientar uma decisão.", "'85 mm em 24h ultrapassou a calha do córrego e inundou o bairro, exigindo obras de bacias de retenção.'", "Fundamenta decretos de emergência, verbas e fiscalização."]
    ]
    story.append(criar_tabela_geral(dados_escada[0], dados_escada[1:], [75, 130, 150, 150], styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("1.2 Como Formular uma Pergunta Investigável", styles['SecTitle']))
    story.append(Paragraph(
        "Muitos projetos ambientais fracassam logo no início porque começam com perguntas genéricas demais, como <i>'As queimadas são ruins?'</i> "
        "ou <i>'A água da cidade é poluída?'</i>. Essas perguntas geram respostas óbvias ou impossíveis de medir.",
        styles['Normal']
    ))
    story.append(Paragraph(
        "Uma boa pergunta científica de gestão territorial possui quatro elementos obrigatórios, que compõem o <b>Recorte Investigativo</b>:",
        styles['Normal']
    ))
    
    recortes = [
        "<b>1. Tema Específico:</b> Qual o fenômeno físico ou social? (Ex: focos de calor, precipitação, descarte de entulho).",
        "<b>2. Recorte Territorial (Espaço):</b> Onde exatamente? (Ex: no município de Piracicaba, na microbacia do Rio Corumbataí).",
        "<b>3. Recorte Temporal (Tempo):</b> Em qual período? (Ex: entre 2018 e 2024, no mês de setembro dos últimos 5 anos).",
        "<b>4. Variável Mensurável:</b> O que vai ser quantificado? (Ex: número de focos detectados por satélite, temperatura máxima diária)."
    ]
    story.append(criar_box("FÓRMULA DA PERGUNTA INVESTIGÁVEL", recortes, tipo="pratica", styles=styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("1.3 Portais de Dados Abertos Brasileiros", styles['SecTitle']))
    story.append(Paragraph(
        "O Brasil é uma das referências mundiais em transparência e disponibilização pública de dados ambientais e espaciais. "
        "Instituições científicas e agências reguladoras fornecem dados diários gratuitos pela internet. Veja as quatro fontes fundamentais deste curso:",
        styles['Normal']
    ))
    
    portais = [
        ["Instituição", "Portal / Sistema", "O que disponibiliza?", "Formato do Dado"],
        ["INMET", "BDMEP (Banco Meteorológico)", "Temperatura, umidade do ar, vento, radiação e chuvas por estação.", "Planilhas CSV e tabelas diárias"],
        ["INPE", "BDQueimadas & TerraBrasilis", "Focos de calor por satélite, alertas DETER e desmatamento PRODES.", "Tabelas, Shapefiles e GeoJSON"],
        ["MapBiomas", "Plataforma MapBiomas", "Séries anuais de cobertura e uso do solo desde 1985 (vegetação, pasto, urbano).", "Mapas interativos, relatórios e estatísticas"],
        ["ANA", "HidroWeb / SNIRH", "Nível de rios, vazão fluviométrica, qualidade da água e dados de bacias.", "Séries históricas e mapas de bacia"]
    ]
    story.append(criar_tabela_geral(portais[0], portais[1:], [80, 115, 185, 125], styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("1.4 O Método CRAAP: Avaliando a Confiabilidade da Fonte", styles['SecTitle']))
    story.append(Paragraph(
        "Na era da desinformação, receber um arquivo com números não significa que o dado seja confiável. O método CRAAP "
        "(adaptado para ciências ambientais) orienta a checagem crítica antes de iniciar qualquer trabalho:",
        styles['Normal']
    ))
    
    craap_pontos = [
        "<b>C (Corrente / Atualidade):</b> Quando a medição foi realizada? O dado reflete a situação recente ou tem atraso histórico?",
        "<b>R (Relevância):</b> O dado responde diretamente à sua pergunta ou apenas tangencia o problema?",
        "<b>A (Autoridade):</b> Quem é a fonte produtora? É uma agência científica oficial (como INPE ou INMET) ou uma postagem em rede social?",
        "<b>A (Acurácia / Precisão):</b> A metodologia de coleta foi descrita? Há notas técnicas explicando a margem de erro dos sensores?",
        "<b>P (Propósito):</b> O dado foi publicado para divulgação científica neutra ou para defender um interesse comercial/ideológico específico?"
    ]
    story.append(criar_box("CHECKLIST CRAAP DE AUDITORIA DE FONTES", craap_pontos, tipo="alerta", styles=styles))
    
    story.append(PageBreak())
    return story

def obter_modulo_2(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 2 — Do Caos à Clareza: Organização de Dados Ambientais em Planilhas", styles['ModTitle']))
    story.append(Paragraph("<i>Dominando colunas, linhas, séries temporais e valores atípicos (outliers)</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Antes de programar computadores sofisticados ou treinar redes neurais, todo gestor ambiental precisa entender como os dados "
        "se organizam no formato mais simples e universal do mundo: as <b>tabelas</b> (ou planilhas eletrônicas).",
        styles['Normal']
    ))
    
    story.append(Paragraph("2.1 Anatomia da Tabela: Linhas, Colunas e Tipos de Variáveis", styles['SecTitle']))
    story.append(Paragraph(
        "Em um banco de dados ambiental profissional, cada <b>linha</b> representa uma única observação (um dia de medição, um foco de queimada ou uma visita de campo). "
        "Cada <b>coluna</b> representa uma <b>variável</b> específica desse evento.",
        styles['Normal']
    ))
    
    story.append(Paragraph(
        "As variáveis ambientais dividem-se em duas categorias primárias que nunca devem ser confundidas:",
        styles['Normal']
    ))
    
    vars_tipos = [
        ["Categoria", "Subtipo", "O que mede?", "Exemplo Ambiental Prático"],
        ["Numérica (Quantitativa)", "Contínua", "Medições físicas que podem ter casas decimais (números quebrados).", "Temperatura: 28.7 °C; Chuva: 12.4 mm"],
        ["Numérica (Quantitativa)", "Discreta", "Contagens de eventos inteiros (sem números quebrados).", "Número de focos de queimada: 14 focos"],
        ["Categórica (Qualitativa)", "Nominal", "Nomes e classificações sem hierarquia ou ordem.", "Bioma: 'Cerrado', 'Mata Atlântica'; Fonte: 'INMET'"],
        ["Categórica (Qualitativa)", "Ordinal", "Categorias que guardam uma ordem ou graduação lógica.", "Risco de Fogo: 'Baixo' < 'Médio' < 'Crítico'"]
    ]
    story.append(criar_tabela_geral(vars_tipos[0], vars_tipos[1:], [110, 85, 160, 150], styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("2.2 Séries Temporais: Tendência e Sazonalidade", styles['SecTitle']))
    story.append(Paragraph(
        "Uma <b>Série Temporal</b> é uma sucessão de medições ordenadas no tempo (por exemplo, a temperatura aferida dia após dia durante 1 ano). "
        "Ao analisar uma série temporal de dados ambientais, o cientista procura dois padrões fundamentais:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>• Sazonalidade:</b> Flutuações regulares que se repetem em ciclos conhecidos (por exemplo, o inverno no Sudeste brasileiro é sazonalmente mais seco e frio, enquanto o verão concentra chuvas e altas temperaturas).<br/>"
        "<b>• Tendência:</b> A direção de longo prazo da curva após eliminar as variações sazonais (por exemplo, um aumento contínuo de 0,3°C na temperatura média a cada década indica uma tendência de aquecimento).",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2.3 Valores Atípicos (Outliers): Erro de Medição ou Evento Extremo?", styles['SecTitle']))
    story.append(Paragraph(
        "Um <b>Outlier</b> é um valor extraordinariamente afastado de todos os outros da mesma amostra. Na gestão ambiental, a identificação "
        "de um outlier exige cuidado investigativo redobrado. Ele pode significar duas coisas opostas:",
        styles['Normal']
    ))
    
    outlier_box = [
        "<b>Hipótese 1: Falha no Instrumento (Erro Humano ou Técnico):</b> Uma estação meteorológica registra '999 °C' ou '-50 °C' em pleno verão no litoral brasileiro. Trata-se claramente de pane no sensor. Esse dado deve ser descartado (limpeza de dados).",
        "<b>Hipótese 2: Evento Climático Extremo Real:</b> Durante 29 dias de um mês choveu entre 0 e 5 mm por dia. No 30º dia, despencou uma tempestade de 110 mm em 3 horas. O número 110 é um outlier estatístico, mas é um <b>fato real catastrófico</b> que causou enchentes! Eliminá-lo seria mascarar o risco real da cidade."
    ]
    story.append(criar_box("O DILEMA DO OUTLIER AMBIENTAL", outlier_box, tipo="ambiental", styles=styles))
    story.append(Spacer(1, 10))
    
    # Inserção da Figura 1
    caminho_fig1 = os.path.join(img_dir, "grafico1_serie_climatica.png")
    if os.path.exists(caminho_fig1):
        story.append(Image(caminho_fig1, width=470, height=230))
        story.append(Paragraph("Figura 1: Exemplo prático de série temporal com temperatura diária e barras de chuva, destacando um outlier de calor e um evento extremo de chuva.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph(
        "<b>Como ler a Figura 1:</b> Observe que a linha contínua vermelha mapeia a oscilação diária de temperatura (eixo da esquerda). "
        "No dia 15, o termômetro atinge 38.5°C — muito acima da média mensal de 27°C. As barras azuis (eixo da direita) mostram a chuva acumulada. "
        "No dia 23, ocorre um temporal concentrado de 45 mm. Gráficos de eixo duplo permitem correlacionar duas grandezas físicas complementares em uma só visão.",
        styles['Normal']
    ))
    
    story.append(PageBreak())
    return story

def obter_modulo_3(styles):
    story = []
    story.append(Paragraph("Módulo 3 — Python sem Medo (Parte 1: Fundamentos da Programação)", styles['ModTitle']))
    story.append(Paragraph("<i>Perdendo o medo do código e entendendo o que a máquina executa</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Por que aprender a programar se já sabemos mexer em planilhas do Excel? A resposta está em três palavras: "
        "<b>Escala, Automação e Reprodutibilidade</b>. Se você precisar analisar dados meteorológicos diários de 5.570 municípios do Brasil "
        "ao longo de 20 anos, o arquivo terá milhões de linhas — o Excel travará. No Python, a mesma análise roda em poucos segundos.",
        styles['Normal']
    ))
    
    story.append(Paragraph("3.1 O Ambiente Google Colab: Programação Direto no Navegador", styles['SecTitle']))
    story.append(Paragraph(
        "Para programar neste curso, você não precisa instalar nenhum programa pesado, nem configurar placas de vídeo ou sistemas operacionais. "
        "O <b>Google Colaboratory (Colab)</b> roda diretamente na nuvem dentro do Google Chrome ou Firefox. "
        "Ele funciona como um caderno digital dividido em <b>células de texto</b> (para anotações) e <b>células de código</b> (onde o Python roda). "
        "Para executar qualquer célula, basta clicar no botão circular de 'Play' ou pressionar as teclas <code>Shift + Enter</code>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("3.2 Variáveis: As Caixas Etiquetadas da Memória", styles['SecTitle']))
    story.append(Paragraph(
        "Pense em uma variável como uma <b>caixa de papelão com uma etiqueta colada</b>. Quando você escreve <code>temperatura = 31.5</code>, "
        "você está dizendo ao computador: <i>'Crie uma caixa com a etiqueta temperatura e guarde o número 31.5 dentro dela'</i>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("3.3 Listas: Guardando Sequências de Medições", styles['SecTitle']))
    story.append(Paragraph(
        "Em gestão ambiental, raramente lidamos com uma única medição isolada. Quase sempre medimos valores ao longo dos dias. "
        "Para guardar vários números na mesma caixa, usamos uma <b>Lista</b> (delimitada por colchetes <code>[ ]</code> e separada por vírgulas).",
        styles['Normal']
    ))
    
    story.append(Paragraph("3.4 Desconstrução Linha a Linha do Código Inicial", styles['SecTitle']))
    story.append(Paragraph(
        "Abaixo está o primeiro bloco de código do <b>Notebook 01</b>. Veja na tabela a tradução exata de cada comando para o português cotidiano:",
        styles['Normal']
    ))
    
    codigo_nb1 = [
        ("chuvas_semana = [0, 15.2, 3.0, 0, 42.5, 8.1, 0]", "Cria uma lista chamada 'chuvas_semana' com os volumes de chuva medidos de domingo a sábado em milímetros."),
        ("total_chuva = sum(chuvas_semana)", "A função nativa sum() soma todos os valores que estão dentro da lista, resultando em 68.8 mm acumulados."),
        ("quantidade_dias = len(chuvas_semana)", "A função len() (do inglês length, comprimento) conta quantos itens existem dentro da lista. Aqui retorna 7 dias."),
        ("media_diaria = total_chuva / quantidade_dias", "Divide o volume total acumulado pelo número de dias, encontrando a média diária de chuva (9.83 mm/dia)."),
        ("chuva_maxima = max(chuvas_semana)", "A função max() vasculha a lista e encontra a maior precipitação pontual registrada na semana (42.5 mm)."),
        ("print('Total acumulado:', total_chuva)", "A instrução print() envia a mensagem e o valor calculado para a tela para que o gestor possa ler o resultado."),
        ("print('Média por dia:', media_diaria)", "Exibe na tela a média calculada para a tomada de decisão."),
        ("print('Maior temporal:', chuva_maxima)", "Exibe o evento extremo registrado na série.")
    ]
    story.append(criar_tabela_codigo(codigo_nb1, styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("3.5 Perdendo o Medo dos Erros (Traceback)", styles['SecTitle']))
    story.append(Paragraph(
        "Quando você digita algo errado e aperta Play, o Python exibe uma caixa vermelha com letras pretas chamada <b>Traceback</b>. "
        "Para iniciantes, isso parece assustador. Mas na verdade, o computador está apenas dizendo onde ele se perdeu. "
        "<b>Regra de Ouro: Olhe sempre para a última linha da mensagem de erro!</b> É lá que está a pista do que aconteceu.",
        styles['Normal']
    ))
    
    erros_tabela = [
        ["Mensagem de Erro", "Causa Comum em Gestão Ambiental", "Como Resolver Rapidamente?"],
        ["NameError: name 'chuvas' is not defined", "Você tentou calcular a média de uma variável que não foi criada ou que está com o nome digitado errado.", "Verifique se rodou a célula anterior onde a lista foi criada e confira maiúsculas/minúsculas."],
        ["SyntaxError: invalid syntax", "Esqueceu de fechar um parêntese, vírgula ou aspas em um texto.", "Confira a linha apontada com a setinha ^ e certifique-se de que todos os parênteses fecham."],
        ["TypeError: unsupported operand", "Tentou somar um número com um texto (ex: 25 + 'calor').", "Verifique se algum número foi digitado com aspas por engano ou se há letras na coluna numérica."],
        ["ZeroDivisionError: division by zero", "Tentou calcular uma média dividindo por uma lista que estava vazia (quantidade = 0).", "Confira se a base de dados tem medições válidas antes de fazer a divisão matemática."]
    ]
    story.append(criar_tabela_geral(erros_tabela[0], erros_tabela[1:], [135, 185, 185], styles))
    
    story.append(PageBreak())
    return story

print("Módulo de conteúdo didático parte 1 compilado com sucesso.")
