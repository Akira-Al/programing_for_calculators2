import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)   

import pickle
import src.my_library.Validator as Validator

def find_best_model(models_path, data_path):
    validator = Validator.Validator()
    validator.load_data(data_path)

    best_accuracy = 0
    best_model_file_path = None

    for model_file in os.listdir(models_path):
        model_file_path = os.path.join(models_path, model_file)
        validator.load_model(model_file_path)
        accuracy, precision, recall = validator.evaluate_model()
        print(f"Evaluating {model_file}:")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model_file_path = model_file_path

    if best_model_file_path is not None:
        best_model_file_path_dest = os.path.join(models_path, 'best_model.pkl')
        validator.load_model(best_model_file_path)
        with open(best_model_file_path_dest, 'wb') as f:
            pickle.dump(validator.model, f)
        print(f"The best model is saved as 'best_model.pkl' with accuracy: {best_accuracy}")

models_path = os.path.join(project_root_path, "models") 
data_path = os.path.join(project_root_path, "data", "validation_preprocessed.pkl") 
#data_path = os.path.join(project_root_path, "data", "train_preprocessed.pkl") 

find_best_model(models_path, data_path)
