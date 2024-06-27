import os,sys
import pytest
import numpy as np
import pickle
from sklearn.svm import SVC

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

from src.my_library.Trainer import Trainer

def test_load_data():
    # サンプルデータを作成
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    file_path = "data.pkl"
    
    # データを一時ファイルに保存
    with open(file_path, 'wb') as f:
        pickle.dump((X, y), f)
    
    # Trainerのインスタンスを作成
    trainer = Trainer()
    
    # データを読み込む
    X_loaded, y_loaded = trainer.load_data(file_path)
    
    # テスト
    assert np.array_equal(X, X_loaded)
    assert np.array_equal(y, y_loaded)
    
    # テスト終了後のクリーンアップ
    os.remove(file_path)


def test_train_SVM():
    # サンプルデータを作成
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    hyperparameter = 1.0
    
    # Trainerのインスタンスを作成
    trainer = Trainer()
    
    # モデルを学習
    trainer.train_SVM(hyperparameter, X, y)
    
    # テスト
    assert isinstance(trainer.model, SVC)
    assert trainer.model.C == hyperparameter

def test_dump_model():
    # サンプルデータを作成
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    
    # Trainerのインスタンスを作成
    trainer = Trainer()
    
    # モデルを学習
    trainer.train_SVM(1.0, X, y)
    
    # モデルを一時ファイルに保存
    model_path = "model.pkl"
    trainer.dump_model(model_path)
    
    # モデルを読み込む
    with open(model_path, 'rb') as f:
        loaded_model = pickle.load(f)
    
    # テスト
    assert isinstance(loaded_model, SVC)
    assert loaded_model.C == 1.0
    
    # テスト終了後のクリーンアップ
    os.remove(model_path)
