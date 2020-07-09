""" 
    MX Market es un programa en terminal que muestra los principales indicadores financieros del pais obtenidos del Banco de México (BANXICO)
    Autor: Santiago Sanchez
    Github: @SantiagoSF
 """

import requests
# import json


def main():
    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF61745,SF331451,SF283,SF282,SF43718,SF110169/datos/oportuno'
    headers = {
        'Accept': 'application/json',
        'Bmx-Token': # Token de ejemplo, obtener el personal en el API de BANXICO
            '20c757a458c3d560aa293c80de6891b99460e86f599853fca6a439d1f6438ad1',
        'Accept-Encoding': 'gzip'
        }
    response = requests.get(url, headers=headers)

    # print(response)
    if response.status_code == 200:
        content_json = response.json()
        content_json = content_json['bmx']['series']
        data = []

        for dictionary in content_json:
            for values in dictionary['datos']:
                data.append((dictionary['titulo'][:40],values['fecha'], values['dato']))

        menu(data)



def menu(data):
    msg = """ \n\t\t\t\t\t\tHola! Bienvenido MX Market!
\t\t\tAquí encontraras informacion relevante del Banco de México (BANXICO)
\tsobre los principales indicadores financieros del país. Son mostrados al ultimo dato oportuno liberado por BANXICO.\n
     """

    indicator= """
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
    """
    indicator_list = []
    for array in data:
        title = array[0]
        title += ' ' * (40-len(title))

        digit = array[2]
        digit = str(digit) + ' ' * (34-len(str(digit)))

        time = array[1]
        time += ' ' * (34-len(time))

        indicator_list.append(title + "|")
        indicator_list.append(digit)
        indicator_list.append(time)

    print(msg)
    display_data = indicator.format(*indicator_list)
    print(display_data)

    # print(indicators_table.format(indicator_list[0],indicator_list[1],indicator_list[2],indicator_list[3],indicator_list[4],indicator_list[5]))

if __name__ == "__main__":
    main()
