# -*- coding: utf-8 -*-

import random
import math
import numpy


class nearest_neighbourhood:

    def odczytZPliku(sciezka):
        u"""Otwiera plik zawierający współrzędne miast, które zostaną użyte do wyznaczenia trasy.
        Odczytuje z pliku dane i przekształca je w tablicę.
        Zwraca tablicę ze współrzędnymi miast.
        """
        plik = open(sciezka, "r")
        try:
            wspolrzedne_miast = numpy.loadtxt(plik)
        finally:
            plik.close()
        return wspolrzedne_miast

    def numerowanieMiast(wspolrzedne_miast, N):
        u"""Tworzy tablicę oraz wypełnia ją liczbami od 1 do N, gdzie N oznacza liczbę miast używanych do wyznaczenia trasy.
        Wstawia utworzoną tablicę jako trzecią kolumnę do tablicy ze współrzędnymi miast.
        Zwraca rozbudowaną tablicę ze współrzędnymi miast."""
        numery_miast = []
        for i in range(N):
            numery_miast.append(i + 1)

        wspolrzedne_miast = numpy.insert(wspolrzedne_miast, 2, numery_miast, axis=1)
        return wspolrzedne_miast

    def losowaniePunktuStartowego(N):
        u"""Losuje punkt z zakresu od 0 do N-1, gdzie N oznacza liczbę miast używanych do wyznaczenia trasy.
        Zwraca wylosowaną wartość."""
        punkt_startowy = random.randint(0, (N - 1))
        return punkt_startowy

    def obliczanieOdleglosci(a, b, wspolrzedne_miast):
        u"""Oblicza odległość dwóch miast, miasta a, którego współrzędne zostają przekazane do funkcji, oraz miasta b, którego indeks zostaje przekazany do funkcji, względem siebie.
        Zwraca obliczoną odległość."""
        odleglosc = math.sqrt(
            (wspolrzedne_miast[b][0] - a[0]) * (wspolrzedne_miast[b][0] - a[0]) + (wspolrzedne_miast[b][1] - a[1]) * (
            wspolrzedne_miast[b][1] - a[1]))
        return odleglosc

    def zapisDoPliku(wynik):
        u"""Otwiera lub tworzy, jeżeli nie istnieje, plik oraz zapisuje do niego wynik działania algorytmu."""
        cel = open("plik_z_wynikami.txt", "w")
        try:
            wynik.tofile(cel, sep="\n", format="%i")
        finally:
            cel.close()

    def algorytmNN(sciezka):
        u"""Przy pomocy funcji odczytZPliku pobiera dane startowe.
        Mierzy długość tablicy wejściowej, oznacza ją jako N, gdzie N to ilość miast używanych do wyznaczenia trasy.
        Przy pomocy funkcji numerowanieMiast modyfikuje tablicę z danymi wejściowymi.
        Przy pomocy funkcji losowaniePunktuStartowego wyznacza indeks punktu startowego trasy.
        Tworzy pustą tablicę, do której zapisywany będzie wynik końcowy.
        Do tablicy z wynikiem końcowym zapisuje punkt startowy trasy.
        Z tablicy ze współrzędnymi miast dostępnymi do odwiedzenia usuwa punkt startowy.
        Inicjalizuje zmienną oznaczającą długość trasy i przypisuje jej wartość początkową 0.
        W pętli składającej się z N kroków, wyznacza kolejność odwiedzanych miast.
        Dla każdego wybranego miasta, zaczynając od wylsowanego punktu startowego, oblicza odległości do miast, wzciąż pozostałych do odwiedzenia i wybiera najbliższe z nich.
        Najbliższe miasto staje się nowym wybranym miastem, a odległość do niego zostaje dodana do długości trasy.
        Wybrane miasto zostaje dodane do tablicy z wynikiem końcowym oraz usunięte z tablicy miast dostępnych do odwiedzenia.
        Po ustaleniu kolejności wszystkich N miast tablica z wynikiem zostaje zapisana do pliku przy pomocy funkcji zapisDoPliku.
        Zwraca tablicę z ustaloną kolejnością odwiedzania miast."""
        dane_startowe = nearest_neighbourhood.odczytZPliku(sciezka)
        N = len(dane_startowe)
        wspolrzedne_miast = nearest_neighbourhood.numerowanieMiast(dane_startowe, N)
        punkt_startowy = nearest_neighbourhood.losowaniePunktuStartowego(N)
        a = wspolrzedne_miast[punkt_startowy,]
        wynik = []
        wynik = numpy.append(wynik, wspolrzedne_miast[punkt_startowy, 2])
        wspolrzedne_miast = numpy.delete(wspolrzedne_miast, punkt_startowy, axis=0)
        dlugosc_trasy = 0

        for i in range(0, (N - 1)):
            najmniejsza_odleglosc = 100 * math.sqrt(2)
            for b in range(0, len(wspolrzedne_miast)):
                odleglosc = nearest_neighbourhood.obliczanieOdleglosci(a, b, wspolrzedne_miast)

                if odleglosc <= najmniejsza_odleglosc:
                    najmniejsza_odleglosc = odleglosc
                    najblizsze_miasto = b

            a = wspolrzedne_miast[najblizsze_miasto,]
            dlugosc_trasy = dlugosc_trasy + najmniejsza_odleglosc

            wynik = numpy.append(wynik, wspolrzedne_miast[najblizsze_miasto, 2])
            wspolrzedne_miast = numpy.delete(wspolrzedne_miast, najblizsze_miasto, axis=0)

        nearest_neighbourhood.zapisDoPliku(wynik)

        return wynik


if __name__ == '__main__':
    nearest_neighbourhood.algorytmNN("TSP30.txt")