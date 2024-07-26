<h1 align="center">
	Automated PDF Infographic for La Mer Skincare USA Best-Selling Products
</h1>

<h3 align="center">
	<img src="https://github.com/DOCUVESTA/la-mer-usa-skincare-infographics/blob/07cc64ce4f9ddfd3eff3ee7a499089b196a451e0/assets/header.png" width=850" height="300"/>
</h3>

## Overview
Who doesn't love neat, themed, and aesthetically pleasing infographics, especially when they're automatically generated. I know I do! This La Mer skincare-themed infographic PDF utilizes data from the brand's website to provide key details on their top-selling products in the USA. This includes a bar plot showing the age distribution of customers who left reviews on one or more of La Mer's 19 best-selling products, along with information on the highest rated, most rated, lowest rated, and least rated products as of Thursday, May 30, 2024.
<br>

## Flow of data
<div align="center"">
  <img src="https://github.com/DOCUVESTA/la-mer-usa-skincare-infographics/blob/d75ef212668ef2dbbd28252fbaf2bab02416bf8d/assets/flow_of_data.png" alt="flow" width="680" height="400" />
</div>



## Repository Contents
### File: lamer_infographic.pdf
#### La Mer Skincare Infographic
<details open>
<summary>Preview</summary>
<div align="center"">
  <img src="https://github.com/DOCUVESTA/la-mer-usa-skincare-infographics/blob/9bb4c7af98e3c3b66360a342f78d465d3bea4c53/assets/preview_infographic.png" alt="preview"/>
</div>
</details>

### Folder: data
#### Raw data
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>lamer_usa_30052024.csv</td>
        <td>information on La Mer's best-selling products (USA)</td>
    </tr>
    <tr>
        <td>lamer_usa_age_distribution_30052024.csv</td>
        <td>number of reviews left on each product by age range</td>
    </tr>
</table>

#### Prepared data
<table style="width:100%">
    <tr>
        <th>File Name</th>
        <th>Data Description</th>
    </tr>
    <tr>
        <td>info_bar_30052024.json</td>
        <td>data displayed on infographic's information bar</td>
    </tr>
    <tr>
        <td>highlighted_products_30052024.json</td>
        <td>information on highest, most, lowest, least rated products</td>
    </tr>
    <tr>
        <td>reviews_age_distribution.json</td>
        <td>data used to create bar plot showing reviews age distribution </td>
    </tr>
</table>
<br>

### Folder: utils
##### Python package that include all modules used to create infographic
```
utils/
        ├── __init__.py
        ├── load_clean_dataframe.py
        ├── prepare_infographics_data.py
        ├── create_graph.py
        └── generate_pdf.py

```


### Folder: assets
##### All assets used to complete project
- background
- pictures
- font


