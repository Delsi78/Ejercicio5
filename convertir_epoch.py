import pandas as pd
import datetime
import pytz
import locale

# Configurar el idioma español según el sistema operativo
try:
    locale.setlocale(locale.LC_TIME, "es_ES.utf8")  # Para Linux/Mac
except:
    locale.setlocale(locale.LC_TIME, "es_PE.UTF-8")
# Cargar el archivo Excel
archivo = "archivoswwww.xlsx"  # Cambia esto por el nombre correcto
df = pd.read_excel(archivo)

# Verifica que la columna tenga el nombre correcto
if "TIME" in df.columns:
    # Convertir de Epoch a fecha y hora en Perú (GMT-5)
    tz_peru = pytz.timezone("America/Lima")
    
    def convertir_fecha(epoch):
        try:
            if pd.notnull(epoch) and isinstance(epoch, (int, float)):
                return datetime.datetime.fromtimestamp(epoch, tz=tz_peru).strftime("%Y-%m-%d %H:%M:%S")
            else:
                return "ERROR"
        except:
            return "ERROR"

    df["Fecha_Legible"] = df["TIME"].apply(convertir_fecha)

    # Guardar el resultado
    resultado = "resultado_peru.xlsx"
    df.to_excel(resultado, index=False)
    print(f"✅ Conversión completada. Archivo guardado como '{resultado}'.")
else:
    print("❌ Error: No se encontró la columna 'TIME'. Verifica el archivo.")



print("Si te esfuerzas triunfaras")
print("Estudia y triunfaras")
print("Se feliz")