import pandas as pd
import re


def detectar_datos_estaticos(df):
    empresa = ""
    fecha = ""
    cliente_n = ""

    for i in range(5):
        if "EMPRESA" in str(df.iloc[i, 0]):
            empresa = df.iloc[i, 1]
        elif "FECHA" in str(df.iloc[i, 0]):
            fecha = pd.to_datetime(df.iloc[i, 1]).strftime('%d/%m/%Y')
        elif "CLIENTE" in str(df.iloc[i, 0]):
            cliente_n = df.iloc[i, 1]
    
    for i in range(-1, -6, -1):
        if "EMPRESA" in str(df.iloc[i, 0]):
            empresa = df.iloc[i, 1]
        elif "FECHA" in str(df.iloc[i, 0]):
            fecha = pd.to_datetime(df.iloc[i, 1]).strftime('%d/%m/%Y')
        elif "CLIENTE" in str(df.iloc[i, 0]):
            cliente_n = df.iloc[i, 1]
    
    return empresa, fecha, cliente_n


def procesar_hoja(df):
    empresa, fecha, cliente_n = detectar_datos_estaticos(df)
    registros = []

    for _, row in df.iterrows():
        if re.match(r"(PS|CO2)", str(row[0])):
            tipo = row[0]
            n_identificacion = row[1]
            carga = row[2]
            peso = row[3]
            presion = row[4]
            revision = row[5]
            vto_b = row[6] if len(row) > 6 else ""
            observaciones = row[7] if len(row) > 7 else ""
            
            registros.append([empresa, fecha, cliente_n, tipo, n_identificacion, carga, peso, "", presion, revision, "", vto_b, observaciones])
    
    return registros

def procesar_excel(archivo_excel):

    excel_data = pd.ExcelFile(archivo_excel)
    todas_las_hojas = excel_data.sheet_names
    todos_los_registros = []
    
    for hoja in todas_las_hojas:
        df = pd.read_excel(archivo_excel, sheet_name=hoja, header=None)
        registros = procesar_hoja(df)
        todos_los_registros.extend(registros)
    
    columnas = ["EMPRESA", "FECHA", "CLIENTE_N", "TIPO", "N_IDENTIFICACION", "CARGA", "PESO", "ZONA", "PRESION", "REVISION", "FECHA_P_H", "VTO_B", "OBSERVACIONES"]
    df_final = pd.DataFrame(todos_los_registros, columns=columnas)
    
    df_final.to_csv("resultado_extintores_general.csv", index=False)
    print("Archivo CSV generado: resultado_extintores_general.csv")

archivo_excel = 'cofrai_data_challenge.xlsx'
procesar_excel(archivo_excel)