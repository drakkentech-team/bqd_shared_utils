from os import getcwd, path
from glob import glob


def collate_logfiles(target_directory: str = None, output_filename: str = None):
    target_directory = target_directory or path.join(getcwd(), 'Logfiles')
    output_filename = output_filename or 'combined_logfile.log'

    # Get list of all files only in the given directory
    file_list = filter(path.isfile, glob(target_directory + '/' + '*'))
    # Sort list of files based on last modification time in ascending order
    file_list = sorted(file_list, key=path.getmtime)

    target = open(path.join(target_directory, output_filename), 'w')
    count = 0
    for file in file_list:
        if output_filename in file or 'collate_logfiles' in file:
            pass
        with open(path.join(target_directory, file), 'r') as source:
            for line in source.readlines():
                target.write(line)
            count += 1
    print(f'combined {count} files into {output_filename}')
    target.close()


if __name__ == '__main__':
    collate_logfiles('c:/temp/test_combine')
