import os,sys
import pytest
import pickle
import numpy as np
from unittest.mock import mock_open, patch

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
sys.path.append(os.path.join(project_root_path, "src", "my_library"))

import src.my_library.Data_preprocessor as DataPreprocessor


# モックデータとモック辞書を用意
mock_sentences1 = ["This is a test sentence", "Another test sentence"]
mock_sentences2 = [
    ["This is a test sentence.", "dummy2", "dummy3", "dummy4", "1"],
    ["Another test sentence.", "dummy2", "dummy3", "dummy4", "0"]
]

mock_dictionary = [["test", "p"], ["sentence", "n"], ["This", "e"]]

mock_count_vectors = [[1, 1, 1, 3], [1, 1, 0, 2]]

def test_preprocess_data():
    dp = DataPreprocessor.DataPreprocessor( mock_sentences1, mock_dictionary)
    dp.preprocess_data()
    assert np.array_equal(dp.X, np.array(mock_count_vectors))

def test_preprocess_data_and_label():
    dp = DataPreprocessor.DataPreprocessor(mock_sentences2, mock_dictionary)
    dp.preprocess_data_and_label()
    assert np.array_equal(dp.X, np.array(mock_count_vectors))
    assert np.array_equal(dp.y, np.array([1, -1]))

def test_dump(tmp_path):
    dp = DataPreprocessor.DataPreprocessor(mock_sentences2, mock_dictionary)
    dp.preprocess_data_and_label()
    file_path = os.path.join(tmp_path , "preprocessed_data.pkl")
    dp.dump(file_path)
    
    with open(file_path, "rb") as f:
        X, y = pickle.load(f)
    
    assert np.array_equal(X, np.array(mock_count_vectors))
    assert np.array_equal(y, np.array([1, -1]))
    os.remove(file_path)