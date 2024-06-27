import os,sys
import pytest
from unittest.mock import mock_open, patch

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

import src.my_library.load_input_data as input_loader

# モックデータ
mock_train_data = "sentence1\tlabel1\nsentence2\tlabel2"
mock_data = "raw_sentence1\nraw_sentence2"

def test_load():
    with patch("builtins.open", mock_open(read_data=mock_train_data)):
        result = input_loader.load("dummy_path")
        expected = [["sentence1", "label1"], ["sentence2", "label2"]]
        assert result == expected, f"Expected {expected}, but got {result}"

def test_load_raw_data():
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = input_loader.load_raw_data("dummy_path")
        expected = ["raw_sentence1", "raw_sentence2"]
        assert result == expected, f"Expected {expected}, but got {result}"
