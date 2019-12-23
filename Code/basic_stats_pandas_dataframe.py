import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_backend()
matplotlib.use('TkAgg')
import dateutil.parser as parser

file_path = 'G:/Semester 8/FYP2/dataset/users/users_part.tsv'
users = pd.read_csv(file_path, sep='\t')

# display more width and columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

#include all to include all columns in describe instead of just numeric columns
print('Rows: ', users.shape[0], ', Columns: ', users.shape[1])
print(users.describe(include='all'))