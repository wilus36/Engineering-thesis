# Engineering-thesis
Engineering thesis part, python scripts to utilize old profilograph data with examples

The profilograph takes 2000 points on a given distance (set on the coomputer) and gives each an integer value between 0 and 4096 where 2048 is the calibrated base level. The point are saved to a text file. This script converts this data to graphs with 3 series on each graph. Please note that mathematical calculations were base on specific machine settings. If you are not working on the same machine from Gdansk University of Technology laboratories treat these files as an example only.

Note 1: this script uses matplotlib
Note 2: The 'correction attempt' folder contains scripts that were supposed to correct a badly-calibrated machine. These will be left here in case someone would like to take a shot at this, for the time-being it has been concluded that bad calibration can not be software-corrected and would not have a great impact on the rest of the thesis research.
