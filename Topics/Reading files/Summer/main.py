#  write your code here 
file = open("C:/Users/jm032/Desktop/Rock-Paper-Scissors (Python)/Topics/Reading files/Summer/data/dataset/input.txt", "r")
count = 0
for line in file:
    if line.strip().lower() == "summer":
        count += 1

file.close()

print(count)

