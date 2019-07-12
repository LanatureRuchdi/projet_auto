import requests
import json
import re
import time
import datetime
from pyzabbix import ZabbixAPI

# url = "http://192.168.126.129/zabbix/api_jsonrpc.php"

# from pyzabbix import ZabbixAPI

# Connexion à l'interface

SERVEUR_ZABBIX='http://192.168.126.129/zabbix'
zbx = ZabbixAPI(SERVEUR_ZABBIX,user='Admin',password='zabbix')

# Récupération des IDs de tous les hotes (liste),et les noms d'hotes sous forme de liste de dictionnaire
#  liste des dictionnaires
liste_dict = zbx.host.get(output=['hostid','host'])

# print(liste_dict)                                    # type (list)
# print (type(all_id))


# lister les valeurs retournées(hosts,hostids)
# for host_id in all_id:
#     print ("les id et serveurs existant dans ce reseau sont:",host_id)
    # print(host_id)

#  separation de la liste afin d'avoir des dictionnaires 
# Liste des HOSTIDs
print("la liste des hostIDs est:")
i = 0
for element in liste_dict:
    onedict_id = liste_dict[i] 
    i+=1
    un_hostid = onedict_id.get("hostid")
    # print(element)
                                              
    for element in un_hostid:
        hostIDs = onedict_id.get("hostid")
    print(hostIDs)                                    #str
   

# liste des SERVEURS
print("la liste des serveurs est:")
i = 0
for element in liste_dict:
    onedict_id = liste_dict[i] 
    i+=1
    un_hostid = onedict_id.get("host")
    # print(element)
                                               
    for element in un_hostid:
        Hosts = onedict_id.get("host")
    print(Hosts)                                         #str
      

                               
#  Récuperer les valeurs(hostIDs) dans le dictionnaire
# print("toutes les valeurs")
# for hostID in onedict_id.values():
#     print(hostID)



# récupérer pour un hote.

j = 0
for items in hostIDs:
    items = zbx.item.get(hostid = [hostIDs],
    search = {'key_' : 'vfs.fs.size' },
    output = ['itemid','name','key'])[j]
    j+=1
    print(items)
    print(type(items))
