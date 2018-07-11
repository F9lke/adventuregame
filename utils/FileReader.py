class FileReader:

    def __init_(self, filename):
        self.filename = filename

    def line(self, filename: str=False):
        if not filename: filename = self.filename
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines
