# В package/__init__.py
from .QuadricMethods import *  # Импортируем все из QuadricMethods.py
from prettytable import PrettyTable
from scipy.integrate import quad
from .funcs import f  # Импортируем функцию f из funcs.py
import matplotlib.pyplot as plt
import numpy as np
from .helpers import func_error  # Импортируем функцию func_error из helpers.py
