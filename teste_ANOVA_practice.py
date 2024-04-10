import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from scipy import stats


# Would you like to determine whether different varieties of apples actually vary in weight? The code below performs a One-way ANOVA test on the weights of Granny Smith, Fuji, and Honeycrisp apples to assess if observed differences are statistically significant. Simply press Run to evaluate the strength of the evidence against the hypothesis that all varieties share the same average weight.

# Predefined weights of three different apple varieties in grams
weights_granny_smith = [150, 152, 154, 149, 151]
weights_fuji = [160, 162, 159, 158, 161]
weights_honeycrisp = [165, 168, 167, 164, 166]

# Perform One-way ANOVA on the apple varieties
f_val, p_val = stats.f_oneway(weights_granny_smith, weights_fuji, weights_honeycrisp)
print(f"F-Value: {f_val:.2f}\n P-Value: {p_val:.2f}")

if p_val < 0.05:
    print('The weights of the apple varieties are significantly different. We reject the null hypothesis.')
else:
    print('The weights of the apple varieties are not significantly different. We fail to reject the null hypothesis.')

# Excellent, Star Seeker! In your next task, you are given three samples of different apple weights and an ANOVA test analysis for them. Run the code, and you will see that the p-value is greater than 0.1.

# Adjust the parameters of the np.random.normal() functions calls to make the p_value less than 0.05. Just try to recall the lesson and understand if the p_value < 0.05 means samples have the same means, or vice versa.

np.random.seed(1)

# Weights of three different types of apples measured in grams
weights_red_apples = np.random.normal(loc=100, scale=7, size=200)
weights_green_apples = np.random.normal(loc=101, scale=8, size=200)
weights_yellow_apples = np.random.normal(loc=99, scale=4, size=200)

# Conducting the one-way ANOVA test to see if there's a significant weight difference
f_stat, p_val = f_oneway(
    weights_red_apples,
    weights_green_apples,
    weights_yellow_apples
)

# Displaying the F-statistic and P-value
print("F-statistic:", round(f_stat, 2), "P-value:", round(p_val, 4))

# Galactic Pioneer, your journey through the ANOVA galaxy continues! Use your newfound knowledge to fill in the blanks and discover whether our apple varieties differ in weight. May your code be as precise as a laser beam!

# Example weights for 3 varieties of apples
fuji_weights = [150.2, 152.5, 151.3, 148.9, 149.6]
gala_weights = [140.1, 142.3, 141.2, 140.5, 139.9]
honeycrisp_weights = [160.4, 161.2, 162.0, 158.5, 159.7]

# TODO: Perform One-way ANOVA on the weights of the different apple varieties
f_statistic, p_value = f_oneway(
    fuji_weights,
    gala_weights,
    honeycrisp_weights
)

# Output: F-value and P-value
print("F-value:", round(f_statistic, 2), "P-value:", format(p_value, '.4f'))

if p_value < 0.05:
    print('The weights of the apple varieties are significantly different. We reject the null hypothesis.')
else:
    print('The weights of the apple varieties are not significantly different. We fail to reject the null hypothesis.')