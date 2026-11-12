"""Exemplo de regra problemática e de bloqueio para revisão. CEP fictício."""

def regra_original(cep):
    if cep == "00000-000":
        return "negar"
    return "continuar análise"


def controle_juridico(usa_cep_para_negar):
    if usa_cep_para_negar:
        return "SUSPENDER: justificar o critério e testar o impacto"
    return "PENDENTE: revisar demais dados e critérios"


if __name__ == "__main__":
    print(regra_original("00000-000"))
    print(controle_juridico(True))
    assert regra_original("00000-000") == "negar"
    assert controle_juridico(True).startswith("SUSPENDER")
