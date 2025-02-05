import numpy as np
import pandas as pd
from gerir_parametros import GerirParamentros
class AnaliseCircuito:
    def __init__(self):

        self.dbar=GerirParamentros.csv_to_df(GerirParamentros.BARRAS_PATH)
        self.dlin=GerirParamentros.csv_to_df(GerirParamentros.LIGACOES_PATH)


        #número de linhas de cada dataframe
        self.n_bar=self.dbar.shape[0]
        self.n_lin=self.dlin.shape[0]

        self.y_bus=np.zeros((self.n_lin,self.n_lin),dtype=complex) # NbxNb
        self.calc_y_bar()
        
    def calc_y_bar(self):
        for c in range(self.n_lin):

            bd=self.dlin[GerirParamentros.COL_LIGACOES[0]][c]
            bp=self.dlin[GerirParamentros.COL_LIGACOES[1]][c]
            r=self.dlin[GerirParamentros.COL_LIGACOES[2]][c]
            x=self.dlin[GerirParamentros.COL_LIGACOES[3]][c]
            b=self.dlin[GerirParamentros.COL_LIGACOES[4]][c]
            z=complex(r,x)

            

            self.y_bus[bd][bd]=self.y_bus[bd,bd]+1/z+b/2
            self.y_bus[bp,bp]=self.y_bus[bp,bp]+1/z+b/2
            self.y_bus[bd,bp]=self.y_bus[bd,bp]-1/z
            self.y_bus[bp,bd]=self.y_bus[bp,bd]-1/z
    def calc_demais_params(self):
        for b in range(self.n_bar):
            bd=self.dbar[GerirParamentros.COL_BARRAS[0]][b]
            
            v_ang=self.dbar[GerirParamentros.COL_BARRAS[5]][b]


            


        
            



    


    