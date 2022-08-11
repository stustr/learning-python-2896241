import os


def main():
    
    total_size = 0
    
    # list all files in ch3 directory
    all_list = os.listdir()
    for i in all_list:
        if os.path.isfile(i):
            size = os.path.getsize(i)
            total_size += size

    # make new directory
    os.mkdir("results")
    
    # create a new file to write into
    f = open("results/results.txt", "w+")
    f.write("Total size = " + str(total_size) + "\n\n")
    for i in all_list:
        f.write(i + "\n")
        

if __name__ == "__main__":
    main()