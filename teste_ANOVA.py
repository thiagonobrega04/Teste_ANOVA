import pandas as pd
from scipy import stats

# Introduction to ANOVA
# Welcome, friends! Today, we're learning about Analysis of Variance or ANOVA. It’s a way to determine if there are significant differences between the means (or averages) of three or more groups. This tool is handy in fields like biology, manufacturing, and education.

# Let's unwrap the ANOVA mystery together!

# What is ANOVA?
# ANOVA is like a detective. It solves a mystery: are the means of certain groups equal? It does this by examining how the individual data values deviate from the group means and the grand mean. Just imagine you have three apples of different types, and you want to know if they weigh the same. ANOVA would be like a scale that helps determine this!

# ANOVA assumes three things:

# 1. Normality: The data from each group looks like a normal distribution.
# 2.Homogeneity of Variance: Each group has the same spread or variance.
# 3. Independence: Each data point doesn't depend on the others.
# Today, we’ll study the ANOVA test in Python.

# One-way ANOVA
# Think of One-way ANOVA like a game where you're comparing the average scores (means) of several teams (groups). The ultimate goal is to figure out if there is at least one team scoring differently than the others.

# The output of the One-way ANOVA test is a value called F-statistic. A simple way to think about the F-statistic is like a signal-to-noise ratio:

# . Signal: How much the group means differ from each other.
# . Noise: How much the group members differ among themselves.
# If the teams' scores are all similar, we would have a low signal and high noise, yielding an F-statistic close to 1.0. But if one of the teams' average score is substantially different from the others, the signal increases compared to the noise, resulting in an F-statistic greater than 1.0.

# Introducing Apple Dataset
# We've gathered weight data for three different types of apples. Now, we’re curious if the average weight is the same for every kind of apple. Here's how we'd explore this mystery in Python using One-way ANOVA:

# Sample weights for 3 different apple types
data = pd.DataFrame({
    'apple_type': ['Apple1']*5 + ['Apple2']*5 + ['Apple3']*5,
    'weight': [162.5, 165.0, 167.5, 160.0, 158.5, 175.0, 177.5, 172.5, 170.0, 160.5, 182.5, 185.0, 180.0, 177.5, 165.5]
})

# Here’s our sample data with weights for three types of apples, 'Apple1', 'Apple2', and 'Apple3'.

# Selecting Data
# We need to select samples from each apple type group before comparing their means. Here is how to do that:

# Select weights for each apple type
apple1_weights = data['weight'][data['apple_type'] == 'Apple1']
apple2_weights = data['weight'][data['apple_type'] == 'Apple2']
apple3_weights = data['weight'][data['apple_type'] == 'Apple3']

# We first select the 'weight' column and then apply boolean selection, retrieving certain apple kind.

# Performing One-way ANOVA
# We can now put the data to the test. We will be using the One-way ANOVA method to see if these apple types are different in weight:

# Perform One-way ANOVA
f_value, p_value = stats.f_oneway(apple1_weights, 
                                  apple2_weights, 
                                  apple3_weights)

# Print the F-value and P-value
print(f'F-value:\n {f_value:.3f}')  # 7.845
print(f'P-value: {p_value:.3f}')  # 0.006

# The f_oneway function from the Scipy stats module provides us with an F-value and a P-value. The P-value tells us whether the test results are significant.

# Interpretation
# Our One-way ANOVA test yielded two results - the F-value and the P-value. Let's understand how to interpret them.

# The F-value (7.85 in our case) is the ratio of the mean square difference between groups to the mean square difference within groups. It tells us how much the apple types differ in weight compared to how much the weights fluctuate within each apple type. A higher F-value suggests the differences in group weights are probably not from random chance.

# The P-value (0.0066 in our case) is well below the typical threshold of 0.05, indicating a statistically significant difference. This suggests that the likelihood of getting our observed data if all apple types had the same average weight is very low - only 0.66%.

# Given these results, we can confidently reject the idea that all apple types have the same average weight. The average weight of the apple types in our data is significantly different.
