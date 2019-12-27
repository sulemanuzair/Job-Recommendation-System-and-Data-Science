from constants import *
import pandas as pd

file_name = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')

title_word_info = jobs.Description.str.split(expand=True).stack().value_counts()
title_word_info.to_csv(reports_path + '/Jobs_Title_Tokens_Info_25percent.csv')
