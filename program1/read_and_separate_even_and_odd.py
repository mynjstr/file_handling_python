#pseudocode
#create numbers.txt
#list 20 integers
#open .txt file and separately read each line from the .txt file
with open("numbers.txt", "r") as integers_file:
    for line in integers_file:
        line = line.strip()

#separate even and odd numbers extracted from the file
#if the number is even
        if int(line) % 2 == 0:

#open the "even.txt" file and write the even numbers extracted
            with open("even.txt", "a") as even_file:
                even_file.write(f'{line}\n')

#if the number is odd
        else:
#open the"odd.txt" file and write the odd numbers extracted
            with open("odd.txt", "a") as odd_file:
                odd_file.write(f'{line}\n')
                