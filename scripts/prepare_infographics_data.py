class LaMerDataInfographicsItems:
    
    def __init__(self, df_all_lamer_data):
        self.df_all_lamer_data = df_all_lamer_data
        self.lamer_info_bar = {}
        self.lamer_highlighted_products = {}
        self.lamer_age_distribution = {}
    
    def generate_values_for_information_bar(self):
        df_all_lamer_data = self.df_all_lamer_data
        info_usa = df_all_lamer_data['country_website'][0]
        num_of_best_sellers = df_all_lamer_data['product_name'].nunique()
        self.lamer_info_bar['info_bar'] = {'info_usa':info_usa, 'num_of_best_sellers': num_of_best_sellers}
        

    def categorize_highlighted_products(self):
        df_all_lamer_data = self.df_all_lamer_data
        df_all_lamer_data['product_name'] = df_all_lamer_data['product_name'].str.title()
        
        highest_rated = df_all_lamer_data['rating'].max()
        highest_rated_product_info = df_all_lamer_data[df_all_lamer_data['rating'] == highest_rated][['product_name', 'rating', 'number_of_reviews', 'image']]
        
        most_rated = df_all_lamer_data['number_of_reviews'].max()
        most_rated_product_info = df_all_lamer_data[df_all_lamer_data['number_of_reviews'] == most_rated][['product_name', 'rating', 'number_of_reviews', 'image']]
        
        lowest_rated = df_all_lamer_data['rating'].min()
        lowest_rated_product_info = df_all_lamer_data[df_all_lamer_data['rating'] == lowest_rated][['product_name', 'rating', 'number_of_reviews', 'image']]
        
        least_rated = df_all_lamer_data['number_of_reviews'].min()
        least_rated_product_info = df_all_lamer_data[df_all_lamer_data['number_of_reviews'] == least_rated][['product_name', 'rating', 'number_of_reviews', 'image']]

        highlighted_dict = {
            'highest_rated_product_info': highest_rated_product_info.to_dict('records'),
            'most_rated_product_info': most_rated_product_info.to_dict('records'),
            'lowest_rated_product_info': lowest_rated_product_info.to_dict('records'),
            'least_rated_product_info': least_rated_product_info.to_dict('records')
        }
    
        self.lamer_highlighted_products['highlighted_products'] = highlighted_dict
    
    
    def calculate_reviews_age_distribution(self):
        df_all_lamer_data = self.df_all_lamer_data
        total_reviews = df_all_lamer_data['number_of_reviews'].sum()
        
        below_18 = ((df_all_lamer_data['below_18'].sum()/total_reviews) * 100).round(2)
        between_18_to_25 = ((df_all_lamer_data['18_to_25'].sum()/total_reviews) * 100).round(2)
        between_26_to_35 = ((df_all_lamer_data['26_to_35'].sum()/total_reviews) * 100).round(1)
        between_36_to_45 = ((df_all_lamer_data['36_to_45'].sum()/total_reviews) * 100).round(1)
        between_46_to_55 = ((df_all_lamer_data['46_to_55'].sum()/total_reviews) * 100).round(1)
        above_56 = ((df_all_lamer_data['above_56'].sum()/total_reviews) * 100).round(1)
        no_age = ((df_all_lamer_data['no_age'].sum()/total_reviews) * 100).round(1)

        self.lamer_age_distribution['age_distribution_percentage'] = {  "below 18": float(below_18), 
                                                                        "18-25": float(between_18_to_25),
                                                                        "26-35": float(between_26_to_35),
                                                                        "36-45": float(between_36_to_45),
                                                                        "46-55": float(between_46_to_55),
                                                                        "above 56": float(above_56),
                                                                        "no age": float(no_age)
                                                                        }


