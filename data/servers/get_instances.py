import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from datetime import datetime
import ssl
 
def get_instance_data(url):
    try:
        ssl_context = ssl.create_default_context()
        with urllib.request.urlopen(url, context=ssl_context) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        print("Error:", e)
        return []
 
def filter_instance_types(instance, region):    
    allowed_prefixes = ['m6a', 'm5a', 'c6a', 'c5a', 'm6i', 'm5i', 'c6i', 'c5i', 'm5zn', 'm5n']
    return [(inst['instance_type'], inst['vCPU'], inst['memory']) for inst in instance if inst['instance_type'].startswith(tuple(allowed_prefixes)) and region in inst['availability_zones']]
 
def list_instance_types_in_region(region):
    url = "https://www.ec2instances.info/instances.json"
    instance_data = get_instance_data(url)
    filtered_instance_types = filter_instance_types(instance_data, region)
    return filtered_instance_types
 
def export_to_file(data, filename):
    with open(filename, 'w') as f:
        for instance_type, vCPU, memory in data:
            f.write(f"{instance_type},{vCPU},{round(memory)}\n")
 
def file_exists_recently(filename, days):
    if not os.path.exists(filename):
        return False
   
    file_creation_time = datetime.fromtimestamp(os.path.getctime(filename))
    current_time = datetime.now()
    return (current_time - file_creation_time).days <= days
 
if __name__ == "__main__":
    region = "sa-east-1"
    filename = os.getcwd() + "/data/servers/instance_types.txt"
    days = 30
 
    print("\n ------------------------------------------------------------ \n")
    print(f"Aguarde enquanto é feito a busca dos tipos de instâncias na região '{region}'...")
   
    arquivo_recente = file_exists_recently(filename, days)
   
    if arquivo_recente == False:
        with ThreadPoolExecutor(max_workers=5) as executor:
            future = executor.submit(partial(list_instance_types_in_region, region))
            filtered_instance_types = future.result()
       
        export_to_file(filtered_instance_types, filename)
 
        print(f"\nArquivo instance_types.txt foi criado/atualizado com sucesso")
        print("\n ------------------------------------------------------------ \n")
    else:
        print(f"\nHouve um erro na tentativa de atualizar o arquivo instance_types.txt")
        print("\n ------------------------------------------------------------ \n")