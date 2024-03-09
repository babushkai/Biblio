# Greedy Algorithms

## Explanation

Greedy algorithms are a type of algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. Greedy algorithms are used when a problem guarantees an optimal solution through local optimizations.

## Example Problems

- **Activity Selection:** Select the maximum number of activities that do not overlap.
- **Coin Change:** Find the minimum number of coins that make a given value, assuming an unlimited supply of coins of given denominations.

## Time Complexity

- The time complexity of greedy algorithms can vary depending on the problem and the sorting requirements of the input data, but it's often O(n log n) due to sorting.

## Space Complexity

- The space complexity of greedy algorithms is generally O(1) or O(n), depending on whether extra space is needed for sorting or storing intermediate values.

## Implementation

```python
# Python implementation for Activity Selection Problem (Greedy)

def activity_selection(activities):
    # Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    # The first activity always gets selected
    last_selected_activity = activities[0]
    selected_activities = [last_selected_activity]

    for current in activities[1:]:
        # If current activity does not overlap with last selected, add it to the list
        if current[0] >= last_selected_activity[1]:
            selected_activities.append(current)
            last_selected_activity = current
    
    return selected_activities

**Python Code Implementation (`activity_selection.py`):**

```python
def activity_selection(activities):
    # Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    # The first activity always gets selected
    last_selected_activity = activities[0]
    selected_activities = [last_selected_activity]

    for current in activities[1:]:
        # If current activity does not overlap with last selected, add it to the list
        if current[0] >= last_selected_activity[1]:
            selected_activities.append(current)
            last_selected_activity = current
    
    return selected_activities

# Example usage:
if __name__ == "__main__":
    activities = [(0, 6), (3, 4), (1, 2), (5, 7), (8, 9), (5, 9)]
    print("Selected activities:", activity_selection(activities))
