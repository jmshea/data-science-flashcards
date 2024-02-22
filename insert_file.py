#!/usr/bin/env python
import argparse

def insert_file_before_string(input_file, insert_file, insert_string, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    found = False
    output_lines = []
    for line in lines:
        if insert_string in line and not found:
            with open(insert_file, 'r') as ins_f:
                insert_content = ins_f.read()
            output_lines.append(insert_content)
            found = True
        output_lines.append(line)

    if not found:
        print(f"String '{insert_string}' not found in the input file.")
        return

    with open(output_file, 'w') as f:
        f.writelines(output_lines)

def main():
    parser = argparse.ArgumentParser(description='Insert content of one file into another before a line containing a specified string.')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('insert_file', help='Path to the file whose content will be inserted')
    parser.add_argument('insert_string', help='String contained in the line before which the content will be inserted')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    insert_file_before_string(args.input_file, args.insert_file, args.insert_string, args.output_file)
    print(f"Content of {args.insert_file} inserted into {args.input_file} before the line containing '{args.insert_string}'. Result saved to {args.output_file}.")

if __name__ == '__main__':
    main()
