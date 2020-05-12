# coding: utf-8

'''
Genera html de páginas de wiki

'''

import requests
from slugify import slugify
import json
import os

DESTINO = 'html'
if not os.path.exists(DESTINO):
    os.mkdir(DESTINO)


vitalinux = 'https://wiki.vitalinux.educa.aragon.es/index.php?curid={}&action=render'

# 500 paginas en espacio de nombres 0 !!
allpages = 'https://wiki.vitalinux.educa.aragon.es/api.php?action=query&list=allpages&aplimit=500&format=json'

r = requests.get(allpages)

paginas = json.loads(r.text)
paginas = [p for p in paginas['query']['allpages']]

# pageid y title 
# guardar en html
for p in paginas:
    curid = p.get('pageid')
    titulo = p.get('title')
    respuesta = requests.get(vitalinux.format(curid))
    if respuesta.ok:
        open('{}/{}.html'.format(DESTINO, slugify(titulo)), 'w').write(respuesta.text)
    else:
        print('ERROR', titulo)
