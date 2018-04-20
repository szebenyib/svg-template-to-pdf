import unittest
from svg_template_to_pdf import svg_template_to_pdf
import os
import math
import pdb

number_of_texts_on_page = 2

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = svg_template_to_pdf.Converter(
            svg_filename='test/input/test.svg',
            replace_filename='test/input/test.txt',
            output_filename='test/output/output_',
            placeholder_text='nev',
            number_of_texts_on_page=
            number_of_texts_on_page)

    def tearDown(self):
        self.converter = None

    def test_load_data(self):
        self.converter.load_data()
        self.assertIsNotNone(self.converter.svg)
        self.assertEqual(self.converter.replace_items,
                    ["Foo", "Bar", "Baz", "Árvíztűrő tükörfúrógép"])

    def test_create_processed_svgs(self):
        self.converter.load_data()
        self.converter.create_processed_svgs()
        self.assertEqual(len(self.converter.processed_svgs), 2)

    def test_export_processed_svgs(self):
        self.converter.load_data()
        self.converter.create_processed_svgs()
        self.converter.export_processed_svgs()
        for string in self.converter.replace_items:
            self.assertTrue(any([string in item.__str__().decode("utf8")
                                 for item in self.converter.processed_svgs]),
                           "All the replace items are found in the processed \
                            svg")

    def test_export_pdfs(self):
        self.converter.load_data()
        self.converter.create_processed_svgs()
        self.converter.export_pdfs()
        file_names = os.listdir("test/output")
        expected_files = math.ceil(len(self.converter.replace_items) /
                                   number_of_texts_on_page)
        for i in range(expected_files):
            self.assertTrue(("output_" +
                             str(i + 1) +
                             ".pdf") in file_names)


if __name__ == '__main__':
    unittest.main()
