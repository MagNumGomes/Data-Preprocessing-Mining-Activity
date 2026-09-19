# Data Preprocessing for Data Mining

Trabalho acadêmico da disciplina de Mineração de Dados sobre normalização, padronização e escalonamento.

## Integrantes

João Góes, João Suzuki, Cláudio Jayme, Davi Miguel, João Gabriel Barros, Avya Alex, Gabriel Cunha, Pedro Prevides e Gustavo Lima.

## Objetivo

Estudar como diferentes técnicas de pré-processamento alteram a escala das variáveis e influenciam a análise de dados.

## Técnicas utilizadas

- **Min-Max:** transforma os valores para um intervalo, normalmente entre 0 e 1.
- **StandardScaler:** padroniza os dados usando média 0 e desvio-padrão 1.
- **RobustScaler:** utiliza a mediana e o intervalo interquartil, sendo mais resistente a valores extremos.

## Trabalho prático

O projeto utiliza dados fictícios para analisar indicadores de um sistema monitorado. O procedimento inclui:

1. Carregamento do arquivo CSV com pandas;
2. Verificação dos tipos, valores ausentes e estatísticas;
3. Tratamento dos valores ausentes;
4. Criação de novos atributos;
5. Aplicação das técnicas de escalonamento;
6. Geração de gráficos;
7. Interpretação dos resultados.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script:

```bash
python trabalho_normalizacao.py
```

## Arquivos principais

- `trabalho_normalizacao.py`: código da análise.
- `roteiro_normalizacao.md`: roteiro da apresentação.
- `requirements.txt`: dependências do projeto.
- `dados_maquinas.csv`: conjunto de dados fictício original.
- `dados_maquinas_tratados.csv`: conjunto de dados após o tratamento.
- `comparacao_escalas.png`: comparação antes e depois do escalonamento.
- `temperatura_vibracao.png`: gráfico de temperatura e vibração.
