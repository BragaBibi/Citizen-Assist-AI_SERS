# Referências e Limitações — Citizen Assist AI

## 1. Referências utilizadas

As fontes abaixo foram selecionadas para fundamentar as informações sobre consumo de energia elétrica, eficiência energética, tarifas e geração solar fotovoltaica.

### 1.1. Agência Nacional de Energia Elétrica (ANEEL)

**Fonte:** Tarifas e Informações Econômico-Financeiras.

A ANEEL disponibiliza informações sobre tarifas homologadas das distribuidoras e explica a composição dos custos relacionados ao fornecimento de energia elétrica.

**Aplicação no projeto:** fundamenta a utilização da tarifa em R$/kWh e a explicação de que o custo estimado pelo Citizen Assist AI não representa necessariamente o valor final da conta de luz.

Link: https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/tarifas-e-informacoes-economico-financeiras

### 1.2. Empresa de Pesquisa Energética (EPE)

**Fonte:** Balanço Energético Nacional 2026 — Relatório Síntese, ano-base 2025.

O relatório apresenta informações sobre a oferta e o consumo de energia no Brasil, incluindo a participação das fontes renováveis na matriz elétrica.

Segundo a publicação, as fontes renováveis representaram 86,8% da matriz elétrica brasileira em 2025.

**Aplicação no projeto:** fundamenta o contexto da utilização de fontes renováveis e a discussão sobre energia solar na matriz elétrica brasileira.

Link: https://www.epe.gov.br/pt/imprensa/noticias/epe-publica-o-relatorio-sintese-do-balanco-energetico-nacional-2026

### 1.3. Instituto Nacional de Pesquisas Espaciais (INPE)

**Fonte:** Atlas Brasileiro de Energia Solar.

O Atlas disponibiliza dados climatológicos de potencial solar para diferentes localidades do território brasileiro, permitindo consultar informações em escala mensal.

**Aplicação no projeto:** fundamenta a importância das condições de irradiação solar na estimativa de geração fotovoltaica. O simulador atual utiliza horas de sol pleno informadas pelo usuário e não consulta automaticamente a base do INPE.

Link: https://www.gov.br/pt-br/servicos/obter-dados-do-atlas-brasileiro-de-energia-solar-atlas-solar

### 1.4. Programa Nacional de Conservação de Energia Elétrica (Procel) e Ministério de Minas e Energia (MME)

**Fonte:** Descubra como aplicar a eficiência energética no seu dia a dia.

A publicação apresenta orientações para reduzir desperdícios, como utilizar lâmpadas LED, escolher equipamentos eficientes e evitar o funcionamento desnecessário de aparelhos.

**Aplicação no projeto:** fundamenta as recomendações de eficiência energética oferecidas aos moradores.

Link: https://www.gov.br/mme/pt-br/assuntos/noticias/julho-26/descubra-como-aplicar-a-eficiencia-energetica-no-seu-dia-a-dia

## 2. Limitações dos cálculos de consumo

O cálculo de consumo utiliza a potência do equipamento, as horas de utilização diária e os dias de uso no mês.

A metodologia considera valores constantes durante o período informado. Na prática, o consumo pode variar conforme o funcionamento dos equipamentos e os hábitos dos moradores.

A tarifa é informada manualmente e não é atualizada automaticamente conforme a distribuidora, os impostos ou as bandeiras tarifárias.

Por esse motivo, o custo apresentado é uma estimativa simplificada.

## 3. Limitações da simulação solar

A simulação utiliza potência dos painéis, horas de sol pleno, eficiência e um período fixo de 30 dias.

O modelo não consulta automaticamente dados meteorológicos ou de irradiação solar da localização da residência.

Também não realiza um dimensionamento técnico completo, nem considera todos os fatores que influenciam a geração real, como orientação, inclinação, sombreamento, temperatura e perdas específicas do sistema.

O cálculo de economia não inclui investimento inicial, manutenção, financiamento ou regras de compensação de energia.

Assim, os resultados não devem ser utilizados como orçamento ou dimensionamento definitivo de uma instalação fotovoltaica.

## 4. Limitações da comparação energética

A comparação apresenta três cenários: energia convencional, energia solar e eficiência energética.

O cenário convencional utiliza o consumo e a tarifa informados pelo usuário.

O cenário solar utiliza a cobertura estimada pelo simulador fotovoltaico, enquanto o cenário de eficiência energética utiliza um percentual selecionado manualmente pelo usuário.

O percentual de eficiência representa uma hipótese de redução para fins de simulação, não uma economia comprovada.

O modelo não realiza uma análise financeira completa, não calcula o retorno do investimento solar e não quantifica as emissões de gases de efeito estufa de cada alternativa.

A comparação ambiental é qualitativa e deve considerar que a própria matriz elétrica brasileira possui participação expressiva de fontes renováveis.

## 5. Limitações das recomendações

As recomendações são geradas a partir do consumo e do custo mensal estimados.

Os limites utilizados pelo código, como consumo acima de 300 kWh e custo acima de R$ 200, são critérios internos definidos para orientar as respostas da aplicação. Não representam limites oficiais de consumo ou padrões universais de economia.

As recomendações têm caráter educativo e não substituem uma avaliação técnica específica da residência.

## 6. Considerações finais

O Citizen Assist AI foi desenvolvido como uma ferramenta educativa para auxiliar moradores a compreender o consumo residencial de energia elétrica e explorar alternativas de economia.

Os cálculos e recomendações permitem visualizar cenários e apoiar decisões mais conscientes, mas dependem dos parâmetros informados pelo usuário e das premissas adotadas.

Os resultados devem ser interpretados como estimativas, sem garantia de redução específica na conta de energia ou de geração fotovoltaica.

Para decisões reais de investimento e instalação, recomenda-se consultar profissionais qualificados e verificar as condições aplicáveis à residência.