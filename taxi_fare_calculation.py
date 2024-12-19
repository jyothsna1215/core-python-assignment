def calculate_fare(distance):
    return 50 + (10 * distance)
distances = []
print("Enter trip distances in kilometers:")
while True:
    distance = input("Enter distance: ").strip()
    if distance.lower() == "done":
        break
    if distance.replace('.', '', 1).isdigit():
        distances.append(float(distance))
    else:
        print("Please enter a valid number.")
if distances:
    total_fare = sum(calculate_fare(d) for d in distances)
    print(f"\nTotal fare for {len(distances)} trips: ${total_fare:.2f}")
else:
    print("\nNo trips entered.")
