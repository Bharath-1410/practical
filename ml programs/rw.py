sread = 0
swrite = 0
r = 0

print("reader writer")

while True:
    print("\nmenu")
    print("\t 1.read from file")
    print("\n \t 2.write to file")
    print("\n \t 3.exit the reader")
    print("\n \t 3.exit the writer")
    print("\n \t 5.exit")
    
    ch = int(input("enter your choice: "))
    
    if ch ==1:
        if swrite ==0:
            sread = 1
            r = r + 1
            print("\nReader", r, "reads")
        else:
            print("\n Not possible")
            
    elif ch == 2:
        if sread == 0 and swrite ==0:
            swrite = 1
            print("\nWriter in progress")
        elif swrite == 1 :
            print("\nWriter writes the files")
        elif sread == 1 :
            print("\n cannot write while reader reads file")
        else:
            print("\ncannot write file")
    
    elif ch == 3:
        if r != 0:
            print("\nThe reader", r, "closes the file")
            r -= 1
        elif r == 0:
            print("\n currently no reader access available")
            sread = 0
        elif r == 1:
            print("\nonly 1 reader file")
        else:
            print(r, "readers are reading the file")
    elif ch == 4:
        if swrite == 1:
            print("\nwriter closes the file")
            swrite = 0
        else:
            print("\nthere is no writer in the file")
            
    elif ch == 5:
        break
            