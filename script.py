def write_name_to_file(name):
    try:
        with open('output.txt', 'w') as file:
            file.write(f'Name: {name}')
        print('File written successfully.')
    except Exception as e:
        print(f'Error writing to file: {e}')

# Example usage:
your_name = 'Your Name'
write_name_to_file(your_name)
