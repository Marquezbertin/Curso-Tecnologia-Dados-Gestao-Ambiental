"""
Conteúdo Didático Parte 3:
- Módulo 7: Ciência Cidadã e Coleta de Dados de Campo na Escola
- Módulo 8: Tratamento Estatístico e Análise Crítica dos Dados Coletados
- Módulo 9: Inteligência Artificial e Aprendizado de Máquina na Gestão Ambiental
- Módulo 10: Do Dado à Solução: Storytelling, Políticas Públicas e Mostra Científica
"""

from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether, Image, HRFlowable
from reportlab.lib import colors
import os
from estilos_apostila import criar_box, criar_tabela_codigo, criar_tabela_geral

def obter_modulo_7(styles):
    story = []
    story.append(Paragraph("Módulo 7 — Ciência Cidadã e Coleta de Dados de Campo na Escola", styles['ModTitle']))
    story.append(Paragraph("<i>Democratizando a ciência com dados reais do pátio, do bairro e da comunidade</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Até agora, trabalhamos com dados disponibilizados por grandes órgãos governamentais (INMET, INPE). "
        "No entanto, as estações oficiais ficam a dezenas de quilômetros da sua escola ou do seu bairro. "
        "Para responder perguntas sobre o <b>microclima local</b>, o descarte irregular de resíduos na praça ou o conforto térmico das salas de aula, "
        "a própria comunidade precisa ir a campo. Essa prática chama-se <b>Ciência Cidadã</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("7.1 O Desenho Amostral: As Três Perguntas Essenciais", styles['SecTitle']))
    story.append(Paragraph(
        "Uma coleta de campo não pode ser um passeio descompromissado. Para que os dados tenham validade científica, "
        "o grupo precisa planejar com antecedência o <b>Desenho Amostral</b>:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>1. O que medir? (Variável Operacional):</b> Escolha grandezas objetivas. Por exemplo, em vez de anotar <i>'aqui é barulhento'</i>, meça o nível de pressão sonora em decibéis (dB); em vez de <i>'muito lixo'</i>, meça o peso em quilogramas ou o número de sacos de entulho.<br/>"
        "<b>2. Onde medir? (Pontos Amostrais):</b> Defina locais fixos e representativos. Exemplo: Ponto 1 (debaixo da árvore frondosa no pátio), Ponto 2 (no centro da quadra de asfalto ao sol) e Ponto 3 (na calçada em frente à avenida).<br/>"
        "<b>3. Quando medir? (Frequência e Horário):</b> Compare apenas medições feitas sob as mesmas condições temporais (ex: sempre às 10h da manhã e às 14h da tarde, ao longo de 5 dias úteis).",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("7.2 Instrumentos de Baixo Custo e Padronização de Protocolos", styles['SecTitle']))
    story.append(Paragraph(
        "Não é necessário ter equipamentos laboratoriais de milhões de reais para fazer ciência séria. Instrumentos simples "
        "oferecem grande precisão, desde que o <b>protocolo de uso seja rigorosamente o mesmo</b> para todos os alunos:",
        styles['Normal']
    ))
    
    instrumentos = [
        ["Tema de Investigação", "Instrumento Simples", "Unidade de Medida", "Cuidados no Protocolo"],
        ["Microclima e Conforto Térmico", "Termohigrômetro digital portátil ou termômetro infravermelho", "Graus Celsius (°C) e Umidade (%)", "Aguardar 2 minutos para estabilização do sensor; não medir encostado no corpo."],
        ["Arborização Urbana", "Fita métrica comum de costura ou trena", "Circunferência à Altura do Peito (CAP em cm)", "Medir sempre a 1,30 metro do solo; manter a fita reta sem folga no tronco."],
        ["Gestão de Resíduos Sólidos", "Balança digital suspensa de mala / gancho", "Massa em quilogramas (kg)", "Tarar a balança descontando o peso do balde ou saco coletor vazio."],
        ["Poluição Sonora Escolar", "Aplicativo decibelímetro calibrado no smartphone", "Nível de ruído em Decibéis (dBA)", "Segurar o aparelho afastado da roupa; registrar a medição média durante 60 segundos."]
    ]
    story.append(criar_tabela_geral(instrumentos[0], instrumentos[1:], [110, 130, 110, 155], styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("7.3 Ética, Segurança e Proteção de Dados (LGPD)", styles['SecTitle']))
    story.append(Paragraph(
        "Toda pesquisa escolar deve respeitar a privacidade e a segurança das pessoas. A Lei Geral de Proteção de Dados (LGPD) "
        "e o bom senso científico exigem normas claras:",
        styles['Normal']
    ))
    
    regras_lgpd = [
        "<b>• Nunca colete dados pessoais:</b> Jamais anote nomes de moradores, telefones, números de documentos ou placas de veículos em planilhas públicas.",
        "<b>• Atenção com fotografias:</b> Ao registrar um ponto de descarte ou calçada, certifique-se de que não aparecem rostos de pedestres ou crianças.",
        "<b>• Respeito à propriedade privada:</b> As coletas devem ocorrer exclusivamente em espaços públicos (praças, ruas, parques) ou dentro da escola, nunca invadindo terrenos privados sem permissão expressa."
    ]
    story.append(criar_box("DIRETRIZES ÉTICAS E LEGAIS DE CAMPO", regras_lgpd, tipo="alerta", styles=styles))
    
    story.append(PageBreak())
    return story

def obter_modulo_8(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 8 — Tratamento Estatístico e Análise Crítica dos Dados", styles['ModTitle']))
    story.append(Paragraph("<i>Saneamento de dados imperfeitos, média versus mediana e limites da ciência</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Ao retornar do campo e abrir a planilha com as anotações da turma, surge a primeira surpresa: "
        "<b>os dados do mundo real são bagunçados</b>. Há números digitados com vírgula onde deveria ser ponto, "
        "palavras com erros ortográficos ('cerrado', 'Cerrado ', 'cerado'), células em branco e números absurdos digitados sem querer. "
        "A primeira tarefa do cientista chama-se <b>Saneamento de Dados (Data Cleaning)</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("8.1 A Armadilha da Média Aritmética e o Poder da Mediana", styles['SecTitle']))
    story.append(Paragraph(
        "Na escola, aprendemos que para resumir um conjunto de valores basta calcular a <b>média</b> (somar tudo e dividir pela quantidade). "
        "No entanto, em gestão ambiental, <b>a média mente com frequência!</b>",
        styles['Normal']
    ))
    story.append(Paragraph(
        "Se uma turma de alunos pesou os resíduos recicláveis recolhidos em 14 salas de aula e encontrou valores entre 12 e 26 kg, "
        "mas na cantina encontrou 110 kg (um descarte excepcional), o que acontece com a média? "
        "A média salta para 25.9 kg, dando a falsa impressão de que todas as salas geram muito resíduo. "
        "Já a <b>mediana</b> (o valor exato que fica no meio quando organizamos os números em ordem crescente) é de 19.0 kg. "
        "A mediana não se deixa enganar por valores extremos!",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    # Inserção da Figura 4
    caminho_fig4 = os.path.join(img_dir, "grafico4_estatistica_outliers.png")
    if os.path.exists(caminho_fig4):
        story.append(Image(caminho_fig4, width=470, height=220))
        story.append(Paragraph("Figura 4: Comparativo visual do impacto de um valor atípico (outlier) sobre a média e a estabilidade da mediana.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph("8.2 Medidas de Dispersão: A Importância do Desvio Padrão", styles['SecTitle']))
    story.append(Paragraph(
        "Imagine duas praças da cidade com a mesma temperatura média de 25°C. "
        "Na Praça A (bem arborizada), o termômetro varia suavemente entre 23°C pela manhã e 27°C à tarde (baixa dispersão). "
        "Na Praça B (puro concreto sem árvores), o termômetro varia de 12°C no amanhecer a 38°C no pico do sol (alta dispersão). "
        "Dizer apenas que ambas têm média de 25°C oculta o desconforto térmico insuportável da Praça B. "
        "O <b>Desvio Padrão</b> mede essa volatilidade: quanto maior o desvio, mais instável e extremo é o ambiente.",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("8.3 A Força das 'Limitações do Estudo'", styles['SecTitle']))
    story.append(Paragraph(
        "Em relatórios amadores, as pessoas tentam esconder as falhas da pesquisa. Em ciência de alto nível, "
        "<b>declarar as limitações do estudo é uma demonstração de honestidade e rigor</b>.",
        styles['Normal']
    ))
    
    limitacoes_box = [
        "<b>O que incluir no seu relatório final:</b>",
        "• <i>'As medições foram realizadas apenas no período matutino; o comportamento noturno não pôde ser avaliado.'</i>",
        "• <i>'Houve perda de dados em um dos pontos de coleta no dia 3 devido a chuvas torrenciais.'</i>",
        "• <i>'Os sensores de temperatura de baixo custo têm margem de erro documentada de ±1.5°C.'</i>",
        "Ao explicitar os limites, você protege suas conclusões contra contestações e orienta futuras pesquisas."
    ]
    story.append(criar_box("HONESTIDADE CIENTÍFICA", limitacoes_box, tipo="pratica", styles=styles))
    
    story.append(PageBreak())
    return story

def obter_modulo_9(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 9 — Inteligência Artificial e Aprendizado de Máquina na Gestão Ambiental", styles['ModTitle']))
    story.append(Paragraph("<i>Machine learning supervisionado, árvores de decisão, matriz de confusão e ética</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "A Inteligência Artificial (IA) tornou-se a expressão mais comentada da atualidade. No entanto, existe uma confusão enorme "
        "sobre o que ela realmente faz. A maioria das pessoas pensa em IA como chatbots que geram textos ou imagens (<b>IA Generativa</b>). "
        "Porém, na gestão ambiental profissional, o ramo mais poderoso é o <b>Aprendizado de Máquina Tradicional (Machine Learning Preditivo)</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("9.1 Aprendizado Supervisionado: Ensinando com Exemplos do Passado", styles['SecTitle']))
    story.append(Paragraph(
        "No aprendizado supervisionado, nós alimentamos o computador com uma tabela de dados históricos. Essa tabela contém:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>• Variáveis de Entrada (Features / Atributos):</b> São as pistas meteorológicas (ex: temperatura máxima, umidade do ar, velocidade do vento, dias sem chuva).<br/>"
        "<b>• Rótulo ou Variável Alvo (Target / Classe):</b> É o resultado real que ocorreu naquele dia histórico (ex: <code>risco_fogo = 1</code> para dia crítico com foco de calor, ou <code>0</code> para dia sem ocorrência).",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("9.2 A Divisão Sagrada: Treino versus Teste", styles['SecTitle']))
    story.append(Paragraph(
        "Se um professor der aos alunos as questões exatas que cairão na prova junto com as respostas para eles estudarem, "
        "todos tirarão nota 10, mas ninguém saberá se eles realmente aprenderam a matéria ou apenas decoraram o gabarito. "
        "Em IA vale o mesmo princípio: <b>nunca avalie o modelo com os mesmos dados que você usou para treiná-lo!</b>",
        styles['Normal']
    ))
    story.append(Paragraph(
        "Por isso, dividimos a tabela histórica em dois blocos: <b>Conjunto de Treino</b> (geralmente 70% ou 80% dos dados para o modelo aprender) "
        "e <b>Conjunto de Teste</b> (os 20% restantes, mantidos trancados em segredo para avaliar se o modelo acerta em dados inéditos).",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("9.3 Árvores de Decisão: A Inteligência Transparente ('Caixa Branca')", styles['SecTitle']))
    story.append(Paragraph(
        "Muitos modelos de IA são 'caixas pretas' misteriosas: tomam decisões, mas ninguém sabe o porquê. "
        "Para a gestão pública ambiental, isso é perigoso, pois o secretário precisa justificar para a população onde alocará verbas. "
        "A <b>Árvore de Decisão (Decision Tree)</b> é o modelo ideal porque ela gera regras lógicas transparentes que qualquer ser humano pode auditar. "
        "Veja na Figura 6 a árvore gerada pelo nosso código no <b>Notebook 03</b>:",
        styles['Normal']
    ))
    
    # Inserção da Figura 6
    caminho_fig6 = os.path.join(img_dir, "grafico6_arvore_decisao.png")
    if os.path.exists(caminho_fig6):
        story.append(Image(caminho_fig6, width=470, height=220))
        story.append(Paragraph("Figura 6: Estrutura lógica de uma Árvore de Decisão para previsão de risco de queimadas florestais.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph("9.4 A Ilusão da Acurácia e o Custo do Erro na Matriz de Confusão", styles['SecTitle']))
    story.append(Paragraph(
        "Se em um município do Pantanal ocorrem queimadas em apenas 2 dias ao longo de 100 dias de inverno, um modelo preguiçoso "
        "que simplesmente diga sempre <i>'não vai pegar fogo'</i> acertará 98 dias em 100 — uma <b>acurácia de 98%!</b> "
        "No entanto, esse modelo é uma tragédia completa, pois deixará os dois incêndios reais queimarem tudo sem dar nenhum alarme. "
        "Por isso, gestores ambientais usam a <b>Matriz de Confusão</b>, ilustrada na Figura 5:",
        styles['Normal']
    ))
    
    # Inserção da Figura 5
    caminho_fig5 = os.path.join(img_dir, "grafico5_matriz_confusao.png")
    if os.path.exists(caminho_fig5):
        story.append(Image(caminho_fig5, width=470, height=230))
        story.append(Paragraph("Figura 5: Matriz de confusão didática destacando a assimetria crítica entre Falsos Positivos e Falsos Negativos.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph(
        "<b>O Custo Assimétrico do Erro:</b><br/>"
        "• <b>Falso Positivo (Alarme Falso):</b> O modelo prevê fogo, a brigada se desloca até a serra, mas não encontra chamas. Custo: combustível e tempo da equipe.<br/>"
        "• <b>Falso Negativo (Incêndio Oculto):</b> O modelo diz que está seguro, o fogo começa, nenhuma brigada é avisada e 5.000 hectares de reserva são cinzas. "
        "Custo: destruição irreversível da biodiversidade. <b>Em meio ambiente, errar para falso negativo é infinitamente pior!</b>",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("9.5 Desconstrução do Código de Machine Learning (Notebook 03)", styles['SecTitle']))
    story.append(Paragraph(
        "Acompanhe o que cada instrução executa na construção do classificador de risco:",
        styles['Normal']
    ))
    
    codigo_ml = [
        ("from sklearn.model_selection import train_test_split", "Importa a ferramenta que sorteia e divide os dados históricos em conjuntos de treino e teste de forma balanceada."),
        ("from sklearn.tree import DecisionTreeClassifier, export_text", "Carrega o algoritmo construtor da Árvore de Decisão e o conversor de regras em texto explicativo."),
        ("entradas = ['temp_max_c', 'umidade_rel_pct', 'vento_kmh', 'chuva_mm']", "Define a lista exata das variáveis meteorológicas que servirão de pistas para o computador."),
        ("X = df[entradas]; y = df['risco_fogo']", "Separa a base em duas partes: X contém as colunas de entrada; y contém a coluna com a resposta correta."),
        ("X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25, random_state=42)", "Divide a base em 75% para aprendizado e reserva 25% para teste cego; fixa a semente 42 para garantir reprodutibilidade."),
        ("modelo = DecisionTreeClassifier(max_depth=3, random_state=42)", "Cria a árvore configurando profundidade máxima de 3 níveis para evitar que o modelo decore os dados (overfitting)."),
        ("modelo.fit(X_treino, y_treino)", "Comando mágico: o computador analisa os milhares de exemplos e descobre automaticamente as melhores regras de divisão."),
        ("y_pred = modelo.predict(X_teste)", "Aplica o modelo treinado sobre os dados de teste para ver quais previsões ele faria."),
        ("print(confusion_matrix(y_teste, y_pred))", "Calcula e exibe a tabela cruzada com as contagens exatas de acertos e erros de cada classe.")
    ]
    story.append(criar_tabela_codigo(codigo_ml, styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("9.6 Ficha de Modelo (Model Card): Prestação de Contas Ética", styles['SecTitle']))
    story.append(Paragraph(
        "Assim como os alimentos trazem uma tabela nutricional no verso da embalagem, todo modelo de IA aplicado a políticas públicas "
        "deve conter uma <b>Ficha de Modelo</b> pública, detalhando quem o criou, quais dados usou e onde ele falha:",
        styles['Normal']
    ))
    
    ficha_modelo = [
        ["Campo da Ficha", "Descrição Prática para o Modelo de Queimadas"],
        ["Finalidade Pretendida", "Classificar dias de alto risco de ignição de queimadas florestais em municípios do interior paulista."],
        ["Dados de Treinamento", "Série meteorológica diária de 2018 a 2023 de estações automáticas do INMET."],
        ["Métricas de Desempenho", "Acurácia global de 88.5%; Sensibilidade (Recall para classe fogo) de 92.0%; 3% de falsos negativos nos testes."],
        ["Limitações Conhecidas", "Não considera a presença de biomassa vegetal acumulada (combustível no solo) nem queimadas criminosas deliberadas."],
        ["Uso Não Recomendado", "Não deve ser utilizado para desligar patrulhas presenciais ou cancelar alertas da Defesa Civil de forma autônoma."]
    ]
    story.append(criar_tabela_geral(ficha_modelo[0], ficha_modelo[1:], [135, 370], styles))
    
    story.append(PageBreak())
    return story

def obter_modulo_10(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 10 — Do Dado à Solução: Storytelling, Políticas Públicas e Mostra", styles['ModTitle']))
    story.append(Paragraph("<i>Comunicando com evidências, encantando gestores e impactando o território</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Um gráfico brilhante dentro de um notebook do Google Colab que ninguém lê não salva uma única árvore. "
        "A ciência e a tecnologia só cumprem seu papel social quando conseguem <b>sair da tela do computador e dialogar "
        "com a comunidade e com os tomadores de decisão</b> (prefeitos, secretários de meio ambiente, vereadores e lideranças comunitárias).",
        styles['Normal']
    ))
    
    story.append(Paragraph("10.1 Storytelling com Dados: A Estrutura em Quatro Atos", styles['SecTitle']))
    story.append(Paragraph(
        "Nenhum gestor público tem tempo para ler centenas de linhas de tabelas estatísticas. "
        "Para convencer quem tem poder de decisão, você deve organizar seus achados em uma <b>Narrativa Baseada em Evidências</b>:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>• Ato 1 — O Contexto Territorial:</b> Qual o lugar e qual o valor ambiental ameaçado? (Ex: A bacia hidrográfica que abastece 40% da população da cidade).<br/>"
        "<b>• Ato 2 — O Problema Revelado pelos Dados:</b> Apresente o gráfico-chave. Mostre que o problema não é um 'achismo', mas uma tendência mensurável (Ex: 'Nos últimos 3 anos, os dias de calor extremo aumentaram 45% e os descartes na margem do rio dobraram').<br/>"
        "<b>• Ato 3 — A Investigação e as Descobertas:</b> Explique o que a análise de dados e a IA revelaram (Ex: 'Descobrimos que 80% dos descartes ocorrem a menos de 500 metros de vias sem iluminação pública e após as 18h').<br/>"
        "<b>• Ato 4 — A Proposta de Ação Viável:</b> Apresente uma solução concreta, com custo realista e indicador de monitoramento (Ex: 'Instalar ecopontos iluminados e rondas comunitárias nesses 3 pontos mapeados, medindo a redução de volume em 6 meses').",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    # Inserção da Figura 7
    caminho_fig7 = os.path.join(img_dir, "grafico7_ciclo_gestao_dados.png")
    if os.path.exists(caminho_fig7):
        story.append(Image(caminho_fig7, width=470, height=210))
        story.append(Paragraph("Figura 7: O ciclo completo e contínuo da gestão ambiental orientada por dados e evidências científicas.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph("10.2 Como Montar um Pôster Científico Impecável para a Mostra", styles['SecTitle']))
    story.append(Paragraph(
        "O pôster científico é o cartão de visitas do seu projeto em feiras de ciências e eventos municipais. "
        "Um bom pôster deve ser lido com clareza a 1,5 metro de distância em menos de 2 minutos. Siga o padrão de diagramação:",
        styles['Normal']
    ))
    
    poster_elementos = [
        ["Bloco do Pôster", "O que deve conter?", "Dica Visual / Recomendação"],
        ["Cabeçalho", "Título claro da investigação, nomes dos alunos, orientador e nome da escola.", "Use fontes grandes e visíveis; evite títulos acadêmicos cansativos."],
        ["Pergunta & Contexto", "O problema local recortado e por que ele importa para a cidade.", "Texto curto de até 100 palavras em tópicos objetivos."],
        ["Metodologia & Dados", "Fontes abertas utilizadas, instrumentos de campo e bibliotecas Python.", "Inclua ícones das ferramentas (Colab, INPE, Folium, Pandas)."],
        ["Resultados Centrais", "Os 2 melhores gráficos (série temporal e mapa territorial) com legendas grandes.", "O gráfico deve 'falar por si mesmo' sem exigir lupa."],
        ["Proposta de Solução", "Ação prática recomendada para a Secretaria de Meio Ambiente.", "Destaque em uma caixa colorida com borda verde."],
        ["Limitações & Próximos Passos", "O que o grupo não conseguiu medir e o que precisa ser continuado.", "Demonstração pública de maturidade e rigor científico."]
    ]
    story.append(criar_tabela_geral(poster_elementos[0], poster_elementos[1:], [110, 240, 155], styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("10.3 O Pitch de 3 Minutos: Como Falar com Autoridades e Moradores", styles['SecTitle']))
    story.append(Paragraph(
        "Durante a Mostra de Ciências, avaliadores e moradores visitarão seu estande. "
        "Você terá no máximo 3 minutos para transmitir a essência do seu trabalho antes que a atenção da pessoa se disperse. "
        "Divida sua fala com um cronômetro rigoroso:",
        styles['Normal']
    ))
    
    pitch_roteiro = [
        "<b>• Minuto 1 (O Gancho e o Problema):</b> Apresente-se, aponte a dor ambiental da cidade e diga qual pergunta científica o grupo se propôs a responder.",
        "<b>• Minuto 2 (A Evidência e o Método):</b> Mostre o mapa e o gráfico. Explique em linguagem simples como vocês usaram dados abertos e Python para comprovar a hipótese.",
        "<b>• Minuto 3 (A Ação e o Impacto):</b> Entregue a proposta de política pública. Diga quanto custaria aproximadamente ou como a comunidade pode se engajar para mudar o quadro."
    ]
    story.append(criar_box("ROTEIRO DO PITCH DE OURO", pitch_roteiro, tipo="pratica", styles=styles))
    
    story.append(PageBreak())
    return story

print("Módulo de conteúdo didático parte 3 compilado com sucesso.")
