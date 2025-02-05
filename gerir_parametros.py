

import pandas as pd
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
    def csv_to_df(name_path):
        return pd.read_csv(name_path)
