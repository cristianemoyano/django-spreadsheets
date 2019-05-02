import datetime
import operator
from google_sheets.google_spreadsheets import get_work_sheets
from autotest.models import Responses


def get_bool_value_from_string(value):
    if value == 'Si':
        return True
    return False


def get_datetime_from_string(datetime_str):
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M:%S")


def generate_responses_from_spreadsheets(title):
    ws = get_work_sheets(title)
    all_records = ws.get_all_records()
    for data in all_records:
            row = list(data.values())
            mapping = {
                'marca_temporal': get_datetime_from_string(row[0]),
                'nombre_completo': row[1],
                'dni': row[2],

                'uno_1': get_bool_value_from_string(row[3]),
                'uno_2': get_bool_value_from_string(row[4]),
                'uno_3': get_bool_value_from_string(row[5]),
                'uno_4': get_bool_value_from_string(row[6]),
                'uno_5': get_bool_value_from_string(row[7]),
                'uno_6': get_bool_value_from_string(row[8]),
                'uno_7': get_bool_value_from_string(row[9]),
                'uno_8': get_bool_value_from_string(row[10]),
                'uno_9': get_bool_value_from_string(row[11]),
                'uno_10': get_bool_value_from_string(row[12]),

                'dos_1': get_bool_value_from_string(row[13]),
                'dos_2': get_bool_value_from_string(row[14]),
                'dos_3': get_bool_value_from_string(row[15]),
                'dos_4': get_bool_value_from_string(row[16]),
                'dos_5': get_bool_value_from_string(row[17]),
                'dos_6': get_bool_value_from_string(row[18]),
                'dos_7': get_bool_value_from_string(row[19]),
                'dos_8': get_bool_value_from_string(row[20]),
                'dos_9': get_bool_value_from_string(row[21]),
                'dos_10': get_bool_value_from_string(row[22]),

                'tres_1': get_bool_value_from_string(row[23]),
                'tres_2': get_bool_value_from_string(row[24]),
                'tres_3': get_bool_value_from_string(row[25]),
                'tres_4': get_bool_value_from_string(row[26]),
                'tres_5': get_bool_value_from_string(row[27]),
                'tres_6': get_bool_value_from_string(row[28]),
                'tres_7': get_bool_value_from_string(row[29]),
                'tres_8': get_bool_value_from_string(row[30]),
                'tres_9': get_bool_value_from_string(row[31]),
                'tres_10': get_bool_value_from_string(row[32]),

                'cuatro_1': get_bool_value_from_string(row[33]),
                'cuatro_2': get_bool_value_from_string(row[34]),
                'cuatro_3': get_bool_value_from_string(row[35]),
                'cuatro_4': get_bool_value_from_string(row[36]),
                'cuatro_5': get_bool_value_from_string(row[37]),
                'cuatro_6': get_bool_value_from_string(row[38]),
                'cuatro_7': get_bool_value_from_string(row[39]),
                'cuatro_8': get_bool_value_from_string(row[40]),
                'cuatro_9': get_bool_value_from_string(row[41]),
                'cuatro_10': get_bool_value_from_string(row[42]),

                'cinco_1': get_bool_value_from_string(row[43]),
                'cinco_2': get_bool_value_from_string(row[44]),
                'cinco_3': get_bool_value_from_string(row[45]),
                'cinco_4': get_bool_value_from_string(row[46]),
                'cinco_5': get_bool_value_from_string(row[47]),
                'cinco_6': get_bool_value_from_string(row[48]),
                'cinco_7': get_bool_value_from_string(row[49]),
                'cinco_8': get_bool_value_from_string(row[50]),
                'cinco_9': get_bool_value_from_string(row[51]),
                'cinco_10': get_bool_value_from_string(row[52]),

                'seis_1': get_bool_value_from_string(row[53]),
                'seis_2': get_bool_value_from_string(row[54]),
                'seis_3': get_bool_value_from_string(row[55]),
                'seis_4': get_bool_value_from_string(row[56]),
                'seis_5': get_bool_value_from_string(row[57]),
                'seis_6': get_bool_value_from_string(row[58]),
                'seis_7': get_bool_value_from_string(row[59]),
                'seis_8': get_bool_value_from_string(row[60]),
                'seis_9': get_bool_value_from_string(row[61]),
                'seis_10': get_bool_value_from_string(row[62]),

                'siete_1': get_bool_value_from_string(row[63]),
                'siete_2': get_bool_value_from_string(row[64]),
                'siete_3': get_bool_value_from_string(row[65]),
                'siete_4': get_bool_value_from_string(row[66]),
                'siete_5': get_bool_value_from_string(row[67]),
                'siete_6': get_bool_value_from_string(row[68]),
                'siete_7': get_bool_value_from_string(row[69]),
                'siete_8': get_bool_value_from_string(row[70]),
                'siete_9': get_bool_value_from_string(row[71]),
                'siete_10': get_bool_value_from_string(row[72]),

                'ocho_1': get_bool_value_from_string(row[73]),
                'ocho_2': get_bool_value_from_string(row[74]),
                'ocho_3': get_bool_value_from_string(row[75]),
                'ocho_4': get_bool_value_from_string(row[76]),
                'ocho_5': get_bool_value_from_string(row[77]),
                'ocho_6': get_bool_value_from_string(row[78]),
                'ocho_7': get_bool_value_from_string(row[79]),
                'ocho_8': get_bool_value_from_string(row[80]),
                'ocho_9': get_bool_value_from_string(row[81]),
                'ocho_10': get_bool_value_from_string(row[82]),
            }

            uno = [
                get_bool_value_from_string(row[3]),
                get_bool_value_from_string(row[4]),
                get_bool_value_from_string(row[5]),
                get_bool_value_from_string(row[6]),
                get_bool_value_from_string(row[7]),
                get_bool_value_from_string(row[8]),
                get_bool_value_from_string(row[9]),
                get_bool_value_from_string(row[10]),
                get_bool_value_from_string(row[11]),
                get_bool_value_from_string(row[12]),
            ].count(True)

            dos = [
                get_bool_value_from_string(row[13]),
                get_bool_value_from_string(row[14]),
                get_bool_value_from_string(row[15]),
                get_bool_value_from_string(row[16]),
                get_bool_value_from_string(row[17]),
                get_bool_value_from_string(row[18]),
                get_bool_value_from_string(row[19]),
                get_bool_value_from_string(row[20]),
                get_bool_value_from_string(row[21]),
                get_bool_value_from_string(row[22]),
            ].count(True)

            tres = [
                get_bool_value_from_string(row[23]),
                get_bool_value_from_string(row[24]),
                get_bool_value_from_string(row[25]),
                get_bool_value_from_string(row[26]),
                get_bool_value_from_string(row[27]),
                get_bool_value_from_string(row[28]),
                get_bool_value_from_string(row[29]),
                get_bool_value_from_string(row[30]),
                get_bool_value_from_string(row[31]),
                get_bool_value_from_string(row[32]),
            ].count(True)
            cuatro = [
                get_bool_value_from_string(row[33]),
                get_bool_value_from_string(row[34]),
                get_bool_value_from_string(row[35]),
                get_bool_value_from_string(row[36]),
                get_bool_value_from_string(row[37]),
                get_bool_value_from_string(row[38]),
                get_bool_value_from_string(row[39]),
                get_bool_value_from_string(row[40]),
                get_bool_value_from_string(row[41]),
                get_bool_value_from_string(row[42]),
            ].count(True)

            cinco = [
                get_bool_value_from_string(row[43]),
                get_bool_value_from_string(row[44]),
                get_bool_value_from_string(row[45]),
                get_bool_value_from_string(row[46]),
                get_bool_value_from_string(row[47]),
                get_bool_value_from_string(row[48]),
                get_bool_value_from_string(row[49]),
                get_bool_value_from_string(row[50]),
                get_bool_value_from_string(row[51]),
                get_bool_value_from_string(row[52]),
            ].count(True)

            seis = [
                get_bool_value_from_string(row[53]),
                get_bool_value_from_string(row[54]),
                get_bool_value_from_string(row[55]),
                get_bool_value_from_string(row[56]),
                get_bool_value_from_string(row[57]),
                get_bool_value_from_string(row[58]),
                get_bool_value_from_string(row[59]),
                get_bool_value_from_string(row[60]),
                get_bool_value_from_string(row[61]),
                get_bool_value_from_string(row[62]),
            ].count(True)

            siete = [
                get_bool_value_from_string(row[63]),
                get_bool_value_from_string(row[64]),
                get_bool_value_from_string(row[65]),
                get_bool_value_from_string(row[66]),
                get_bool_value_from_string(row[67]),
                get_bool_value_from_string(row[68]),
                get_bool_value_from_string(row[69]),
                get_bool_value_from_string(row[70]),
                get_bool_value_from_string(row[71]),
                get_bool_value_from_string(row[72]),
            ].count(True)
            ocho = [
                get_bool_value_from_string(row[73]),
                get_bool_value_from_string(row[74]),
                get_bool_value_from_string(row[75]),
                get_bool_value_from_string(row[76]),
                get_bool_value_from_string(row[77]),
                get_bool_value_from_string(row[78]),
                get_bool_value_from_string(row[79]),
                get_bool_value_from_string(row[80]),
                get_bool_value_from_string(row[81]),
                get_bool_value_from_string(row[82]),
            ].count(True)

            stats_yes = {
                'uno': uno,
                'dos': dos,
                'tres': tres,
                'cuatro': cuatro,
                'cinco': cinco,
                'seis': seis,
                'siete': siete,
                'ocho': ocho,
            }
            maximo = max(stats_yes.items(), key=operator.itemgetter(1))
            maximo_segundo = (0, 0)
            for key, val in stats_yes.items():
                if (val > maximo_segundo[1] and val < maximo[1]):
                        maximo_segundo = (key, val)

            inteligencias_multiples_map = {
                'uno': 'Inteligencia Lingüística-verbal',
                'dos': 'Inteligencia Lógico-Matemática',
                'tres': 'Inteligencia Viso-Espacial',
                'cuatro': 'Inteligencia Cinético-Corporal',
                'cinco': 'Inteligencia Musical',
                'seis': 'Inteligencia Interpersonal',
                'siete': 'Inteligencia Intrapersonal',
                'ocho': 'Inteligencia Naturalista',
            }
            stats_maximo = {
                'key_max_first': inteligencias_multiples_map.get(maximo[0], ''),
                'val_max_first': maximo[1],
                'map_key_first': maximo[0],
                'percent_max_first': '{0:.2f}%'.format((maximo[1] / 10 * 100)),
                'key_max_second': inteligencias_multiples_map.get(maximo_segundo[0], ''),
                'val_max_second': maximo_segundo[1],
                'percent_max_second': '{0:.2f}%'.format((maximo_segundo[1] / 10 * 100)),
                'map_key_second': maximo_segundo[0],
            }
            mapping.update(stats_maximo)
            try:
                Responses.objects.create(**mapping)
            except Exception:
                pass
