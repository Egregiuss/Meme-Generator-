class QuoteModel:
    """Class that instantiates and returns both Body and Author"""
    def __init__(self, body, author):
        self.author = author
        self.body = body

    def __repr__(self) -> str:
        return f"<{self.author} , {self.body}>"

    def __str__(self):
        return f"{self.author} is {self.body}"
