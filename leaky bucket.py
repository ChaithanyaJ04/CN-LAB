print("--- Leaky Bucket Simulation ---")
capacity = int(input("Enter Bucket Capacity: "))
output_rate = int(input("Enter Sending Rate: "))
n = int(input("Enter Number of Clock Cycles: "))

# Taking incoming packet sizes
a = []
for i in range(n):
    packet = int(input(f"Enter packet size for cycle {i+1}: "))
    a.append(packet)

bucket = 0

# Displaying table header
print(f"\n{'i':<5} | {'a[i]':<6} | {'Accept by Bucket':<16} | {'Sent':<6} | {'Remaining':<10}")
print("-" * 55)

for i in range(n):
    # Check if the incoming packet can fit in the available space
    if bucket + a[i] <= capacity:
        bucket += a[i]
        accepted = str(a[i])
    else:
        accepted = "Dropped"
        
    # Send packets at the fixed output rate
    sent = min(bucket, output_rate)
    bucket -= sent
    
    # Display table row
    print(f"{i+1:<5} | {a[i]:<6} | {accepted:<16} | {sent:<6} | {bucket:<10}")