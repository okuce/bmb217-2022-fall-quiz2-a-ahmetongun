class Otobus:
    """Otobus bilet satis takip sinifi"""
    def _init_(self,plaka,nereden,nereye,koltuk):
        self.plaka = plaka
        self.nereden = nereden
        self.nereye = nereye
        self.koltuk = koltuk
        self.doluKoltuk = 0
        self.bosKoltuk = koltuk
        
    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        doluKoltuk += 1
        
    def bilet_iade(self):
        """otobusteki dolu koltuk sayisini 1 azaltir"""
        bosKoltuk -= 1
        
    def durum_yaz(self):
        """otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""    
        print(self.nereden,",",self.nereye,",",self.plaka,self.doluKoltuk,",",self.bosKoltuk)
