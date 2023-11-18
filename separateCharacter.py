import argparse

def separateCharacter(input_path, output_path):
    # Open the input file for reading
    with open(input_path, 'r') as input_file:
        # Open a new file for writing the filtered content
        with open(output_path, 'w') as output_file:
            # Read and process each line in the input file
            for line in input_file:
                if line == '\n':
                    continue
                # Change whitespace to underscore
                line_with_underscore = line.replace(' ', '_')
                # Separacter characters with whitespace
                output_line = ' '.join(line_with_underscore) + '\n'
                # Write line to file
                output_file.write(output_line)

def main():
    parser = argparse.ArgumentParser(description='Separate characters in file and modify whitespace to underscore')
    parser.add_argument('input_path', help='Path of file that needs to be processed')
    parser.add_argument('output_path', help='Path of file after processed')

    args = parser.parse_args()
    separateCharacter(args.input_path, args.output_path)
    
if __name__ == "__main__":
    main()