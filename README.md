# Um sistema pode negar serviço só pelo CEP?

Considere esta regra fictícia:

```python
def avaliar(cep):
    if cep == "00000-000":
        return "negar"
    return "continuar análise"
```

1. **Código:** todos os moradores daquele CEP recebem a mesma negativa, sem exame individual.
2. **Resultado:** a regra pode reproduzir exclusão territorial ou funcionar como substituta indireta de características sociais. O código funcionar corretamente não comprova que o critério seja justo ou lícito.
3. **Fundamento:** a LGPD veda tratamento discriminatório ilícito ou abusivo. Quando uma decisão que afeta interesses é tomada **unicamente** com base em tratamento automatizado de dados pessoais, o titular pode solicitar revisão e informações sobre os critérios e procedimentos.
4. **Decisão do gestor:** exigir justificativa para o CEP, testar o impacto nos grupos afetados, examinar alternativas menos prejudiciais e guardar a versão da regra aplicada.

**Papel do advogado:** não declarar que qualquer uso de localização é proibido; verificar a finalidade concreta e impedir que uma correlação estatística seja tratada, sem crítica, como motivo suficiente para excluir uma pessoa.

Fontes: [LGPD, arts. 6º, IX, e 20](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm) e [ANPD — direitos dos titulares](https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares).

*Exemplo didático com CEP fictício, não aplicável a pessoas reais.*
