"""
    MX Market es un programa en terminal que muestra los principales
    indicadores financieros del pais obtenidos del Banco de México (BANXICO)
    Autor: Santiago Sanchez
    Github: @SantiagoSF
 """

import requests
import json

"""
    El programa esta dividido en 2 funciones:
        main: aqui va la logica de la consulta
        menu: aqui va la logica para mostrar en pantalla

    Esto lo hice asi para poder mantener y actualizar de manera mas sencilla. 
"""

def main():
    """ Logica de consulta de la API. """

    # La url se constrye con los siguientes parametros: series a consultar
    # y fecha: puede ser una determinada, un rango u
    # 'oportuno' para el ultimo dato
    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/{0}'
    # Al agrega una nueva serie tambien es necesario agregar los indices de formateo
    # en la variable indicator de la funcion menu para poder imprimir.
    series = 'SF61745,SF331451,SF283,SF282,SF43718,SF110169,\
SP30577,SP74660,SP68257,SE40521,SP4,SL1'

    date = '/datos/oportuno'  # Agregar fecha despues de /datos/
    params = series + date
    url = url.format(params)
    
    headers = {
        'Accept': 'application/json',
        'Bmx-Token': # Token de ejemplo, obtener el personal en el API de BANXICO
            '20c757a458c3d560aa293c80de6891b99460e86f599853fca6a439d1f6438ad1',
        'Accept-Encoding': 'gzip'
        }
    response = requests.get(url, headers=headers)

    
     
    if response.status_code == 200:
        content_json = response.json()
        content_json = content_json['bmx']['series']
        data = []
        """ Codigo para guardar consulta en documento json.
            with open('response-banxico.json', 'w', encoding='utf8') as f:
            d = json.dumps(content_json, indent=4, ensure_ascii=False)
            f.write(d) """

        for dictionary in content_json:
            for values in dictionary['datos']:
                data.append(
                    (dictionary['titulo'][:40],
                        values['fecha'],
                        values['dato'])
                    )

        menu(data)


def menu(data):
    """ Funcion para imprimir por terminal el resultado de las consultas."""

    msg = """ \n\t\t\t\t\t\tHola! Bienvenido MX Market!
\t\t\tAquí encontraras informacion relevante del Banco de México (BANXICO)
\tsobre los principales indicadores financieros del país. Son mostrados al\
 ultimo dato oportuno liberado por BANXICO.
     """

    # Este es la variable conteniendo lo que se mostrara en terminal.
    # Sera formateado con los respectivos datos y se
    # representara cada dato en una columna y fila
    indicator = """
-----------------------------------------------------------------------------------------------------------------------------
| {0}{3}{6}
|                                         |                                        |                                        |
 \t{1}\t {4}\t{7}
|                                         |                                        |                                        |
 \t{2}\t{5}\t{8}
|-----------------------------------------|----------------------------------------------------------------------------------
|                                         |                                        |                                        |
| {9}{12}{15}
|                                         |                                        |                                        |
 \t{10}\t{13}\t{16}
|                                         |                                        |                                        |
  \t{11}\t{14}\t{17}
|                                         |                                        |                                        |
 -----------------------------------------------------------------------------------------------------------------------------
|                                         |                                        |                                        |
| {18}{21}{24}
|                                         |                                        |                                        |
 \t{19}\t{22}\t{25}
|                                         |                                        |                                        |
  \t{20}\t{23}\t{26}
|                                         |                                        |                                        |
 -----------------------------------------------------------------------------------------------------------------------------
|                                         |                                        |                                        |
| {27}{30}{33}
|                                         |                                        |                                        |
 \t{28}\t{31}\t{34}
|                                         |                                        |                                        |
  \t{29}\t{32}\t{35}
|                                         |                                        |                                        |
 -----------------------------------------------------------------------------------------------------------------------------
    """

    # Creamos una variables para almacenar los respectivos datos formateados para sumarse
    # a indicators
    indicator_list = []
    for array in data:
        title = array[0]
        # Sumamos los espacios necesarios para alinear columnas en 'indicators'
        title += ' ' * (40-len(title))

        digit = array[2]
        digit = str(digit) + ' ' * (34-len(str(digit)))

        time = array[1]
        time += ' ' * (34-len(time))

        # Sumamos los datos formateados en el siguiente orden para ser
        #  mostrados de esa forma
        indicator_list.append(title + "|")
        indicator_list.append(digit)
        indicator_list.append(time)

    # Imprimimos el msj de bienvenida y la lista de indicadores formateada
    print(msg)
    display_data = indicator.format(*indicator_list)
    print(display_data)


if __name__ == "__main__":
    main()
