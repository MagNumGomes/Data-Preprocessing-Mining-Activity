# Normalizacao, padronizacao e escalonamento

## Trabalho de Mineracao de Dados

**Apresentacao:** 25/09/2026  
**Integrante:** Claudio  
**Tema:** Normalizacao, padronizacao e escalonamento

> Este arquivo e um esqueleto. As secoes podem ser transformadas em slides e complementadas com referencias, imagens e resultados do experimento.

## 1. Estrutura sugerida do PPTX

### Slide 1 - Titulo e integrante
- Normalizacao, padronizacao e escalonamento em mineracao de dados
- Nome: Claudio
- Disciplina: Mineracao de Dados
- Data: 25/09/2026

### Slide 2 - Problema que sera estudado
- Dados reais costumam ter variaveis em escalas muito diferentes.
- Exemplo: consumo de energia em kWh, temperatura em graus e numero de falhas.
- Algoritmos baseados em distancia ou gradiente podem dar mais importancia a variaveis com valores numericamente maiores.
- Pergunta central: como colocar as variaveis em escalas comparaveis sem perder a informacao relevante?

### Slide 3 - Definicao dos conceitos

**Normalizacao**
- Em sentido amplo, e a transformacao dos dados para uma escala comum.
- A normalizacao Min-Max costuma levar os valores para o intervalo `[0, 1]`.
- Formula: `x' = (x - minimo) / (maximo - minimo)`.

**Padronizacao**
- Transforma os dados para media 0 e desvio-padrao 1.
- Formula: `z = (x - media) / desvio_padrao`.
- Tambem e conhecida como transformacao por Z-Score.

**Escalonamento**
- E o processo geral de alterar a escala das variaveis.
- Pode incluir Min-Max, Z-Score, RobustScaler e outras tecnicas.

### Slide 4 - Por que essas tecnicas foram criadas?
- Evitar que uma variavel domine as outras por causa da unidade de medida.
- Melhorar algoritmos como K-Means, KNN, SVM e redes neurais.
- Tornar a comparacao entre atributos mais justa.
- Ajudar na estabilidade e na velocidade de alguns modelos.

### Slide 5 - Breve historico
- Estatistica ja utiliza medidas padronizadas para comparar observacoes.
- Com a popularizacao do aprendizado de maquina, o pre-processamento tornou-se uma etapa comum do pipeline.
- Bibliotecas como Scikit-learn facilitaram a aplicacao consistente dessas transformacoes.

### Slide 6 - Funcionamento conceitual
1. Identificar as colunas numericas.
2. Separar treino e teste quando houver um modelo preditivo.
3. Ajustar o transformador somente com os dados de treino.
4. Aplicar a mesma transformacao aos dados de treino e teste.
5. Comparar os resultados antes e depois do escalonamento.

**Cuidado importante:** nunca calcular minimo, maximo, media ou desvio usando o conjunto inteiro antes da separacao. Isso causa vazamento de dados.

### Slide 7 - Comparacao das tecnicas

| Tecnica | Resultado | Vantagem | Limitacao |
|---|---|---|---|
| Min-Max | Intervalo `[0, 1]` | Facil de interpretar | Sensivel a outliers |
| StandardScaler | Media 0, desvio 1 | Bom para muitos modelos | Sensivel a outliers |
| RobustScaler | Usa mediana e intervalo interquartil | Mais resistente a outliers | Pode ser menos intuitivo |
|
### Slide 8 - Aplicacoes
- K-Means e agrupamento de clientes.
- KNN para classificacao de registros semelhantes.
- SVM para separar classes.
- Redes neurais e modelos baseados em gradiente.
- Analise de sensores industriais e consumo de energia.
- Comparacao de indicadores financeiros ou operacionais.

### Slide 9 - Limitacoes
- Escalonar nao corrige dados errados ou mal coletados.
- Min-Max e padronizacao podem ser afetados por outliers.
- Nem todo algoritmo precisa de escalonamento, como arvores de decisao.
- A transformacao pode dificultar a interpretacao dos valores originais.
- E necessario salvar o transformador para aplicar a mesma regra em novos dados.

### Slide 10 - Caso de sucesso
- Situacao: agrupar maquinas por comportamento usando temperatura, vibracao e consumo.
- Sem escalonamento, o consumo pode dominar a distancia.
- Com escalonamento, as tres caracteristicas contribuem de forma mais equilibrada.
- Mostrar no trabalho pratico um grafico antes/depois e a comparacao do agrupamento.

### Slide 11 - Tendencias
- Pipelines automatizados de pre-processamento.
- Transformacoes robustas para dados com muitos outliers.
- Pre-processamento integrado a plataformas de dados e MLOps.
- Uso de tecnicas adaptativas para dados que mudam ao longo do tempo.
- Maior preocupacao com reproducibilidade e ausencia de vazamento de dados.

### Slide 12 - Conclusao
- Escalonar e uma etapa essencial para muitos algoritmos de mineracao de dados.
- A escolha depende da distribuicao dos dados, dos outliers e do algoritmo.
- Min-Max, StandardScaler e RobustScaler nao sao equivalentes.
- O resultado deve ser avaliado no contexto do problema.

### Slide 13 - Referencias
- Documentacao oficial do Scikit-learn: `sklearn.preprocessing`.
- Han, Kamber e Pei. *Data Mining: Concepts and Techniques*.
- James et al. *An Introduction to Statistical Learning*.
- Outras fontes consultadas pelo grupo.

## 2. Estrutura do trabalho pratico

### Problema escolhido
**Monitoramento de maquinas em uma industria.** O objetivo e comparar as escalas das medidas de sensores antes e depois das transformacoes.

### CSV ficticio
O script `trabalho_normalizacao.py` gera `dados_maquinas.csv` com:
- 60 registros;
- identificador da leitura;
- data da leitura;
- tres ou mais caracteristicas numericas;
- uma caracteristica categorica;
- valores ausentes;
- situacoes anormais conhecidas;
- uma anomalia causada pela combinacao de caracteristicas.

### Etapas obrigatorias
1. Carregar o CSV com pandas.
2. Verificar tipos, valores ausentes e estatisticas.
3. Tratar valores ausentes pela mediana.
4. Criar novos atributos, como `energia_por_hora` e `indice_estresse`.
5. Aplicar Min-Max, StandardScaler e RobustScaler.
6. Comparar estatisticas antes e depois.
7. Criar pelo menos dois graficos.
8. Interpretar os resultados no contexto das maquinas.

## 3. Perguntas para a interpretacao
- Qual tecnica sofreu mais influencia dos valores extremos?
- As variaveis ficaram em escalas comparaveis?
- Qual transformacao parece mais adequada para este CSV?
- O que muda na interpretacao dos graficos?
- Em que situacao uma arvore de decisao poderia dispensar escalonamento?

## 4. Divisao sugerida dos slides
- Introducao e problema: Claudio
- Conceitos e formulas: Claudio
- Aplicacao pratica: Claudio
- Graficos e interpretacao: Claudio
- Limitacoes, tendencias e conclusao: Claudio
