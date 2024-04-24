#pseudocode
#write many lines of content into a text file named mylife.txt
#continue requesting additional lines until the person rejects
resume = True
while resume:

#Ask for the user's input
    input_line = ("Enter line: ")

#Insert a newline character at the line's end.
    input_line_break = input_line + ("\n")

#Open mylife.txt file in append mode
    with open("mylife.txt", "a") as mylife_file:
        mylife_file.write(input_line)
        
#inquire the user as to whether additional lines are needed.
        while resume:
                extra = input("Are there more lines y/n? ")

#Break the inner loop if the user wishes to add additional lines
                if extra.lower() == "y":
                    break

#When the user is finished, break both loops and print a message
                elif again.lower() == "n":
                    print ("You're Done Let's gooooo")
                    resume = False 

#Produce a message indicating that the user's input is incorrect
