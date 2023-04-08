from Polozenie import Polozenie
from Zwierze import Zwierze


class Czlowiek(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Czlowiek, self).__init__(9, 5, swiat, polozenie)

    def sklonuj(self):
        return Czlowiek(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "C"

    def pobierz_kolor(self):
        return "background-color : pink"

    def akcja(self):
        nowe = self.swiat.zwroc_polozenie_czlowieka(self.polozenie, 1, 0)
        sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if self.swiat.kierunek==1:
            nowe = self.swiat.zwroc_polozenie_czlowieka(self.polozenie, 1, 1)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if self.swiat.kierunek==2:
            nowe = self.swiat.zwroc_polozenie_czlowieka(self.polozenie, 1, 2)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if self.swiat.kierunek==3:
            nowe = self.swiat.zwroc_polozenie_czlowieka(self.polozenie, 1, 3)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if self.swiat.kierunek==4:
            nowe = self.swiat.zwroc_polozenie_czlowieka(self.polozenie, 1, 4)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if sasiad is not None and sasiad is not self:

            sasiad.kolizja(self)
        else:
            self.polozenie = nowe

    def kolizja(self, atakujacy):
        if self.swiat.umiejetnosc == 1:
            print("tarcza")
            super(Czlowiek, self).kolizja(atakujacy)
        else:
            if atakujacy.get_sila() > self._sila:
                atakujacy.polozenie = self.polozenie
                self.swiat.usun_organizm(self)
                print(atakujacy.pobierz_znak() + " zjadl " + self.pobierz_znak())


            else:
                self.swiat.usun_organizm(atakujacy)
                print(self.pobierz_znak() + " zjadl " + atakujacy.pobierz_znak())
