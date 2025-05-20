Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Basic Statistics in Python
>>> 
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from statistics import mode
>>> 
>>> # Sample dataset - student scores
>>> scores = [65, 70, 85, 90, 75, 85, 95, 80, 90, 70]
>>> 
>>> # Convert to Pandas Series
>>> data = pd.Series(scores)
>>> 
>>> print("Data:", scores)
Data: [65, 70, 85, 90, 75, 85, 95, 80, 90, 70]
>>> print("Mean:", data.mean())
Mean: 80.5
>>> print("Median:", data.median())
Median: 82.5
>>> print("Mode:", mode(scores))
Mode: 70
>>> print("Standard Deviation:", data.std())
Standard Deviation: 10.124228365658293
>>> print("Variance:", data.var())
Variance: 102.5
>>> 
>>> # Visualization
>>> plt.figure(figsize=(8, 4))
<Figure size 800x400 with 0 Axes>
>>> sns.histplot(scores, bins=5, kde=True)
<Axes: ylabel='Count'>
>>> plt.title("Distribution of Student Scores")
Text(0.5, 1.0, 'Distribution of Student Scores')
>>> plt.xlabel("Scores")
Text(0.5, 0, 'Scores')
>>> plt.ylabel("Frequency")
Text(0, 0.5, 'Frequency')
>>> plt.show()
