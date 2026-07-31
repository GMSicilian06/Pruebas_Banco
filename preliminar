import pandas as pd
from pandas import DataFrame
import requests


TC = 36.6243

pd.set_option('display.max_rows', None)

Variable_BG = [
'Activo ()',
'Moneda Nacional (Efectivo y Equivalentes de Efectivo)',
'Caja (Moneda Nacional)',
'Banco Central de Nicaragua (Moneda Nacional)',
'Instituciones Financieras (Moneda Nacional)',
'Depósitos Restringidos (Moneda Nacional)',
'Equivalentes de Efectivo (Moneda Nacional)',
'Moneda Extranjera (Efectivo y Equivalentes de Efectivo)',
'Caja (Moneda Extranjera)',
'Banco Central de Nicaragua (Moneda Extranjera)',
'Instituciones Financieras (Moneda Extranjera)',
'Depósitos Restringidos (Moneda Extranjera)',
'Equivalentes de Efectivo (Moneda Extranjera)',
'Inversiones a Valor Razonable con Cambios en Resultados (Activo)'
'Inversiones a Valor Razonable con Cambios en Otro Resultado Integral (Activo)',
'Cartera a Costo Amortizado (Activo)',
'Inversiones a Costo Amortizado, Neto (Activo)',
'Cartera de Créditos, Neta (Activo)',
'Vigentes (Cartera de Créditos, Neta)',
'Prorrogados (Cartera de Créditos, Neta)',
'Reestructurados (Cartera de Créditos, Neta)',
'Vencidos (Cartera de Créditos, Neta)',
'Cobro Judicial (Cartera de Créditos, Neta)',
'(-) Comisiones Devengadas con la Tasa de Interés Efectiva (Cartera de Créditos, Neta)',
'Intereses y Comisiones por Cobrar sobre Cartera de Créditos (Cartera de Créditos, Neta)',
'(-) Provisión de Cartera de Créditos (Cartera de Créditos, Neta)',
'Cuentas por Cobrar, Neto (Activo)',
'Activos Recibidos en Recuperación de Créditos (Activo)',
'Participaciones (Activo)',
'Activo Material (Activo)',
'Activos Intangibles (Activo)',
'Activos Fiscales (Activo)',
'Otros Activos (Activo)',
'Pasivo ()',
'Pasivos Financieros a Costo Amortizado (Pasivo)',
'Obligaciones con el Público (Pasivo)',
'Moneda Nacional (Obligaciones con el Público)',
'Depósitos a la Vista (Moneda Nacional)',
'Depósitos de Ahorro (Moneda Nacional)',
'Depósitos a Plazo (Moneda Nacional)',
'Moneda Extranjera (Obligaciones con el Público)',
'Depósitos a la Vista (Moneda Extranjera)',
'Depósitos de Ahorro (Moneda Extranjera)',
'Depósitos a Plazo (Moneda Extranjera)',
'Intereses sobre Obligaciones con el Público por Depósitos (Obligaciones con el Público)',
'Otras Obligaciones Diversas con el Público (Pasivo)',
'Obligaciones por Depósitos de Instituciones Financieras y de Organismos Internacionales (Pasivo)',
'Obligaciones por Emisión de Deuda (Pasivo)',
'Obligaciones con Instituciones Financieras y por otros Financiamientos (Pasivo)',
'Obligaciones con el Banco Central de Nicaragua (Pasivo)',
'Pasivos Fiscales (Pasivo)',
'Obligaciones Subordinadas y/o Convertibles en Capital (Pasivo)',
'Otros Pasivos y Provisiones (Pasivo)',
'PATRIMONIO ()',
'Fondos Propios (PATRIMONIO)',
'Capital Social Pagado (Fondos Propios)',
'Aportes a Capitalizar (Fondos Propios)',
'Capital Donado (Fondos Propios)',
'Reservas Patrimoniales (Fondos Propios)',
'Resultados Acumulados (Fondos Propios)',
'Resultado del Ejercicio (Fondos Propios)',
'Otro Resultado Integral Neto (PATRIMONIO)',
'Ajustes de Transición (PATRIMONIO)',
'CUENTAS CONTINGENTES ()',
'CUENTAS DE ORDEN ()',
'Diferimiento de comisiones y otros (Cartera de Créditos, Neta)'
]

Variable_IF = [ 
'2.- Vulnerabilidad del Patrimonio', '9. Tarjetas de Crédito Personales', '1. Exposición de partes relacionadas (%)', 
'2. Ganadería', 'Cobertura de la Cartera de Créditos Improductiva Bruta', '1.- Total Activos Improductivos netos', 
'7. Vehículos', '17. Intrafinanciamiento de Tarjeta Crédito Corporativas', 'Indice de Morosidad de Cartera de Credito Bruta', 
'Cobertura de la Cartera de Créditos Bruta', '18. Intrafinanciamiento de Tarjeta Crédito por Operaciones de Microfinanzas', 
'19. Viviendas de Interés Social', '1.1 - Créditos Vigentes', '9.- Cartera en Riesgo / Cartera Bruta', '2.- Margen Financiero en Riesgo / Patrimonio', 
'Indice de Morosidad de Cartera de Credito Neta', '1.3 Clasificación C', '12. Otros', '1. - Total Evaluación de Cartera', 
'2.- Cuota de Mercado en Captaciones del Público', '1.3 - Créditos Reestructurados', '8.- Cobertura con Provisiones Individuales', 
'1.2 Clasificación B', '3.- Capital Primario + Resultados de periodos anteriores / APBR', '16. Intrafinanciamiento de Tarjeta Crédito Personales', 
'1.1 Clasificación A', '2.- Activos Improductivos Brutos / Activo Total', '1.- Efectivo y Equivalentes de Efectivo / Captaciones del Público', 
'4.- Cuota de Mercado de Cartera de Créditos Bruta', '6. Personales', '4.- Indice de Morosidad de Cartera de Créditos Bruta', 
'1.4 - Créditos Vencidos', '10. Sector Público', '1.- Captaciones del Publico', '13. Extrafinanciamientos', 
'15. Tarjetas de Crédito Microfinanzas', '3.- Valor Económico del Capital', '7.- Cobertura de la Cartera de Créditos Bruta', 
'8. Adelantos de Salario', '4.- Valor Económico del Capital (Dism)', '1.- % Margen Financiero en Riesgo', '1. Agricultura', 
'11. Desarrollo Habitacional o Urbano', '3.- Activos Improductivos Netos / Activo Total', '3. Industria', 
'14. Tarjetas de Crédito Corporativas', 'b.- Razón de Endeudamiento (Nivel 1 + 2 + 3)', 'Cartera de Riesgo / Cartera Bruta', 
'4. Comercio', '1.5 Clasificación E', '2.- Efectivo y Equivalentes de Efectivo / Cartera de Crédito Bruta', '3.- Cartera de Créditos Bruta', 
'1.5 - Créditos en Cobro Judicial', '1.4 Clasificación D', 'a.- Razón de Apalancamiento Financiero (Nivel 1+2+3)', '5. Hipotecarios para vivienda', 
'1.- Razón de Capital (Nivel 1 + 2 + 3)* s/ APBR', '1.2 - Créditos Prorrogados', '6.- Cobertura de la Cartera de Créditos Improductiva'
]

bancos = ['BANPRO','BANCO LAFISE BANCENTRO', 'BAC', 'BDF', 'BANCO FICOHSA', 'AVANZ', 'BANCO PRODUZCAMOS', 'BANCO ATLÁNTIDA', 'Financiera FDL, S.A.', 'SFN', 'SFB']
Variable_ER = [
    'Ingresos Financieros',
    'Ingresos Financieros por Efectivo',
    'Ingresos Financieros por Inversiones',
    'Ingresos Financieros por Cartera de Créditos',
    'Otros Ingresos Financieros',
    'Gastos Financieros',
    'Gastos Financieros por Obligaciones con el Público',
    'Gastos Financieros por Depósitos de Instituciones Financieras y de Organismos Internacionales',
    'Gastos Financieros por Emisión de Deuda',
    'Gastos Financieros por Operaciones de Reporto',
    'Gastos Financieros por Obligaciones con Instituciones Financieras y por Otros Financiamientos',
    'Gastos Financieros por Obligaciones con el Banco Central de Nicaragua',
    'Gastos Financieros por Obligaciones Subordinadas y/o Convertibles en Capital',
    'Otros Gastos Financieros',
    'Margen Financiero antes de Mantenimiento de Valor',
    'Margen Financiero, bruto',
    'Resultados por Deterioro de Activos Financieros',
    'Margen Financiero, neto después de Deterioro de Activos Financieros',
    'Ingresos (Gastos) Operativos, neto',
    'Resultado Operativo',
    'Resultados por Participación en Asociadas, Negocios Conjuntos y Subsidiarias',
    'Ganancia por Valoración y Venta de Activos y Otros Ingresos',
    'Pérdida por Valoración y Venta de Activos',
    'Resultado después de Ingresos y Gastos operativos',
    'Ajustes netos por Diferencial Cambiario',
    'Resultado después de Diferencial Cambiario',
    'Gastos de Administración',
    'Resultados de operaciones antes de Impuestos y Contribuciones por Leyes Especiales',
    'Contribuciones por Leyes Especiales',
    'Gasto por Impuesto sobre la Renta',
    'Resultado del Ejercicio',
    'RESULTADO DEL EJERCICIO'
    ]

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#lo ocupo para una función luegos
def flatten(lista):
    lista1 = []
    for item in lista:
        lista1.extend(item)
    return lista1

pd.set_option('display.float_format', lambda x: '%.2f' % x)

def read_json(reporte, fecha_min, fecha_max):

    url = "https://www.siboif.gob.ni/rest/estadisticas"
    params = {
            "intendencia": "Bancos",
            "fecha[min]": fecha_min,
            "fecha[max]": fecha_max,
            "tipo_reporte": reporte
            }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
                
        print(f"Datos recibidos exitosamente: {reporte[1]}")
    except requests.exceptions.HTTPError as http_err:
        print(f"Ocurrió un error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"La petición superó el tiempo de espera: {timeout_err}")
    except ValueError:
        print("La respuesta no tiene un formato JSON válido.")
        print("Contenido recibido:", response.text)
    except Exception as err:
        print(f"Ocurrió un error inesperado: {err}")

    return pd.DataFrame(data)


# Estadisticas_BG = read_json("Estado de Situación Financiera (ESF)", '2026-05-01', '2026-06-31')
#Estadisticas_ER = read_json("Estado de Resultados (ER)", '2026-05-01', '2026-06-31')
# Estadisticas_IF = read_json("Indicadores Financieros", "2026-05-01", "2026-05-31") 

def transformar_pasar_base_BG(tabla, campos, bancos):
    dict_insertar = {banco: {campo :[] for campo in campos} for banco in bancos}

    for _, row in tabla.iterrows():
        institucion, variable, valor, mes, fecha, año, grupo = row['institucion'], row['variable_1'], row['valor_1'], row['mes'], row['fecha'], row['anio'], row['grupo']

        variable_2 = str(variable) +' ()' if pd.isnull(grupo) else str(variable) +' ('+ str(grupo) + ')' 

        if institucion not in bancos or variable_2 not in campos:
            continue
        else:
            dict_insertar[institucion][variable_2].append((valor, mes, fecha, año, grupo)) 
        
        #Convertir a dataframe y despues concatenar con la base
    data = []    
    for banco, campos_dict in dict_insertar.items():
        for campo, valores_list in campos_dict.items():
            for valor, mes, fecha, año, grupo in valores_list:
                data.append({
                    'Banco': banco,
                    'Campo': campo,
                    'Valor': valor,
                    'MES': mes, 
                    'Fecha': fecha,
                    'Año': año,
                    'Grupo': grupo
                })
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df = pd.DataFrame(data)
    return df, dict_insertar

def transformar_pasar_base_ER(tabla: DataFrame, campos: list, bancos: list):

    dict_insertar = {banco: {campo:[] for campo in campos} for banco in bancos}

    for _, row in tabla.iterrows():
        institucion, variable, valor, mes, fecha, año, grupo = row['institucion'], row['variable_1'], row['valor_1'], row['mes'], row['fecha'], row['anio'], row['grupo']

        if institucion not in bancos or variable not in campos:
            continue
        else:
            dict_insertar[institucion][variable].append((valor, mes, fecha, año, grupo)) 
    
    #Convertir a dataframe y despues concatenar con la base
    data = []

    for banco, campos_dict in dict_insertar.items():
        for campo, valores_list in campos_dict.items():
            for valor, mes, fecha, año, grupo in valores_list:
                data.append({
                    'Banco': banco,
                    'Campo': campo,
                    'Valor': valor,
                    'MES': mes, 
                    'Fecha': fecha,
                    'Año': año,
                    'Grupo': grupo
                })
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df = pd.DataFrame(data)
    return df, dict_insertar

# x = transformar_pasar_base_ER(Estadisticas_BG, Variable_ER)
# print(x)

#definamos para enviar a power BI

def EEFF_Balance_Indicadores(dicti: dict, campos: list, bancos:list):
    Banco_1 = flatten([[banco] * len(campos) for banco in bancos])
    campos_1 = [campo for campo in campos] * len(bancos)
    valores = []

    for banco, campo in zip(Banco_1, campos_1):
        try:
            valor = dicti[banco][campo]
            valores.append(valor[0][0])
        except IndexError:
            valores.append(0)
    data = {
        'Banco':Banco_1,
        'campos': campos_1,
        'valores': valores
    }
    df = pd.DataFrame(data)
    
    tabla_pivote = df.pivot_table(index='campos', columns='Banco', values='valores', aggfunc='sum')
    tabla_pivote = tabla_pivote.reset_index()

    # with pd.ExcelWriter(r"C:\Users\PR00538\Documents\Libro1-Prueba.xlsx", mode='a', engine='openpyxl') as writer:
    #     df.to_excel(writer, index=False)
    return tabla_pivote

def Bancos(tabla: DataFrame, banco: str, año_1: int, año_2: int, campos: list, meses: list, ER: bool, TC: float):
    """La tabla proviene de transformar_pasar_ER_BG, transformar_pasar_base_BG(tabla, campos)"""
    años_rango = list(range(año_1, año_2 + 1))
    diccionario = {}

    def to_float(val):
        if val is None:
            return 0.0
        if isinstance(val, (int, float)):
            return float(val)

        s = str(val).strip()
        if s == '' or s in ('-', '--', 'N/A', 'n/a', 'NA', 'nan', 'NaN'):
            return 0.0

        negativo = s.startswith('(') and s.endswith(')')
        if negativo:
            s = s[1:-1]

        s = s.replace('$', '').replace('%', '').strip()

        if ',' in s and '.' in s:
            if s.rfind(',') > s.rfind('.'):
                s = s.replace('.', '').replace(',', '.')
            else:
                s = s.replace(',', '')
        elif ',' in s:
            partes = s.split(',')
            if len(partes[-1]) == 2:
                s = s.replace(',', '.')
            else:
                s = s.replace(',', '')

        try:
            resultado = float(s)
        except ValueError:
            return 0.0

        return -resultado if negativo else resultado

    banco_norm = str(banco).strip().lower()

    for _, row in tabla.iterrows():
        año_raw, bank, valor, campo, mes_raw = row['Año'], row['Banco'], row['Valor'], row['Campo'], row['MES']

        # Normalización estricta del año
        try:
            año_num = int(float(str(año_raw).strip()))
        except (ValueError, TypeError):
            continue

        if año_num not in años_rango:
            continue

        año_str = str(año_num)
        mes_str = str(mes_raw).strip()
        
        if str(bank).strip().lower() == banco_norm:
            col_key = f"{mes_str} {año_str}"
            dict_tempo = {col_key: to_float(valor)}

            if campo in diccionario:
                diccionario[campo].update(dict_tempo)
            else:
                diccionario[campo] = dict_tempo

    if not diccionario:
        bancos_disponibles = sorted(set(str(b).strip() for b in tabla['Banco'].unique()))
        print(f"[AVISO] No se encontraron filas para banco='{banco}'. "
              f"Bancos disponibles en la tabla: {bancos_disponibles}")

    df = pd.DataFrame.from_dict(diccionario, orient='index').fillna(0)

    rangos = [col for col in df.columns if col != 'index']

    def _mes_pos(mes_str):
        m = str(mes_str).strip().lower()
        for i, ref in enumerate(meses):
            if str(ref).strip().lower()[:3] == m[:3]:
                return i
        return 0

    def _sort_key(fecha):
        partes = str(fecha).split(' ')
        mes_str = partes[0]
        año_str = partes[1] if len(partes) > 1 else '0'
        try:
            año_num = int(float(año_str))
        except ValueError:
            año_num = 0
        return (año_num, _mes_pos(mes_str))

    rangos = sorted(rangos, key=_sort_key)

    def normalizar(t):
        return (str(t).lower().strip()
                .replace('á', 'a').replace('é', 'e').replace('í', 'i')
                .replace('ó', 'o').replace('ú', 'u'))

    def get_v(campo, fecha, debug=False):
        try:
            fecha_clean = str(fecha).strip()

            if fecha_clean not in df.columns:
                if debug:
                    print(f"[get_v] fecha no encontrada: '{fecha_clean}' (columnas: {list(df.columns)})")
                return 0.0

            campo_norm = normalizar(campo)

            for idx_real in df.index:
                if campo_norm == normalizar(idx_real):
                    return to_float(df.at[idx_real, fecha_clean])

            matches = [idx_real for idx_real in df.index if campo_norm in normalizar(idx_real)]

            if len(matches) >= 1:
                if len(matches) > 1 and debug:
                    print(f"[get_v] AMBIGUO: campo='{campo}' coincide con {matches}. Usando el primero.")
                return to_float(df.at[matches[0], fecha_clean])
            else:
                if debug:
                    print(f"[get_v] campo no encontrado: '{campo}' (índices disponibles: {list(df.index)})")
                return 0.0
        except Exception as e:
            print(f"[get_v] ERROR con campo='{campo}', fecha='{fecha}': {e}")
            return 0.0

    if ER:
        calculos = [
            'Ingresos totales', 'Gastos', 'Costo de crédito', 'Impuesto', 'Utilidad',
            'Validación Utilidad', 'Eficiencia', 'Utilidad acumulada (U$ M)',
            'Margen financiero U$ M', 'INGRESOS FINANCIEROS', 'GASTOS FINANCIEROS', 'INGRESOS POR FX'
        ]
    else:
        calculos = [
            'CARTERA', 'DEPOSITOS', 'OTRAS OBLIGACIONES', 'TOTAL OBLIGACIONES', 'INVERSIONES',
            'INTERESES', 'PRINCIPAL + INTERESES', 'CARTERA + INTERESES PROMEDIO', 'CARTERA PROMEDIO',
            'INVERSIONES PROMEDIO', 'OBLIGACIONES PROMEDIO', 'Depositos totales', 'Depósitos Core',
            'Inversiones 1', 'ROA', 'ROE', 'Depósitos Promedios', 'Obligaciones Promedios',
            'CRECIMIENTO DEPOSITOS', 'CARTERA / DEPOSITOS', 'Loan to Deposit', 'Loans+Bonds/Deposits',
            'Fecha', 'Dia', 'Dias Acumulados', 'UTILIDAD NETA MENSUAL', 'ACTIVOS PROMEDIO', 'PATRIMONIO PROMEDIO'
        ]

    estadisticas = {fecha: {calculo: [] for calculo in calculos} for fecha in rangos}

    if ER:
        for fecha in rangos:
            ingresos_totales = (
                get_v('Margen Financiero, bruto', fecha)
                + get_v('Ingresos (Gastos) Operativos, neto', fecha)
                + get_v('Resultados por Participación en Asociadas, Negocios Conjuntos y Subsidiarias', fecha)
                + get_v('Ganancia por Valoración y Venta de Activos y Otros Ingresos', fecha)
                + get_v('Ajustes netos por Diferencial Cambiario', fecha)
                - get_v('Resultados por Deterioro de Activos no Financieros', fecha)
                - get_v('Pérdida por Valoración y Venta de Activos', fecha)
            )
            estadisticas[fecha]['Ingresos totales'].append(ingresos_totales)

            gastos = (
                get_v('Gastos de Administración', fecha)
                + get_v('Contribuciones por Leyes Especiales', fecha)
            )
            estadisticas[fecha]['Gastos'].append(gastos)

            costo_credito = get_v('Resultados por Deterioro de Activos Financieros', fecha)
            estadisticas[fecha]['Costo de crédito'].append(costo_credito)

            impuesto = get_v('Gasto por Impuesto sobre la Renta', fecha)
            estadisticas[fecha]['Impuesto'].append(impuesto)

            utilidad_calculada = ingresos_totales - gastos - costo_credito - impuesto
            estadisticas[fecha]['Utilidad'].append(utilidad_calculada)

            resultado_ejercicio = get_v('RESULTADO DEL EJERCICIO', fecha)
            estadisticas[fecha]['Validación Utilidad'].append(utilidad_calculada - resultado_ejercicio)

            eficiencia = gastos / ingresos_totales if ingresos_totales != 0 else 0
            estadisticas[fecha]['Eficiencia'].append(eficiencia)

            estadisticas[fecha]['Utilidad acumulada (U$ M)'].append(resultado_ejercicio / TC / 1000)

            ing_fin = get_v('INGRESOS FINANCIEROS', fecha)
            gas_fin = get_v('GASTOS FINANCIEROS', fecha)
            estadisticas[fecha]['INGRESOS FINANCIEROS'].append(ing_fin)
            estadisticas[fecha]['GASTOS FINANCIEROS'].append(gas_fin)

            ing_fx = (
                get_v('Ajustes netos por Diferencial Cambiario', fecha)
                + get_v('Ajustes netos por Mantenimiento de Valor', fecha)
            )
            estadisticas[fecha]['INGRESOS POR FX'].append(ing_fx)

            margen_fin = (ing_fin - gas_fin + ing_fx) / TC / 1000
            estadisticas[fecha]['Margen financiero U$ M'].append(margen_fin)

    else:
        dias_mes = {'ene': 31, 'feb': 28, 'mar': 31, 'abr': 30, 'may': 31, 'jun': 30,
                    'jul': 31, 'ago': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dic': 31}

        for idx, fecha in enumerate(rangos):
            mes_str, año_str = fecha.split(' ')
            es_enero = mes_str.strip().lower()[:3] == 'ene'
            dia_actual = dias_mes.get(mes_str.lower()[:3], 30)
            año_num = int(float(año_str))
            fecha_anterior = rangos[idx - 1] if idx > 0 else None

            # --- CARTERA ---
            cartera = (
                get_v('Vigentes (Cartera de Créditos, Neta)', fecha)
                + get_v('Prorrogados (Cartera de Créditos, Neta)', fecha)
                + get_v('Reestructurados (Cartera de Créditos, Neta)', fecha)
                + get_v('Vencidos (Cartera de Créditos, Neta)', fecha)
                + get_v('Cobro Judicial (Cartera de Créditos, Neta)', fecha)
            )
            estadisticas[fecha]['CARTERA'].append(cartera)

            # --- DEPOSITOS ---
            depositos = (
                get_v('Moneda Extranjera (Obligaciones con el Público)', fecha)
                + get_v('Moneda Nacional (Obligaciones con el Público)', fecha)
                + get_v('Obligaciones por Depósitos de Instituciones Financieras y de Organismos Internacionales (Pasivo)', fecha)
                + get_v('Obligaciones con el Banco Central de Nicaragua (Pasivo)', fecha)
            )
            estadisticas[fecha]['DEPOSITOS'].append(depositos)
            estadisticas[fecha]['Depositos totales'].append(depositos)

            # --- Depósitos Core ---
            depositos_core = (
                get_v('Depósitos a la Vista (Moneda Nacional)', fecha)
                + get_v('Depósitos de Ahorro (Moneda Nacional)', fecha)
                + get_v('Depósitos a la Vista (Moneda Extranjera)', fecha)
                + get_v('Depósitos de Ahorro (Moneda Extranjera)', fecha)
            )
            estadisticas[fecha]['Depósitos Core'].append(depositos_core)

            # --- OTRAS OBLIGACIONES ---
            otras_obligaciones = (
                get_v('Obligaciones Subordinadas y/o Convertibles en Capital (Pasivo)', fecha)
                + get_v('Obligaciones con Instituciones Financieras y por otros Financiamientos (Pasivo)', fecha)
                + get_v('Otras Obligaciones Diversas con el Público (Pasivo)', fecha)
                + get_v('Intereses sobre Obligaciones con el Público por Depósitos (Obligaciones con el Público)', fecha)
            )
            estadisticas[fecha]['OTRAS OBLIGACIONES'].append(otras_obligaciones)

            # --- TOTAL OBLIGACIONES ---
            total_obligaciones = depositos + otras_obligaciones
            estadisticas[fecha]['TOTAL OBLIGACIONES'].append(total_obligaciones)

            # --- INVERSIONES ---
            inversiones = (
                get_v('Inversiones a Valor Razonable con Cambios en Otro Resultado Integral (Activo)', fecha)
                + get_v('Inversiones a Valor Razonable con Cambios en Resultados (Activo)', fecha)
                + get_v('Inversiones a Costo Amortizado, Neto (Activo)', fecha)
                + get_v('Equivalentes de Efectivo (Moneda Extranjera)', fecha)
                + get_v('Equivalentes de Efectivo (Moneda Nacional)', fecha)
            )
            estadisticas[fecha]['INVERSIONES'].append(inversiones)
            estadisticas[fecha]['Inversiones 1'].append(inversiones)

            # --- INTERESES ---
            intereses = (
                get_v('Intereses y Comisiones por Cobrar sobre Cartera de Créditos (Cartera de Créditos, Neta)', fecha)
                + get_v('(-) Comisiones Devengadas con la Tasa de Interés Efectiva (Cartera de Créditos, Neta)', fecha)
            )
            estadisticas[fecha]['INTERESES'].append(intereses)

            # --- PRINCIPAL + INTERESES ---
            principal_intereses = cartera + intereses
            estadisticas[fecha]['PRINCIPAL + INTERESES'].append(principal_intereses)

            if fecha_anterior:
                cartera_ant = estadisticas[fecha_anterior]['CARTERA'][-1]
                inv_ant = estadisticas[fecha_anterior]['INVERSIONES'][-1]
                pi_ant = estadisticas[fecha_anterior]['PRINCIPAL + INTERESES'][-1]
                obli_ant = estadisticas[fecha_anterior]['TOTAL OBLIGACIONES'][-1]
                dep_ant = estadisticas[fecha_anterior]['DEPOSITOS'][-1]
                act_ant = get_v('Activo ()', fecha_anterior)
                pat_ant = get_v('PATRIMONIO ()', fecha_anterior)
                resultado_ant = get_v('Resultado del Ejercicio (Fondos Propios)', fecha_anterior)
            else:
                cartera_ant, inv_ant, pi_ant, obli_ant, dep_ant = (
                    cartera, inversiones, principal_intereses, total_obligaciones, depositos
                )
                act_ant = get_v('Activo ()', fecha)
                pat_ant = get_v('PATRIMONIO ()', fecha)
                resultado_ant = 0.0

            estadisticas[fecha]['CARTERA PROMEDIO'].append(
                cartera if es_enero else (cartera + cartera_ant) / 2
            )
            estadisticas[fecha]['INVERSIONES PROMEDIO'].append(
                inversiones if es_enero else (inversiones + inv_ant) / 2
            )
            estadisticas[fecha]['OBLIGACIONES PROMEDIO'].append(
                total_obligaciones if es_enero else (total_obligaciones + obli_ant) / 2
            )
            estadisticas[fecha]['CARTERA + INTERESES PROMEDIO'].append(
                principal_intereses if es_enero else (principal_intereses + pi_ant) / 2
            )

            fechas_mismo_año = [f for f in rangos[:idx + 1]
                                 if int(float(f.split(' ')[1])) == año_num]
            deposit_vals_ytd = [estadisticas[f]['DEPOSITOS'][-1] for f in fechas_mismo_año]
            otras_oblig_vals_ytd = [estadisticas[f]['OTRAS OBLIGACIONES'][-1] for f in fechas_mismo_año]

            estadisticas[fecha]['Depósitos Promedios'].append(sum(deposit_vals_ytd) / len(deposit_vals_ytd))
            estadisticas[fecha]['Obligaciones Promedios'].append(sum(otras_oblig_vals_ytd) / len(otras_oblig_vals_ytd))

            resultado_actual = get_v('Resultado del Ejercicio (Fondos Propios)', fecha)
            utilidad_neta_mensual = resultado_actual if es_enero else (resultado_actual - resultado_ant)
            estadisticas[fecha]['UTILIDAD NETA MENSUAL'].append(utilidad_neta_mensual)

            estadisticas[fecha]['CARTERA / DEPOSITOS'].append(cartera / depositos if depositos else 0)
            estadisticas[fecha]['Loan to Deposit'].append(cartera / depositos if depositos else 0)
            estadisticas[fecha]['Loans+Bonds/Deposits'].append((cartera + inversiones) / depositos if depositos else 0)
            estadisticas[fecha]['CRECIMIENTO DEPOSITOS'].append(
                (depositos - dep_ant) / dep_ant if dep_ant else 0
            )

            estadisticas[fecha]['Fecha'].append(fecha)
            estadisticas[fecha]['Dia'].append(dia_actual)
            if es_enero or fecha_anterior is None:
                dias_acumulados = dia_actual
            else:
                dias_acumulados = estadisticas[fecha_anterior]['Dias Acumulados'][-1] + dia_actual
            estadisticas[fecha]['Dias Acumulados'].append(dias_acumulados)

            estadisticas[fecha]['ACTIVOS PROMEDIO'].append((get_v('Activo ()', fecha) + act_ant) / 2)
            estadisticas[fecha]['PATRIMONIO PROMEDIO'].append((get_v('PATRIMONIO ()', fecha) + pat_ant) / 2)

            ventana = rangos[max(0, idx - 11): idx + 1]
            utilidad_trailing = sum(estadisticas[f]['UTILIDAD NETA MENSUAL'][-1] for f in ventana)
            activos_trailing = [get_v('Activo ()', f) for f in ventana]
            patrimonio_trailing = [get_v('PATRIMONIO ()', f) for f in ventana]

            activos_prom_trailing = sum(activos_trailing) / len(activos_trailing) if activos_trailing else 0
            patrimonio_prom_trailing = sum(patrimonio_trailing) / len(patrimonio_trailing) if patrimonio_trailing else 0

            estadisticas[fecha]['ROA'].append(
                utilidad_trailing / activos_prom_trailing if activos_prom_trailing else 0
            )
            estadisticas[fecha]['ROE'].append(
                utilidad_trailing / patrimonio_prom_trailing if patrimonio_prom_trailing else 0
            )

    df_estadisticas = pd.DataFrame.from_dict(
        {k: {m: v[0] if v else 0 for m, v in ver.items()} for k, ver in estadisticas.items()},
        orient='index'
    )
    return df, df_estadisticas.T

def resumen(tabla_ER, tabla_BG, mes, bancos, años, TC):

    fecha_actual = f'{mes} {años}'
    fecha_anterior = f'{mes} {años - 1}'

    # ==========================================================
    # Build data once
    # ==========================================================

    datos = {}

    for banco in bancos:

        er_raw, er_stats = Bancos(
            tabla_ER,
            banco,
            años - 1,
            años,
            Variable_ER,
            meses,
            True,
            TC
        )

        bg_raw, bg_stats = Bancos(
            tabla_BG,
            banco,
            años - 1,
            años,
            Variable_BG,
            meses,
            False,
            TC
        )

        datos[banco] = {
            'ER': er_raw,
            'BG': bg_raw,
            'ER_stats': er_stats,
            'BG_stats': bg_stats
        }

    # ==========================================================
    # Helpers
    # ==========================================================

    def get_raw(banco, campo, fecha):

        er = datos[banco]['ER']
        bg = datos[banco]['BG']

        if campo in er.index:
            return er.loc[campo, fecha]

        if campo in bg.index:
            return bg.loc[campo, fecha]

        return 0.0

    def get_stat(banco, indicador, fecha):

        er = datos[banco]['ER_stats']
        bg = datos[banco]['BG_stats']

        if indicador in er.index:
            return er.loc[indicador, fecha]

        if indicador in bg.index:
            return bg.loc[indicador, fecha]

        return 0.0

    def safe_growth(actual, anterior):

        if anterior == 0:
            return 0.0

        return (actual - anterior) / anterior

    def market_share(values):

        total = sum(values)

        if total == 0:
            return [0.0 for _ in values]

        return [v / total for v in values]


    # ==========================================================
    # Comparación interanual
    # ==========================================================

    def comparacion_año_anterior():

        metricas = {
            'Activos': ('raw', 'Activo ()'),
            'Cartera': ('raw', 'Cartera de Créditos, Neta (Activo)'),
            'Patrimonio': ('raw', 'PATRIMONIO ()'),
            'Depósitos': ('stat', 'Depositos totales'),
            'Depósitos Core': ('stat', 'Depositos Core'),
            'Inversiones': ('stat', 'INVERSIONES'),
            'Utilidad': ('stat', 'Utilidad acumulada (U$ M)')
        }

        resultados = {}

        for nombre, (tipo, campo) in metricas.items():

            actuales = []
            anteriores = []

            for banco in bancos:

                if tipo == 'raw':
                    actual = get_raw(banco, campo, fecha_actual) / 1000
                    anterior = get_raw(banco, campo, fecha_anterior) / 1000
                else:
                    actual = get_stat(banco, campo, fecha_actual)
                    anterior = get_stat(banco, campo, fecha_anterior)

                actuales.append(actual)
                anteriores.append(anterior)

            participacion_actual = market_share(actuales)
            participacion_anterior = market_share(anteriores)

            df = pd.DataFrame({
                'Institución': bancos,
                fecha_actual: actuales,
                fecha_anterior: anteriores,
                'Variación %': [
                    safe_growth(a, b) for a, b in zip(actuales, anteriores)
                ],
                'Variación USD': [
                    a - b for a, b in zip(actuales, anteriores)
                ],
                f'{fecha_actual} Part. Mercado': participacion_actual,
                f'{fecha_anterior} Part. Mercado': participacion_anterior
            })

            resultados[nombre] = df

        return resultados

    # ==========================================================
    # Margen financiero
    # ==========================================================

    def margen_financiero(bancos_input, fechas_list):
        """
        bancos_input: list of banks OR a single bank name as string
        fechas_list: list of date strings (e.g., ['ene 2025', 'feb 2025', 'mar 2025'])
        """
        filas_nombres = [
            'Inversiones',
            'Cartera',
            'Otros',
            'Int. Recibidos',
            'Depósitos',
            'Oblig. Bancarias',
            'Int. Pagados',
            'Margen financiero',
            'Validación margen financiero'
        ]

        # Normalize bank input to list
        is_single_bank = isinstance(bancos_input, str) or len(bancos_input) == 1
        b_list = [bancos_input] if isinstance(bancos_input, str) else bancos_input

        # Build MultiIndex Columns based on mode
        col_tuples = []
        if is_single_bank:
            # Layout: Single Bank -> Dates across columns
            banco = b_list[0]
            banco_code = banco.replace('BANCO ', '').replace(' ', '')
            for fecha in fechas_list:
                partes = fecha.split(' ')
                mes_c = partes[0][:3].lower()
                yr = partes[1][-2:] if len(partes) > 1 else ''
                label = f"{mes_c}-{yr}"
                
                col_tuples.append((banco, f"{label}{banco_code}", fecha))
            
            columns = pd.MultiIndex.from_tuples(col_tuples, names=['Banco', 'Ref', 'Fecha'])
        else:
            # Layout: Multiple Banks -> Selected Dates
            for banco in b_list:
                banco_code = banco.replace('BANCO ', '').replace(' ', '')
                for fecha in fechas_list:
                    partes = fecha.split(' ')
                    mes_c = partes[0][:3].lower()
                    yr = partes[1][-2:] if len(partes) > 1 else ''
                    label = f"{mes_c}-{yr}"
                    
                    col_tuples.append((f"{label}{banco_code}", f"{banco} ER", fecha))
            
            columns = pd.MultiIndex.from_tuples(col_tuples, names=['Ref', 'Banco', 'Fecha'])

        df = pd.DataFrame(index=filas_nombres, columns=columns)

        # Fill Data
        for banco in b_list:
            banco_code = banco.replace('BANCO ', '').replace(' ', '')
            for fecha in fechas_list:
                partes = fecha.split(' ')
                mes_c = partes[0][:3].lower()
                yr = partes[1][-2:] if len(partes) > 1 else ''
                label = f"{mes_c}-{yr}"

                if is_single_bank:
                    col_key = (banco, f"{label}{banco_code}", fecha)
                else:
                    col_key = (f"{label}{banco_code}", f"{banco} ER", fecha)

                # Extract components
                ing_inv = get_raw(banco, 'Ingresos Financieros por Inversiones', fecha) / TC / 1000
                ing_cart = get_raw(banco, 'Ingresos Financieros por Cartera de Créditos', fecha) / TC / 1000
                ing_tot = get_raw(banco, 'Ingresos Financieros', fecha) / TC / 1000

                gasto_pub = get_raw(banco, 'Gastos Financieros por Obligaciones con el Público', fecha) / TC / 1000
                gasto_tot = get_raw(banco, 'Gastos Financieros', fecha) / TC / 1000

                mantenimiento = get_raw(banco, 'Ajustes netos por Mantenimiento de Valor', fecha) / TC / 1000
                fx = get_raw(banco, 'Ajustes netos por Diferencial Cambiario', fecha) / TC / 1000

                otros_ing = ing_tot - ing_inv - ing_cart
                int_rec = ing_inv + ing_cart + otros_ing
                obli_banc = gasto_tot - gasto_pub
                int_pag = gasto_pub + obli_banc
                margen = int_rec - int_pag + mantenimiento + fx

                df.loc['Inversiones', col_key] = ing_inv
                df.loc['Cartera', col_key] = ing_cart
                df.loc['Otros', col_key] = otros_ing
                df.loc['Int. Recibidos', col_key] = int_rec
                df.loc['Depósitos', col_key] = gasto_pub
                df.loc['Oblig. Bancarias', col_key] = obli_banc
                df.loc['Int. Pagados', col_key] = int_pag
                df.loc['Margen financiero', col_key] = margen
                
                margen_siboif = get_stat(banco, 'Margen financiero U$ M', fecha)
                df.loc['Validación margen financiero', col_key] = margen - margen_siboif

        return df


    # ==========================================================
    # Utilidad acumulada
    # ==========================================================

    def utilidad_acumulada(bancos_input, fechas_list):
        filas_nombres = [
            'Margen Financiero',
            '(-) Provisiones',
            'Otros Ingresos',
            'Margen Amplio',
            '(-) Gastos Administrativos',
            'Util. Antes impuestos',
            'Impuesto',
            'Utilidad',
            'Validación Utilidad U$'
        ]

        is_single_bank = isinstance(bancos_input, str) or len(bancos_input) == 1
        b_list = [bancos_input] if isinstance(bancos_input, str) else bancos_input

        col_tuples = [(banco, fecha) for banco in b_list for fecha in fechas_list]
        columns = pd.MultiIndex.from_tuples(col_tuples, names=['Banco', 'Fecha'])

        df = pd.DataFrame(index=filas_nombres, columns=columns)

        for banco in b_list:
            for fecha in fechas_list:
                col_key = (banco, fecha)

                margen = get_stat(banco, 'Margen financiero U$ M', fecha) * TC
                provisiones = get_raw(banco, 'Resultados por Deterioro de Activos Financieros', fecha) / 1000
                gastos_admin = get_raw(banco, 'Gastos de Administración', fecha) / 1000
                contribuciones = get_raw(banco, 'Contribuciones por Leyes Especiales', fecha) / 1000
                impuesto_renta = get_raw(banco, 'Gasto por Impuesto sobre la Renta', fecha) / 1000

                operativos = get_raw(banco, 'Ingresos (Gastos) Operativos, neto', fecha) / 1000
                venta_act = get_raw(banco, 'Ganancia por Valoración y Venta de Activos y Otros Ingresos', fecha) / 1000
                perdida_act = get_raw(banco, 'Pérdida por Valoración y Venta de Activos', fecha) / 1000
                asociadas = get_raw(banco, 'Resultados por Participación en Asociadas, Negocios Conjuntos y Subsidiarias', fecha) / 1000

                otros_ingresos = operativos + venta_act - perdida_act + asociadas
                margen_amplio = margen - provisiones + otros_ingresos
                utilidad_antes = margen_amplio - gastos_admin
                impuesto_total = contribuciones + impuesto_renta
                utilidad = utilidad_antes - impuesto_total

                utilidad_usd_calculada = utilidad / TC
                utilidad_usd_siboif = get_stat(banco, 'Utilidad acumulada (U$ M)', fecha)
                validacion_usd = utilidad_usd_calculada - utilidad_usd_siboif

                df.loc['Margen Financiero', col_key] = margen
                df.loc['(-) Provisiones', col_key] = -provisiones
                df.loc['Otros Ingresos', col_key] = otros_ingresos
                df.loc['Margen Amplio', col_key] = margen_amplio
                df.loc['(-) Gastos Administrativos', col_key] = -gastos_admin
                df.loc['Util. Antes impuestos', col_key] = utilidad_antes
                df.loc['Impuesto', col_key] = impuesto_total
                df.loc['Utilidad', col_key] = utilidad
                df.loc['Validación Utilidad U$', col_key] = validacion_usd

        return df


    # ==========================================================
    # Indicadores financieros
    # ==========================================================

    def indicadores_financieros():

        filas_indicadores = []
        filas_crecimiento = []

        def crecimiento(actual, anterior):
            if anterior == 0:
                return 0
            return ((actual - anterior) / anterior) * 100

        activos_sistema = sum(
            get_raw(b, "Activo ()", fecha_actual)
            for b in bancos
        )

        for banco in bancos:

            # ---------- Valores actuales ----------
            activos = get_raw(banco, "Activo ()", fecha_actual) / 1000
            activos_ant = get_raw(banco, "Activo ()", fecha_anterior) / 1000

            cartera = get_raw(
                banco,
                "Cartera de Créditos, Neta (Activo)",
                fecha_actual
            ) / 1000

            cartera_ant = get_raw(
                banco,
                "Cartera de Créditos, Neta (Activo)",
                fecha_anterior
            ) / 1000

            patrimonio = get_raw(
                banco,
                "PATRIMONIO ()",
                fecha_actual
            ) / 1000

            patrimonio_ant = get_raw(
                banco,
                "PATRIMONIO ()",
                fecha_anterior
            ) / 1000

            inversiones = get_stat(
                banco,
                "INVERSIONES",
                fecha_actual
            )

            inversiones_ant = get_stat(
                banco,
                "INVERSIONES",
                fecha_anterior
            )

            depositos = get_stat(
                banco,
                "Depositos totales",
                fecha_actual
            )

            depositos_ant = get_stat(
                banco,
                "Depositos totales",
                fecha_anterior
            )

            depositos_core = get_stat(
                banco,
                "Depositos Core",
                fecha_actual
            )

            depositos_core_ant = get_stat(
                banco,
                "Depositos Core",
                fecha_anterior
            )

            utilidad = get_stat(
                banco,
                "Utilidad acumulada (U$ M)",
                fecha_actual
            )

            utilidad_ant = get_stat(
                banco,
                "Utilidad acumulada (U$ M)",
                fecha_anterior
            )

            roe = get_stat(banco, "ROE", fecha_actual)
            roa = get_stat(banco, "ROA", fecha_actual)
            eficiencia = get_stat(banco, "Eficiencia", fecha_actual)

            marketshare = (
                get_raw(banco, "Activo ()", fecha_actual) / activos_sistema * 100
                if activos_sistema else 0
            )

            # ---------------- Indicadores ----------------

            filas_indicadores.append({

                "Banco": banco,
                "Activos (US$ M)": activos,
                "Cartera (US$ M)": cartera,
                "Inversiones (US$ M)": inversiones,
                "Depósitos (US$ M)": depositos,
                "Depósitos Core (US$ M)": depositos_core,
                "Patrimonio (US$ M)": patrimonio,
                "Utilidad Neta (US$ M)": utilidad,
                "ROE (%)": roe,
                "ROA (%)": roa,
                "Eficiencia (%)": eficiencia,
                "Participación Activos (%)": marketshare

            })

            # ---------------- Crecimiento ----------------

            filas_crecimiento.append({

                "Banco": banco,
                "Activos (%)": crecimiento(activos, activos_ant),
                "Cartera (%)": crecimiento(cartera, cartera_ant),
                "Inversiones (%)": crecimiento(inversiones, inversiones_ant),
                "Depósitos (%)": crecimiento(depositos, depositos_ant),
                "Depósitos Core (%)": crecimiento(depositos_core, depositos_core_ant),
                "Patrimonio (%)": crecimiento(patrimonio, patrimonio_ant),
                "Utilidad Neta (%)": crecimiento(utilidad, utilidad_ant)

            })

        indicadores_df = pd.DataFrame(filas_indicadores)
        crecimiento_df = pd.DataFrame(filas_crecimiento)

        return indicadores_df, crecimiento_df

    # ==========================================================
    # Build outputs
    # ==========================================================

    indicadores_df, crecimiento_df = indicadores_financieros()

    resultados = {
        "Comparacion": comparacion_año_anterior(),
        "Margen_Financiero": margen_financiero(),
        "Utilidad_Acumulada": utilidad_acumulada(),
        "Indicadores": indicadores_df,
        "Crecimiento_Interanual": crecimiento_df
    }

    return resultados

def Indicadores_Banco(tabla_ER, tabla_BG, banco, fecha_min, fecha_max, año_1, año_2, TC):
    """
    Genera una tabla cruzada (Cross Table) para UN solo banco a lo largo de un rango de fechas/meses.
    
    Filas (Index): Indicadores Financieros
    Columnas: Cada fecha ('Enero 2025', 'Febrero 2025', ..., 'Junio 2026')
    """
    # Lista de todos los indicadores requeridos
    indicadores = [
        'ROE', 'ROA', 'IAC', 'Liquidez', 'NIM', 
        'Eficiencia', 'Mora', 'Cobertura de Mora', 'MarketShareActividad'
    ]

    # 1. Obtener y transformar datos de Indicadores Financieros desde SIBOIF
    IF = read_json("Indicadores Financieros", fecha_min, fecha_max)
    limpio_indicadores, _ = transformar_pasar_base_ER(IF, Variable_IF, [banco])

    # 2. Mapeo de indicadores directos desde 'limpio_indicadores'
    mapeo_siboif = {
        'Cobertura de Mora': '6.- Cobertura de la Cartera de Créditos Improductiva',
        'Mora': '4.- Indice de Morosidad de Cartera de Créditos Bruta',
        'IAC': '1.- Razón de Capital (Nivel 1 + 2 + 3)* s/ APBR'
    }

    # Helper para convertir texto/porcentaje a float
    def to_float(val):
        if pd.isnull(val):
            return 0.0
        try:
            s = str(val).replace('%', '').replace(',', '').strip()
            return float(s)
        except ValueError:
            return 0.0

    # 3. Obtener estadísticas del banco para el rango de años
    er_raw, er_stats = Bancos(tabla_ER, banco, año_1, año_2, Variable_ER, meses, True, TC)
    bg_raw, bg_stats = Bancos(tabla_BG, banco, año_1, año_2, Variable_BG, meses, False, TC)

    # Identificar las fechas disponibles en las estadísticas
    rangos_fechas = list(bg_stats.columns)

    # Inicializar el DataFrame final (Filas: Indicadores, Columnas: Fechas 'mes año')
    df_indicadores = pd.DataFrame(0.0, index=indicadores, columns=rangos_fechas)

    # --- A. Llenar indicadores que vienen de SIBOIF ---
    for _, row in limpio_indicadores.iterrows():
        bank = row['Banco']
        campo = row['Campo']
        valor = to_float(row['Valor'])
        mes_raw = str(row['MES']).strip()
        anio_raw = str(row['Año']).strip()
        
        fecha_col = f"{mes_raw} {anio_raw}"

        if bank == banco and fecha_col in df_indicadores.columns:
            for ind_col, var_origen in mapeo_siboif.items():
                if campo == var_origen:
                    df_indicadores.at[ind_col, fecha_col] = valor

    # --- B. Llenar indicadores calculados por fecha ---
    for fecha_str in rangos_fechas:

        # 1. ROE
        if 'ROE' in er_stats.index:
            df_indicadores.at['ROE', fecha_str] = er_stats.loc['ROE', fecha_str]
        elif 'ROE' in bg_stats.index:
            df_indicadores.at['ROE', fecha_str] = bg_stats.loc['ROE', fecha_str]

        # 2. ROA
        if 'ROA' in er_stats.index:
            df_indicadores.at['ROA', fecha_str] = er_stats.loc['ROA', fecha_str]
        elif 'ROA' in bg_stats.index:
            df_indicadores.at['ROA', fecha_str] = bg_stats.loc['ROA', fecha_str]

        # 3. Eficiencia
        if 'Eficiencia' in er_stats.index:
            df_indicadores.at['Eficiencia', fecha_str] = er_stats.loc['Eficiencia', fecha_str]

        # 4. Liquidez: Efectivo / Depósitos Totales
        depositos = bg_stats.loc['Depositos totales', fecha_str] if 'Depositos totales' in bg_stats.index else 0.0
        efectivo = 0.0
        for idx in bg_raw.index:
            if 'efectivo y equivalentes' in str(idx).lower():
                efectivo += to_float(bg_raw.loc[idx, fecha_str])
        
        df_indicadores.at['Liquidez', fecha_str] = (efectivo / depositos) if depositos != 0 else 0.0

        # 5. NIM (Net Interest Margin): Margen Financiero / Activos Promedio (en U$ M)
        margen_fin = er_stats.loc['Margen financiero U$ M', fecha_str] if 'Margen financiero U$ M' in er_stats.index else 0.0
        activos_prom = bg_stats.loc['ACTIVOS PROMEDIO', fecha_str] if 'ACTIVOS PROMEDIO' in bg_stats.index else 0.0
        
        activos_prom_usd_m = (activos_prom / TC / 1000) if activos_prom != 0 else 0.0
        df_indicadores.at['NIM', fecha_str] = (margen_fin / activos_prom_usd_m) if activos_prom_usd_m != 0 else 0.0

        # 6. MarketShareActividad
        # Si se requiere el market share del sistema por mes, podemos calcularlo comparando los activos del banco contra el sistema
        activo_banco = 0.0
        for idx in bg_raw.index:
            if idx.strip() == 'Activo ()':
                activo_banco = to_float(bg_raw.loc[idx, fecha_str])
                break

        # Si cuentas con activos totales por fecha del sistema, se divide aquí
        # Por ejemplo, calculamos participación sobre el valor disponible
        df_indicadores.at['MarketShareActividad', fecha_str] = activo_banco

    return df_indicadores

def indicadores_banco(tabla_ER, tabla_BG, banco, año_1, año_2, TC):
    """
    Genera la tabla de 'Indicadores Financieros' para un banco específico 
    con estructura de MultiIndex en las filas y serie de tiempo en las columnas (formato mmm-aa).
    
    Parámetros:
    - tabla_ER: DataFrame con datos de Estado de Resultados.
    - tabla_BG: DataFrame con datos de Balance General.
    - banco: Nombre del banco (string), ej. 'BANCO FICOHSA', 'BANPRO', 'BAC', etc.
    - año_1: Año inicial del rango (int), ej. 2025.
    - año_2: Año final del rango (int), ej. 2026.
    - TC: Tasa de cambio.
    """
    # 1. Obtener los DataFrames procesados mediante la función Bancos para el banco especificado
    er_raw, er_stats = Bancos(tabla_ER, banco, año_1, año_2, Variable_ER, meses, True, TC)
    bg_raw, bg_stats = Bancos(tabla_BG, banco, año_1, año_2, Variable_BG, meses, False, TC)

    rangos_fechas = list(bg_stats.columns)

    # Convertir nombres de columnas de 'Mayo 2025' a 'may-25'
    def format_fecha_col(fecha_str):
        partes = fecha_str.split(' ')
        mes_c = partes[0][:3].lower()
        yr = partes[1][-2:] if len(partes) > 1 else ''
        return f"{mes_c}-{yr}"

    columnas_formateadas = [format_fecha_col(f) for f in rangos_fechas]

    # 2. Definir la jerarquía de filas (Categoría, Subcategoría)
    filas_estructura = [
        ('NIM', 'NIM'),
        ('Rendimiento', 'Cartera'),
        ('Rendimiento', 'Inversiones'),
        ('Costo de Fondos', 'Depósitos'),
        ('Costo de Fondos', 'Obligaciones'),
        ('Activo Productivo', 'Activo Productivo'),
        ('Liquidez', 'Liquidez'),
        ('Loan to Deposit', 'Loan to Deposit'),
        ('Depósito/Fondeo', 'Depósito/Fondeo'),
        ('Depósitos Core', 'Depósitos Core')
    ]

    row_index = pd.MultiIndex.from_tuples(filas_estructura, names=['Categoría', 'Subcategoría'])
    df_res = pd.DataFrame(index=row_index, columns=columnas_formateadas)

    # Helpers
    def safe_div(n, d):
        return (n / d) if (d and d != 0) else 0.0

    def get_val(df, metric, col):
        return df.loc[metric, col] if metric in df.index else 0.0

    # 3. Calcular métricas para el banco seleccionado en cada fecha
    for fecha_orig, col_fmt in zip(rangos_fechas, columnas_formateadas):
        # Datos base calculados por Bancos
        cartera_prom = get_val(bg_stats, 'CARTERA PROMEDIO', fecha_orig)
        inversiones_prom = get_val(bg_stats, 'INVERSIONES PROMEDIO', fecha_orig)
        depositos_prom = get_val(bg_stats, 'Depósitos Promedios', fecha_orig)
        obligaciones_prom = get_val(bg_stats, 'Obligaciones Promedios', fecha_orig)
        activos_prom = get_val(bg_stats, 'ACTIVOS PROMEDIO', fecha_orig)
        
        depositos_tot = get_val(bg_stats, 'Depositos totales', fecha_orig)
        depositos_core = get_val(bg_stats, 'Depósitos Core', fecha_orig)
        cartera_tot = get_val(bg_stats, 'CARTERA', fecha_orig)
        inversiones_tot = get_val(bg_stats, 'INVERSIONES', fecha_orig)
        
        # --- NIM ---
        margen_fin_usd = get_val(er_stats, 'Margen financiero U$ M', fecha_orig)
        activos_prom_usd = (activos_prom / TC / 1000)
        nim = safe_div(margen_fin_usd, activos_prom_usd) * 100

        # --- Rendimiento ---
        dias_acum = get_val(bg_stats, 'Dias Acumulados', fecha_orig)
        dias_acum = dias_acum if dias_acum > 0 else 360

        ing_cartera = get_val(er_raw, 'Ingresos Financieros por Cartera de Créditos', fecha_orig)
        rend_cartera = safe_div(ing_cartera * (360 / dias_acum), cartera_prom) * 100

        ing_inv = get_val(er_raw, 'Ingresos Financieros por Inversiones', fecha_orig)
        rend_inv = safe_div(ing_inv * (360 / dias_acum), inversiones_prom) * 100

        # --- Costo de Fondos ---
        gasto_pub = get_val(er_raw, 'Gastos Financieros por Obligaciones con el Público', fecha_orig)
        costo_depositos = safe_div(gasto_pub * (360 / dias_acum), depositos_prom) * 100

        gasto_obli = get_val(er_raw, 'Gastos Financieros por Obligaciones con Instituciones Financieras y por otros Financiamientos', fecha_orig)
        costo_obligaciones = safe_div(gasto_obli * (360 / dias_acum), obligaciones_prom) * 100

        # --- Activo Productivo y Liquidez ---
        activo_tot = get_val(bg_raw, 'Activo ()', fecha_orig)
        act_productivo = safe_div(cartera_tot + inversiones_tot, activo_tot) * 100

        efectivo = 0.0
        for idx in bg_raw.index:
            if 'efectivo' in str(idx).lower():
                efectivo += get_val(bg_raw, idx, fecha_orig)
        liquidez = safe_div(efectivo, depositos_tot) * 100

        # --- Loan to Deposit ---
        loan_to_deposit = get_val(bg_stats, 'Loan to Deposit', fecha_orig) * 100

        # --- Depósito/Fondeo y Depósitos Core ---
        total_fondeo = get_val(bg_stats, 'TOTAL OBLIGACIONES', fecha_orig)
        dep_fondeo = safe_div(depositos_tot, total_fondeo) * 100
        dep_core_pct = safe_div(depositos_core, depositos_tot) * 100

        # Asignación al DataFrame
        df_res.loc[('NIM', 'NIM'), col_fmt] = f"{nim:.2f}%"
        df_res.loc[('Rendimiento', 'Cartera'), col_fmt] = f"{rend_cartera:.1f}%"
        df_res.loc[('Rendimiento', 'Inversiones'), col_fmt] = f"{rend_inv:.1f}%"
        df_res.loc[('Costo de Fondos', 'Depósitos'), col_fmt] = f"{costo_depositos:.2f}%"
        df_res.loc[('Costo de Fondos', 'Obligaciones'), col_fmt] = f"{costo_obligaciones:.1f}%"
        df_res.loc[('Activo Productivo', 'Activo Productivo'), col_fmt] = f"{act_productivo:.1f}%"
        df_res.loc[('Liquidez', 'Liquidez'), col_fmt] = f"{liquidez:.1f}%"
        df_res.loc[('Loan to Deposit', 'Loan to Deposit'), col_fmt] = f"{loan_to_deposit:.2f}%"
        df_res.loc[('Depósito/Fondeo', 'Depósito/Fondeo'), col_fmt] = f"{dep_fondeo:.1f}%"
        df_res.loc[('Depósitos Core', 'Depósitos Core'), col_fmt] = f"{dep_core_pct:.1f}%"

        df_res = df_res.reset_index()

    return df_res

import pandas as pd

def tabla_evolucion_mensual(tabla_ER, tabla_BG, banco, año_inicio=2025, año_fin=2026, TC=36.6243):
    """
    Genera un DataFrame en formato de evolución mensual similar a la tabla de Excel:
    Muestra los meses consecutivos (e.g. jul-25 a jun-26) en las columnas,
    y los conceptos clave (Activos, Cartera, Depósitos, etc.) en las filas.
    """
    # 1. Obtener los DataFrames procesados por la función Bancos
    er_raw, er_stats = Bancos(tabla_ER, banco, año_inicio, año_fin, Variable_ER, meses, True, TC)
    bg_raw, bg_stats = Bancos(tabla_BG, banco, año_inicio, año_fin, Variable_BG, meses, False, TC)
    
    # 2. Definir las filas requeridas y mapear cómo extraerlas
    # Formato: 'Nombre en Tabla': ('tipo', 'Nombre Interno', divisor_para_millones)
    metricas = {
        'Activos': ('raw', 'Activo ()', 1000),
        'Inversiones': ('stat', 'INVERSIONES', 1),
        'Cartera': ('raw', 'Cartera de Créditos, Neta (Activo)', 1000),
        'Depósitos': ('stat', 'Depositos totales', 1),
        'Depósitos Core': ('stat', 'Depósitos Core', 1),
        'Patrimonio': ('raw', 'PATRIMONIO ()', 1000),
        'Utilidad Neta': ('stat', 'UTILIDAD NETA MENSUAL', 1) # O 'Utilidad acumulada (U$ M)'
    }

    # Helper para obtener valores de forma segura
    def get_val(tipo, campo, fecha, divisor):
        try:
            if tipo == 'raw' and campo in bg_raw.index and fecha in bg_raw.columns:
                return bg_raw.loc[campo, fecha] / divisor
            elif tipo == 'stat':
                if campo in bg_stats.index and fecha in bg_stats.columns:
                    return bg_stats.loc[campo, fecha] / divisor
                elif campo in er_stats.index and fecha in er_stats.columns:
                    return er_stats.loc[campo, fecha] / divisor
        except Exception:
            pass
        return 0.0

    # 3. Extraer todas las fechas/columnas disponibles ordenadas
    columnas_fechas = list(bg_stats.columns) if not bg_stats.empty else list(er_stats.columns)

    # 4. Construir la estructura del diccionario para el DataFrame
    data_matriz = {}
    
    for metrica, (tipo, campo, divisor) in metricas.items():
        fila_valores = {}
        for fecha in columnas_fechas:
            # Formatear la etiqueta de la fecha de "Julio 2025" -> "jul-25"
            partes = fecha.split(' ')
            if len(partes) == 2:
                mes_certo = partes[0][:3].lower()
                año_corto = partes[1][-2:]
                col_header = f"{mes_certo}-{año_corto}"
            else:
                col_header = fecha
                
            fila_valores[col_header] = get_val(tipo, campo, fecha, divisor)
            
        data_matriz[metrica] = fila_valores

    # 5. Convertir a DataFrame (Filas: Métricas, Columnas: Meses)
    df_evolucion = pd.DataFrame(data_matriz).T

    # 6. Agregar columna opcional de Validación (Suma o Máximo según necesidades)
    df_evolucion['Validacion'] = df_evolucion.max(axis=1)

    return df_evolucion


tabla_ER = read_json('Estado de Resultados (ER)', '2025-06-01', '2026-06-31')
tabla_BG = read_json('Estado de Situación Financiera (ESF)', '2025-06-01', '2026-06-31')
# tabla_IF = read_json('Indicadores Financieros', '2025-06-01', '2026-06-01')

tabla_1 = transformar_pasar_base_ER(tabla_ER, Variable_ER, bancos)[0]
tabla_2 = transformar_pasar_base_BG(tabla_BG, Variable_BG, bancos)[0]

tabla_ev = tabla_evolucion_mensual(tabla_1, tabla_2, 'BANCO FICOHSA', 2025, 2026, TC)
print(tabla_ev)

# indicador_ficohsa =indicadores_banco(tabla_1, tabla_2, 'BANCO FICOHSA', 2025, 2026, TC)
# print(indicador_ficohsa)

# avanz=Bancos(tabla_1, 'AVANZ', 2025, 2026, Variable_ER, meses, True, TC)
# Indicador_Ficohsa = Indicadores_Banco(tabla_1, tabla_2, 'Banco Ficohsa', '2025-06-01', '2026-06-31', 2025, 2026, TC)
# print(Indicador_Ficohsa)



# resumen = resumen(tabla_1, tabla_2, 'Junio', bancos, 2026, TC)
# print(resumen)



