import subprocess

# Abrir o arquivo e ler todas as linhas
with open('contas1.txt', 'r') as f:
    lines = f.readlines()

# Iterar sobre as linhas e executar o comando saml2aws
for profile in lines:
    aws_account = profile.strip()  # remova a quebra de linha no final da linha
    command = f'saml2aws login -a {aws_account}'
    subprocess.run(command, shell=True)
