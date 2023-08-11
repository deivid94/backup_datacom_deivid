import paramiko;
import tftpy
import csv
import pandas as pd
  
#devices = {"hostname":"Pedra_branca", "ip":"172.24.13.4 ", "username":"backup", "password":"backup"}
def carrega_dados_olt():
  dados = pd.read_csv('data\dados_olts.csv')
  return dados

def conecta_olt_e_pega_dados(ip, usuario, senha):
   #ip = dados_conexao_olt=["ip"]
   #usuario = dados_conexao_olt=["usuario"]
    #senha = dados_conexao_olt=["senha"] 
  try:
    ssh_olt = paramiko.SSHClient()
    ssh_olt.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
    ssh_olt.connect(hostname=ip, username=usuario, password=senha) 
    ##se backup.txt  existe
      #pegar backup backup.txt
      


    ssh_olt.close()
    return True
  except Exception as e:
    print(f"Falha ao conecta-se a OLT {ip}: {e}")
    return False
def  ():
