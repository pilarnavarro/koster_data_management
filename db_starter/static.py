import os, cv2, csv, json, sys, io
import operator, argparse, requests
import pandas as pd
import sqlite3
from datetime import datetime
from utils.server_utils import get_sites_movies_species
import utils.db_utils as db_utils
import utils.koster_utils as koster_utils
import utils.spyfish_utils as spyfish_utils
import utils.movie_utils as movie_utils


def add_sites(sites_csv, db_path):

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

    # Add values to sites table
    db_utils.add_to_table(
        db_path, "sites", [tuple(i) for i in sites_df.values], 6
    )

    
def add_movies(movies_csv, movies_path, project_name, db_path):

    # Load the csv with movies information
    movies_df = pd.read_csv(movies_csv)
    
    # Check if the project is the Spyfish Aotearoa
    if project_name == "Spyfish_Aotearoa":
        movies_df = spyfish_utils.process_spyfish_movies_csv(movies_df)
            
    # Check if the project is the KSO
    if project_name == "Koster_Seafloor_Obs":
        movies_df = koster_utils.process_koster_movies_csv(movies_df)
    
    # Ensure all videos have fps, duration, starting and ending time of the survey
    movies_df = movie_utils.get_movie_parameters(movies_df, movies_csv, project_name)
    
    print("Movie parameters checked")
    # Ensure date is ISO 8601:2004(E) compatible with Darwin Data standards
    #try:
    #    date.fromisoformat(movies_df['eventDate'])
    #except ValueError:
    #    print("Invalid eventDate column")

    # Connect to database
    conn = db_utils.create_connection(db_path)
    
    # Reference movies with their respective sites
    sites_df = pd.read_sql_query("SELECT id, siteName FROM sites", conn)
    sites_df = sites_df.rename(columns={"id": "Site_id"})


    
    movies_df = pd.merge(
        movies_df, sites_df, how="left", on="siteName"
    )
    

    # Select only those fields of interest
    movies_db = movies_df[
        ["movie_id", "filename", "created_on", "fps", "duration", "survey_start", "survey_end", "Author", "Site_id", "Fpath"]
    ]
    
    # Roadblock to prevent empty information
    db_utils.test_table(
        movies_db, "movies", movies_db.columns
    )
    
    # Add values to movies table
    db_utils.add_to_table(
        db_path, "movies", [tuple(i) for i in movies_db.values], 10
    )


def add_species(species_csv, db_path):

    # Load the csv with species information
    species_df = pd.read_csv(species_csv)
    
    # Select relevant fields
    species_df = species_df[
        ["species_id", "commonName", "scientificName", "taxonRank", "kingdom"]
    ]
    
    # Roadblock to prevent empty information
    db_utils.test_table(
        species_df, "species", species_df.columns
    )
    
    # Add values to species table
    db_utils.add_to_table(
        db_path, "species", [tuple(i) for i in species_df.values], 5
    )
    

def static_setup(movies_path: str,
                 project_name: str,
                 db_path: str):   
    
    # Get the location of the csv files with initial info to populate the db
    sites_csv, movies_csv, species_csv = get_sites_movies_species()
    
    add_sites(sites_csv, db_path)
    add_movies(movies_csv, movies_path, project_name, db_path)
    add_species(species_csv, db_path)
