#Written by Deryc T. Painter 11/20/2020#

'''This snippet of code is meant to take
Web of Science files downloaded as tab
seperated files with UTF-8 encoding. The
output file will be a .pkl (pickle) file
of a pandas dataframe.'''

import os
from pathlib import Path
import pandas as pd
import pickle


class combineWoS():

    def __init__(self):
        print('Starting program...')

    def user_input(self):
        input_folder = input('Enter complete folder path containing Web of Science files: ')
        self.inFolder = input_folder

    def create_filelist(self):
        print('Creating file list...')
        filelist = []
        for subdir, dirs, files in os.walk(self.inFolder):
            for file in files:
                if file.endswith('.txt'):
                    filename = os.path.join(subdir, file)
                    filelist.append(filename)
        self.filelist = filelist

    def create_dataframe(self):
        corruptionCounter = 0
        df_list = []
        for file in self.filelist:
            df = pd.read_csv(file, sep='\t',
                              encoding='utf-8',
                              low_memory=False,
                              error_bad_lines=False)
            df_list.append(df)
            if df.shape[1] < 500:
                corruptionCounter += 1
        print('There are {} corrupted records.'.format(corruptionCounter))
        dfx = pd.concat(df_list, ignore_index=True)
        print(dfx)
        self.df = dfx
        
    def save_pickle(self):
        pickle_file = input('Enter complete file path to save dataframe: ')
        print('Saving dataframe as pickle...')
        with open(pickle_file,'wb') as f:
            pickle.dump(self.df, f)
        print('Finished creating pickle of dataframe of combined Web of Science files.')
        
    def runScript(self):
        self.user_input()
        self.create_filelist()
        self.create_dataframe()
        self.save_pickle()


if __name__ == '__main__':
    app = combineWoS()
    app.runScript()

    
