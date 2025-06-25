import pandas as pd

# Step 1: Create a small DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['Vancouver', 'Toronto', 'Vancouver', 'Calgary', 'Toronto']
}
df = pd.DataFrame(data)

# Step 2: Show the DataFrame
print("Original DataFrame:")
print(df)

# Step 3: Filter rows where City is Vancouver
vancouver_residents = df[df['City'] == 'Vancouver']

print("\nFiltered: People from Vancouver:")
print(vancouver_residents)

# Step 4: Calculate average age
average_age = df['Age'].mean()
print(f"\nAverage Age: {average_age:.2f}")