import numpy as np
from scipy.sparse import csr_matrix

# Klasse Funktion repräsentiert eine quadratische mehrdimensionale mathematische Funktion 1/1x^tAx - b^tx.
# _A: Matrix der Funktion
# _b: Vektor b der Funktion
# Bereitgestellt werden zudem Funktionen zu Auswertung der Funktion am Punkt x, sowie des Gradienten und der Hessematrix
class Funktion(object):
    def __init__(self, A, b):
        self._A = A
        self._b = b

    def A(self):
        return self._A

    def b(self):
        return self._b

    def wert(self, x):
        return 0.5 * np.dot(x, np.dot(self._A, x)) - np.dot(self._b, x)

    def gradient(self, x):
        return np.dot(self._A, x) - self._b

    def hesse(self, x):
        return self._A

    def __repr__(self):
        return "Funktion(A = {0},b = {1})".format(self._A, self._b)

    def __str__(self):
        return "A: {0}, b: {1}".format(self._A, self._b)
