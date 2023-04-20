# SCRIPT CRIADO POR DIEGO MARIN/VINICIUS JESUS
# FUNÇÃO: AUTOMATIZAR BUSCAS POR USUARIOS IAM E DELETAR
import boto3
import datetime
import dateutil.parser
from datetime import date
from botocore.exceptions import ClientError

# profiles = ["3Coracoes", "Fleetzil", "FleetzilQA"]
profiles = ["AWS 2Lar (Conceito Prd)", "AWS 3Coracoes", "AWS Abastece Ai (EAI)", "AWS Alcon", "AWS Allin", "AWS Aplic Teste", "AWS Araucaria Rail Tech IANR-Prd", "AWS Araucaria Rail Techs", "AWS Araucaria RailTech - Sydney", "AWS Brasil Saude", "AWS Britania", "AWS Britania Archiving", "AWS Britania DEVOPS", "AWS BRT", "AWS BRT Dev", "AWS BRT Hml", "AWS Canon", "AWS CDLBH", "AWS Cielo", "AWS CISA PRD", "AWS CloudBlue", "AWS Cloudpar", "AWS Cluster2Go", "AWS Cmtech", "AWS CPlug Apps", "AWS Credisis Alfresco", "AWS Credisis DBA Cobrança", "AWS Credisis DEV Corebanking", "AWS Credisis HML CoreBanking", "AWS Credisis HML ServCore", "AWS Credisis HML ServCore Composer", "AWS Credisis HML Trace", "AWS Credisis Microserviços HML", "AWS Credisis Network", "AWS Credisis PRD Core Banking", "AWS Credisis PRD ServCore", "AWS Credisis PRD Trace", "AWS Credisis QA Corebaking", "AWS Delivery Direto 2", "AWS DirectTalk", "AWS DNS NEXTIOS", "AWS Dooca", "AWS EMS Archiving", "AWS Evoy Hml", "AWS Evoy Prd", "AWS FDTE Prod", "AWS FDTE PSA", "AWS Fermentech", "AWS Fleetzil", "AWS Fleetzil-QA", "AWS Fourbank_DEV", "AWS FourBank_HML", "AWS Fourbank_PRD",
            "AWS FPromo", "AWS FPromo Prd", "AWS Gestão DS", "AWS HDT Digital", "AWS HDT Digital_HML", "AWS HDT-Saque-HML", "AWS HDT-Saque-PRD", "AWS Hospital Sao Judas", "AWS João Ribeiro", "AWS Lello DR", "AWS LifeSeg", "AWS MelhorEnvio AD", "AWS MelhorEnvio Centuriao", "AWS MelhorEnvio Lab", "AWS NEC", "AWS OmronBrasil", "AWS Pay4Fun", "AWS Pay4Fun Compliance", "AWS Pay4fun Global", "AWS Pay4Fun Veeam", "AWS Procenge", "AWS Procenge2", "AWS Prompt Solution", "AWS Roche PRD", "AWS Romagnole HML", "AWS RV BackOffice (Aplic)", "AWS RV Backup (Aplic)", "AWS RV Cellcard (Aplic)", "AWS RV Hub-Dev (Aplic)", "AWS RV Hub-Prod (Aplic)", "AWS Sombrero Susep", "AWS Trinovati", "AWS SAGRES PRD", "AWS Sawluz", "AWS Security Nextios", "AWS Social Miner antiga", "AWS Sodre Santoro Hml", "AWS Sodre Santoro Prd", "AWS Sol Millennium", "AWS Sombrero", "AWS Stericycle", "AWS Taggen", "AWS TaggenIoT", "AWS TCS PROD", "AWS Tray", "AWS Uninove", "AWS Universo Solicitações", "AWS Valeshop", "AWS Vegas AdminTI", "AWS Vegas Graal", "AWS Vigitrack", "AWS Vindi Aceita Prd", "AWS Vindi Dev", "AWS Vindi DPI", "AWS Vindi SBX", "AWS Vindi Sec", "AWS Vindi Smartbillrbm", "AWS VIVO", "AWS Yapay System"]

for profile in profiles:
    try:
        session = boto3.Session(profile_name=profile)
        client = session.client('iam')
        print("-----------------------------")
        print("\n["+profile+"]\n")
        response = client.list_users()

        for user in response['Users']:
            if 'valcan' in user['UserName']:
                print(user['UserName'])

    except Exception as e:
        print(f"Erro: {e}")