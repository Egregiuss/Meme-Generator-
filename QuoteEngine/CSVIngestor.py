from typing import List
import pandas


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class that ingests CSV files"""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot import")

        quotes = []
        df = pandas.read_csv(path)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row["body"], row["author"])
            quotes.append(new_quote)

        return quotes
