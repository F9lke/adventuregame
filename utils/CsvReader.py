from utils.FileReader import FileReader


class CsvReader(FileReader):

    def __init__(self, filename):
        super().__init__(filename)

    def line(self):
        lines = super().line()
        lines_splitted = []

        for line in lines:
            lines_splitted.append(line.split(","))
