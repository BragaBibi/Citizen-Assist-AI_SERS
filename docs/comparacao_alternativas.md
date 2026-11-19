# Comparação de Alternativas Energéticas — Citizen Assist AI

## 1. Objetivo

O módulo de comparação energética do Citizen Assist AI permite analisar três cenários para uma mesma necessidade residencial de eletricidade: fornecimento convencional, utilização de energia solar e redução do consumo por meio da eficiência energética.

O objetivo é apresentar diferenças estimadas de consumo e custo mensal, auxiliando moradores a compreender alternativas que podem contribuir para a redução dos gastos com energia elétrica.

## 2. Alternativas analisadas

### 2.1. Energia convencional

Representa o cenário de referência, considerando o consumo mensal informado pelo usuário e a tarifa de energia utilizada na simulação.

Nesse cenário, não é aplicada nenhuma redução no consumo.

### 2.2. Energia solar

Representa um cenário hipotético em que parte do consumo convencional é compensada pela utilização de energia solar.

O usuário informa um percentual de redução, utilizado pelo sistema para estimar o consumo restante e seu custo mensal.

A energia solar é uma fonte renovável que pode contribuir para a diversificação da matriz energética e para a redução da dependência da eletricidade fornecida pela rede.

### 2.3. Eficiência energética

Representa um cenário em que o consumo residencial é reduzido por meio de medidas de eficiência energética.

O usuário informa um percentual estimado de redução, que pode representar mudanças nos hábitos de utilização dos equipamentos e a adoção de práticas mais eficientes.

Exemplos dessas medidas incluem substituir lâmpadas convencionais por LED, evitar desperdícios e utilizar equipamentos com melhor eficiência energética.

## 3. Dados e premissas

Os percentuais utilizados na comparação possuem origens diferentes:

- **Energia solar:** o percentual de redução é obtido a partir da cobertura calculada pelo módulo `solar.py`, considerando o consumo informado, a geração estimada e a quantidade de painéis.
- **Eficiência energética:** o percentual é selecionado pelo usuário por meio de um controle deslizante na barra lateral da aplicação. O controle permite valores entre 0% e 50%, com valor inicial de 15% e incrementos de 5 pontos percentuais.

O percentual de eficiência energética representa uma hipótese de redução para fins de simulação. Não corresponde a uma economia medida ou garantida.

## 4. Metodologia de cálculo

A comparação está implementada no arquivo `modules/energy/comparison.py`, por meio da função `compare_energy_sources()`.

### 4.1. Cenário convencional

O custo mensal é calculado por:

**Custo convencional = Consumo mensal × Tarifa**

### 4.2. Cenário de energia solar

O consumo restante é estimado por:

**Consumo solar = Consumo mensal × (1 − Percentual de redução solar ÷ 100)**

O custo correspondente é:

**Custo solar = Consumo solar × Tarifa**

### 4.3. Cenário de eficiência energética

O consumo restante é estimado por:

**Consumo eficiente = Consumo mensal × (1 − Percentual de eficiência ÷ 100)**

O custo correspondente é:

**Custo eficiente = Consumo eficiente × Tarifa**

## 5. Exemplo de comparação

Considere uma residência com consumo mensal de 300 kWh e tarifa de R$ 0,80/kWh.

Para demonstrar a comparação, são utilizados os percentuais iniciais apresentados pela aplicação:

- Redução atribuída à energia solar: 70%;
- Redução atribuída à eficiência energética: 20%.

### Resultados estimados

| Cenário | Consumo mensal | Custo mensal |
|---|---:|---:|
| Energia convencional | 300 kWh | R$ 240,00 |
| Energia solar | 90 kWh | R$ 72,00 |
| Eficiência energética | 240 kWh | R$ 192,00 |

### Economia estimada em relação ao cenário convencional

- Energia solar: R$ 168,00 por mês.
- Eficiência energética: R$ 48,00 por mês.

Nesse exemplo, o cenário de energia solar apresenta o menor custo estimado, seguido pelo cenário de eficiência energética.

Os percentuais foram escolhidos para demonstração e não representam economias garantidas.

## 6. Viabilidade das alternativas

### Energia convencional

É o cenário de referência, baseado no fornecimento de eletricidade pela rede. Sua utilização não exige que o consumidor instale um sistema próprio de geração, mas os custos dependem da tarifa e das condições de fornecimento.

### Energia solar

Pode ser uma alternativa interessante para residências com condições adequadas de instalação, espaço disponível e incidência solar favorável.

Entretanto, sua viabilidade depende do investimento inicial, dos custos de instalação e manutenção, das características do imóvel e das regras aplicáveis à compensação de energia.

### Eficiência energética

Pode ser implementada por meio de mudanças de hábitos e substituição gradual de equipamentos. Algumas medidas apresentam baixo custo de implementação, enquanto outras podem exigir investimentos.

A viabilidade depende dos equipamentos existentes e das condições de utilização da residência.

## 7. Impactos ambientais

A energia solar fotovoltaica utiliza uma fonte renovável e pode contribuir para reduzir a necessidade de eletricidade proveniente de fontes com maiores emissões de gases de efeito estufa.

A eficiência energética também pode trazer benefícios ambientais, pois reduz a quantidade de eletricidade necessária para atender à mesma necessidade.

O cenário convencional representa a dependência do fornecimento pela rede elétrica, cuja composição depende da matriz energética disponível.

A comparação ambiental apresentada é qualitativa. O sistema não calcula emissões de carbono nem realiza uma análise de ciclo de vida dos equipamentos.

## 8. Limitações da comparação

A comparação utiliza percentuais hipotéticos de redução informados pelo usuário. Portanto, os resultados são simulações simplificadas.

O percentual atribuído à energia solar não é calculado diretamente pela quantidade de painéis ou pela geração estimada no módulo de energia solar. Da mesma forma, o percentual de eficiência energética não resulta de uma medição real da economia obtida por equipamentos específicos.

O modelo também não considera investimento inicial, financiamento, manutenção, impostos, taxas ou regras de compensação de energia.

Assim, os resultados permitem comparar cenários matemáticos sob uma mesma tarifa e um mesmo período mensal, mas não representam uma análise financeira completa ou uma garantia de economia.

## 9. Integração ao Citizen Assist AI

A comparação está integrada à página **Comparação energética** da aplicação.

O usuário informa seu consumo mensal, a tarifa e os percentuais de redução desejados para os cenários de energia solar e eficiência energética.

O sistema apresenta os custos e consumos estimados de cada alternativa, acompanhados de gráficos que facilitam a interpretação dos resultados.

Dessa maneira, a aplicação transforma os parâmetros informados em informações comparativas que podem apoiar decisões relacionadas à economia de energia residencial.