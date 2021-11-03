import os, cv2, sys, io
import operator
import pandas as pd
from tqdm import tqdm
import utils.server_utils as server_utils
import utils.spyfish_utils as spyfish_utils


# Calculate length and fps of a movie
def get_length(video_file):
    
    #final_fn = video_file if os.path.isfile(video_file) else koster_utils.unswedify(video_file)
    
    if os.path.isfile(video_file):
        cap = cv2.VideoCapture(video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)     
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        length = frame_count/fps
    else:
        print("Length and fps for", video_file, "were not calculated")
        length, fps = None, None
        
    return fps, length


def get_movie_parameters(df, movies_csv, project_name):
    
    # Specify the parameters of the movies
    parameters = ["fps", "duration", "survey_start", "survey_end"]
    
    for parameter in parameters:
    
        # Check if the parameter is missing from any movie
        if df[parameter].isna().any():
            
            # Select only those movies with the missing parameter
            miss_par_df = df[df[parameter].isna()]
            
            if parameter in ["fps","duration"]:
                
                # Add info about accessing the Spyfish movies from AWS
                if project_name == "Spyfish_Aotearoa":
                    # Start AWS session
                    aws_access_key_id, aws_secret_access_key = server_utils.aws_credentials()
                    client = server_utils.connect_s3(aws_access_key_id, aws_secret_access_key)

                    # Check the movies are accessible
                    miss_par_df = spyfish_utils.check_spyfish_movies(miss_par_df, client)
                        
                # Prevent missing parameters from movies that don't exists
                if len(miss_par_df[~miss_par_df.exists]) > 0:
                    print(
                        f"There are {len(miss_par_df) - miss_par_df.exists.sum()} out of {len(miss_par_df)} movies missing from the server without {parameter} information. The movies are {miss_par_df[~miss_par_df.exists].filename.tolist()}"
                    )

                    return
                
                else:
                    # Check if the project is the Spyfish Aotearoa
                    if project_name == "Spyfish_Aotearoa":
                        # Download from s3, calculate and add fps/length info
                        df = spyfish_utils.add_fps_length_spyfish(df, miss_par_df, client)
                        
                    else:    
                        # Set the fps and duration of each movie
                        df.loc[df["fps"].isna()|df["duration"].isna(), "fps": "duration"] = pd.DataFrame(df["Fpath"].apply(get_length, 1).tolist(), columns=["fps", "duration"])
            
            if parameter == "survey_start":
                # Set the start of each movie to 0 if empty
                df.loc[df["survey_start"].isna(),"survey_start"] = 0

            if parameter == "survey_end":
                # Set the end of each movie to the duration of the movie if empty
                df.loc[df["survey_end"].isna(),"survey_end"] = df["duration"]

            # Update the local movies.csv file with the new fps/duration and survey start/end info
            df.drop(["Fpath","exists"], axis=1).to_csv(movies_csv,index=False)

            print(
                f" The {parameter} information of {len(miss_par_df)} movies have been succesfully added to the local csv file"
            )

        # Prevent ending survey times longer than actual movies
        if parameter is ["survey_end"] and (df["survey_end"] > df["duration"]).any():
            print(
                f"The survey_end times of {df[~df.exists].filename.tolist()} are longer than the actual movies"
            )

            return

    return df