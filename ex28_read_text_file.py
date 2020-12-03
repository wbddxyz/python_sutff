'''
Colin Anderson
03/11/20
Reading data from text file
'''





def main():
    

    # open file for reading
    file_in = open("scores.txt", "r")

    scores = []
    for line in file_in:
        # remove the newline character and convert to integer
        scores.append((int)(line.strip()))
    #close file after reading the lines
    file_in.close()

    for x in scores:
        print(x)

        # min' maz, avg




if __name__ == "__main__":
    main()