def calculate_positive_feedback(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100
ratings = []
print("Enter customer ratings")
while True:
    rating = input("Enter a rating: ").strip()
    if rating.lower() == "done":
        break
    if rating.isdigit() and 1 <= int(rating) <= 5:
        ratings.append(int(rating))
    else:
        print("Please enter a valid rating between 1 and 5.")
if ratings:
    positive_percentage = calculate_positive_feedback(ratings)
    print(f"\nPositive Feedback: {positive_percentage:.2f}%")
else:
    print("\nNo ratings provided.")
