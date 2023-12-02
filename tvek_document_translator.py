import csv
import os
import time
from googletrans import Translator

class TVEKDocumentTranslator():
    def __init__(self, file_extension = '.csv') -> None:
        self._translator = Translator()
        self._extension = file_extension

    def translate(self, s, lang = "en"):
        return self._translator.translate(text=s, dest=lang).text
    
    def translate_all_csv(self, input_folder:str, output_folder:str,target_language:str = "en"):
        all_files = os.listdir(input_folder)
        csv_files = [ filename for filename in all_files if filename.endswith( self._extension ) ]
        for csv_file in csv_files:
            file_path = input_folder + os.path.sep + csv_file
            translated_file_path = output_folder + os.path.sep + csv_file[:-4] + '_' + target_language + self._extension
            with open(file_path, "r") as infile, open(translated_file_path, "w") as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)

                for row in reader:
                    print(row)
                    translated_row = [self.translate(item, target_language) for item in row]
                    writer.writerow(translated_row)
                    time.sleep(0.5) # Added intentionally to ensure we are not spamming Google Server

if __name__ == '__main__':
    translator = TVEKDocumentTranslator()
    translator.translate_all_csv('input_csvs', 'output_csvs')