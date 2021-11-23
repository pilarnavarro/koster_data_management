import os
from ipyfilechooser import FileChooser
from ipywidgets import interactive, Layout
from ipywidgets import interactive

import utils.movie_utils as movie_utils
import utils.server_utils as server_utils
import pandas as pd
import ipywidgets as widgets
import numpy as np
import subprocess
import datetime

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
def select_site(db_initial_info):
    
    # Read csv as pd
    sitesdf = pd.read_csv(db_initial_info["sites_csv"])

    # Existing sites
    exisiting_sites = sitesdf.siteName.unique()

    def f(Existing_or_new):
        if Existing_or_new == 'Existing':
            site_widget = widgets.Dropdown(
                options = exisiting_sites,
                description = 'Site:',
                disabled = False,
                layout=Layout(width='50%'),
                style = {'description_width': 'initial'}
            )
            
        if Existing_or_new == 'New site':   
            site_widget = widgets.Text(
                placeholder='Type sitename',
                description='Sitename:',
                disabled=False,
                layout=Layout(width='50%'),
                style = {'description_width': 'initial'}
            )

        display(site_widget)

        return site_widget

    w = interactive(f, 
                    Existing_or_new = widgets.Dropdown(
                        options = ['Existing','New site'],
                        description = 'Existing or new:',
                        disabled = False,
                        layout=Layout(width='50%'),
                        style = {'description_width': 'initial'}
                    )
                   )

    display(w)
    
    return w

def select_date():
    
    # Select the date 
    date_widget = widgets.DatePicker(
        description='Start Date',
        disabled=False,
        layout=Layout(width='50%'),
        style = {'description_width': 'initial'}
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
    
    video_info_dict = {
        "fps": fps, 
        "length": length, 
        "concat_video": concat_video, 
        "filename_i": filename_i, 
        "siteName_i": siteName_i, 
        "created_on_i": created_on_i, 
        "go_pro_list": go_pro_list, 
        "unique_survey_name": unique_survey_name
    }
    
    return video_info_dict


# Select author of the video
def select_author(db_initial_info):
    
    # Read csv as pd
    movies_df = pd.read_csv(db_initial_info["movies_csv"])
    
    # Existing authors
    exisiting_authors = movies_df.Author.unique()

    def f(Existing_or_new):
        if Existing_or_new == 'Existing':
            author_widget = widgets.Dropdown(
                options = exisiting_authors,
                description = 'Author:',
                disabled = False,
                layout=Layout(width='50%'),
                style = {'description_width': 'initial'}
            )

        if Existing_or_new == 'New author':   
            author_widget = widgets.Text(
                placeholder='Type Author',
                description='Author:',
                disabled=False,
                layout=Layout(width='50%'),
                style = {'description_width': 'initial'}
            )

        display(author_widget)

        return(author_widget)

    w = interactive(f,
                    Existing_or_new = widgets.Dropdown(
                        options = ['Existing','New author'],
                        description = 'Existing or new:',
                        disabled = False,
                        layout=Layout(width='50%'),
                        style = {'description_width': 'initial'}
                    )
                   )

    display(w)

    return w
    
def select_bad_deployment():
    
    def deployment_to_true_false(deploy_value):
        if deploy_value == 'No, it is a great video':
            return False
        else:
            return True

    w = interactive(deployment_to_true_false, deploy_value = widgets.Dropdown(
        options=['Yes, unfortunately it is marine crap', 'No, it is a great video'],
            value='No, it is a great video',
            description='Is it a bad deployment?',
            disabled=False,
            layout=Layout(width='50%'),
            style = {'description_width': 'initial'}
        ))

    display(w)

    return w
    
    
    
# Display in hours, minutes and seconds
def to_hhmmss(seconds):
    print("Time selected:", datetime.timedelta(seconds=seconds))
    
    return seconds

def select_start_survey(duration_i):

    # Select the start of the survey 
    surv_start = interactive(to_hhmmss, seconds=widgets.IntSlider(
        value=0,
        min=0,
        max=duration_i,
        step=1,
        description='Survey starts (seconds):',
        layout=Layout(width='50%'),
        style = {'description_width': 'initial'}))

    display(surv_start)    
    
    return surv_start
 
    
def select_end_survey(duration_i, surv_start_i):
    
    # Set default to 30 mins or max duration
    start_plus_30 = surv_start_i+(30*60)
    
    if start_plus_30>duration_i:
        default_end = duration_i
    else:
        default_end = start_plus_30
    
    
    # Select the end of the survey 
    surv_end = interactive(to_hhmmss, seconds=widgets.IntSlider(
        value=default_end,
        min=0,
        max=duration_i,
        step=1,
        description='Survey ends (seconds):',
        layout=Layout(width='50%'),
        style = {'description_width': 'initial'}))

    display(surv_end)  
    
    return surv_end
    
# Select s3 folder to upload the video
def select_s3_folder(db_initial_info):

    # Specify the bucket
    bucket_i = 'marine-buv'
    
    # Retrieve info from the bucket
    contents_s3_pd = server_utils.get_matching_s3_keys(db_initial_info["client"], bucket_i, "")

    # Extract the prefix (directory) of the objects        
    s3_folders_available = contents_s3_pd[0].str.rsplit('/',0).str[0]

    # Conver folders available df to tuple
    s3_folders_available_tuple = tuple(s3_folders_available.unique())

    # Select the s3 folder
    s3_folder_widget = widgets.Combobox(
                    options=s3_folders_available,
                    description="S3 folder:",
                    ensure_option=True,
                    disabled=False,
                )
    
    
    display(s3_folder_widget)
    return s3_folder_widget

# Write a comment about the video
def write_comment():

    # Create the comment widget
    comment_widget = widgets.Text(
            placeholder='Type comment',
            description='Comment:',
            disabled=False,
            layout=Layout(width='50%'),
            style = {'description_width': 'initial'}
        )

    
    display(comment_widget)
    return comment_widget


def review_movie_details(video_info_dict_i,
                         IsBadDeployment_i,
                         survey_start_i,
                         survey_end_i,
                         author_i,
                         bucket_i,
                         comment_i,
                         s3_prefix_i,
                        ):
    
    # Get the location of the csv files with initial info to populate the db
    sites_csv, movies_csv, species_csv = server_utils.get_sites_movies_species()

    # Add movie id
    movies_df = pd.read_csv(movies_csv)
    movie_id_i = 1 + movies_df.movie_id.iloc[-1]
    
    # Save the prefix (s3 path) to upload the video
    prefix_i = s3_prefix + "/" + video_info_dict["unique_survey_name"]

    row_i = [[movie_id_i, 
              video_info_dict_i["filename_i"], 
              video_info_dict_i["siteName_i"],
              video_info_dict_i["created_on_i"],
              author_i,
              video_info_dict_i["fps_i"],
              video_info_dict_i["duration_i"],
              survey_start_i, 
              survey_end_i,
              go_pro_list_i, 
              bucket_i,
              prefix_i, 
              IsBadDeployment_i, 
              comment_i]]
    
    new_row = pd.DataFrame(row_i, columns = movies_df.columns)
    
    return new_row

