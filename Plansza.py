import pickle
import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Czlowiek import Czlowiek
from Zwierzeta.Antylopa import Antylopa
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Guarana import Guarana
from Zwierzeta.Lis import Lis
from Rosliny.Mlecz import Mlecz
from OrgButton import OrgButton
from Zwierzeta.Owca import Owca
from Polozenie import Polozenie
from Swiat import Swiat
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Zolw import Zolw
from Zwierzeta.CyberOwca import CyberOwca


class Plansza(QWidget):

    def __init__(self, swiat: Swiat):
        super(Plansza, self).__init__()
        self.title = 'Natalia Czapla 188813'
        self.left = 200
        self.top = 200
        self.width = 700
        self.height = 700
        self.wlacz=1
        self.cooldown=0
        self._swiat = swiat
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        for i in range(0, 20):
            for j in range(0, 20):
                button = OrgButton(self, self._swiat, i, j)
                button.resize(30, 30)
                button.move(i * 30, j * 30)
                button.setStyleSheet("background-color : lightgreen")

        # text = QTextEdit(self)
        # text.move(800, 100)
        # text.resize(300, 400)
        # Komentator.set_text_edit(text)
        self.show()

    def keyPressEvent(self, q_key_event):
        self._swiat.key_pressed = q_key_event.key()
        super().keyPressEvent(q_key_event)
        self._swiat.wykonaj_ture()
        input = self._swiat.key_pressed
        if self.wlacz==0:
            self.cooldown=self.cooldown-1
            if self.cooldown>5:
                self._swiat.umiejetnosc = 1
            else:
                self._swiat.umiejetnosc = 0
            if self.cooldown==0:
                self.wlacz=1
        if input == 85:
            if self.wlacz==1:
                print("umiejetnosc")
                self.wlacz=0
                self.cooldown=10

        if input == 87:
            print("up")
            self._swiat.kierunek=1
        if input == 83:
            print("down")
            self._swiat.kierunek=2
        if input == 65:
            print("left")
            self._swiat.kierunek=3
        if input == 68:
            print("right")
            self._swiat.kierunek=4
        if input == 90:
            mylist = self._swiat
            with open('mylist.txt', 'wb') as f:
                pickle.dump(mylist, f)
        if input == 79:
            with open('mylist.txt', 'rb') as f:
                obiekt = pickle.load(f)
            self.close()
            self.Open = Plansza(obiekt)
            self.Open.show()

        self.repaint()

    def cos(self, plansza1, plansza2):
        plansza1 = plansza2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Swiat(20, 20)
    ex = Plansza(s)

    s.dodaj_organizm_z_losowaniem(CyberOwca(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Antylopa(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(BarszczSosnowskiego(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Guarana(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Lis(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Mlecz(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Owca(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Trawa(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(WilczeJagody(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Wilk(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Zolw(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Czlowiek(s, Polozenie()))


    ex.repaint()
    sys.exit(app.exec_())