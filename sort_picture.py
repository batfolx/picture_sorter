import os
import datetime
from shutil import copyfile

# allowed extensions to copy and sort
extensions = ['png', 'jpg', 'jpeg', 'mov']

# the output directory of where you want the data
output_dir = 'pictures'


def sort_pictures(dirname: str) -> bool:
    """
    Goes through and looks for pictures (jpgs, pngs) and sorts them
    :param dirname: the directory name to walk through; the directory that contains the pictures
    :return: true if successful, false otherwise
    """

    if not os.path.exists(dirname):
        print(f"{dirname} does not exist. Exiting...")
        return False

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for root, dirs, files in os.walk(dirname):

        # for each file it finds, iterate over it
        for file in files:

            # print(f'file: {root}/{file}')
            # get the absolute path and see if it is a picture
            absolute_path = f'{root}/{file}'
            stop = True

            file_ext = ''

            for ext in extensions:
                if absolute_path.lower().endswith(ext):
                    stop = False
                    file_ext = ext
                    break

            if stop:
                print('stop is true')
                continue

            info = os.stat(absolute_path)

            time_created = info.st_mtime

            time_stamp = datetime.datetime.fromtimestamp(time_created)
            #print(f'time created: {time_created} and time stamp: {time_stamp}')

            month = time_stamp.month
            day = time_stamp.day
            year = time_stamp.year
            seconds = time_stamp.second
            microseconds = time_stamp.microsecond

            month = time_stamp.strftime("%b")

            #print(f'month: {month}, day: {day}, year: {year}, seconds: {seconds}')
            pic_dirname = f'{output_dir}/{year}/{month}'

            if not os.path.exists(f'{output_dir}/{year}'):
                os.mkdir(f'{output_dir}/{year}')

            if not os.path.exists(pic_dirname):
                os.mkdir(pic_dirname)

            filename = f'{pic_dirname}/{year}_{month}_{day}_{seconds:02}.{file_ext}'
            copyfile(absolute_path, filename)

    return True




sort_pictures("data")

