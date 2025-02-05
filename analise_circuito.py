import numpy as np
import pandas as pd
from gerir_parametros import GerirParamentros
class AnaliseCircuito:
    def __init__(self):
        #TODOS OS VALORES UTILIZADOS PARA CALCULOS ESTÃO EM PU
        try:
            self.dbar=GerirParamentros.csv_to_df(GerirParamentros.BARRAS_PATH)
            self.dlin=GerirParamentros.csv_to_df(GerirParamentros.LIGACOES_PATH)
        except:
            print("Não foi possível carregar os arquivos .csv ")
        else:
            print("Arquivos carregados com sucesso !")

        self.pot_base= 100 #MVA

        #número de linhas de cada dataframe
        self.n_bar=self.dbar.shape[0]
        self.n_lin=self.dlin.shape[0]

        self.y_bus=np.zeros((self.n_lin,self.n_lin),dtype=complex) # NbxNb
        self.v_bus=np.zeros(self.n_bar)
        
        
    def calc_y_bus(self):
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
    

        
      
    def calc_other_params(self):
        #TODO: organizar e dividir essa função
        for b in range(self.n_bar):
            bd=self.dbar[GerirParamentros.COL_BARRAS[0]][b]
            xg=complex(0,self.dbar[GerirParamentros.COL_BARRAS[1]][b])
            Pd=self.dbar[GerirParamentros.COL_BARRAS[2]][b]/self.pot_base
            Qd=self.dbar[GerirParamentros.COL_BARRAS[3]][b]/self.pot_base
            v_mod=np.abs(self.dbar[GerirParamentros.COL_BARRAS[5]][b])
            v_ang=self.dbar[GerirParamentros.COL_BARRAS[6]][b] #em graus



            self.v_bus[b]=GerirParamentros.mod_to_complex(v_mod,v_ang)
            Sd=complex(Pd,Qd) #MVA


            yd=Sd.conjugate()/(np.abs(self.v_bus[b])**2)

            yg=1/xg

            self.y_bus[bd][bd]+=yg+yd


        
        self.i_bus=np.dot(self.y_bus,self.v_bus)




            


        
            



    


    