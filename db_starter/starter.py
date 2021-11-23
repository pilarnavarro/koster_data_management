import argparse

from init import init_db
from static import static_setup
from utils.tutorials_utils import get_project_info

def main():
    
    "Handles argument parsing and launches the correct function."
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-pj",
        "--project_name",
        type=str,
        help="the name of your project",
        default=r"Project example",
        required=False,
    )

    args = parser.parse_args()
    
    # Get the project-specific name of the database
    db_path = get_project_info(args.project_name, "db_path")
    
    # Initiate the sql db
    init_db(db_path)
    
    # Populate the db with initial info from csv files
    static_setup(args.project_name, db_path)
    
    
if __name__ == "__main__":
    main()
