from fpdf import FPDF

class CustomPDF(FPDF):
    
    def __init__(self, lamer_info_bar, lamer_highlighted_products):
        super().__init__()
        self.lamer_info_bar = lamer_info_bar
        self.lamer_highlighted_products = lamer_highlighted_products
        
    def initiate_pdf(self):
        width = 960
        height = 540
        self.add_font('League_bold', '', '/Users/micheleescano/Desktop/Python/Projects/Font/Font/League_bold.ttf', uni=True)
        self.set_auto_page_break(auto=False, margin=0.0)
        self.add_page(orientation='P', format=(width, height))
        
    def use_custom_background(self):
        self.image('/Users/micheleescano/Desktop/Python/Dev/VENV/Age distribution/images/lamer_background.png', w=960-10, h=540-10)
        
    def add_website_country_information(self):
        website_country = self.lamer_info_bar['info_bar']['info_usa']
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=100)
        self.set_text_color(58, 87, 63)
        self.text(176, 219, website_country)
        
    def add_number_of_bestsellers_information(self):
        number_of_bestsellers = self.lamer_info_bar['info_bar']['num_of_best_sellers']
        number_of_bestsellers = str(number_of_bestsellers)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=100)
        self.set_text_color(58, 87, 63)
        self.text(315, 200, number_of_bestsellers )

        
    def add_highlighted_product_names(self):
        # highest
        highest_rated_name = self.lamer_highlighted_products['highlighted_products']['highest_rated_product_info'][0]['product_name']
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=45)
        self.set_text_color(58, 87, 63)
        self.text(438, 136, highest_rated_name)
    
        # most
        most_rated_name = self.lamer_highlighted_products['highlighted_products']['most_rated_product_info'][0]['product_name']
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=45)
        self.set_text_color(58, 87, 63)
        self.text(438, 252, most_rated_name)
        
        
        # lowest
        lowest_rated_name = self.lamer_highlighted_products['highlighted_products']['lowest_rated_product_info'][0]['product_name']
        self.set_xy(438, 350)
        self.set_font("League_bold" ,size=45)
        self.set_text_color(58, 87, 63)
        self.multi_cell(151, 20, lowest_rated_name)
        
        
        # least
        least_rated_name = self.lamer_highlighted_products['highlighted_products']['least_rated_product_info'][0]['product_name']
        self.set_xy(438, 467)
        self.set_font("League_bold" ,size=45)
        self.set_text_color(58, 87, 63)
        self.multi_cell(115, 20, least_rated_name)
    
    def add_highlighted_product_ratings(self):
        # highest
        highest_rated_rating = self.lamer_highlighted_products['highlighted_products']['highest_rated_product_info'][0]['rating']
        highest_rated_rating = str(highest_rated_rating)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(623, 136, highest_rated_rating)
    
        # most
        most_rated_rating = self.lamer_highlighted_products['highlighted_products']['most_rated_product_info'][0]['rating']
        most_rated_rating = str(most_rated_rating)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(623, 252, most_rated_rating)
    
        # lowest
        lowest_rated_rating = self.lamer_highlighted_products['highlighted_products']['lowest_rated_product_info'][0]['rating']
        lowest_rated_rating = str(lowest_rated_rating)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(623, 368, lowest_rated_rating)
    
         # least
        least_rated_rating = self.lamer_highlighted_products['highlighted_products']['least_rated_product_info'][0]['rating']
        least_rated_rating = str(least_rated_rating)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(623, 485, least_rated_rating)
    
    
    def add_highlighted_product_reviews(self):
        # highest
        highest_rated_reviews = self.lamer_highlighted_products['highlighted_products']['highest_rated_product_info'][0]['number_of_reviews']
        highest_rated_reviews = str(highest_rated_reviews)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(725, 136, highest_rated_reviews)
    
        # most
        most_rated_reviews = self.lamer_highlighted_products['highlighted_products']['most_rated_product_info'][0]['number_of_reviews']
        most_rated_reviews = str(most_rated_reviews)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(716, 252, most_rated_reviews)
    
        # lowest
        lowest_rated_reviews = self.lamer_highlighted_products['highlighted_products']['lowest_rated_product_info'][0]['number_of_reviews']
        lowest_rated_reviews = str(lowest_rated_reviews)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(725, 368, lowest_rated_reviews)
    
         # least
        least_rated_reviews = self.lamer_highlighted_products['highlighted_products']['least_rated_product_info'][0]['number_of_reviews']
        least_rated_reviews = str(least_rated_reviews)
        self.set_xy(0,0)
        self.set_font("League_bold" ,size=50)
        self.set_text_color(58, 87, 63)
        self.text(730, 485, least_rated_reviews)
    
    
    def add_highlighted_product_images(self):
        # highest
        highest_rated_image = self.lamer_highlighted_products['highlighted_products']['highest_rated_product_info'][0]['image']
        self.set_xy(0,0)
        self.image(highest_rated_image, 828, 42, 100, 145)
    
        # most
        most_rated_image = self.lamer_highlighted_products['highlighted_products']['most_rated_product_info'][0]['image']
        self.set_xy(0,0)
        self.image(most_rated_image, 815, 152, 125, 145)
    
        # lowest
        lowest_rated_image = self.lamer_highlighted_products['highlighted_products']['lowest_rated_product_info'][0]['image']
        self.set_xy(0,0)
        self.image(lowest_rated_image, 831, 270, 100, 145)
    
         # least
        least_rated_image = self.lamer_highlighted_products['highlighted_products']['least_rated_product_info'][0]['image']
        self.set_xy(0,0)
        self.image(least_rated_image, 836, 403, 85, 125)
        
        
    def add_age_distribution_bar_plot(self):
        age_dist_graph = '/Users/micheleescano/Desktop/Python/Dev/VENV/Age distribution/images/lamer_age_dist_plot_bar.png'
        self.set_xy(0,0)
        self.image(age_dist_graph, -2, 260, 425, 280)
    
    def save_pdf(self):
        self.output('lamer_infographic.pdf')