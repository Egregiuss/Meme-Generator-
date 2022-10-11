import os
import random
import argparse

from QuoteEngine import Ingestor

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Meme")
    parser.add_argument("--path", type=str, help="Specify path to the Image")
    parser.add_argument("--body", type=str, help="Body of the quote goes here")
    parser.add_argument(
        "--author", type=str, help="Author of the quote goes here"
    )

    args = parser.parse_args()
    path, body, author = args.path, args.body, args.author
    print(generate_meme(args.path, args.body, args.author))
