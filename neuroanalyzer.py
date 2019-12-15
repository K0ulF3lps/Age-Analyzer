import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statistics as st
import datetime
import pickle
import numpy as np

def find_average_mode(arr):
    list_table = st._counts(arr)
    len_table = len(list_table)
    new_list = []
    for i in range(len_table):
        new_list.append(list_table[i][0])
    return int(st.mean(new_list))


class neuralNetwork:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        self.log("INIT", f"Model inited.", "log/neuroanalyzer.log")
        pass
    def prepare_data_from_df(self, df):
        mean_arr_train = []
        hmean_arr_train = []
        mode_arr_train = []
        median_arr_train = []
        std_arr_train = []
        real_age_arr_train = []
        for i in range(len(df)):
            if df["Mean"][i] != "PROFILE CLOSED":
                mean_arr_train.append(df["Mean"][i]);
                hmean_arr_train.append(df["Harmonic Mean"][i]);
                mode_arr_train.append(df["Mode"][i]);
                median_arr_train.append(df["Median"][i]);
                std_arr_train.append(df["std"][i]);
                real_age_arr_train.append(df["Real Age"][i])
        self.x_train_dict = {
            "Mean": mean_arr_train,
            "Mode": mode_arr_train,
            "HMean": hmean_arr_train,
            "Median": median_arr_train,
            "std": std_arr_train
        }
        self.y_train_dict = {
            "Real Age": real_age_arr_train
        }
        self.log("DATA PREPARED", f"Data prepared sucessfully. Data length: {len(self.x_train_df)}", "log/neuroanalyzer.log")


    def train(self, df):
        self.prepare_data_from_df(df)
        self.x_train_df = pd.DataFrame(self.x_train_dict)
        self.y_train_df = pd.DataFrame(self.y_train_dict)
        self.reg.fit(self.x_train_df, self.y_train_df)
        self.log("MODEL TRAINED", f"Model trained successfully. Data length: {len(self.x_train_df)}", "log/neuroanalyzer.log")


    def save_model(self, filename):
        pickle.dump(self.reg, open(filename, 'wb'))
        self.log("MODEL SAVED", "Model saved successfully", "log/neuroanalyzer.log")


    def open_model(self, filename):
        self.reg = pickle.load(open(filename, 'rb'))
        self.log("MODEL LOADED", "Model loaded successfully", "log/neuroanalyzer.log")


    def query(self, ages):
        mean = st.mean(ages)
        median = st.median(ages)
        hmean = st.harmonic_mean(ages)
        mode = find_average_mode(ages)
        std = np.array(ages).std()
        predicted = self.reg.predict([[mean, hmean, mode, median, std]])
        predicted = float(predicted, 2)
        self.log("QUERY", f"Predicted successfully. Result: {predicted}.", "log/neuroanalyzer.log")


    def log(self, event, text, file):
        read = open(file, 'r')
        input = read.read()
        read.close()
        now = datetime.datetime.now()
        log_text = f"{now}::{event}::{text}"
        f = open(file, 'w')
        f.write(input + log_text + '\n')


