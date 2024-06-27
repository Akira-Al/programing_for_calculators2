import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)   

import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
from my_library.Data_preprocessor import DataPreprocessor

data_path = input("Enter the path for the data file: ")
dictionary_path = input("Enter the path for the dictionary file: ")
preprocessed_data_path = input("Enter the path to save the preprocessed data: ")

labeled = input("Enter if the data is labeled (Y/N):")

dictionary = dictionary_loader.load(dictionary_path)
if labeled == "Y":
    sentence_arrays = input_loader.load(data_path)
    data_preprocessor = DataPreprocessor(sentence_arrays[1:], dictionary)
    data_preprocessor.preprocess_data_and_label()
else:
    sentence_arrays = input_loader.load_raw_data(data_path)
    data_preprocessor = DataPreprocessor(sentence_arrays, dictionary)
    data_preprocessor.preprocess_data()

data_preprocessor.dump(preprocessed_data_path)