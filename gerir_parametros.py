import pandas as pd
import numpy as np
class GerirParamentros:
    BARRAS_PATH="barras.csv"
    LIGACOES_PATH="ligacoes.csv"
    COL_LIGACOES=["De","Para","R (%)","X (%)","b (%)","tap (pu)","defas (pu)"]
    COL_BARRAS=["Barra","XG (pu)","PD (MW)","QD (MVAr)","Qsh (MVAr)","V (pu)","Ang. (graus)"]
    @staticmethod
    def cria_csv(name_path:str,df:pd.DataFrame):
        df.to_csv(name_path,index=False,encoding="utf-8")
        print(f"arquivo {name_path} criado com sucesso!")
    
    @staticmethod
    def csv_to_df(name_path)->pd.DataFrame:
        return pd.read_csv(name_path)

    @staticmethod
    def mod_to_complex(valor:float,angle:float)->complex:
        '''Valor em  polar para retangular '''
        radiano=angle*np.pi/180
        return complex(valor*np.cos(radiano),valor*np.sin(radiano))
    