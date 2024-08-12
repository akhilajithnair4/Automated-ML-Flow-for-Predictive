from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from exception import CustomException
from logger import logging
from data_transformation import DataTransformationConfig,DataTransformation
from data_ingestion import DataIngestionConfig,DataIngestion

from utils import save_object,evaluate_model
from dataclasses  import dataclass
import os 
import sys



class ModelTrainingConfig:
    model_training_config=os.path.join("artifact","model.pkl")
    
class ModelTrainer:
    def __init__(self):
       self.model_trainer=ModelTrainingConfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            
            X_train,y_train,X_test,y_test=train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]
            
 
            
            model_dict={
                "AdaBoostRegressor":AdaBoostRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "LinearRegression":LinearRegression(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "DecisionTreeRegressor":DecisionTreeRegressor()
            }           

            params={
                "DecisionTreeRegressor": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'splitter':['best','random'],
                    'max_features':['sqrt','log2'],
                },
                "RandomForestRegressor":{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "GradientBoostingRegressor":{
                    'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'criterion':['squared_error', 'friedman_mse'],
                    'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "LinearRegression":{},
                 
                 "KNeighborsRegressor":{},
             
                "AdaBoostRegressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            logging.info("Model Evaluation Started")


            
            model_report=model_evaluate(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,model_dict=model_dictionary)
            
            print(model_report)
            
            

        except Exception as e:
            
            print(e)
            



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.inititate_data_ingestion()
    
    obj1=DataTransformation()
    train_arr,test_arr=obj1.initiate_data_transformation(train_data,test_data)
    
    obj2=ModelTrainer()
    
    obj2.initiate_model_training(train_arr,test_arr)
    
