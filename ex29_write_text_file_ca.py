'''
ex29_write_text_



'''

def convert_to_uppercase(text):
    new_text = ' '
    for line in text:
        new_text += line.upper() + '\n' # '\' = newline
    return new_text

def write_text_to_file(file_out, msg):
    with open(file_out, 'w') as file_out: # w write to file)
        file_out.write(msg)



def main():
    try:
        file_in = 'ex29_lowercase.txt'
        with open(file_in, 'r') as file_in:
            all_lines = file_in.readlines()
    except FileNotFoundError:
        print(f'The File {file_in} was not found')
        input('press enter to close the program.')
        exit(0)




    msg = convert_to_uppercase(all_lines)
    #print(msg)
    # write text back to a new file

    file_out = "ex29_uppercase.txt"
    write_text_to_file(file_out, msg)

    print (f'New text written to file{file_out}.')




if __name__== "__main__":
    main()