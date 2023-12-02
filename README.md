# CSV-Translator-Python

This repository is providing a wrapper class TVEKDocumentTranslator which can be used to translate any CSV files from any source language to any destionation language.

# Environment Setup
pip install -r requirements.txt
python tvek_document_translator.py

# API Documentation

Translate all the documents using below snippet<br />
input_csvs = Directory in which all the csv's are placed<br />
output_csvs = Directory in which all the translated csv's are to be placed<br />
en = Language code for language into which input_csvs needs to be translated<br />
> translator = TVEKDocumentTranslator();<br />
> translator.translate_all_csv('input_csvs', 'output_csvs', 'en')