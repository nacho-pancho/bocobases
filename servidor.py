#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# bibliotecas standard de Python
#
import hashlib # generar hashes
import os
import sys
import io
import base64
import time
# 
# paquetes publicos de Python
#
import bottle
from datetime import datetime

logfile = None
#
#----------------------------------------------------------------------------------------------------
# SERVICIO DE URLs / INTERFAZ DE USUARIO 
#----------------------------------------------------------------------------------------------------
#

@bottle.route('/report')
def main():
    estacion = bottle.request.query.get('id')
    tstamp   = int(bottle.request.query.get('tstamp'))
    status   = bottle.request.query.get('status')
    timedata = time.localtime(tstamp)
    timestr  = time.strftime('%Y-%m-%d-%H:%M:%S')
    print(timestr,estacion,status,file=logfile)
    logfile.flush()
    return("<html><header><title>mensaje recibido</title></header><body><p>Mensaje recibido fuerte y claro</p></body></html>");

#
#----------------------------------------------------------------------------------------------------
# INICIO DE SERVIDOR
#----------------------------------------------------------------------------------------------------
#
if __name__ == '__main__':
    fname = f'servidor_'+time.strftime('%Y%m%d_%H:%M:%S')+'.txt'
    with open(fname,'w') as f:
        logfile = f
        bottle.run(host='0.0.0.0',port='80',debug=True)

#
#----------------------------------------------------------------------------------------------------
# FIN
#----------------------------------------------------------------------------------------------------
#

