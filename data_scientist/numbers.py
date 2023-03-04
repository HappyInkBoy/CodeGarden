# Create a file named data.txt in the current folder
# Fill up that file with integers from 0 to 1 million (1 per line)
# Go in the finder and open that file to confirm it is filled

f = open("data.txt", "x")
for i in range (1000000):
    f.write(str(i) + "\n")
f.close()
