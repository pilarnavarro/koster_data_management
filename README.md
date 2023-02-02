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

## KSO Information architecture
The system processes underwater footage and its associatead metadata into biologically-meaningfull information. The format of the underwater media is standard (.mp4 or .png) and the associated metadata should be captured in three csv files (“movies”, “sites” and “species”) following  the [Darwin Core standards (DwC)](https://dwc.tdwg.org/simple/). 
![koster_info_diag][high-level-overview]

## Module Overview
This data management module contains scripts and resources to move and process underwater footage and its associated data (e.g. location, date, sampling device). 

![Data_man_module][Data_management_module]

The system is built around a series of easy-to-use Jupyter notebook tutorials. Each tutorial allows users to perform a specific task of the system (e.g. upload footage to the citizen science platform or analyse the classified data). The notebooks rely on the [koster utility functions][koster_utils_repo].

## Tutorials
| Name                                              | Description                                                                                 | Try it!  | 
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------|
| 1. Check footage and metadata                     | Check format and contents of footage and sites, media and species csv files                 | [![Open In Colab][colablogo]][colab_tut_1] [![binder][binderlogo]][binder_tut_1] | 
| 2. Upload new media to the system*                | Upload new underwater media to the cloud/server and update the csv files                    | [![Open In Colab][colablogo]][colab_tut_2] [![binder][binderlogo]][binder_tut_2] | 
| 3. Upload clips to Zooniverse                     | Prepare original footage and upload short clips to Zooniverse                               | [![Open In Colab][colablogo]][colab_tut_3] [![binder][binderlogo]][binder_tut_3] |
| 4. Upload frames to Zooniverse                    | Extract frames of interest from original footage and upload them to Zooniverse              | [![Open In Colab][colablogo]][colab_tut_4] [![binder][binderlogo]][binder_tut_4] |
| 5. Train ML models                                | Prepare the training and test data, set model parameters and train models                   | [![Open In Colab][colablogo]][colab_tut_5] [![binder][binderlogo]][binder_tut_5] | 
| 6. Evaluate ML models                            | Use ecologically-relevant metrics to test the models                                        | [![Open In Colab][colablogo]][colab_tut_6] [![binder][binderlogo]][binder_tut_6]   |
| 7. Publish ML models                               | Publish the model to a public repository                                                   | [![Open In Colab][colablogo]][colab_tut_7] [![binder][binderlogo]][binder_tut_7]  | 
| 8. Analyse Zooniverse classifications             | Pull up-to-date classifications from Zooniverse and report summary stats/graphs             | [![Open In Colab][colablogo]][colab_tut_8] [![binder][binderlogo]][binder_tut_8] |
| 9. Download and format Zooniverse classifications | Pull up-to-date classifications from Zooniverse and format them for further analysis        | Coming soon  | 
| 10. Run ML models on footage                      | Automatically classify new footage                                                          | Coming soon  |

  
\* Project-specific tutorial

## Local Installation
If you want to fully use our system (Binder and Colab has computing limitations), you will need to download this repository on your local computer or server.

### Requirements
* [Python 3.7+](https://www.python.org/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
* [GIT](https://git-scm.com/downloads)

### Installation
#### Create a new conda environment
Follow the [documentation to create a new environment in conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)

#### Download this repository
Clone this repository using
```python
git clone --recurse-submodules https://github.com/ocean-data-factory-sweden/kso-data-management.git
``` 

#### Install dependecies
Navigate to the folder where you have cloned the repository or unzipped the manually downloaded repository. 
```python
cd kso-data-management
```

Then install the requirements by running.
```python
pip install -r requirements.txt
```

#### Create initial information for the database 
If you will work in a new project you will need to input the information about the underwater footage files, sites and species of interest. You can use a [template of the csv files](https://drive.google.com/file/d/1PZGRoSY_UpyLfMhRphMUMwDXw4yx1_Fn/view?usp=sharing) and move the directory to the "db_starter" folder.


#### Link your footage to the database 
You will need files of underwater footage to run this system. You can [download some samples](https://drive.google.com/drive/folders/1t2ce8euh3SEU2I8uhiZN1Tu-76ZDqB6w?usp=sharing) and move them to `db_starter`. You can also store your own files and specify their directory in the tutorials.


## Dev instructions

If you would like to expand and improve the KSO capabilities, please follow the instructions below and reach out if there are any issues. 

### Dev requirements
* [Python 3.7+](https://www.python.org/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
* [GIT](https://git-scm.com/downloads)
* [Black](https://pypi.org/project/black/)

### Dev set up
- Install conda 
- Create new environment
- Install git and pip (with conda)
- Clone kso repo and its submodules (ideally your fork)
- To avoid issues with different notebook kernels we recommend creating a new one: 
```python
pip install ipykernel
python -m ipykernel install --user --name="new_environment"
```

### Merging your changes
Before pushing your code to the main branch of KSO, please: 
* run Black on the code you have edited 
```shell
black filename 
```
* update the timestamp on the notebook
```shell
python update_ts.py filename 
```
Remember to follow the [conventional commits guidelines](https://www.conventionalcommits.org/en/v1.0.0/) to facilitate code sharing. 

## Installation in High Performance Computers
### Installation for SNIC Users*
\* SNIC login credentials and access to Chalmers VPN using [Windows](https://it.portal.chalmers.se/itportal/NonCDAWindows/VPN) or [MAC](https://it.portal.chalmers.se/itportal/NonCDAMac/VPN) required.

Log in the [Alvis Portal](https://portal.c3se.chalmers.se) and click on "Interactive Apps" and then "Jupyter". This open the server creation options.

Creating a Jupyter session requires a custom environment file, which is available on our shared drive */mimer/NOBACKUP/groups/snic2022-22-1210/jupter_envs*. Please copy these files to your **Home Directory** in order to use the custom environments we have created.

Here you can keep the settings as default, apart from the "Number of hours" which you can set to the desired limit. Then choose either **Data Management (Runtime (User specified jupyter1.sh))** or **Machine Learning (Runtime (User specified jupyter2.sh))** from the Runtime dropdown options.

![screenshot_load][screenshot_loading]

This will directly queue a server session using the correct container image, first showing a blue window and then you should see a green window when the session has been successfully started and the button **"Connect to Jupyter"** appears on the screen. Click this to launch into the Jupyter notebook environment. 


![screenshot_start][screenshot_started]

Important note: The remaining time for the server is shown in green window as well. If you have finished using the notebook server before the alloted time runs out, please select **"Delete"** so that the resources can be released for use by others within the project. 

## Troubleshooting

If you experience issues uploading movies to Zooniverse, it might be related to the libmagic package. In Windows, the following commands seem to work:
```python
pip install python-libmagic
pip install python-magic-bin
```


## Citation

If you use this code or its models in your research, please cite:

Anton V, Germishuys J, Bergström P, Lindegarth M, Obst M (2021) An open-source, citizen science and machine learning approach to analyse subsea movies. Biodiversity Data Journal 9: e60548. https://doi.org/10.3897/BDJ.9.e60548

## Collaborations/questions
You can find out more about the project at https://www.zooniverse.org/projects/victorav/the-koster-seafloor-observatory.

We are always excited to collaborate and help other marine scientists. Please feel free to [contact us](matthias.obst@marine.gu.se) with your questions.




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ocean-data-factory-sweden/kso-data-management.svg?style=for-the-badge
[contributors-url]: https://https://github.com/ocean-data-factory-sweden/kso-data-management/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ocean-data-factory-sweden/kso-data-management.svg?style=for-the-badge
[forks-url]: https://github.com/ocean-data-factory-sweden/kso-data-management/network/members
[stars-shield]: https://img.shields.io/github/stars/ocean-data-factory-sweden/kso-data-management.svg?style=for-the-badge
[stars-url]: https://github.com/ocean-data-factory-sweden/kso-data-management/stargazers
[issues-shield]: https://img.shields.io/github/issues/ocean-data-factory-sweden/kso-data-management.svg?style=for-the-badge
[issues-url]: https://github.com/ocean-data-factory-sweden/kso-data-management/issues
[license-shield]: https://img.shields.io/github/license/ocean-data-factory-sweden/kso-data-management.svg?style=for-the-badge
[license-url]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/LICENSE.txt
[high-level-overview]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/images/high-level-overview-2.png?raw=true "Overview of the three main modules and the components of the Koster Seafloor Observatory"
[Data_management_module]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/images/Koster_data_management_module.png?raw=true
[koster_utils_repo]: https://github.com/ocean-data-factory-sweden/kso_utils
[colablogo]: https://colab.research.google.com/assets/colab-badge.svg
[binderlogo]: https://mybinder.org/badge_logo.svg
[colab_tut_1]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/01_Check_and_update_csv_files.ipynb
[binder_tut_1]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_2]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/02_Upload_new_footage.ipynb
[binder_tut_2]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_3]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/03_Upload_clips_to_Zooniverse.ipynb
[binder_tut_3]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_4]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/04_Upload_frames_to_Zooniverse.ipynb
[binder_tut_4]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_5]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-object-detection/blob/master/tutorials/05_Train_ML_models.ipynb
[binder_tut_5]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-object-detection/master
[colab_tut_6]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-object-detection/blob/master/tutorials/06_Evaluate_ML_Models.ipynb
[binder_tut_6]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-object-detection/master
[colab_tut_7]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-object-detection/blob/master/tutorials/07_Transfer_ML_Models.ipynb
[binder_tut_7]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-object-detection/master
[colab_tut_8]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/08_Analyse_Aggregate_Zooniverse_Annotations.ipynb
[binder_tut_8]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_11]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/11_Concatenate_videos_from_AWS.ipynb
[binder_tut_11]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[colab_tut_12]: https://colab.research.google.com/github/ocean-data-factory-sweden/kso-data-management/blob/main/tutorials/12_Display_movies_available_on_the_server.ipynb
[binder_tut_12]: https://mybinder.org/v2/gh/ocean-data-factory-sweden/kso-data-management/main
[objdecmodule]: https://github.com/ocean-data-factory-sweden/kso-object-detection
[OBIS-site]: https://www.gbif.org/network/2b7c7b4f-4d4f-40d3-94de-c28b6fa054a6
[Koster_info_diagram]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/images/Koster_information_flow.png?raw=true "Information architecture of the Koster Seafloor Observatory"
[screenshot_loading]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/images/screenshot_loading.png?raw
[screenshot_started]: https://github.com/ocean-data-factory-sweden/kso-data-management/blob/main/images/screenshot_started.png?raw
