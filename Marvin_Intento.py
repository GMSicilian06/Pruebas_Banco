from lxml import etree
import pandas as pd
import os
from pathlib import Path
from datetime import datetime

def leer_xml(file_path):
    tree = etree.parse(file_path)

    ns = {
        "ss": "urn:schemas-microsoft-com:office:spreadsheet"
    }

    rows = []

    for row in tree.xpath("//ss:Row", namespaces=ns):
        values = []

        for cell in row.xpath("./ss:Cell", namespaces=ns):
            data = cell.xpath("./ss:Data/text()", namespaces=ns)

            values.append(data[0] if data else "")

        rows.append(values)

    df = pd.DataFrame(rows)
    return df

def read_file_to_dataframe(file_path):
    """
    Leer los archivos
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get file extension in lowercase
    ext = os.path.splitext(file_path)[1].lower()

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        if ext in ['.xml']:
           df = leer_xml(file_path)
           
        elif ext in ['.xls', '.xlsx']:
            """try:
               df = pd.read_csv(file_path, sep= "\t")
            except Exception as e:"""
            df = pd.read_csv(file_path, header=None)
                
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
        return df

    except Exception as e:
        raise ValueError(f"Error reading {file_path}: {e}")
    
def is_valid_date(date_string, date_format="%d%m%Y"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

#separar los excels según los nombres en las filas
def encontrar_fila_separadora(df: pd.DataFrame, marker1: str, marker2: str):
    marker1_idx = None
    marker2_idx = None

    print(df)
    print("")
    print("")
    print("")

    for idx, row in df.iterrows():
        print(idx, row.loc[0])
        row_text = " ".join(str(v) for v in row.values if pd.notna(v))
        if marker1_idx is None and marker1 in row_text:
            marker1_idx = idx
        elif marker2_idx is None and marker2 in row_text:
            marker2_idx = idx

    if marker1_idx is None or marker2_idx is None:
        print(
            f"No encuentra los separadores o tal vez no tienen los mismos nombres"
            f"no se encontró el primer separador "
            f"no se encontró el segundo separador"
        )

    return marker1_idx, marker2_idx

def dividir_dataframe(df: pd.DataFrame, marker1_idx: int, marker2_idx: int):
    """
    Divide la data en dos bloques 
    """
    # del inicio, obvia la primera y sigue hasta encontrar el "REMESAS ENVIADAS"
    header1_idx = marker1_idx + 1
    df1 = df.iloc[header1_idx + 1 : marker2_idx].copy()
    df1.columns = df.iloc[header1_idx]
    df1 = df1.reset_index(drop=True)

    #corre hasta el final
    header2_idx = marker2_idx + 1
    df2 = df.iloc[header2_idx + 1 :].copy()
    df2.columns = df.iloc[header2_idx]
    df2 = df2.reset_index(drop=True)

    return df1, df2

def main(fecha, file_path):
    folder_path = Path(file_path)
    df_PAGADAS = pd.DataFrame()
    df_ENVIADAS = pd.DataFrame()

    for item in folder_path.iterdir():
        nueva_fecha = [item.name[i:i+2] for i in range(len(item.name) - 2)]
        if item.is_dir() and is_valid_date(item.name) and int(nueva_fecha[0]) <= int(fecha):
            for documento in item.iterdir():
                print(documento)
                df = read_file_to_dataframe(documento)
                marker__1, marker__2 = encontrar_fila_separadora(df, "REMESAS PAGADAS", 'REMESAS ENVIADAS')
                df__1, df__2 = dividir_dataframe(df, marker__1, marker__2)
                df_PAGADAS = pd.concat([df_PAGADAS, df__1], ignore_index=True)
                df_ENVIADAS = pd.concat([df_ENVIADAS, df__2], ignore_index=True)

    with pd.ExcelWriter(r"C:\Users\NI38504\Documents\Home\REMESAS\PRUEBAS-PY\REMESAS_ENVIADAS_PAGADAS.xlsx") as writer:
        df_PAGADAS.to_excel(writer, sheet_name='PAGADAS', index=False)
        df_ENVIADAS.to_excel(writer, sheet_name='ENVIADAS', index=False)

if __name__ == "__main__":
    main(20260701, r"\\172.25.16.15\Reportes Cobis_BI\Remesas\2026\Julio")
