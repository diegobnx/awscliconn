# SCRIPT CRIADO POR DIEGO MARIN
# FUNÇÃO: AUTOMATIZAR BUSCAS POR USUARIOS IAM
import boto3

profiles = ["PROFILES"]

for profile in profiles:
    try:
        session = boto3.Session(profile_name=profile)
        client = session.client('iam')
        print("-----------------------------")
        print("\n["+profile+"]\n")
        response = client.list_users()

        for user in response['Users']:
            if 'filtrar_users' in user['UserName']:
                print(user['UserName'])

    except Exception as e:
        print(f"Erro: {e}")
