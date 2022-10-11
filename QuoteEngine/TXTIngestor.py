from typing import List
import numpy as np

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class that Ingests TXT files"""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot import")

        quotes = []
        with open(path) as file:
            for line in file.readlines():
                line = line.strip("\n\r").strip("ï»¿")
                if len(line) > 0:
                    parse = line.split("-")
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
