import os

from commondata import DATA_DIR


class DataRetrievalBase:
    """An abstract class for common dataset retrieval classes."""

    data = None

    def __init__(self, dataset=None):
        """Retrieve the dataset based on the subclass name.

        Builds a file path for accessing a given dataset, using the subclass name
        to access the file in the 'data/' directory, and populates 'data' as a
        list with one element per line of the file. Assumes a single line per entry
        in the dataset file. Method should be overridden in the subclass if a
        different method of loading the data is required.

        :param dataset: dataset file to access, assumes 'default.txt' if none given
        """
        filename = dataset if dataset is not None else 'default.txt'
        filepath = os.path.join(DATA_DIR, self.__class__.__name__, filename)

        with open(filepath, 'r') as f:
            self.data = f.read().splitlines()
