# SCRIPT CRIADO POR DIEGO MARIN
import boto3

profiles = ["SamlProfile"]

for profile in profiles:
    try:
        session = boto3.Session(profile_name=profile)
        print("-----------------------------")
        print("\n["+profile+"]\n")

        regions = ['us-east-1', 'sa-east-1']

        for region in regions:
            print(f"VERIFICANDO REGIAO {region}")
            print("===========================================")
            client = session.client('backup', region_name=region)

            response = client.list_backup_vaults()
            vaults = response.get('BackupVaultList', [])
            num_vaults = len(vaults)

            if num_vaults != 0:
                for vault in vaults:
                    vault_name = vault['BackupVaultName']
                    response = client.list_recovery_points_by_backup_vault(
                        BackupVaultName=vault_name)
                    recovery_points = response.get('RecoveryPoints', [])
                    num_recovery_points = len(recovery_points)

                    if num_recovery_points != 0:
                        print(
                            f"EXISTEM {num_recovery_points} BACKUPS NO VAULT {vault_name}")
                    else:
                        print(f"NÃO EXISTEM BACKUPS NO VAULT {vault_name}")
            else:
                print("NÃO EXISTEM VAULTS NA CONTA")

            print("===========================================")

    except Exception as e:
        print(f"Erro: {e}")
