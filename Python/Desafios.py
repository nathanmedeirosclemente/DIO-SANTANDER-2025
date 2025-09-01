# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:


def validar_email(email):
    # Não pode conter espaços
    if " " in email:
        return "E-mail inválido"
    # Deve conter exatamente um @
    if email.count("@") != 1:
        return "E-mail inválido"
    # Não pode começar ou terminar com @
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    # Deve conter um domínio após o @
    usuario, dominio = email.split("@")
    if not usuario or not dominio:
        return "E-mail inválido"
    # Domínio deve conter pelo menos um ponto
    if "." not in dominio:
        return "E-mail inválido"
    return "E-mail válido"


print(validar_email(email))
