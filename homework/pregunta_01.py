"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """

    # Leer archivo
    with open("files/input/clusters_report.txt", "r") as f:
        lineas = f.readlines()
        cluster = None
        data = []
        for linea in lineas[4:]:
            linea = linea.strip()
            parte = linea.split()
            if linea:
                if parte[0].isdigit():
                    cluster = {
                        "cluster": int(parte[0]),
                        "cantidad_de_palabras_clave": int(parte[1]),
                        "porcentaje_de_palabras_clave": float(
                            parte[2].replace(",", ".").replace("%", "")
                        ),
                        "principales_palabras_clave": " ".join(parte[3:]).lstrip("%"),
                    }
                else:
                    cluster["principales_palabras_clave"] += " " + " ".join(parte)

            else:
                data.append(cluster)
        df = pd.DataFrame(data)

        df["principales_palabras_clave"] = (
            df["principales_palabras_clave"]
            .str.replace(r"\s+", " ", regex=True)  # Normalizar espacios
            .str.replace(r",\s*", ", ")  # Espacio después de comas
            .str.strip(". ")
        )

        df.columns = [col.lower().replace(" ", "_") for col in df.columns]
        print(df)

    return df


print(pregunta_01())
