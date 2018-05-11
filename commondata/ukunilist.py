from ._dataretrievalbase import DataRetrievalBase


class UkUniList(DataRetrievalBase):
    """Class for retrieving search terms."""

    def __init__(self, *args, **kwargs):
        """Invoke the superclass dataset retriever by default."""
        super(self.__class__, self).__init__(*args, **kwargs)
