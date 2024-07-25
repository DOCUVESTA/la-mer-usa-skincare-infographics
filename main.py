from scripts import load_clean_dataframe, prepare_infographics_data, create_graph, generate_pdf

def main():
    
    # load data into a dataframe
    file1 = 'data/raw data/lamer_usa_30052024.csv'
    file2 = 'data/raw data/lamer_usa_age_distribution_30052024.csv'

    lamer_data = load_clean_dataframe.LaMerDataLoader(file1, file2)
    lamer_data.create_dataframes()
    lamer_data.merge_dataframes()
    lamer_data.calculate_reviews_with_no_age()
    
    df_all_lamer_data = lamer_data.df_all_lamer_data

    # prepare infographics data
    lamer_infographics = prepare_infographics_data.LaMerDataInfographicsItems(df_all_lamer_data)
    
    lamer_infographics.generate_values_for_information_bar()
    lamer_infographics.categorize_highlighted_products()
    lamer_infographics.calculate_reviews_age_distribution()
    
    lamer_info_bar = lamer_infographics.lamer_info_bar
    lamer_highlighted_products = lamer_infographics.lamer_highlighted_products
    lamer_age_distribution = lamer_infographics.lamer_age_distribution
    
    
    # create reviews age distribution graph
    lamer_graph = create_graph.LaMerAgeDistributionGraph(lamer_age_distribution)
    
    lamer_graph.create_reviews_age_distribution_plot_bar()
    
    
    # generate infographics in pdf format
    lamer_pdf = generate_pdf.CustomPDF(lamer_info_bar, lamer_highlighted_products)
    
    lamer_pdf.initiate_pdf()
    lamer_pdf.use_custom_background()
    lamer_pdf.add_website_country_information()
    lamer_pdf.add_number_of_bestsellers_information()
    lamer_pdf.add_highlighted_product_names()
    lamer_pdf.add_highlighted_product_ratings()
    lamer_pdf.add_highlighted_product_reviews()
    lamer_pdf.add_highlighted_product_images()
    lamer_pdf.add_age_distribution_bar_plot ()
    lamer_pdf.save_pdf()
    

if __name__ == '__main__':
    main()