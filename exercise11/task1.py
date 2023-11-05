class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"Title: {self.name}\nAuthor: {self.author}\nPage: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        print(f"Title: {self.name}\nChief editor: {self.chief_editor}")


publication1 = Magazine("Donald Duck", "Aki Hyyppä")
publication2 = Book("Compartment No. 6", "Rosa Liksom", 192)

publication1.print_info()
publication2.print_info()
