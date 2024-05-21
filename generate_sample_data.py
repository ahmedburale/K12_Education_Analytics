import pandas as pd
import numpy as np
from faker import Faker
import os

# Create directory if it does not exist
output_dir = 'K12_Education_Analytics'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

fake = Faker()
np.random.seed(42)

# Generate synthetic data
num_samples = 10000

data = {
    'Student_ID': [fake.uuid4() for _ in range(num_samples)],
    'Gender': np.random.choice(['Male', 'Female'], num_samples, p=[0.48, 0.52]),
    'DOB': [fake.date_of_birth(minimum_age=5, maximum_age=18) for _ in range(num_samples)],
    'Grade': np.random.choice([str(i) for i in range(1, 13)], num_samples, p=[1/12]*12),
    'Attendance': np.random.uniform(75, 100, num_samples).round(1),  # Attendance percentage
    'Math_Score': np.random.uniform(50, 100, num_samples).round(1),
    'Reading_Score': np.random.uniform(50, 100, num_samples).round(1),
    'Science_Score': np.random.uniform(50, 100, num_samples).round(1),
}

df = pd.DataFrame(data)

# Save to CSV
output_path = os.path.join(output_dir, 'sample_k12_data.csv')
df.to_csv(output_path, index=False)
print(f"Sample dataset generated and saved to '{output_path}'.")

#%%
