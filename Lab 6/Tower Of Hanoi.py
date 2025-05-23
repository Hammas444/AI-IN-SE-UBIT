def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Disk 1 moved from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Disk {n} moved from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example: 3 disks
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')






