#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
'''
Sentinela de bases
Proyecto Bocosur
autor: Ignacio Ramírez
primera versión: Julio de 2021

PENDIENTE: leer imagen y enviarla
'''
import time
#import requests
import ftplib 
import sys
import os
import io
from PIL import Image

FTP_HOST='bolidos.fisica.edu.uy'
FTP_USER='cambiame'
FTP_PASS='cambiame'

def get_time_suffix():
    return time.strftime('%Y_%m_%d_%H_%M_%S') 


if __name__ == '__main__':

    ftp = ftplib.FTP(FTP_HOST)  # connect to host, default port
    
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
                #
                # login
                #
                ftp.login(user=FTP_USER,passwd=FTP_PASS,timeout=)
                #
                # ir a directorio correspondiente
                #
                ftp.cwd(FTP_DIR)
                #
                # enviar status
                # 
                status = "ok"
                rfname = f"{id_estacion}_{tstamp}.txt"
                txtf   = io.StringIO(f"{id_stacion} {tstamp} {status}")
                ftp.storlines(f"STOR {rfname} ",txtf)
                #
                # enviar imagen
                #
                ftp.storbinary(imgf)
                msg = tstamp_str + ':OK:'
                #
                # imprimir status actual a consola y archivo de log local
                #
                print(msg)
                print(msg,file=f)
            except ftplib.error_reply:
                msg = tstamp_str +':ERROR: respuesta inesperada de FTP'
                print(msg)
                print(msg,file=f)
            except ftplib.error_temp:
                msg = tstamp_str +':ERROR: error TEMPORAL de protocolo FTP'
                print(msg)
                print(msg,file=f)
            except ftplib.error_perm:
                msg = tstamp_str +':ERROR: error PERMANENTE de protocolo FTP'
                print(msg)
                print(msg,file=f)
            except ftplib.error_proto:
                msg = tstamp_str +':ERROR: error de protocolo FTP'
                # error desde el server HTTP
                print(msg)
                print(msg,file=f)

            except KeyboardInterrupt:
                print('Sentinela terminado manualmente,',time.asctime())
                exit(1)
            time.sleep(30) # 30 segundos



