from lxml import etree
import pandas as pd

tree = etree.parse(r"\\172.25.16.15\Reportes Cobis_BI\Remesas\2026\Julio\16072026\remesasdi_RIA_1616072026.xml")

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

print(df.head())
