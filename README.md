# ⚡ Citizen Assist AI

## Sistema inteligente de análise e eficiência energética

O **Citizen Assist AI** é uma aplicação desenvolvida em Python com o objetivo de auxiliar moradores de residências a compreender o consumo de energia elétrica, estimar custos e analisar alternativas sustentáveis.

O sistema permite realizar simulações de consumo, estimar a geração de energia solar, comparar alternativas energéticas e receber recomendações para promover o uso consciente e eficiente da eletricidade.

## 👤 Identificação do projeto

- **Integrante:** Maria Beatriz Braga de Lima
- **RM:** 570501
- **Turma:** 1 CCPO
- **Disciplina:** Soluções em Energias Renováveis e Sustentáveis

## 🎯 Público-alvo e necessidade energética

O projeto tem como público-alvo moradores de residências que desejam compreender melhor seu consumo de energia elétrica e encontrar alternativas para reduzir os gastos com a conta de luz.

A solução busca facilitar a interpretação do consumo, apresentar estimativas de custos e demonstrar possibilidades de economia por meio da eficiência energética e da utilização de fontes renováveis.

## 🚀 Funcionalidades

O sistema apresenta cinco funcionalidades principais:

### 1. Início
- Painel de controle com indicadores energéticos.
- Visualização do consumo mensal.
- Estimativa do custo de energia.
- Quantidade estimada de painéis solares necessários.

### 2. Consumo de energia
- Cálculo do consumo mensal em kWh.
- Estimativa do custo mensal em reais.
- Utilização da potência dos equipamentos e do tempo de uso para calcular o consumo.

### 3. Energia solar
- Simulação da geração mensal de energia solar.
- Estimativa da quantidade de painéis necessários.
- Cálculo do percentual de consumo atendido.
- Estimativa da economia mensal.

### 4. Comparação energética
- Comparação entre energia convencional, energia solar e eficiência energética.
- Apresentação de tabela comparativa.
- Gráficos para visualização dos resultados.
- Estimativas de consumo e custos para os diferentes cenários.

### 5. Recomendações
- Sugestões para reduzir o consumo de energia.
- Orientações sobre eficiência energética.
- Recomendações relacionadas ao uso de fontes renováveis.
- Orientações personalizadas conforme o consumo e o custo informados.

## 🧮 Metodologia e dados utilizados

A aplicação utiliza parâmetros informados pelo usuário para realizar as simulações.

### Análise de consumo

O consumo mensal é calculado pela fórmula:

**Consumo (kWh) = Potência (W) × Horas de uso por dia × Dias de utilização ÷ 1.000**

O custo estimado é calculado por:

**Custo (R$) = Consumo (kWh) × Tarifa (R$/kWh)**

### Simulação solar

A geração mensal estimada considera:
- Potência dos painéis;
- Horas de sol pleno por dia;
- Eficiência estimada;
- Período de 30 dias.

A quantidade de painéis é calculada com base no consumo mensal e na geração estimada por painel.

### Comparação de alternativas

O sistema compara três cenários:
- Energia convencional;
- Energia solar;
- Eficiência energética.

A comparação utiliza o mesmo consumo inicial e a mesma tarifa informada pelo usuário. O percentual de cobertura solar vem da simulação fotovoltaica, enquanto o percentual de eficiência energética é selecionado pelo usuário.

### Origem dos dados e premissas

Os dados de consumo, tarifa, potência dos equipamentos, potência dos painéis, horas de sol pleno e eficiência são informados manualmente ou utilizados como parâmetros de demonstração.

Os valores estimados são identificados como simulações e não representam medições reais de uma residência específica.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Streamlit:** criação da interface interativa.
- **Pandas:** manipulação e organização de dados.
- **NumPy:** operações numéricas.
- **Plotly:** criação de gráficos e visualizações.

## 📁 Estrutura do projeto

```text
Citizen_Assist_AI/
│
├── data/
│
├── docs/
│   ├── contexto_projeto.md
│   ├── analise_consumo.md
│   ├── analise_energia_solar.md
│   ├── comparacao_alternativas.md
│   ├── referencias_limitacoes.md
│   └── testes_e_ajustes.md
│
├── modules/
│   └── energy/
│       ├── __init__.py
│       ├── comparison.py
│       ├── consumption.py
│       ├── recommendations.py
│       └── solar.py
│
├── tests/
│   └── test_energy.py
│
├── utils/
│   └── calculations.py
│
├── main.py
├── README.md
└── requirements.txt
```

## ▶️ Como executar o projeto

### 1. Baixar o projeto

Faça o download ou clone o repositório para o computador.

### 2. Criar o ambiente virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
streamlit run main.py
```

A aplicação será disponibilizada no navegador, normalmente no endereço `http://localhost:8501`.

## 🧪 Testes automatizados

O projeto possui testes automatizados para verificar o funcionamento das funções de cálculo energético.

Para executar os testes, utilize:

```bash
python -m unittest tests.test_energy
```

Os sete testes automatizados foram executados e apresentaram resultado satisfatório durante a verificação do projeto.

## 👥 Testes com usuários

Foram realizadas avaliações com duas pessoas para verificar a compreensão e a utilidade das orientações.

Os resultados registrados foram:

- Os dois participantes compreenderam as informações de consumo e custo.
- Os dois consideraram úteis as recomendações.
- Os dois compreenderam a comparação entre as alternativas energéticas.
- Um participante sugeriu acrescentar explicações sobre os tipos de energia.

A sugestão recebida foi utilizada para melhorar a página de comparação, acrescentando explicações sobre energia convencional, energia solar e eficiência energética.

Os registros completos estão disponíveis em `docs/testes_e_ajustes.md`.

## 📚 Referências e documentação

As referências e premissas utilizadas no projeto estão documentadas em `docs/referencias_limitacoes.md`.

Também estão disponíveis documentos específicos sobre:
- Contexto do projeto;
- Análise de consumo;
- Simulação de energia solar;
- Comparação de alternativas;
- Testes e ajustes realizados.

## ⚠️ Limitações

Os resultados apresentados pelo Citizen Assist AI são estimativas baseadas nos parâmetros informados pelo usuário.

A aplicação não realiza medições automáticas de consumo, não consulta automaticamente as condições meteorológicas e não substitui um dimensionamento técnico de sistemas fotovoltaicos.

Os custos estimados não representam necessariamente o valor final da conta de energia, pois existem tarifas, tributos e cobranças que podem não estar incluídos nos cálculos.

As recomendações possuem caráter educativo e não garantem uma economia específica.

## 🌱 Considerações finais

O Citizen Assist AI busca utilizar a programação e a análise de dados como ferramentas de apoio à educação energética.

Por meio de simulações, comparações e recomendações, o projeto procura incentivar o consumo consciente de eletricidade e apresentar alternativas relacionadas à eficiência energética e às fontes renováveis.

## 🔗 Links do projeto

- **Repositório GitHub:** https://github.com/BragaBibi/Citizen-Assist-AI_SERS
- **Vídeo de demonstração:** [https://youtu.be/jW9Pc8_yokw](https://youtu.be/jW9Pc8_yokw)
