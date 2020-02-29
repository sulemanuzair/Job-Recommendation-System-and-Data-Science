from constants import *
import pandas as pd

file_name = dataset_path + '/users/users.tsv'
file_name_to_save = dataset_path + '/users/users_preprocessed.tsv'
users = pd.read_csv(file_name, sep='\t')

BOOLEAN_COLUMNS = ['CurrentlyEmployed', 'ManagedOthers']

for column in BOOLEAN_COLUMNS:
    users[column] = users[column].map({'Yes': 1, 'No': 0})
users.to_csv(file_name_to_save, sep='\t', index=False)
