# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:35:18 2021

@author: Furkan
"""
  
class NVezir:
    def __init__(self, boyut):
        self.boyut = boyut
        self.cozumler = 0
        self.coz()

    def coz(self):
        pozisyonlar = [-1] * self.boyut
        self.vezir_ekle(pozisyonlar, 0)
        print( self.cozumler, " tane çözüm bulundu.")

    def vezir_ekle(self, pozisyonlar, satir):
        if satir == self.boyut:
            self.tahta(pozisyonlar)
            self.cozumler += 1
        else:
            for sutun in range(self.boyut):
                if self.kontrol_et(pozisyonlar, satir, sutun):
                    pozisyonlar[satir] = sutun
                    self.vezir_ekle(pozisyonlar, satir + 1)


    def kontrol_et(self, pozisyonlar, dolu_satir, sutun):
        for i in range(dolu_satir):
            if pozisyonlar[i] == sutun or \
                pozisyonlar[i] - i == sutun - dolu_satir or \
                pozisyonlar[i] + i == sutun + dolu_satir:

                return False
        return True

    def tahta(self, pozisyonlar):
        print("Çözüm ",(self.cozumler+1))
        for satirlar in range(self.boyut):
            tahta_satir = ""
            for sutun in range(self.boyut):
                if pozisyonlar[satirlar] == sutun:
                    tahta_satir += "Q "
                else:
                    tahta_satir += ". "
            print(tahta_satir)
        print("\n")

def main():
    try:
        vezirSayisi=  int(input("Vezir Sayısını Giriniz: "))
        if vezirSayisi <0:
            vezirSayisi=vezirSayisi*-1
        NVezir(vezirSayisi)
    except Exception:
        print("Bir hata oluştu... Tekrar Deneyiniz!")
        main()
main()

