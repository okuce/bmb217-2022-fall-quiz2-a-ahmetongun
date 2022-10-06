class Otobus:
    """Otobus bilet satis takip sinifi"""
    def _init_(self,plaka,nereden,nereye,doluKoltuk):
        self.plaka = plaka
        self.nereden = nereden
        self.nereye = nereye
        self.doluKoltuk = doluKoltuk
        class Otobus:
    """Otobus bilet satis takip sinifi"""
    
    def _init_(self,plaka,nereden,nereye,doluKoltuk):
        self.plaka = plaka
        self.nereden = nereden
        self.nereye = nereye
        self.doluKoltuk = doluKoltuk    
    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        self.dolukoltuk -= 1
        
    def bilet_iade(self):
        """otobusteki dolu koltuk sayisini 1 azaltir"""
        self.doluKoltuk += 1
        
    def durum_yaz(self):
        """otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""    
        print(self.nereden,",",self.nereye,",",self.plaka,self.doluKoltuk,",",self.doluKoltuk)

