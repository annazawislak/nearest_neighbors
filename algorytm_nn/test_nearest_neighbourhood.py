from unittest import TestCase
from NearestNeighbors import nearest_neighbourhood


class TestOdczytZPliku(TestCase):
    def setUp(self):
        self.zrodlo = nearest_neighbourhood.odczytZPliku('testowy.txt')

    def test_odczytZPliku(self):
        self.assertIsNotNone(self.zrodlo)


class TestNumerowanieMiast(TestCase):
    def setUp(self):
        wspolrzedne_miast = [[0 for col in range(2)] for row in range(5)]
        self.miasta = nearest_neighbourhood.numerowanieMiast(wspolrzedne_miast, 5)

    def test_numerowanieMiast(self):
        self.assertEqual(len(self.miasta.transpose()), 3)


class TestLosowaniePunktuStartowego(TestCase):
    def setUp(self):
        self.punkt = nearest_neighbourhood.losowaniePunktuStartowego(30)

    def test_losowaniePunktuStartowego(self):
        tab = []
        for i in range(30):
            tab.append(i)
        self.assertIn(self.punkt, tab)


class TestObliczanieOdleglosci(TestCase):
    def setUp(self):
        a = [7, 60]
        b = 4
        wspolrzedne_miast = [[24, 18], [7, 87], [66, 24], [3, 5], [8, 60]]
        self.odleglosc = nearest_neighbourhood.obliczanieOdleglosci(a, b, wspolrzedne_miast)

    def test_obliczanieOdleglosci(self):
        odl_ab = 1.0
        self.assertEqual(self.odleglosc, odl_ab)


class TestZapisDoPliku(TestCase):
    def test_zapisDoPliku(self):
        self.zrodlo = open("plik_z_wynikami.txt", "r")
        self.assertIsNotNone(self.zrodlo)


class TestAlgorytmNN(TestCase):
    def test_algorytmNN(self):
        self.wynik = nearest_neighbourhood.algorytmNN('testowy.txt')
        self.assertEqual(len(self.wynik), 5)

