import pandas as pd
from pathlib import Path
from datetime import datetime

# df = pd.read_excel('/Users/carlossequeira/Downloads/Estudiantes(Público).xlsx')


#info importante, modificar antes de ejecutar

#ver si es una fecha válida
def is_valid_date(date_string, date_format="%d%m%Y"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
        
folder_path = Path("path/to/your/folder")

df_PAGADAS= pd.DataFrame()
df_ENVIADAS= pd.DataFrame()

#separar los excels según los nombres en las filas
def encontrar_fila_separadora(df: pd.DataFrame, marker1: str, marker2: str):
    marker1_idx = None
    marker2_idx = None
 
    for idx, row in df.iterrows():
        row_text = " ".join(str(v) for v in row.values if pd.notna(v))
        if marker1_idx is None and marker1 in row_text:
            marker1_idx = idx
        elif marker2_idx is None and marker2 in row_text:
            marker2_idx = idx
 
    if marker1_idx is None or marker2_idx is None:
        raise ValueError(
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

def main(fecha):
	for item in folder_path.iterdir():
		nueva_fecha = [item.name[i:i+2] for i in range(len(item.name) - 2)]
		if item.is_dir() and is_valid_date(item.name) and int(nueva_fecha[0]) <= int(fecha):
			for documento in item.iterdir():
				if documento.name.startswith('remesasdi'):
					df_remesas_di = pd.read_excel(documento)
					del df_remesas_di['MTO_PAGADOS_CORDOBAS']

					marker1, marker2 = encontrar_fila_separadora(df_remesas_di, "REMESAS PAGADAS", 'REMESAS ENVIADAS')
					df1, df2 = dividir_dataframe(df_remesas_di, marker1, marker2)

					df_PAGADAS = pd.concat([df_PAGADAS, df1], ignore_index=True)
					df_ENVIADAS = pd.concat([df_ENVIADAS, df2], ignore_index=True)

				elif documento.name.startswith('transnetwork_di'):
					df_transnetwork_di = pd.read_excel(documento)
					del df_transnetwork_di['MTO_PAGADOS_CORDOBAS']

					marker_1, marker_2 = encontrar_fila_separadora(df_transnetwork_di, "REMESAS PAGADAS", 'REMESAS ENVIADAS')
					df_1, df_2 = dividir_dataframe(df_transnetwork_di, marker_1, marker_2)

					df_PAGADAS = pd.concat([df_PAGADAS, df_1], ignore_index=True)
					df_ENVIADAS = pd.concat([df_ENVIADAS, df_2], ignore_index=True)

				elif documento.name.startswith('pairpack_di'):
					df_pairpack_di = pd.read_excel(documento)

					marker__1, marker__2 = encontrar_fila_separadora(df_pairpack_di, "REMESAS PAGADAS", 'REMESAS ENVIADAS')
					df__1, df__2 = dividir_dataframe(df_pairpack_di, marker__1, marker__2)

					df_PAGADAS = pd.concat([df_PAGADAS, df__1], ignore_index=True)
					df_ENVIADAS = pd.concat([df_ENVIADAS, df__2], ignore_index=True)

with pd.ExcelWriter('REMESAS_ENVIADAS_PAGADAS.xlsx') as writer:
    df_PAGADAS.to_excel(writer, sheet_name='PAGADAS', index=False)
    df_ENVIADAS.to_excel(writer, sheet_name='ENVIADAS', index=False)