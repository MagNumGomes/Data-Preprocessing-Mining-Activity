# Mineração de Dados: Normalização, Padronização e Escalonamento

Trabalho prático e acadêmico da disciplina de **Mineração de Dados**  
**Tema 3:** Normalização, padronização e escalonamento
**Data de referência:** 25/09/2026

---

## 👥 Integrantes da Equipe

- João Góes
- João Suzuki
- Cláudio Jayme
- Davi Miguel
- João Gabriel Barros
- Avya Alex
- Gabriel Cunha
- Pedro Prevides
- Gustavo Lima

---

## 🎯 Objetivo

Investigar como diferentes técnicas de pré-processamento alteram a distribuição de atributos numéricos com magnitudes discrepantes, garantindo estabilidade, convergência rápida e justiça matemática em modelos de Machine Learning.

---

## ⚙️ Técnicas de Escalonamento Aplicadas

1. **Normalização Min-Max (`MinMaxScaler`):**  
   Reescala os atributos para um intervalo delimitado $[0, 1]$ através da fórmula $X' = \frac{X - X_{min}}{X_{max} - X_{min}}$. Preserva valores nulos em matrizes esparsas, porém é vulnerável ao achatamento de escala na presença de outliers.

2. **Padronização Z-Score (`StandardScaler`):**  
   Centraliza a distribuição em torno da média zero e fixa o desvio-padrão em um: $Z = \frac{X - \mu}{\sigma}$. Permite identificar com clareza anomalias extremas que ultrapassam $\pm 3$ desvios-padrão.

3. **Escalonamento Robusto (`RobustScaler`):**  
   Baseado na mediana ($Q_2$) e no intervalo interquartil ($\text{IQR} = Q_3 - Q_1$). É altamente imune a picos e ruídos pontuais, preservando a escala central dos dados saudáveis do maquinário.

---

## 🏭 Dataset: Sensores de Máquinas Industriais (`dados_maquinas.csv`)

O projeto utiliza um conjunto de dados fictício e reprodutível simulando telemetria de maquinário fabril:
- **Tamanho:** 60 registros (superando o requisito mínimo de 50).
- **Identificador Único:** `id_leitura` (1 a 60).
- **Período e Temporalidade:** `data` (formato AAAA-MM-DD) e `turno` (`manha`, `tarde`, `noite`).
- **4 Variáveis Numéricas:**
  - `temperatura_c`: temperatura operacional em °C (faixa típica: 65–76 °C).
  - `vibracao_mm_s`: vibração mecânica em mm/s (faixa típica: 2.0–3.25 mm/s).
  - `consumo_kwh`: consumo de energia em kWh (faixa típica: 80–107 kWh).
  - `horas_operacao`: tempo de funcionamento contínuo (6 a 10 h).
- **2 Variáveis Categóricas:** `turno` e indicativo de `falha` (`sim`/`nao`).
- **Valores Ausentes:** 2 nulos intencionais (registros 12 e 26), tratados via **imputação pela mediana**.
- **Anomalias Conhecidas:**
  - Picos univariados isolados nos registros 7 (temp: 115 °C), 18 (vibração: 9.5 mm/s) e 31 (energia: 180 kWh).
  - **Anomalia combinada no registro 44:** alta temperatura (95 °C) em conjunto com alta vibração (8.0 mm/s), culminando em `falha = "sim"`.

---

## 🧪 Engenharia de Atributos

Foram criados dois novos atributos derivados:
1. `energia_por_hora = consumo_kwh / horas_operacao`: indicador de eficiência energética da máquina.
2. `indice_estresse = (temperatura_c / 100) + (vibracao_mm_s / 10) + (energia_por_hora / 30)`: indicador composto que isola o risco operacional e detecta o ponto exato da quebra no registro 44.

---

## 📊 Gráficos Gerados

- [`comparacao_escalas.png`](comparacao_escalas.png): Boxplots comparativos das 4 variáveis antes vs. depois da padronização com `StandardScaler`, demonstrando visualmente a unificação das ordens de grandeza.
- [`temperatura_vibracao.png`](temperatura_vibracao.png): Gráfico de dispersão entre Temperatura e Vibração colorido pelo Índice de Estresse, destacando o isolamento da anomalia crítica e a quebra da máquina.

---

## 🖥️ Apresentação em Slides (`Normalização e Escalonamento de Dados.pdf`)

Contém **15 slides em formato 16:9** estruturados rigorosamente segundo o PDF da atividade:
1. Capa e integrantes
2. O problema das escalas (analogia didática Altura x Salário e Sensores)
3. Por que essa técnica foi criada (3 motivos diretos)
4. Breve histórico (Gauss e Karl Pearson)
5. Definição do tema: Min-Max Scaler
6. Padronização: StandardScaler e RobustScaler
7. Comparação e limitações
8. Aplicações práticas na Ciência de Dados
9. Caso de sucesso real (Manutenção Preditiva na Indústria 4.0)
10. Tendências (LayerNorm, Transformers e Streaming Scalers)
11. Trabalho prático: descrição do CSV
12. Trabalho prático: tratamento e engenharia de atributos
13. Gráfico 1: Boxplots antes e depois
14. Gráfico 2: Dispersão e detecção da falha combinada
15. Conclusão geral e perguntas

---

## 🚀 Como Executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o script da análise
```bash
python trabalho_normalizacao.py
```

O script criará o CSV original, executará o tratamento, aplicará os escaladores, exibirá a interpretação no terminal e salvará os gráficos e o CSV tratado.

---

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| [`trabalho_normalizacao.py`](trabalho_normalizacao.py) | Código Python completo com carga, tratamento, novos atributos, escalonadores e gráficos. |
| [`Normalização e Escalonamento de Dados.pdf`](Normalização%20e%20Escalonamento%20de%20Dados.pdf) | Slides da apresentação formatados com gráficos e conteúdos embutidos. |
| [`dados_maquinas.csv`](dados_maquinas.csv) | Dataset fictício de sensores industriais (60 registros). |
| [`dados_maquinas_tratados.csv`](dados_maquinas_tratados.csv) | Dataset limpo com nulos preenchidos e novos atributos calculados. |
| [`comparacao_escalas.png`](comparacao_escalas.png) | Gráfico 1: Boxplots comparando distribuições antes e depois da padronização. |
| [`temperatura_vibracao.png`](temperatura_vibracao.png) | Gráfico 2: Dispersão de temperatura x vibração mapeada pelo estresse. |
| [`requirements.txt`](requirements.txt) | Lista de bibliotecas Python necessárias para execução. |
| [`Trabalhos_25092026.pdf`](Trabalhos_25092026.pdf) | Documento com as diretrizes e requisitos da atividade. |

