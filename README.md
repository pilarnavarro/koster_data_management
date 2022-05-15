# KSO - Data management

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

## Module Overview
This data management module contains scripts and resources to move and process underwater footage and its associated data (e.g. location, date, sampling device). 

![Data_man_module][Data_management_module]

The system is built around a series of easy-to-use Jupyter notebook tutorials. Each tutorial allows users to perform a specific task of the system (e.g. upload footage to the citizen science platform or analyse the classiffied data). The notebooks rely on the [koster utility functions][koster_utils_repo].

### Tutorials
| Name                                              | Description                                                                                 | Try it!  | 
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------|
| 1. Check and update csv files                     | Check and update initial information about sites, media and species of interestest          | [![Open In Colab][colablogo]][colab_tut_1] [![binder][binderlogo]][binder_tut_1] | 
| 2. Upload new footage                             | Upload new underwater media to the cloud/server and update the csv files                    | [![Open In Colab][colablogo]][colab_tut_2] [![binder][binderlogo]][binder_tut_2] | 
| 3. Upload clips to Zooniverse                     | Prepare original footage and upload short clips to Zooniverse                               | [![Open In Colab][colablogo]][colab_tut_3] [![binder][binderlogo]][binder_tut_3] |
| 4. Upload frames to Zooniverse                    | Extract frames with animals of interest from original footage and upload them to Zooniverse | Coming soon         |
| 5. Train ML models                                | Prepare the training and test data, set model parameters and train models                   | [![Open In Colab][colablogo]][colab_tut_5] [![binder][binderlogo]][binder_tut_5] | 
| 6. Evaluate ML models                            | Use ecologically-relevant metrics to test the models                                        | Coming soon  |
| 7. Expose ML models                               | Expose model to the API                                                                     | Coming soon | 
| 8. Analyse Zooniverse classifications             | pull up-to-date classifications from Zooniverse and report summary stats/graphs             | [![Open In Colab][colablogo]][colab_tut_8] [![binder][binderlogo]][binder_tut_8] |
| 9. Download and format Zooniverse classifications | pull up-to-date classifications from Zooniverse and format them for further analysis        | Coming soon  | 
| 10. Publish classifications                       | Publish classifications to  [OBIS][OBIS-site]                                               | Coming soon  | 
  
### Database
The system uses a series of csv files to create a SQLite database to link all information related to the underwater footage and the classifications. The database follows the [Darwin Core standards (DwC)](https://dwc.tdwg.org/simple/) to maximise the sharing, use and reuse of open-access biodiversity data.
The database has seven interconnected tables. The “movies”, “sites” and “species” tables have project-specific information from the underwater movie metadata, as well as the species choices available for citizen scientists to annotate the clips, retrieved from Zooniverse. The “agg_annotations_frame” and “agg_annotations_clip” tables contain information related to the annotations provided by citizen scientists. The “subjects” table has information related to the clips and frames uploaded to the Koster Seafloor Observatory. The "model_annotations" table holds information related to the annotations provided by the machine learning algorithms. 

![Database_diag][Database_diagram]


## Dev Installation
If you want to fully use our system (Binder has computing limitations), you will need to download this repository on your local computer or server.

### Requirements
* [Python 3.7+](https://www.python.org/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
* [GIT](https://git-scm.com/downloads)

### Option 1: Local / Cloud Installation
-----------------
#### Download this repository
Clone this repository using
```python
git clone --recurse-submodules https://github.com/ocean-data-factory-sweden/koster_data_management.git
``` 

#### Install dependecies
Navigate to the folder where you have cloned the repository or unzipped the manually downloaded repository. 
```python
cd koster_data_management
```

Then install the requirements by running.
```python
pip install -r requirements.txt
```

#### Create initial information for the database 
If you will work in a new project you will need to input the information about the underwater footage files, sites and species of interest. You can use a [template of the csv files](https://drive.google.com/file/d/1PZGRoSY_UpyLfMhRphMUMwDXw4yx1_Fn/view?usp=sharing) and move the directory to the "db_starter" folder.


#### Link your footage to the database 
You will need files of underwater footage to run this system. You can [download some samples](https://drive.google.com/drive/folders/1t2ce8euh3SEU2I8uhiZN1Tu-76ZDqB6w?usp=sharing) and move them to `db_starter`. You can also store your own files and specify their directory in the tutorials.


### Option 2: SNIC Users (VPN required)

-----------------

**Before using Option 2, users should have login credentials and have setup the Chalmers VPN on their local computers**

Information for Windows users: [Click here](https://it.portal.chalmers.se/itportal/NonCDAWindows/VPN)
Information for MAC users: [Click here](https://it.portal.chalmers.se/itportal/NonCDAMac/VPN)

To use the Jupyter Notebooks within the Alvis HPC cluster, please visit [Alvis Portal](https://portal.c3se.chalmers.se) and login using your SNIC credentials. 

Once you have been authorized, click on "Interactive Apps" and then "Jupyter". This open the server creation options. 

Here you can keep the settings as default, apart from the "Number of hours" which you can set to the desired limit. Then choose either **Data Management (Runtime (User specified jupyter1.sh))** or **Machine Learning (Runtime (User specified jupyter2.sh))** from the Runtime dropdown options.

![screenshot_load][screenshot_loading]

This will directly queue a server session using the correct container image, first showing a blue window and then you should see a green window when the session has been successfully started and the button **"Connect to Jupyter"** appears on the screen. Click this to launch into the Jupyter notebook environment. 


![screenshot_start][screenshot_started]

Important note: The remaining time for the server is shown in green window as well. If you have finished using the notebook server before the alloted time runs out, please select **"Delete"** so that the resources can be released for use by others within the project. 


## Citation

If you use this code or its models in your research, please cite:

Anton V, Germishuys J, Bergström P, Lindegarth M, Obst M (2021) An open-source, citizen science and machine learning approach to analyse subsea movies. Biodiversity Data Journal 9: e60548. https://doi.org/10.3897/BDJ.9.e60548

## Collaborations/questions
You can find out more about the project at https://www.zooniverse.org/projects/victorav/the-koster-seafloor-observatory.

We are always excited to collaborate and help other marine scientists. Please feel free to [contact us](matthias.obst@marine.gu.se) with your questions.

## Dev instructions

- Installing conda 
- Create new environment (e.g. "new environment")
- Install git and pip (with conda)
- Clone kso repo
- pip install ipykernel
- python -m ipykernel install --user --name="new_environment"
- from the jupyter notebook select kernel/change kernel

## Troubleshooting

If you experience issues to upload movies to zooniverse. It might be related to the libmagic package. In windows the following commands seem to work.
```python
pip install python-libmagic
pip install python-magic-bin
```


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ocean-data-factory-sweden/koster_data_management.svg?style=for-the-badge
[contributors-url]: https://https://github.com/ocean-data-factory-sweden/koster_data_management/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ocean-data-factory-sweden/koster_data_management.svg?style=for-the-badge
[forks-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/network/members
[stars-shield]: https://img.shields.io/github/stars/ocean-data-factory-sweden/koster_data_management.svg?style=for-the-badge
[stars-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/stargazers
[issues-shield]: https://img.shields.io/github/issues/ocean-data-factory-sweden/koster_data_management.svg?style=for-the-badge
[issues-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/issues
[license-shield]: https://img.shields.io/github/license/ocean-data-factory-sweden/koster_data_management.svg?style=for-the-badge
[license-url]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/LICENSE.txt
[high-level-overview]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/images/high-level-overview.png?raw=true "Overview of the three main modules and the components of the Koster Seafloor Observatory"
[Data_management_module]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/images/Koster_data_management_module.png?raw=true
[koster_utils_repo]: https://github.com/ocean-data-factory-sweden/kso_utils
[colablogo]: https://colab.research.google.com/assets/colab-badge.svg
[binderlogo]: https://mybinder.org/badge_logo.svg
[colab_tut_1]: https://colab.research.google.com/github/ocean-data-factory-sweden/koster_data_management/blob/dev/colab_tutorials/1_Check_and_update_csv_files.ipynb
[binder_tut_1]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/dev
[colab_tut_2]: https://colab.research.google.com/github/ocean-data-factory-sweden/koster_data_management/blob/dev/colab_tutorials/2_Upload_new_footage.ipynb
[binder_tut_2]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/dev
[colab_tut_3]: https://colab.research.google.com/github/ocean-data-factory-sweden/koster_data_management/blob/dev/colab_tutorials/3_Upload_clips_to_Zooniverse.ipynb
[binder_tut_3]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/dev
[colab_tut_5]: https://colab.research.google.com/github/ocean-data-factory-sweden/koster_yolov4/blob/master/Colab/5_Colab_Train_Koster_ML_models.ipynb
[binder_tut_5]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/dev
[colab_tut_8]: https://colab.research.google.com/github/ocean-data-factory-sweden/koster_data_management/blob/dev/colab_tutorials/8_Analyse_Zooniverse_classifications.ipynb
[binder_tut_8]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/koster_data_management/dev
[objdecmodule]: https://github.com/ocean-data-factory-sweden/koster_yolov4
[OBIS-site]: https://www.gbif.org/network/2b7c7b4f-4d4f-40d3-94de-c28b6fa054a6
[Database_diagram]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/images/Database_diagram.png?raw=true "Entity relationship diagram of the SQLite database of the Koster Seafloor Observatory"
[screenshot_loading]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/images/screenshot_loading.png?raw=true
[screenshot_started]: https://github.com/ocean-data-factory-sweden/koster_data_management/blob/main/images/screenshot_started.png?raw=true
