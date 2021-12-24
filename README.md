# InformationRetrieval21
Repository to host the files for the IR2021 project by Niek Heijnen, Emma Schipper and Mees Spaan

## Experiment
The experiment itself can be performed by executing experiment.py.
For this it is important that the following files/directories are present:
- queries.txt  (containing the queries to search for)
- Trainingprofiles (containing a list with all training urls for each profile, in this list the cookie buttons are hardcoded)
- queryhtmls    (here the html files will be stored for later comparison)
- screenshotstrain (here the screenshots of the trainingsession will be stored for later control)
- screenshotsquery (here the screenshots of query sessions will be stored for later control)
- downloads1  (here the files that are being downloaded during training will be stored, the path to these directories needs to be added in the code itself)
- downloads2
- downloads3
- downloads4
- downloads5
- downloads6
- downloads6c

## Comparison
The comparison can then be performed by executing computeIndices.py
for this the directory with the queryhtmls that is created in experiment is needed.
This will compute the Jaccard and Damerau-Levenshtein indices and plot the averages per profile in a bar graph.
