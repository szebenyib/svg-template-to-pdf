import svglue
import copy
import cairosvg
import pdb

class Converter:

    """Reads and svg file as a template and a text file, which contains the
       values to replace. The svg file should have spath tags with unique
       'template-id's to allow replacement."""

    def __init__(self, svg_filename, replace_filename, placeholder_text,
                 number_of_texts_on_page, output_filename):
        """Storing filenames, placeholder and template-id's per page"""
        self.svg_filename = svg_filename
        self.replace_filename = replace_filename
        self.output_filename = output_filename
        self.placeholder_text = placeholder_text
        self.number_of_texts_on_page = number_of_texts_on_page
        self.svg = None
        self.replace_items = None
        self.processed_svgs = []

    def load_data(self):
        """Loads the svg and the replacement data"""
        self.svg = svglue.load(file=self.svg_filename)
        with open(self.replace_filename, 'r') as f:
            self.replace_items = f.readlines()
        self.replace_items = [item.rstrip() for item in self.replace_items]

    def create_processed_svgs(self):
        """Creates a list of svgs with template-id's replaced with the values
           of the replacement file"""
        number_of_items_to_replace = len(self.replace_items)
        position_in_page = 0
        svg_counter = 0

        for i in range(number_of_items_to_replace):
            if (i % self.number_of_texts_on_page == 0 and
                i >= self.number_of_texts_on_page):
                self.processed_svgs.append(copy.deepcopy(self.svg))
                svg_counter += 1
                position_in_page = 0
            self.svg.set_text(self.placeholder_text + str(position_in_page),
                              self.replace_items[i])
            position_in_page += 1
        self.processed_svgs.append(copy.deepcopy(self.svg))


    def export_processed_svgs(self):
        """Creates svg files on the disk, 1 based numbering"""
        for i in range(len(self.processed_svgs)):
            with open(self.output_filename + str(i + 1) + ".svg",
                      "w") as f:
                src = self.processed_svgs[i].__str__().decode("utf8")
                f.write(src)


    def export_pdfs(self):
        """Creates a pdf from the processed svgs, 1 based numbering"""
        for i in range(len(self.processed_svgs)):
            with open(self.output_filename + str(i + 1) + ".pdf",
                      "wb") as f:
                src = self.processed_svgs[i].__str__().decode("utf8")
                cairosvg.svg2pdf(bytestring=src, write_to=f)


if __name__ == '__main__':
    converter = Converter(svg_filename='../input/template.svg',
                          replace_filename='../input/items.txt',
                          output_filename='../output/output_',
                          placeholder_text='nev',
                          number_of_texts_on_page=6)
    converter.load_data()
    converter.create_processed_svgs()
    converter.export_processed_svgs()
    converter.export_pdfs()
