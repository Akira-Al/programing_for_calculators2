import os
import pickle
import my_library.load_input_data as input_loader

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(project_root_path, "models", "best_model.pkl")
preprocessed_data_path = os.path.join(project_root_path, "data", "data_preprocessed.pkl")
data_path = os.path.join(project_root_path, "data", "data.txt")
data_ans_path = os.path.join(project_root_path, "data", "data_ans.txt")

with open(model_path, "rb") as f:
    predictor = pickle.load(f)
with open(preprocessed_data_path, "rb") as f:
    preprocessed_data, _ = pickle.load(f)

print(preprocessed_data[1:10])
sentence_array = input_loader.load_raw_data(data_path)
sentence_ans_array = input_loader.load_raw_ans_data(data_ans_path)
predictions = predictor.predict(preprocessed_data)
# result = [不正解数, 正解数]
result = [0, 0]
for i in range(len(predictions)):
    is_correct = 1 if predictions[i] == sentence_ans_array[i] else 0
    result[is_correct] += 1
    if not is_correct:
        print(sentence_array[i])
        print("結果:", predictions[i], "解答:", sentence_ans_array[i])

print("正答率:", result[1] / (result[0] + result[1]))
