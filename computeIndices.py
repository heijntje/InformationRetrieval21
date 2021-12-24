from bs4 import BeautifulSoup
from fastDamerauLevenshtein import damerauLevenshtein
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def jaccardIndex(list1, list2):
	intersection = len(list(set(list1).intersection(list2)))
	union = (len(set(list1)) + len(set(list2))) - intersection
	return float(intersection) / union

jaccardIndices6 = {1:[], 2:[] , 3:[], 4:[], 5:[], 6: [], 7: []}
jaccardIndices7 = {1:[], 2:[] , 3:[], 4:[], 5:[], 6: [], 7: []}

damerauLevenshteinIndices6 = {1:[], 2:[] , 3:[], 4:[], 5:[], 6:[], 7:[]}
damerauLevenshteinIndices7 = {1:[], 2:[] , 3:[], 4:[], 5:[], 6:[], 7:[]}

# We compute the Jaccard indices and the Damerau Levenshtein indices for all queries
for queryid in range(0, 98):
	# First we create a list of all search results that we deem important,
	# being, actual webpage results, newsarticles and videos
	# these are all retrieved from the first page of google only.
	# We first do this for the two control profiles as we want to compare all others to these two.
	base6c = open("queryhtmls/" + str(queryid) + "-6c.txt", encoding="utf8")
	htmlSource = base6c.read()
	soup = BeautifulSoup(htmlSource, 'html.parser')
	searchresults6c = soup.find_all("h3", class_="LC20lb MBeuO DKV0Md")
	newsresults6c = soup.find_all("div", class_ = "mCBkyc tNxQIb oz3cqf ynAwRc nDgy9d")
	videoresults6c = soup.find_all("div", class_ = "fc9yUc tNxQIb ynAwRc OSrXXb")
	searchresults6c = [el.text for el in searchresults6c]
	newsresults6c = [el.text for el in newsresults6c]
	videoresults6c = [el.text for el in videoresults6c]
	results6c = searchresults6c + newsresults6c + videoresults6c
	base6c.close()

	base7c = open("queryhtmls/" + str(queryid) + "-7c.txt", encoding="utf8")
	htmlSource = base7c.read()
	soup = BeautifulSoup(htmlSource, 'html.parser')
	searchresults7c = soup.find_all("h3", class_="LC20lb MBeuO DKV0Md")
	newsresults7c = soup.find_all("div", class_ = "mCBkyc tNxQIb oz3cqf ynAwRc nDgy9d")
	videoresults7c = soup.find_all("div", class_ = "fc9yUc tNxQIb ynAwRc OSrXXb")
	searchresults7c = [el.text for el in searchresults7c]
	newsresults7c = [el.text for el in newsresults7c]
	videoresults7c = [el.text for el in videoresults7c]
	results7c = searchresults7c + newsresults7c + videoresults7c
	base7c.close()

	# Then we loop over the other profiles, including the two base profiles and compute the two indices
	# and add them to the list of results for each profile
	for profileno in range (1, 8):
		base = open("queryhtmls/" + str(queryid) + "-" + str(profileno) +".txt", encoding="utf8")
		htmlSource = base.read()
		soup = BeautifulSoup(htmlSource, 'html.parser')
		searchresults = soup.find_all("h3", class_="LC20lb MBeuO DKV0Md")
		newsresults = soup.find_all("div", class_ = "mCBkyc tNxQIb oz3cqf ynAwRc nDgy9d")
		videoresults = soup.find_all("div", class_ = "fc9yUc tNxQIb ynAwRc OSrXXb")
		searchresults = [el.text for el in searchresults]
		newsresults = [el.text for el in newsresults]
		videoresults = [el.text for el in videoresults]
		results = searchresults + newsresults + videoresults
		jI6 = jaccardIndex(results6c, results)
		jI7 = jaccardIndex(results7c, results)
		jaccardIndices6[profileno] = jaccardIndices6[profileno] + [jI6]
		jaccardIndices7[profileno] = jaccardIndices7[profileno] + [jI7]
		dlI6 = damerauLevenshtein(results6c, results, similarity=False)
		dlI7 = damerauLevenshtein(results7c, results, similarity=False)
		damerauLevenshteinIndices6[profileno] = damerauLevenshteinIndices6[profileno] + [dlI6]
		damerauLevenshteinIndices7[profileno] = damerauLevenshteinIndices7[profileno] + [dlI7]

		base.close()


# Next we compute the averages of all profiles, including the baseprofiles
# against the two control profiles

averageJaccard6 = []
averageJaccard7 = []
averageLevenshtein6 = []
averageLevenshtein7 = []


for i in range (1,8):
	avgJC6 = round(sum(jaccardIndices6[i])/len(jaccardIndices6[i]),2)
	averageJaccard6.append(avgJC6)
	avgJC7 = round(sum(jaccardIndices7[i])/len(jaccardIndices7[i]),2)
	averageJaccard7.append(avgJC7)
	avgLT6 = round(sum(damerauLevenshteinIndices6[i])/len(damerauLevenshteinIndices6[i]),2)
	averageLevenshtein6.append(avgLT6)
	avgLT7 = round(sum(damerauLevenshteinIndices7[i])/len(damerauLevenshteinIndices7[i]),2)
	averageLevenshtein7.append(avgLT7)


# And finally we plot the two bar graphs of our results
# as explained in the report, the results of profile 6 are left out,
# as these are mostly identical to those of profile 7

labels = ["Left.\nProg.", "Cent.\nProg.", "Cent.\nCent.", "Right\nCent.", "Right\nCons.", "None*"]
x = np.arange(len(labels))
width = 0.35

# Jaccard
figJ, axJ = plt.subplots()
rectsJ = axJ.bar(x, averageJaccard7[0:5]+[averageJaccard7[6]], width, label='Jaccard 7')
rectsJ[5].set_color('g')

axJ.set_ylabel('Avgs.')
axJ.set_title('Jaccard')
axJ.set_xticks(x,labels)
axJ.bar_label(rectsJ, padding=3)

figJ.tight_layout()

# Levenshtein
figL, axL = plt.subplots()
rectsL = axL.bar(x, averageLevenshtein7[0:5]+[averageLevenshtein7[6]], width, label='Damerau 7')
rectsL[5].set_color('g')

axL.set_ylabel('Avgs.')
axL.set_title('Damerau Levenshtein')
axL.set_xticks(x,labels)
axL.bar_label(rectsL, padding=3)

figL.tight_layout()


plt.show()
