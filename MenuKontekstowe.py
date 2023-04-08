from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMenu, QAction

from Polozenie import Polozenie
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody
from Swiat import Swiat
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.Lis import Lis
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Zolw import Zolw


class MenuKontekstowe(QMenu):

    def __init__(self, swiat: Swiat, orgButton, *__args):
        super().__init__(*__args)
        self.swiat = swiat
        self.orgButton = orgButton
        self.dodaj_pola()



    def dodaj_pola(self):
        self.addAction(QAction('barszcz', self))
        self.addAction(QAction('guarana', self))
        self.addAction(QAction('mlecz', self))
        self.addAction(QAction('trawa', self))
        self.addAction(QAction('jagody', self))
        self.addAction(QAction('antylopa', self))
        self.addAction(QAction('lis', self))
        self.addAction(QAction('owca', self))
        self.addAction(QAction('wilk', self))
        self.addAction(QAction('zolw', self))
        self.triggered.connect(self.actionClicked)

    def actionClicked(self, action):
        print("Dodajesz: ")
        try:
            print(action.text())
        except AttributeError as e:
            print(e)

        if action.text() == 'barszcz':
            self.swiat.dodaj_organizm(BarszczSosnowskiego(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'guarana':
            self.swiat.dodaj_organizm(Guarana(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'mlecz':
            self.swiat.dodaj_organizm(Mlecz(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'trawa':
            self.swiat.dodaj_organizm(Trawa(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'jagody':
            self.swiat.dodaj_organizm(WilczeJagody(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'antylopa':
            self.swiat.dodaj_organizm(Antylopa(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'lis':
            self.swiat.dodaj_organizm(Lis(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'wilk':
            self.swiat.dodaj_organizm(Wilk(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'owca':
            self.swiat.dodaj_organizm(Owca(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))
        if action.text() == 'zolw':
            self.swiat.dodaj_organizm(Zolw(self.swiat, Polozenie(self.orgButton.zwrocX(), self.orgButton.zwrocY())))


