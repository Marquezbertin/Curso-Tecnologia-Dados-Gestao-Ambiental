# Ética e Segurança no Uso de IA

Este documento define as regras do curso para uso de inteligência artificial. Ele vale para
alunos, professores e monitores. A regra central é simples:

> **A IA é assistente. A pessoa é autora, verificadora e responsável.**

---

## 1. O que a IA faz bem e o que ela não faz

| A IA faz bem | A IA não faz |
|---|---|
| Explicar um conceito com outra linguagem | Garantir que a informação é verdadeira |
| Sugerir hipóteses e perguntas | Coletar dados no território |
| Ajudar a depurar um código | Assumir responsabilidade pelo resultado |
| Revisar clareza de um texto | Citar a fonte original sem você conferir |
| Organizar ideias e roteiros | Decidir politicamente o que fazer |

---

## 2. Tipos de IA no curso

| Tipo | Exemplo | Uso no curso |
|---|---|---|
| **IA generativa** | Chatbot de texto, gerador de imagem | Explicar, revisar, organizar, ensaiar |
| **Machine learning supervisionado** | Árvore de decisão, classificação | Prever risco de fogo, classificar imagens |
| **Visão computacional** | Modelo pré-treinado de imagens | Classificar imagens do pátio ou de satélite |

O aluno precisa saber **qual dos três** está usando e **qual é o limite** de cada um.

---

## 3. Sete regras para o aluno

1. **Registre o prompt.** Toda interação com IA vai para a ficha de registro.
2. **Confira o número.** Nenhum dado da IA entra no pôster sem conferência na fonte.
3. **Não copie.** A IA pode sugerir; o texto final é seu.
4. **Não cole dados pessoais.** Nome, foto, endereço, telefone e saúde nunca entram no prompt.
5. **Cite quando usar.** No pôster, diga que usou IA e para quê.
6. **Aceite o erro.** Se a IA errou, registre o erro; isso vale mais que acertar por sorte.
7. **Decida você.** A proposta final é do grupo, não da ferramenta.

---

## 4. Cinco regras para o professor

1. **Teste antes.** Nunca use uma ferramenta de IA pela primeira vez na frente da turma.
2. **Conta e chave.** Use conta do professor; nunca exponha chave de API no navegador do aluno.
3. **Dados mínimos.** Não submeta dados de aluno a serviços externos.
4. **Verificação obrigatória.** Toda entrega com IA passa por conferência sua.
5. **Transparência.** Avise às famílias e à coordenação quais ferramentas serão usadas.

---

## 5. Riscos que precisamos ensinar

| Risco | O que é | Exemplo no curso |
|---|---|---|
| **Alucinação** | A IA inventa informação com aparência de verdade | Citar um portal ou um número que não existe |
| **Viés** | O modelo reproduz desequilíbrios dos dados | Modelo treinado só em uma região erra em outra |
| **Vazamento de dados** | Dado pessoal enviado a serviço externo | Colar nome de aluno no chatbot |
| **Direito autoral** | Uso de imagem/texto sem permissão | Gerar imagem e publicar sem checar licença |
| **Custo ambiental** | Treinar e usar modelos consome energia | Discutir o custo energético da IA |
| **Dependência** | Aluno deixa de pensar e só copia | Entregar texto sem entender |
| **Falta de rastreabilidade** | Não se sabe como o resultado foi obtido | Não registrar prompt e versão do modelo |

---

## 6. Ficha de registro de uso de IA

Preencher para **cada** uso relevante. Anexar ao notebook ou ao pôster.

```
Data: ________  Aluno/grupo: __________________________
Ferramenta: ____________________  Versão: _____________
Prompt usado: ________________________________________
Finalidade: __________________________________________
Resposta (resumo): ___________________________________
O que eu verifiquei (fonte/planilha/código): ___________
O que eu corrigi: ____________________________________
O que eu descartei e por quê: ________________________
Risco percebido: _____________________________________
```

---

## 7. Ficha de modelo (machine learning)

```
Nome do modelo: ______________________________________
O que ele faz (1 frase): _____________________________
Quem usa e para quê: _________________________________
Dados de treino (fonte, período, tamanho): ____________
Variáveis de entrada: ________________________________
Rótulo previsto: _____________________________________
Métrica usada: ______________  Resultado: _____________
Falsos positivos: ______  Falsos negativos: ___________
Onde ele erra mais: __________________________________
Quem é afetado pelo erro: ____________________________
Limitação principal: _________________________________
Uso recomendado: _____________________________________
Uso NÃO recomendado: _________________________________
```

Base: Mitchell et al. (2019) e Gebru et al. (2021).

---

## 8. Proteção de dados (LGPD e ECA)

### 8.1 O que nunca entra em prompt

- Nome completo, apelido, foto ou voz de aluno.
- Endereço, telefone, e-mail, documento.
- Dados de saúde, deficiência, religião, orientação sexual.
- Notas, histórico escolar ou diagnóstico.
- Localização exata da residência.

### 8.2 O que pode entrar

- Dados ambientais agregados.
- Coordenadas de pontos públicos (escola, praça, nascente).
- Trechos de código sem dados pessoais.
- Perguntas conceituais.

### 8.3 Publicação no GitHub

- Nenhum notebook com nome de aluno.
- Nenhuma foto com rosto identificável sem consentimento.
- Nenhuma planilha com dado pessoal.
- Usar códigos (`G1`, `Ponto A`) em vez de nomes.

Base legal: LGPD (Lei 13.709/2018), art. 14; ECA (Lei 8.069/1990).

---

## 9. Protocolo de incidente

| Situação | O que fazer | Prazo |
|---|---|---|
| Dado pessoal colado em IA | Parar o uso, registrar, avisar a coordenação | Imediato |
| Resposta de IA ofensiva ou inadequada | Interromper, acolher, registrar | Imediato |
| Suspeita de risco a menor | Acolher, não investigar, registrar e acionar a coordenação | No mesmo dia |
| Vazamento em repositório | Remover, registrar, avaliar comunicação à ANPD | 24 h |
| Uso de imagem sem autorização | Remover e registrar | 24 h |

A coordenação decide sobre comunicação à ANPD e aos titulares.

---

## 10. Política de IA para as famílias (resumo)

> O curso usa ferramentas de inteligência artificial como apoio à aprendizagem. Os alunos são
> orientados a **verificar** as respostas, **registrar** o uso e **não inserir dados pessoais**.
> Nenhuma decisão sobre o aluno é tomada por IA. A avaliação é feita pelo professor, com rubrica
> pública. As ferramentas usadas são gratuitas e não exigem dados sensíveis. Em caso de dúvida,
> procure a coordenação.

---

## 11. Como avaliar uma resposta de IA (checklist do aluno)

- [ ] A resposta cita uma fonte que eu consigo abrir?
- [ ] Os números batem com a minha planilha ou com o portal oficial?
- [ ] A resposta distingue correlação de causalidade?
- [ ] A resposta admite limite ou parece certeza absoluta?
- [ ] A resposta usa linguagem respeitosa e inclusiva?
- [ ] Eu consigo explicar a resposta com as minhas palavras?
- [ ] Eu registrei o prompt e o que verifiquei?

Se alguma resposta for "não", a IA não está pronta para entrar no projeto.

---

## 12. Referências

- BRASIL. **Lei 13.709/2018** — LGPD.
- BRASIL. **Lei 8.069/1990** — ECA.
- GEBRU, T. et al. Datasheets for Datasets. *Communications of the ACM*, 2021.
- MITCHELL, M. et al. Model Cards for Model Reporting. *FAT* '19*, 2019.
- O'NEIL, C. *Weapons of Math Destruction*. Crown, 2016.
- UNESCO. *Recommendation on the Ethics of Artificial Intelligence*. 2021.
