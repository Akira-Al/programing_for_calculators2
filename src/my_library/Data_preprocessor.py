import os
import sys
import pickle
import numpy as np
import count_statistics as counter 

class DataPreprocessor:
    def __init__(self, sentence_arrays, dictionary):
        """
        DataPreprocessorクラスのコンストラクタ
        Args:
            sentence_arrays (list of lists): 処理する文章の配列
            dictionary (dict): 極性辞書         
        """
        self.sentence_arrays = sentence_arrays
        self.dictionary = dictionary
        self.X = None
        self.y = None

    def preprocess_data(self):
        """
        data.txtのデータ形式を前提に前処理を行う
        """
        X_list = []
        for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i]     # 配列の要素が文章であると想定
            count_vector = counter.count_and_vectorize(self.dictionary, sentence)
            X_list.append(count_vector)
        self.X = np.array(X_list)                  # リストをnumpyの多次元配列に変換

    def preprocess_data_and_label(self):
        """
        train.txtのデータ形式を前提に前処理を行う
        """
        X_list, y_list = [], []
        for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i][0]  # Sentenceの列を取得
            count_vector = counter.count_and_vectorize(self.dictionary, sentence)
            X_list.append(count_vector)
            if self.sentence_arrays[i][4] == "0":  # Writer_Joyの列が"0"なら負例とする 
                y_list.append(-1)
            else:                                  # Writer_Joyの列が"0"でないなら正例とする 
                y_list.append(1)
            if len(X_list) < 4:
                print(X_list[-1], y_list[-1])
        self.X, self.y = np.array(X_list), np.array(y_list)  # リストをnumpyの多次元配列に変換


    def dump(self, file_path):
        """
        前処理されたデータとラベルをファイルに保存する
        Args:
            file_path (str): 前処理データを保存するファイルのパス
        """
        with open(file_path, "wb") as f:
            pickle.dump((self.X, self.y), f)