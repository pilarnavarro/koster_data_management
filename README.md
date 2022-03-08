# Koster Seafloor Observatory - Data management

The Koster Seafloor Observatory is an open-source, citizen science and machine learning approach to analyse subsea movies.

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

![high-level][high-level-overview]


<!-- TOC -->
##### Table of Contents  
[Overview](#OVERVIEW)  
[Tutorials](#TUTORIALS) 
[Database](#DATABASE)
[Quickstart](#QUICKSTART)
[Requirements](#REQUIREMENTS)
[Installation](#INSTALLATION)
   


<a name="OVERVIEW"/>
## Overview
This repository contains scripts related to the data management component of the Koster Seafloor Observatory. The system is built around a series of easy-to-use Jupyter notebook tutorials. Each tutorial allows users to perform a specific task of the system (e.g. upload footage to the citizen science platform or analyse the classiffied data).


<a name="TUTORIALS"/>
## Tutorials
| Name                                              | Description                                                                                 | Status             |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- | :-----------------:|
| 1. Upload new footage                             | Upload new underwater media to the cloud/server and update the csv files                    | Coming soon        |
| 2. Check and update csv files                     | Check and update initial information about sites, media and species of interestest          | In progress        |
| 3. Upload clips to Zooniverse                     | Prepare original footage and upload short clips to Zooniverse                               | Completed          |
| 4. Upload frames to Zooniverse                    | Extract frames with animals of interest from original footage and upload them to Zooniverse | Completed          |
| 5. Train ML models                                | Prepare the training and test data, set model parameters and train models                   | Go to [Object Detection module][objdecmodule]|
| 6. Evalutate ML models                            | Use ecologically-relevant metrics to test the models                                        | Coming soon        |
| 7. Expose ML models                               | Expose model to the API                                                                     | Coming soon        |
| 8. Analyse Zooniverse classifications             | pull up-to-date classifications from Zooniverse and report summary stats/graphs             | Completed          |
| 9. Download and format Zooniverse classifications | pull up-to-date classifications from Zooniverse and format them for further analysis        | Coming soon        |
| 10. Publish classifications                       | Publish classifications to  [OBIS][OBIS-site]                                               | Completed          |
  
  
<a name="DATABASE"/>
## Database
The system uses a series of csv files to create a SQLite database to link all information related to the underwater footage and the classifications. The database follows the `Darwin Core (DwC) <https://dwc.tdwg.org/simple/>`_  standards to maximise the sharing, use and reuse of open-access biodiversity data.
The database has seven interconnected tables. The “movies”, “sites” and “species” tables have project-specific information from the underwater movie metadata, as well as the species choices available for citizen scientists to annotate the clips, retrieved from Zooniverse. The “agg_annotations_frame” and “agg_annotations_clip” tables contain information related to the annotations provided by citizen scientists. The “subjects” table has information related to the clips and frames uploaded to the Koster Seafloor Observatory. The "model_annotations" table holds information related to the annotations provided by the machine learning algorithms. 

![Database_diag][Database_diagram]


<a name="QUICKSTART"/>
## Quickstart
[![binder][binderlogo]][binderlink]

<a name="REQUIREMENTS"/>
## Requirements
* Python 3.7+
* Python dependencies listed in requirements.txt

<a name="INSTALLATION"/>
## Installation
### Option 1: Local / Cloud Installation
#### Download this repository
For those with a [Github](https://github.com/) account or git installed simply clone this
repository using
```python
git clone https://github.com/ocean-data-factory-sweden/koster_data_management.git
```

If you don't have a Github account you can manually download the repository. Click on the green "Code" download button visible on the top right of this screen and choose the Download ZIP option from the Code pull-down menu. 

#### Download Anaconda
[Anaconda](https://docs.anaconda.com/anaconda/install/index.html) allows you to create virtual Python environments for and features a simple package manager to keep track of dependencies.

#### Install dependecies
Navigate to the folder where you have cloned the repository or unzipped the manually downloaded repository and run
```python
pip install -r requirements.txt
```

#### Create initial information for the database 
If you will work in a new project you will need to input the information about the underwater footage files, sites and species of interest. You can use a [template of the csv files](https://drive.google.com/file/d/1PZGRoSY_UpyLfMhRphMUMwDXw4yx1_Fn/view?usp=sharing) and move the directory to the "db_starter" folder.


#### Link your footage to the database 
You will need underwater movies to run KSO. You can `download some samples <https://drive.google.com/drive/folders/1t2ce8euh3SEU2I8uhiZN1Tu-76ZDqB6w?usp=sharing/>`_. Remember where you store the movies as you will need to specify the directory of the movies in the tutorials.


### Option 2: SNIC Users
To use the Jupyter Notebooks within the Alvis HPC cluster, please visit `<https://portal.c3se.chalmers.se>`_ and login using your SNIC credentials. 

Once you have been authorized, click on "Interactive Apps" and then "Jupyter". This open the server creation options. 

Here you can keep the settings as default, apart from the "Number of hours" which you can set to the desired limit. Then choose either **Data Management (Runtime (User specified jupyter1.sh))** or **Machine Learning (Runtime (User specified jupyter2.sh))** from the Runtime dropdown options.

.. image:: images/screenshot_loading.png
   :align: center
   :alt: "(Session queued window")

This will directly queue a server session using the correct container image, first showing a blue window and then you should see a green window when the session has been successfully started and the button **"Connect to Jupyter"** appears on the screen. Click this to launch into the Jupyter notebook environment. 

.. image:: images/screenshot_started.png
   :align: center
   :alt: "(Session started window")

Important note: The remaining time for the server is shown in green window as well. If you have finished using the notebook server before the alloted time runs out, please select **"Delete"** so that the resources can be released for use by others within the project. 


## Citation

If you use this code or its models in your research, please cite:

Anton V, Germishuys J, Bergström P, Lindegarth M, Obst M (2021) An open-source, citizen science and machine learning approach to analyse subsea movies. Biodiversity Data Journal 9: e60548. https://doi.org/10.3897/BDJ.9.e60548

## Collaborations/questions
You can find out more about the project at https://www.zooniverse.org/projects/victorav/the-koster-seafloor-observatory.

We are always excited to collaborate and help other marine scientists. Please feel free to [contact us](matthias.obst@marine.gu.se) with your questions.

## Troubleshooting

If you experience issues to upload movies to zooniverse. It might be related to the libmagic package. In windows the following commands seem to work.
```python
pip install python-libmagic
pip install python-magic-bin
```


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ocean-data-factory-sweden/koster_app.svg?style=for-the-badge
[contributors-url]: https://https://github.com/ocean-data-factory-sweden/koster_data_management/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ocean-data-factory-sweden/koster_app.svg?style=for-the-badge
[forks-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/network/members
[stars-shield]: https://img.shields.io/github/stars/ocean-data-factory-sweden/koster_app.svg?style=for-the-badge
[stars-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/stargazers
[issues-shield]: https://img.shields.io/github/issues/ocean-data-factory-sweden/koster_app.svg?style=for-the-badge
[issues-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/issues
[license-shield]: https://img.shields.io/github/license/ocean-data-factory-sweden/koster_app.svg?style=for-the-badge
[license-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/LICENSE.txt
[high-level-overview]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/dev/images/high-level-overview.png?raw=true "Overview of the three main modules and the components of the Koster Seafloor Observatory"
[objdecmodule]: https://github.com/ocean-data-factory-sweden/koster_yolov4
[OBIS-site]: https://www.gbif.org/network/2b7c7b4f-4d4f-40d3-94de-c28b6fa054a6
[Database_diagram]: https://github.com/ocean-data-factory-sweden/koster_data_management/tree/dev/images/Database_diagram.png "Entity relationship diagram of the SQLite database of the Koster Seafloor Observatory"
[binderlogo]: https://mybinder.org/badge_logo.svg
[binderlink]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/main
