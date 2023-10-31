class Aviao:
    def __init__(self, qtd_asas, qtd_banherios, tem_bico, qtd_janelas, qtd_turbinas, tem_trem_pouso, logos):
        self.qtd_asas = qtd_asas
        self.qtd_banherios = qtd_banherios
        self.tem_bico = tem_bico
        self.qtd_janelas = qtd_janelas
        self.qtd_turbinas = qtd_turbinas
        self.tem_trem_pouso = tem_trem_pouso
        self.logos = logos
        
aviao = Aviao(
    qtd_asas=2,
    qtd_banherios=1,
    tem_bico=True, 
    qtd_janelas=14, 
    qtd_turbinas=4, 
    tem_trem_pouso=True,
    logos=2)