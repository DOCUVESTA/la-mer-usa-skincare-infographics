import pandas as pd

import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px


class LaMerAgeDistributionGraph:
   
    def __init__(self, lamer_age_distribution):
        self.lamer_age_distribution = lamer_age_distribution
        
    
    def create_reviews_age_distribution_plot_bar(self):
        age_distribution = self.lamer_age_distribution['age_distribution_percentage']
        df_age_dist = pd.DataFrame(list(age_distribution.items()), columns=['age_group', 'percentage'])
        
        fig = px.bar(df_age_dist, 
             x='age_group', 
             y='percentage',
             color='age_group',
             text='percentage', 
             width=710, 
             height=480,
             color_discrete_map={'below 18': '#E1FF5C', 
                                 '18-25': '#A6B175',
                                 '26-35': '#6C8762',
                                 '36-45':'#A6B175' ,
                                 '46-55': '#224026',
                                 'above 56': '#D1D891',
                                 'no age': '#024F38'
                                }
            
            )

        fig.update_layout(showlegend=False,
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                xaxis_title=None,
                yaxis_title=None,
                font_family="Verdana"
)

        fig.update_traces(textposition='outside',textfont_size=14, texttemplate='<b>%{y} % </b>')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

        fig.write_image("lamer_age_plot_bar.png")
