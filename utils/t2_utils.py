import pandas as pd
import numpy as np
import json, io
from ast import literal_eval
from utils import db_utils
from collections import OrderedDict
from IPython.display import HTML, display, update_display, clear_output
from datetime import date
import ipywidgets as widgets
import utils.movie_utils as movie_utils

def check_sites_csv(sites_csv):

    # Load the csv with sites information
    sites_df = pd.read_csv(sites_csv)
    
    # Select relevant fields
    sites_df = sites_df[
        ["site_id", "siteName", "decimalLatitude", "decimalLongitude", "geodeticDatum", "countryCode"]
    ]
    
    # Roadblock to prevent empty lat/long/datum/countrycode
    db_utils.test_table(
        sites_df, "sites", sites_df.columns
    )
    
    print("The sites.csv file doesn't have any empty fields")
    
    return sites_df

    
def check_movies_csv(movies_csv, sites_df, project_name):

    # Load the csv with movies information
    movies_df = pd.read_csv(movies_csv)
    
    # Check for missing fps and duration info
    movies_df = movie_utils.check_fps_duration(movies_df, movies_csv, project_name)
    
    # Check for survey_start and survey_end info
    movies_df = movie_utils.check_survey_start_end(movies_df, movies_csv)
    
    # Ensure date is ISO 8601:2004(E) and compatible with Darwin Data standards
    date_time_check = pd.to_datetime(movies_df.created_on, infer_datetime_format=True)
    print("The last dates from the created_on column are:")
    print(date_time_check.tail())

    # Check the sites information of the movies
    sites_df = sites_df.rename(columns={"id": "site_id"})

    # Merge movies and sites dfs
    movies_df = pd.merge(
        movies_df, 
        sites_df[["siteName","site_id"]], 
        how="left", 
        on="siteName"
    )
    
    # Select only those fields of interest
    movies_db = movies_df[
        ["movie_id", "filename", "created_on", "fps", "duration", "survey_start", "survey_end", "Author", "site_id"]
    ]

    # Roadblock to prevent empty information
    db_utils.test_table(
        movies_db, "movies", movies_db.columns
    )
    
    print("The movies.csv file doesn't have any empty fields")    
    
    return movies_df
    
    
    
def upload_movies():
    
    # Define widget to upload the files
    mov_to_upload = widgets.FileUpload(
        accept='.mpg',  # Accepted file extension e.g. '.txt', '.pdf', 'image/*', 'image/*,.pdf'
        multiple=True  # True to accept multiple files upload else False
    )
    
    # Display the widget?
    display(mov_to_upload)
    
    main_out = widgets.Output()
    display(main_out)
    
    # TODO Copy the movie files to the movies folder
    
    # Provide the site, location, date info of the movies
    upload_info_movies()
    print("uploaded")
    
# Check that videos can be mapped
    movies_df['exists'] = movies_df['Fpath'].map(os.path.isfile)    
    
def upload_info_movies():

    # Select the way to upload the info about the movies
    widgets.ToggleButton(
    value=False,
    description=['I have a csv file with information about the movies',
                 'I am happy to write here all the information about the movies'],
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='check'
)
    
    # Upload the information using a csv file
    widgets.FileUpload(
    accept='',  # Accepted file extension e.g. '.txt', '.pdf', 'image/*', 'image/*,.pdf'
    multiple=False  # True to accept multiple files upload else False
)
    # Upload the information 
    
    # the folder where the movies are
    
    # Try to extract location and date from the movies 
    widgets.DatePicker(
    description='Pick a Date',
    disabled=False
)
    
    # Run an interactive way to write metadata info about the movies
    
    print("Thanks for providing all the required information about the movies")
    
    