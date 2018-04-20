# A simple svg to pdf creator with text replacement

## Introduction

This tool heavily relies on svglue. The purpose is to have a template file
with some texts that need to be replaced. Ideally this svg file consists of the
same objects multiple times (like an invitation card), with the only difference
being that some text spans have unique 'template-id's. Then this tool can
use an input text file to replace those template-ids with the real texts.
This way the same output can be regenerated over and over again if the
template changes and there will not be misalignments and everything will
look the same.

For an example see the unit tests.

## Installation

`git clone https://github.com/szebenyib/svg_to_pdf`

`pip install -r requirements.txt`

## Testing and example

`python -m unittest`

Then check the output in the test folder.
