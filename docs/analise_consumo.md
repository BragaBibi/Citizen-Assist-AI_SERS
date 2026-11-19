# Análise de Consumo de Energia — Citizen Assist AI

## 1. Objetivo

A análise de consumo do Citizen Assist AI tem como objetivo auxiliar moradores de residências a compreender o consumo de energia elétrica de seus equipamentos e estimar os custos associados à sua utilização.

A ferramenta permite inserir informações de um equipamento e visualizar o consumo mensal estimado em quilowatt-hora (kWh) e seu custo aproximado em reais (R$).

## 2. Dados utilizados

A calculadora utiliza os seguintes dados informados pelo usuário:

| Dado | Unidade | Descrição |
|---|---|---|
| Potência do equipamento | Watt (W) | Potência elétrica do equipamento |
| Horas de uso por dia | Horas (h) | Tempo médio de utilização diária |
| Dias de utilização no mês | Dias | Quantidade de dias de uso no período |
| Tarifa de energia | R$/kWh | Valor informado para cada quilowatt-hora consumido |

Os dados são inseridos manualmente pelo usuário. Portanto, a aplicação não realiza medições diretamente nos equipamentos nem consulta automaticamente a conta de energia da residência.

## 3. Origem dos dados e período considerado

Os dados utilizados na análise são fornecidos pelo próprio usuário, de acordo com as características e os hábitos de utilização dos equipamentos residenciais.

A análise considera um período mensal, utilizando a quantidade de dias de utilização informada pelo usuário. O sistema permite informar de 1 a 31 dias de uso no mês.

A tarifa também é informada manualmente. O valor inicial apresentado pela aplicação é de R$ 0,80/kWh, utilizado apenas como parâmetro de demonstração.

Assim, os resultados são estimativas calculadas a partir dos parâmetros inseridos, e não medições reais de uma residência específica.

## 4. Metodologia e fórmulas

O cálculo do consumo mensal é realizado pela função `calculate_consumption()`, localizada no arquivo `modules/energy/consumption.py`.

A fórmula utilizada é:

**Consumo mensal (kWh) = [Potência (W) × Horas de uso por dia × Dias de utilização] ÷ 1.000**

A divisão por 1.000 converte o resultado de watt-hora (Wh) para quilowatt-hora (kWh).

Após calcular o consumo, a função `calculate_cost()` estima o custo mensal:

**Custo mensal (R$) = Consumo mensal (kWh) × Tarifa (R$/kWh)**

Essas funções permitem estimar o impacto do uso de cada equipamento no consumo e nos gastos com energia elétrica.

## 5. Exemplo de aplicação

Para demonstrar o funcionamento da calculadora, foram utilizados os valores iniciais apresentados pelo sistema:

| Parâmetro | Valor |
|---|---:|
| Equipamento | Chuveiro elétrico |
| Potência | 5.500 W |
| Horas de uso por dia | 1 hora |
| Dias de utilização | 30 dias |
| Tarifa de demonstração | R$ 0,80/kWh |

**Cálculo do consumo:**

(5.500 × 1 × 30) ÷ 1.000 = 165 kWh/mês

**Cálculo do custo:**

165 × 0,80 = R$ 132,00/mês

Portanto, nesse cenário hipotético, o chuveiro apresenta um consumo mensal estimado de 165 kWh e um custo de R$ 132,00.

Os valores apresentados são exemplos de simulação e não representam uma medição real.

## 6. Como a análise contribui para a economia de energia

A análise permite que o usuário identifique equipamentos com consumo elevado e compreenda como o tempo de utilização influencia os gastos com eletricidade.

Com essas informações, o morador pode avaliar mudanças nos hábitos de consumo, como reduzir o tempo de utilização de determinados equipamentos e evitar desperdícios.

Os resultados também servem como referência para as demais funcionalidades do Citizen Assist AI, especialmente a comparação energética e a simulação de energia solar.

## 7. Premissas e limitações

A calculadora utiliza uma metodologia simplificada e considera que a potência informada e o tempo de utilização permanecem constantes durante o período analisado.

Na prática, o consumo pode variar conforme o funcionamento do equipamento, sua eficiência, as condições de utilização e os hábitos dos moradores.

O custo calculado não representa necessariamente o valor final da conta de energia, pois não considera automaticamente impostos, taxas, bandeiras tarifárias, iluminação pública ou outros componentes da cobrança.

A precisão da estimativa depende da qualidade dos dados informados pelo usuário. Por isso, os resultados devem ser interpretados como referências para análise e planejamento, e não como valores garantidos.

## 8. Integração ao Citizen Assist AI

A análise de consumo está integrada à página **Consumo de energia** do assistente.

Após informar os parâmetros solicitados, o usuário recebe os resultados de consumo mensal e custo estimado. Essas informações ajudam a compreender os gastos associados aos equipamentos e servem de apoio às orientações de economia energética apresentadas pelo sistema.
