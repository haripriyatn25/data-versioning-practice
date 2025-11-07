"""
data_analysis.py
Simple Python script to demonstrate version control.
"""

import pandas as pd

# Sample dataset
data = {
    "Name": ["Asha", "Ravi", "Kiran", "Meena"],
    "Score": [88, 92, 79, 95]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

print("\nAverage Score:", df["Score"].mean())
