"""
Utitility methods
"""
import csv

def load_choices(path, reversed=False):
    """ Load choices from a CSV file.
    The choices are expected to be a list of CSV pairs `v,k` where `k` is the
    short symbol value of the choice, and `v` is the human-readable value of
    choice.

    :param path: Path of the CSV file to load.

    :param reversed: key and value are reversed.
    :optional reversed: True

    :return: List of tuples containing the choices.
    """
    choices = []
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        for (symbol, value) in reader:
            if reversed:
                states.append(value, symbol)
            else:
                states.append(symbol, value)
    return states

def get_current_year
