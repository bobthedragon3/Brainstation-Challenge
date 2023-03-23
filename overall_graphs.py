import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("campaign_data.txt", delimiter="\t")

"""""
#Pledged vs. Duration
plt.scatter(x=data['duration'][data["outcome"] == 'successful'],y=data['Pledged_USD'][data["outcome"] == 'successful'],label = 'success')
plt.scatter(x=data['duration'][data["outcome"] == 'failed'],y=data['Pledged_USD'][data["outcome"] == 'failed'],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,60])
plt.xticks(range(0, 60, 10))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Duration")
plt.ylabel("Pledged")
plt.title("Pledged vs. Duration")
plt.show()

#Pledged vs. Goal
plt.scatter(x=data['goal'][data["outcome"] == 'successful'],y=data['Pledged_USD'][data["outcome"] == 'successful'],label = 'success')
plt.scatter(x=data['goal'][data["outcome"] == 'failed'],y=data['Pledged_USD'][data["outcome"] == 'failed'],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,30000])
plt.xticks(range(0, 30001, 5000))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Goal")
plt.ylabel("Pledged")
plt.title("Pledged vs. Goal")
plt.show()

#Pledged vs. Backers
plt.scatter(x=data['backers'][data["outcome"] == 'successful'],y=data['pledged'][data["outcome"] == 'successful'],label = 'success')
plt.scatter(x=data['backers'][data["outcome"] == 'failed'],y=data['pledged'][data["outcome"] == 'failed'],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,700])
plt.xticks(range(0, 701, 100))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Backers")
plt.ylabel("Pledged")
plt.title("Pledged vs. Backers")
plt.show()


#Goal vs. Duration
plt.scatter(x=data['duration'][data["outcome"] == 'successful'],y=data['goal'][data["outcome"] == 'successful'],label = 'success')
plt.scatter(x=data['duration'][data["outcome"] == 'failed'],y=data['goal'][data["outcome"] == 'failed'],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,70])
plt.xticks(range(0, 71, 10))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Duration")
plt.ylabel("Goal")
plt.title("Goal vs. Duration")
plt.show()
"""

# plotting histograms for count vs. Goals
bins = range(-2500, 30000, 2500)
plt.hist(data['goal'][data["outcome"] == "successful"],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['goal'][data["outcome"] == "failed"],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,30000])
plt.legend(loc='upper right')
plt.xlabel("Goal (USD)")
plt.ylabel("# of Campaigns")
plt.title('Campaign Goals Success/Failures')

threshold = 12000   #calculate % of successes w/ goal < 12.5k
variable_descr_1 = f"when the goal is less than ${threshold}"
success_rate_1 = round(100*len(data[(data["outcome"] == 'successful')&(data["goal"]<threshold)])/len(data[(data["goal"]<threshold)]))
print(f"There is a {success_rate_1}% chance of success {variable_descr_1}")
variable_descr_2 = f"when the goal is more than or equal to ${threshold}"
success_rate_2 = round(100*len(data[(data["outcome"] == 'successful')&(data["goal"]>=threshold)])/len(data[(data["goal"]>=threshold)]))
print(f"There is a {success_rate_2}% chance of success {variable_descr_2}")
plt.show()


# plotting histograms for count vs. duration - shows most campaigns around 30 days
bins = range(-5, 70, 10)
plt.hist(data['duration'][data["outcome"] == "successful"],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['duration'][data["outcome"] == "failed"],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,70])
plt.legend(loc='upper right')
plt.xlabel("Duration (Days)")
plt.ylabel("# of Campaigns")
plt.title('Campaign Duration Success/Failures')

threshold = 30   #calculate % of successes w/ duration < 35 days
threshold_name = "duration"
threshold_descr_1 = f"when the {threshold_name} is less than {threshold}"
success_rate_1 = round(100*len(data[(data["outcome"] == 'successful')&(data[f"{threshold_name}"]<threshold)])/len(data[(data[f"{threshold_name}"]<threshold)]))
print(f"There is a {success_rate_1}% chance of success {threshold_descr_1}")
variable_descr_2 = f"when the {threshold_name} is more than or equal to {threshold}"
success_rate_2 = round(100*len(data[(data["outcome"] == 'successful')&(data[f"{threshold_name}"]>=threshold)])/len(data[(data[f"{threshold_name}"]>=threshold)]))
print(f"There is a {success_rate_2}% chance of success {variable_descr_2}")
plt.show()

# plotting histograms for count vs. backers - shows almost all successes after 280 backers
bins = range(-25, 1000, 50)
plt.hist(data['backers'][data["outcome"] == "successful"],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['backers'][data["outcome"] == "failed"],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,1000])
plt.xticks(range(0,1000,100))
plt.legend(loc='upper right')
plt.xlabel("# Backers")
plt.ylabel("# of Campaigns")
plt.title('Campaign Backers Success/Failures')

threshold = 75   #calculate % of successes w/ backers > 75
threshold_name = "backers"
variable_descr_2 = f"when the number of {threshold_name} is more than {threshold}"
success_rate_2 = round(100*len(data[(data["outcome"] == 'successful')&(data[f"{threshold_name}"]>threshold)])/len(data[(data[f"{threshold_name}"]>threshold)]))
print(f"There is a {success_rate_2}% chance of success {variable_descr_2}")
threshold_descr_1 = f"when the number of {threshold_name} is less than or equal to {threshold}"
success_rate_1 = round(100*len(data[(data["outcome"] == 'successful')&(data[f"{threshold_name}"]<=threshold)])/len(data[(data[f"{threshold_name}"]<=threshold)]))
print(f"There is a {success_rate_1}% chance of success {threshold_descr_1}")
plt.show()

# plotting histograms for count vs. pledged - shows all campaigns that got 15k were successful -> weak though
bins = range(0, 30000, 1000)
plt.hist(data['pledged'][data["outcome"] == "successful"],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['pledged'][data["outcome"] == "failed"],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,30000])
plt.ylim([0,20])
plt.xticks(range(0, 30000, 5000))
plt.legend(loc='upper right')
plt.xlabel("Pledged")
plt.ylabel("# of Campaigns")
plt.title('Campaign Pledged Success/Failures')
plt.show()


#Pledged vs. Duration w/Goals of 10-20k
plt.scatter(x=data['duration'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'success')
plt.scatter(x=data['duration'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,60])
plt.xticks(range(0, 60, 10))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Duration")
plt.ylabel("Pledged")
plt.title("Pledged vs. Duration for Campaigns with Goals of 10-20k")
plt.show()


#Pledged vs. Goal w/Goals of 10-20k
plt.scatter(x=data['goal'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'success')
plt.scatter(x=data['goal'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'failed')
plt.legend(loc='upper right')
plt.xlim([0,30000])
plt.xticks(range(0, 30001, 5000))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Goal")
plt.ylabel("Pledged")
plt.title("Pledged vs. Goal for Campaigns with Goals of 10-20k")
plt.show()

#Pledged vs. Backers w/Goals of 10-20k
plt.scatter(x=data['backers'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'success')
plt.scatter(x=data['backers'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['Pledged_USD'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'failed')

plt.legend(loc='upper right')
plt.xlim([0,700])
plt.xticks(range(0, 701, 100))
plt.ylim([0,30000])
plt.yticks(range(0, 30001, 5000))
plt.xlabel("Backers")
plt.ylabel("Pledged")
plt.title("Pledged vs. Backers for Campaigns with Goals of 10-20k")
plt.show()

#Goal vs. Duration w/Goals of 10-20k
plt.scatter(x=data['duration'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['goal'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'success')
plt.scatter(x=data['duration'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],y=data['goal'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],label = 'failed')

plt.legend(loc='upper right')
plt.xlim([0,70])
plt.xticks(range(0, 71, 10))
plt.ylim([5000,25000])
plt.yticks(range(5000, 25001, 5000))
plt.xlabel("Duration")
plt.ylabel("Goal")
plt.title("Goal vs. Duration for Campaigns with Goals of 10-20k")
plt.show()

# plotting histograms for count vs. duration w/Goals of 10-20k - shows most campaigns around 30 days
bins = np.arange(-1.25, 70, 2.5)
plt.hist(data['duration'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['duration'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,70])
plt.legend(loc='upper right')
plt.xlabel("Duration")
plt.ylabel("# of Campaigns")
plt.title('Campaign Duration Success/Failures for Campaigns with Goals of 10-20k')



# plotting histograms for count vs. backers for Campaigns with Goals of 10-20k
bins = np.arange(-12.5, 600, 25)
plt.hist(data['backers'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000)],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['backers'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000)],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,600])
plt.xticks(range(0,601,100))
plt.legend(loc='upper right')
plt.xlabel("# Backers")
plt.ylabel("# of Campaigns")
plt.title('Campaign Backers Success/Failures for Campaigns with Goals of 10-20k')

#calculate %of successes that are between 15 and 35 days



plt.show()


# plotting histograms for count vs. backers for Campaigns with Goals of 10-20k and Duration between 20 and 40 Days
bins = np.arange(-12.5, 600, 25)
plt.hist(data['backers'][(data["outcome"] == 'successful') & (data["goal"]>10000) & (data["goal"]<20000) & (data["duration"]>20) & (data["duration"]<40)],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['backers'][(data["outcome"] == 'failed') & (data["goal"]>10000) & (data["goal"]<20000) & (data["duration"]>20) & (data["duration"]<40)],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.xlim([0,600])
plt.xticks(range(0,601,100))
plt.legend(loc='upper right')
plt.xlabel("# Backers")
plt.ylabel("# of Campaigns")
plt.title('Campaign Backers Success/Failures for Campaigns with Goals of 10-20k and Duration btwn 20 and 40 Days')
plt.show()

