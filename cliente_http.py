#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import time
import requests
import sys
import os

def get_time_suffix():
    return time.strftime('%Y_%m_%d_%H_%M_%S') 


if __name__ == '__main__':

    id_estacion = 'indef'
    if len(sys.argv) > 1:
        id_estacion = sys.argv[1]
    
    log_fname = 'estacion_'+id_estacion+'_'+get_time_suffix()+'.txt'

    with open(log_fname,'w') as f:
        print('Sentinela iniciado, estacion',id_estacion,'fecha',time.asctime())
        for r in range(12*240): # correr por 10 dias
            tstamp     = int(time.time())
            tstamp_str = time.strftime('%Y%m%d-%H:%M:%S') 
            try:
                consulta = requests.get(f'http://gongorg.ddns.net/report?id={id_estacion}&status=ok&tstamp={tstamp}',timeout=1.000)
                msg = tstamp_str + ':OK: codigo ' + str(consulta.status_code)
                print(msg)
                print(msg,file=f)
            except requests.exceptions.Timeout:
                msg = tstamp_str +':ERROR: excedido tiempo de espera para conectar'
                # timeout intentando conectarse 
                print(msg)
                print(msg,file=f)
            except requests.exceptions.ConnectionError:
                # error al intentar conectarse
                msg = tstamp_str +':ERROR: no se pudo establecer conexión'
                print(msg)
                print(msg,file=f)
            except requests.exceptions.HTTPError:
                msg = tstamp_str +':ERROR: error de protocolo HTTP'
                # error desde el server HTTP
                print(msg)
                print(msg,file=f)
            except KeyboardInterrupt:
                print('Sentinela terminado manualmente,',time.asctime())
                exit(1)
            time.sleep(30) # 30 segundos



