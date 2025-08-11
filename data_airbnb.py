import os
import pandas as pd
from IPython.display import display, HTML

try:
    path = os.path.dirname(os.path.abspath(__file__))
    listings_path = os.path.join(path, "Data")
    print("Loading data from:", listings_path)
    
    # Esta línea es correcta y funcionará después de instalar openpyxl
    listings_df = pd.read_excel(os.path.join(listings_path, "listings.xlsx"))
    
    print("\nData loaded successfully.")
    display(HTML("<h2>Airbnb Listings Data</h2>"))
    display(listings_df.head())
    #print("\nDataFrame shape:", listings_df.shape)
    #print("\nDataFrame columns:", listings_df.columns.tolist())
    #print("\nDataFrame info:")
    #print(listings_df.info())

except FileNotFoundError:
    # Corregido para mostrar el nombre de archivo correcto en el error
    print("\nError: El archivo 'listings.xlsx' no fue encontrado en el directorio 'Data'.")
    raise