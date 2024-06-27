import os
import pickle
import my_library.load_input_data as input_loader

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(project_root_path, "models", "best_model.pkl")
preprocessed_data_path = os.path.join(project_root_path, "data", "data_preprocessed.pkl")
data_path = os.path.join(project_root_path, "data", "data.txt")

with open(model_path, "rb") as f:
    predictor = pickle.load(f)
with open(preprocessed_data_path, "rb") as f:
    preprocessed_data, _ = pickle.load(f)

print(preprocessed_data[1:10])
sentence_array = input_loader.load_raw_data(data_path)
predictions = predictor.predict(preprocessed_data)
for i in range(len(predictions)):
    print(sentence_array[i], predictions[i])
