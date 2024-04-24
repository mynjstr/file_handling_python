#pseudocode
#create integers.txt
#list 20 integers
#open .txt file and separately read each line from the .txt file
with open("integers.txt", "r") as integers_file:
    for line in integers_file:
        line = line.strip()

#separate even and odd numbers extracted from the file
#if the number is even

        if int(line) % 2 == 0:
#Put each even integer into double.txt and square them.
            squared_even_numbers = int(line) ** 2

#open the "double.txt" file and write the squared even numbers extracted
            with open("double.txt", "a") as squared_even_file:
                squared_even_file.write(f'{squared_even_numbers}\n')

#if the number is odd
#Put each odd integer into triple.txt and cube them.
        else:
            cubed_odd_numbers = int(line) ** 3
#open the"triple.txt" file and write the cubed odd numbers extracted
            with open("triple.txt", "a") as cubed_odd_file:
                cubed_odd_file.write(f'{cubed_odd_numbers}\n')
