# Análise de Energia Solar — Citizen Assist AI

## 1. Objetivo

O módulo de energia solar do Citizen Assist AI tem como objetivo apresentar uma estimativa da quantidade de painéis fotovoltaicos necessária para atender ao consumo mensal de uma residência.

A ferramenta permite explorar a contribuição da energia solar como alternativa renovável, apresentando estimativas de geração mensal, economia financeira e percentual de consumo atendido.

## 2. Dados utilizados

Para realizar a simulação, o sistema solicita os seguintes parâmetros:

| Parâmetro | Unidade | Descrição |
|---|---|---|
| Consumo mensal | kWh | Consumo de energia da residência |
| Tarifa de energia | R$/kWh | Valor informado para cada quilowatt-hora |
| Potência do painel | W | Potência nominal de cada painel solar |
| Horas de sol pleno | h/dia | Média diária estimada de horas de sol pleno |
| Eficiência do sistema | Proporção | Fator estimado de aproveitamento da geração |

Os dados são informados manualmente pelo usuário. A aplicação não consulta automaticamente dados meteorológicos nem realiza medições de geração fotovoltaica.

## 3. Premissas da simulação

O cálculo considera um período fixo de 30 dias por mês.

A geração estimada depende da potência informada para o painel, das horas de sol pleno e da eficiência adotada.

Os valores iniciais apresentados pela aplicação são:

- Consumo mensal: 300 kWh;
- Tarifa: R$ 0,80/kWh;
- Potência do painel: 550 W;
- Horas de sol pleno: 5 horas por dia;
- Eficiência estimada: 80%.

Esses valores são parâmetros de demonstração e não representam necessariamente as condições reais de uma residência.

## 4. Metodologia e fórmulas

O módulo está implementado no arquivo `modules/energy/solar.py`.

### 4.1. Geração mensal de um painel

A função `calculate_panel_generation()` calcula a geração estimada de cada painel:

**Geração por painel (kWh/mês) = [Potência do painel (W) ÷ 1.000] × Horas de sol pleno por dia × 30 × Eficiência**

A divisão por 1.000 converte a potência de watts para quilowatts.

### 4.2. Quantidade necessária de painéis

A função `calculate_required_panels()` estima a quantidade de painéis:

**Quantidade de painéis = arredondamento para cima de (Consumo mensal ÷ Geração mensal por painel)**

O arredondamento para cima utiliza a função `ceil()` da biblioteca `math`, garantindo que a quantidade inteira calculada seja suficiente para atingir a geração estimada necessária no modelo.

### 4.3. Geração total estimada

A geração total é calculada multiplicando a geração individual pela quantidade de painéis:

**Geração total = Geração por painel × Quantidade de painéis**

### 4.4. Energia solar aproveitada

O sistema limita a energia considerada como aproveitada ao menor valor entre o consumo residencial e a geração total:

**Energia aproveitada = mínimo entre Consumo mensal e Geração total**

Essa regra evita que a economia estimada ultrapasse o consumo informado na simulação.

### 4.5. Economia mensal estimada

A economia é calculada multiplicando a energia aproveitada pela tarifa informada:

**Economia estimada (R$) = Energia aproveitada (kWh) × Tarifa (R$/kWh)**

### 4.6. Percentual de consumo atendido

O percentual é calculado pela relação entre a energia aproveitada e o consumo mensal:

**Cobertura (%) = (Energia aproveitada ÷ Consumo mensal) × 100**

## 5. Exemplo de aplicação

Considerando os parâmetros iniciais da aplicação:

| Parâmetro | Valor |
|---|---:|
| Consumo mensal | 300 kWh |
| Tarifa | R$ 0,80/kWh |
| Potência por painel | 550 W |
| Horas de sol pleno | 5 h/dia |
| Eficiência | 80% |
| Período | 30 dias |

**Geração mensal por painel:**

(550 ÷ 1.000) × 5 × 30 × 0,80 = 66 kWh

**Quantidade de painéis:**

300 ÷ 66 = 4,54

Com o arredondamento para cima, são estimados 5 painéis.

**Geração total estimada:**

66 × 5 = 330 kWh/mês

**Energia aproveitada:**

Mínimo entre 300 e 330 = 300 kWh/mês

**Economia mensal estimada:**

300 × 0,80 = R$ 240,00

**Cobertura estimada:**

(300 ÷ 300) × 100 = 100%

Nesse cenário hipotético, o sistema estima cinco painéis, geração mensal de 330 kWh, aproveitamento de até 300 kWh e economia teórica de R$ 240,00 por mês.

A geração excedente não é contabilizada como economia adicional nesse cálculo.

## 6. Contribuição para a sustentabilidade

A energia solar fotovoltaica é uma alternativa renovável de fornecimento de eletricidade. Sua utilização pode contribuir para diversificar a matriz energética e reduzir a dependência da eletricidade proveniente de fontes não renováveis.

No Citizen Assist AI, o simulador permite que moradores explorem cenários de geração solar e compreendam como a potência dos painéis e as condições de geração influenciam os resultados.

## 7. Limitações da simulação

O cálculo utiliza um modelo simplificado e considera uma média constante de horas de sol pleno e uma eficiência fixa durante os 30 dias do período.

Na prática, a geração pode variar conforme localização geográfica, orientação e inclinação dos módulos, sombreamento, temperatura, condições meteorológicas, perdas elétricas e características dos equipamentos.

A simulação também não considera o investimento inicial, custos de instalação e manutenção, financiamento, regras de compensação de energia ou componentes fixos da conta de eletricidade.

Portanto, a economia apresentada é uma estimativa teórica e não representa uma garantia de redução equivalente na conta de energia.

Para dimensionar um sistema real, é necessária uma avaliação técnica específica da residência.

## 8. Integração ao Citizen Assist AI

O simulador está integrado à página **Energia solar** da aplicação.

O usuário informa os dados de consumo e os parâmetros do sistema fotovoltaico. Em seguida, recebe a quantidade estimada de painéis, a geração mensal, a economia financeira estimada e o percentual de consumo atendido.

Esses resultados ajudam a comparar a energia solar com outras alternativas e apoiam a compreensão das possibilidades de utilização de fontes renováveis em residências.