def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Example usage:
marks = [80, 90, 85, 75, 95]
total, avg = sum_avg(marks)
print("Total:", total, "Average:", avg)
