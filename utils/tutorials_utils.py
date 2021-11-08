import pandas as pd
import ipywidgets as widgets


def choose_project():
    
    # Specify location of the latest list of projects
    projects_csv = "../db_starter/projects_list.csv" 
    
    # Read the latest list of projects
    projects_df = pd.read_csv(projects_csv)
    
    # Display the project options
    choose_project = widgets.Dropdown(
        options=projects_df.Project_name.unique().tolist(),
        value=projects_df.Project_name.unique().tolist()[0],
        description="Project:",
        disabled=False,
    )
    
    display(choose_project)
    return choose_project

def choose_server():
    
    # Select server storage
    server_i = widgets.Dropdown(
        options=["local","S3","Chalmers"],
        description='Choose server:',
        ensure_option=True,
        disabled=False,
    )
    
    display(server_i)
    
    return server_i    
    
def choose_single_workflow(workflows_df):

    layout = widgets.Layout(width="auto", height="40px")  # set width and height

    # Display the names of the workflows
    workflow_name = widgets.Dropdown(
        options=workflows_df.display_name.unique().tolist(),
        value=workflows_df.display_name.unique().tolist()[0],
        description="Workflow name:",
        disabled=False,
    )

    # Display the type of subjects
    subj_type = widgets.Dropdown(
        options=["frame", "clip"],
        value="clip",
        description="Subject type:",
        disabled=False,
    )

    display(workflow_name)
    display(subj_type)

    return workflow_name, subj_type

def choose_clip_workflows(workflows_df):

    layout = widgets.Layout(width="auto", height="40px")  # set width and height

    # Display the names of the workflows
    workflow_name = widgets.SelectMultiple(
        options=workflows_df.display_name.unique().tolist(),
        description="Workflow name:",
        disabled=False,
    )

    
    display(workflow_name)

    return workflow_name