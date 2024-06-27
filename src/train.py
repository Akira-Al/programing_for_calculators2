import os
import sys
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)
import my_library.Trainer as Trainer

preprocessed_train_data_path = input("Enter the path for the preprocessed data:")
model_dump_path_base = input("Enter the path for the directory to save the models:")

trainer = Trainer.Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

hyperparameters = [0.1,1,10,100,1000]
for h in hyperparameters:
    model_dump_path = os.path.join(model_dump_path_base , "SVM_"+str(h)+".pkl")
    trainer.train_SVM(h, X, y)
    trainer.dump_model(model_dump_path)