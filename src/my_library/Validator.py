import sklearn.metrics as metrics
import pickle

class Validator:
    def __init__(self):
        """
        Validatorクラスのコンストラクタ。
        """
        self.model = None  # モデルを格納するインスタンス変数を初期化
        self.X = None  # 前処理済みの検証データを格納するインスタンス変数を初期化
        self.y = None  # 検証データのラベルを格納するインスタンス変数を初期化
    def load_data(self, file_path):
        """
        データセットのファイルパスからデータを読み込み、特徴量とラベルを分けて返す。
        Args:
            file_path (str): データセットのファイルパス
        Returns:
            None
        """        
        with open(file_path, 'rb') as f:
            self.X, self.y = pickle.load(f)        
        return self.X, self.y

    def load_model(self, file_path):
        """
        モデルのファイルパスからモデルを読み込みインスタンス変数に格納する。
        Args:
            file_path (str): モデルのファイルパス
        Returns:
            None
        """        
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)
    def evaluate_model(self):
        """
        検証データを用いてモデルの評価を行い、精度、適合率、再現率を返す
        Returns:
            accuracy(float): 分類精度
            precision(float): 適合率
            recall(float): 再現率
        """        
        y_pred = self.model.predict(self.X)
        accuracy = metrics.accuracy_score(self.y, y_pred)
        precision = metrics.precision_score(self.y, y_pred)
        recall = metrics.recall_score(self.y, y_pred)
        return accuracy, precision, recall