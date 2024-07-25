import pandas as pd

class LaMerDataLoader:
    
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.df_lamer_usa = None
        self.df_lamer_age_distribution = None
        self.df_lamer_merged = None
        self.df_all_lamer_data = None
    
    
    def create_dataframes(self):
        self.df_lamer_usa = pd.read_csv(self.file1)
        self.df_lamer_age_distribution = pd.read_csv(self.file2)
    
    def merge_dataframes(self):
        self.df_lamer_merged = pd.merge(self.df_lamer_usa, self.df_lamer_age_distribution, on='product_name')
    
    def calculate_reviews_with_no_age(self):
        df_lamer_merged = self.df_lamer_merged
        new_col = ['no_age']
        df_lamer_combined = pd.concat([df_lamer_merged, pd.DataFrame(columns = new_col)])
        df_lamer_combined['no_age'] = df_lamer_combined['number_of_reviews'] - df_lamer_combined.iloc[:, 8:15].sum(axis=1)
        df_lamer_combined = df_lamer_combined.astype({  "number_of_reviews": 'int', 
                                                    "below_18": 'int',
                                                    "18_to_25": 'int',
                                                    "26_to_35": 'int',
                                                    "36_to_45": 'int',
                                                    "46_to_55": 'int',
                                                    "above_56": 'int',
                                                    "no_age": 'int',
                                                })
        self.df_all_lamer_data = df_lamer_combined