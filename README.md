# CSV-Translator-Python

This repository is providing a wrapper class TVEKDocumentTranslator which can be used to translate any CSV files from any source language to any destionation language.

# Environment Setup
pip install -r requirements.txt
python tvek_document_translator.py

# API Documentation

Translate all the documents using below snippet
input_csvs = Directory in which all the csv's are placed
output_csvs = Directory in which all the translated csv's are to be placed
en = Language code for language into which input_csvs needs to be translated
> translator = TVEKDocumentTranslator()
> translator.translate_all_csv('input_csvs', 'output_csvs', 'en')