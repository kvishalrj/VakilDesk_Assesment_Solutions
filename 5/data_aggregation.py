from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    # Step 1: Grouping dictionaries by the provided key
    grouped_data = {}
    
    for entry in data:
        # Get the value of the provided key
        group_key = entry.get(key)
        
        # Initialize the list if the group_key is not already in the dictionary
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        
        # Append the dictionary to the corresponding group
        grouped_data[group_key].append(entry)
    
    # Step 2: Apply the aggregator function to the grouped data
    aggregated_result = {}
    
    for group_key, group_values in grouped_data.items():
        # Apply the aggregator function to the list of dictionaries in each group
        aggregated_result[group_key] = aggregator(group_values)
    
    return aggregated_result



# Example

from statistics import mean

data = [
    {'region': 'North', 'sales': 100},
    {'region': 'South', 'sales': 150},
    {'region': 'North', 'sales': 200},
    {'region': 'East', 'sales': 130},
    {'region': 'South', 'sales': 170},
    {'region': 'East', 'sales': 110},
]

# Aggregator function to calculate the total sales for each region
def total_sales(group):
    return sum(item['sales'] for item in group)

# Aggregator function to calculate the average sales for each region
def average_sales(group):
    return mean(item['sales'] for item in group)

# Example 1: Aggregate total sales by region
result_total = aggregate_data(data, key='region', aggregator=total_sales)
print(result_total)  # {'North': 300, 'South': 320, 'East': 240}

# Example 2: Aggregate average sales by region
result_avg = aggregate_data(data, key='region', aggregator=average_sales)
print(result_avg)  # {'North': 150, 'South': 160, 'East': 120}
