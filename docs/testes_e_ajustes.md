# Testes e Ajustes — Citizen Assist AI

## 1. Objetivo

Registrar os testes funcionais realizados no Citizen Assist AI, verificando o comportamento das funcionalidades de recomendações personalizadas e comparação de alternativas energéticas.

## 2. Testes de recomendações personalizadas

Foram realizados dois testes com diferentes valores de consumo e tarifa.

### Teste 1 — Consumo elevado

**Parâmetros informados:**
- Consumo mensal: 400 kWh;
- Tarifa: R$ 0,80/kWh.

**Resultado esperado:**
- Custo mensal estimado de R$ 320,00;
- Recomendação para reduzir o uso de equipamentos de alto consumo;
- Orientação para avaliar alternativas de redução da conta.

**Resultado observado:**

A aplicação apresentou o custo estimado de R$ 320,00 e cinco recomendações, incluindo as orientações esperadas.

**Status:** aprovado.

### Teste 2 — Consumo menor

**Parâmetros informados:**
- Consumo mensal: 150 kWh;
- Tarifa: R$ 0,80/kWh.

**Resultado esperado:**
- Custo mensal estimado de R$ 120,00;
- Recomendação para acompanhar o consumo;
- Orientações gerais de eficiência energética.

**Resultado observado:**

A aplicação apresentou o custo estimado de R$ 120,00 e quatro recomendações, incluindo as orientações esperadas.

**Status:** aprovado.

## 3. Teste de comparação energética

**Parâmetros e resultados observados:**

| Alternativa | Consumo mensal | Custo mensal |
|---|---:|---:|
| Convencional | 150 kWh | R$ 150,00 |
| Energia solar | 0 kWh | R$ 0,00 |
| Eficiência energética | 127,5 kWh | R$ 127,50 |

A aplicação apresentou os três cenários na tabela comparativa e nos gráficos de consumo e custo.

O cenário de eficiência energética corresponde à redução inicial de 15% configurada no controle da aplicação. O cenário solar apresentou cobertura estimada de 100% do consumo informado.

**Status:** aprovado para o cenário testado.

## 4. Ajustes realizados

Durante a verificação do projeto, foi identificada a necessidade de integrar as recomendações personalizadas à interface da aplicação.

Foi ajustada a página de recomendações para utilizar a função `generate_recommendations()`, localizada no módulo `modules/energy/recommendations.py`.

Após o ajuste, foram realizados testes com diferentes valores de consumo e custo mensal. As recomendações passaram a variar de acordo com os parâmetros informados.

Também foi verificada a integração entre o simulador solar e a função de comparação energética.

## 5. Limitações dos testes

Os testes apresentados verificam o funcionamento da aplicação com valores de simulação.

Eles não representam medições reais de consumo residencial nem comprovam a economia efetivamente obtida por uma residência.

As recomendações e os resultados financeiros devem ser interpretados como estimativas de apoio à decisão.

## 6. Testes com usuários

Os testes registrados neste documento são testes funcionais realizados durante o desenvolvimento da aplicação.

A avaliação específica com outros moradores, incluindo comentários sobre compreensão e utilidade das orientações, deverá ser registrada separadamente caso seja realizada.

Nenhum comentário ou depoimento de participante foi inventado para este documento.

## 7. Avaliação com usuários

Foram realizadas avaliações com duas pessoas, identificadas anonimamente como Pessoa 1 e Pessoa 2, para verificar a compreensão e a utilidade das orientações apresentadas pelo Citizen Assist AI.

### 7.1. Perguntas realizadas

1. Você conseguiu entender as informações sobre consumo e custo de energia?
2. As recomendações apresentadas são úteis para reduzir a conta de luz?
3. A comparação entre energia convencional, solar e eficiência energética ficou clara?
4. O que você mudaria ou acrescentaria na aplicação?

### 7.2. Resultados obtidos

**Pessoa 1:**
- Compreendeu as informações sobre consumo e custos.
- Considerou as recomendações úteis.
- Compreendeu a comparação energética.
- Sugeriu acrescentar mais explicações sobre os tipos de energia.

**Pessoa 2:**
- Compreendeu as informações sobre consumo e custos.
- Considerou as recomendações úteis.
- Compreendeu a comparação energética.
- Não apresentou sugestões adicionais.

### 7.3. Análise dos resultados

Os dois participantes demonstraram compreensão das informações apresentadas e consideraram úteis as recomendações do assistente.

A principal oportunidade de melhoria identificada foi ampliar as explicações sobre as alternativas energéticas, especialmente para facilitar o entendimento das diferenças entre energia convencional, energia solar e eficiência energética.

### 7.4. Ajustes propostos

Com base no retorno recebido, foi identificada a necessidade de acrescentar explicações mais detalhadas sobre as alternativas energéticas, apresentando suas características, vantagens e limitações.

Os ajustes serão incorporados à documentação e à interface do projeto, buscando tornar as orientações mais claras e acessíveis.

### 7.5. Privacidade

Os participantes foram identificados apenas como Pessoa 1 e Pessoa 2. Nenhum nome ou dado pessoal foi incluído no registro dos testes.

## 8. Melhoria realizada após avaliação dos usuários

Com base na sugestão apresentada pela Pessoa 1, foi adicionada à página de comparação energética uma seção explicativa sobre as três alternativas analisadas:

- Energia convencional;
- Energia solar;
- Eficiência energética.

As explicações apresentam características, vantagens e limitações de cada alternativa, com o objetivo de facilitar a compreensão dos moradores.

Após a implementação, foi corrigido um problema de indentação no código Python, permitindo a execução normal da aplicação.

A melhoria busca tornar a comparação energética mais acessível e atender ao comentário recebido durante a avaliação com usuários.