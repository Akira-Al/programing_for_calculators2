from janome.tokenizer import Tokenizer
import dataclasses
from enum import Enum
import abc
import re
import jaconv
import my_library.load_dictionary as dictionary_loader

# カタカナの確認
KATAKANA_PAT = re.compile(r"[\u30A1-\u30FF]+")
# 辞書の読み込み
dict1 = dictionary_loader.load_dict1()
dict2 = dictionary_loader.load_dict2()


def count_and_vectorize(sent):
    """
    my_library/Data_preprocessor.pyから呼ばれる
    Args:
        sent (str): 文章(1文)
    Returns:
        list: [num_positive, num_negative, num_neutral, num_total]
    """

    tokenizer = Tokenizer()
    # 最終的に返す値たち
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    # 1文を形態素解析してwordsリストに格納
    # token.base_formの型らしい
    words = []
    # 2語以上で辞書の確認をしたいもの
    pending = []
    for token in tokenizer.tokenize(sent):
        words.append(token.base_form)
    # 各token(単語)に対応した極性を保存するpolarityリスト
    polarity = [0. for i in range(len(words))]
    for i in range(len(words)):
        # 否定の処理
        # あとで"助動詞"も条件に足す
        if words[i] in ["ない", "ぬ", "ん"] and i > 0:
            polarity[i-1] *= -1.
        # 接続詞の処理
        # あとで"接続詞"or"助詞"も条件に足す
        if words[i] in ["しかし", "けど", "ただ", "だが", "しかしながら", "けれど", "けれども", "だけど", "だけども", "そうではあるが", "それでも", "でも", "ではあるが", "にもかかわらず", "ところが", "ですが", "ものの", "しかるに", "とはいうものの", "のに", "なのに", "それなのに", "とはいえ", "そうはいうものの", "でも", "そのくせ"]:
            for j in range(i):
                polarity[j] *= -0.5
            continue

        # 否定系の処理にひっかからなかったら以降を実行
        # dictionary1.txt
        if words[i] in dict1:
            polarity[i] = dict1[words[i]][0]
        # dictionary2.txt
        elif words[i] in dict2:
            for record in dict2[words[i]]:
                partial = False
                if [words[i]] == record[0]:
                    # full
                    polarity[i] = record[1]
                # もし2語以上の辞書に一致するなら
                elif len([words[i]]) <= len(record[0]):
                    # partial
                    pending.append([words[i]])
                    break  # ひらがな確認が1語にしか対応してない
                else:
                    # none
                    # もしこの時点で一致するものがない場合、カタカナをひらがなに変換して確認
                    if polarity[i] == 0. and partial == False and KATAKANA_PAT.fullmatch(words[i]) is not None:
                        # hira_token = words[i]
                        hira_token = jaconv.kata2hira(words[i])
                        if hira_token in dict1:
                            polarity[i] = dict1[hira_token][0]
                        elif hira_token in dict2:
                            for record in dict2[hira_token]:
                                if [hira_token] == record[0]:
                                    polarity[i] = record[1]
        if len(pending) < i+1:
            pending.append([None])

        # 2語以上の辞書の確認
        drop_list = []
        for j, tokens in enumerate(pending):
            if j == i:
                # 今の単語に対しては確認済み
                break
            if tokens[0] is None:
                continue
            pending[j] = tokens + [words[i]]
            tokens = pending[j]
            if tokens[0] in dict2:
                # partial True: 一部一致 False: 完全一致or一致なし
                partial = False
                for record in dict2[tokens[0]]:
                    if tokens == record[0]:
                        # full 完全に一致するものがあった
                        polarity[j] = record[1]
                        break
                    elif partial == False and len(tokens) <= len(record[0]):
                        partial = True
                        for k in range(len(tokens)):
                            if tokens[k] != record[0][k]:
                                partial = False
                                break
                                # このbreakでfor文を抜ける
                    # ここでpartialが性格な値になってるはず
                if partial:
                    # partial
                    pass
                else:
                    # none
                    drop_list.append(j)
        for j in drop_list:
            pending = pending[:j]+[[None]]+pending[j+1:]


    # 極性の数をカウント
    for i in range(len(polarity)):
        if polarity[i] > 0:
            num_positive += polarity[i]
        elif polarity[i] < 0:
            num_negative += polarity[i] * -1
        else:
            num_neutral += 1
    num_total = len(polarity)

    print(" ".join(words), [num_positive,
          num_negative, num_neutral, num_total])
    return [num_positive, num_negative, num_neutral, num_total]
