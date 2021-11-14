import os
from ipyfilechooser import FileChooser
from IPython.display import display 
from ipywidgets import interactive

import utils.movie_utils as movie_utils
import utils.server_utils as server_utils
import pandas as pd
import ipywidgets as widgets
import numpy as np
import subprocess

def select_go_pro_folder():
    # Create and display a FileChooser widget
    fc = FileChooser('/')
    
    display(fc)
    
    return fc

def select_go_pro_movies(go_pro_folder):
    # Save the names of the go_pro files
    go_pro_files_i = [go_pro_folder + movie for movie in os.listdir(go_pro_folder)]
    
    # Specify the formats of the movies to select
    movie_formats = movie_utils.get_movie_extensions()
    
    # Select only movie files
    go_pro_movies_i = [s for s in go_pro_files_i if any(xs in s for xs in movie_formats)]

    return go_pro_movies_i
    

# Select site and date of the video
def select_site():
    
    # Get the location of the csv files with initial info to populate the db
    sites_csv, movies_csv, species_csv = server_utils.get_sites_movies_species()

    # Read csv as pd
    sitesdf = pd.read_csv(sites_csv)

    # Existing sites
    exisiting_sites = sitesdf.siteName.unique()

    def f(Existing_or_new):
        if Existing_or_new == 'Existing':
            site_widget = widgets.Dropdown(
                options = exisiting_sites,
                description = 'Site:',
                disabled = False
            )

        if Existing_or_new == 'New site':   
            site_widget = widgets.Text(
                placeholder='Type sitename',
                description='Sitename:',
                disabled=False
            )

        display(site_widget)

        return(site_widget)

    w = interactive(f, Existing_or_new=['Existing','New site'])

    display(w)
    
    return w
    
def select_date():
    
    # Select the date 
    date_widget = widgets.DatePicker(
        description='Start Date',
        disabled=False
    )
    
    
    display(date_widget)
    return date_widget  
    

# Function to download go pro videos, concatenate them and upload the concatenated videos to aws 
def concatenate_go_pro_videos(siteName_i, created_on_i, go_pro_folder, go_pro_list):

    # Specify the name of the survey
    unique_survey_name = siteName_i+"_"+created_on_i

    # Specify the filename and path for the concatenated movie
    filename_i = unique_survey_name+".MP4"
    concat_video = go_pro_folder+filename_i

    # Save list as text file
    textfile = open("a_file.txt", "w")
    for go_pro_file in go_pro_list:
        textfile.write("file '"+ go_pro_file + "'"+ "\n")
    textfile.close()

    
    if not os.path.exists(concat_video):
        print("Concatenating ", concat_video)
        
        # Concatenate the videos
        subprocess.call(["ffmpeg",
                         "-f", "concat", 
                         "-safe", "0",
                         "-i", "a_file.txt", 
                         "-c", "copy",
                         concat_video])
            
        print(concat_video, "concatenated successfully")
        
    # Delete the text file
    os.remove("a_file.txt")
        
    # Update the fps and length info
    fps, length = movie_utils.get_length(concat_video)

    print("Temporary files removed")
    
    return fps, length
           
    
    
    