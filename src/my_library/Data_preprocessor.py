import os
import sys
import pickle
import numpy as np
import my_library.count_statistics as counter 

class DataPreprocessor:
    def __init__(self, sentence_arrays):
        """
        DataPreprocessorクラスのコンストラクタ
        Args:
            sentence_arrays (list of lists): 処理する文章の配列
        """
        self.sentence_arrays = sentence_arrays
        self.X = None
        self.y = None

    def preprocess_data(self, verbose=False):
        """
        data.txtのデータ形式を前提に前処理を行う
        """
        X_list = []
        for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i]     # 配列の要素が文章であると想定
            count_vector = counter.count_and_vectorize( sentence)
            if verbose:
                print(sentence, count_vector)
            X_list.append(count_vector)
        self.X = np.array(X_list)                  # リストをnumpyの多次元配列に変換

    def preprocess_data_and_label(self):
        """
        train.txtのデータ形式を前提に前処理を行う
        """
        X_list, y_list = [], []
        for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i][0]  # Sentenceの列を取得
            print(sentence)
            count_vector = counter.count_and_vectorize(sentence)
            X_list.append(count_vector)
            if self.sentence_arrays[i][48] == "-2":  # Avg. Readers_Sentimentの列"-2" 
                y_list.append(-2)
            elif self.sentence_arrays[i][48] == "-1":                             
                y_list.append(-1)
            elif self.sentence_arrays[i][48] == "1":
                y_list.append(1)  
            elif self.sentence_arrays[i][48] == "2":  
                y_list.append(2)
            else:
                y_list.append(0)
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
