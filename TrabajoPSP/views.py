from django.http import HttpResponse
import datetime

def saludo(request): # Primera vista

    documento = """<html>
    <body>
    <h1>
    ¡Hola mundo! ¡Este es nuestro primer trabajo con Django!
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, anio):

    periodo = anio - 2022
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" % (anio, edadFutura)

    return HttpResponse(documento)