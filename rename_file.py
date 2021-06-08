import os
# path = '/Users/myName/Desktop/directory'
import sys

# CHANGE THIS TO YOUR FOLDER NAME ####################
arg1 = 'GDice'  # default name of the FOLDER to apply to
######################################################

backup_file_name = 'Renaming_backup.txt'  # name of the BACKUP txt
backup_delimiter = '===='  # when writing backup, this goes between oldName and newName


# takes list of path and returns either
# not reverse : path name ( "home/GDice/folder" )
# reverse : file name ( "folder_GDice_home" )
def get_pathname(path_list, delimiter, reverse=False):
    path2 = ''
    for name in path_list:
        if reverse:
            path2 = name + delimiter + path2
        else:
            path2 = path2 + name + delimiter
    return path2


def rename(folder_to_affect):

    def rename_recursive(path_list, folder_name, backup_file):
        path_list_2 = list(path_list)
        path_list_2.append(folder_name)

        path = get_pathname(path_list_2, '/')
        path_name_to_add = get_pathname(path_list_2, '_', True)

        layer_file_count = 0
        files = os.listdir(path)
        for index, file in enumerate(files):
            # IGNORE BACKUP, this prevents changing the backup file's name
            if file == backup_file_name:
                continue
            if os.path.isdir(os.path.join(path, file)):
                # for FOLDERS, go into folder and change all names
                rename_recursive(path_list_2, file, backup_file)
            else:
                # get NEW NAME for item (with number counter)
                pic_name = str(path_name_to_add) + str(layer_file_count)
                layer_file_count += 1
                file_format = file[file.rfind('.'):]  # .jpg
                old_name = os.path.join(path, file)
                new_name = os.path.join(path, ''.join([pic_name, file_format]))
                # RENAME the file
                os.rename(old_name, new_name)
                # write to BACKUP = "oldName.jpg====newName.jpg"
                backup_file.write(str(old_name + backup_delimiter + new_name) + '\n')

    backup_file2 = open(os.path.join(folder_to_affect, backup_file_name), "w")
    rename_recursive([], folder_to_affect, backup_file2)
    backup_file2.close()


def undo(folder_name):
    # get the data from backup
    with open(folder_name + '/' + str(backup_file_name)) as f:
        my_list = f.read().splitlines()

    # follow the orders from the backup and return the files names
    for line in my_list:
        # from line entry, get index of the second part ( "oldName.jpg====newName.jpg" )
        index_after_delimiter = line.find(backup_delimiter) + len(backup_delimiter)
        backup_name = line[:index_after_delimiter - len(backup_delimiter)]
        current_name_name = line[index_after_delimiter:]
        # if file is missing, skip
        if os.path.isfile(current_name_name):
            os.rename(current_name_name, backup_name)
    # clear the file
    backup_file2 = open(os.path.join(folder_name, backup_file_name), "w")
    backup_file2.close()


def main():
    global arg1
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    if os.path.isfile(arg1):
        pass
    if os.path.isfile(arg1 + '/' + str(backup_file_name)):
        with open(arg1 + '/' + str(backup_file_name)) as f:
            my_list = f.read().splitlines()
        if my_list:
            undo(arg1)
            return
    rename(arg1)


if __name__ == '__main__':
    main()


# rename('Green Dice')
# undo_renaming('Green Dice')

# backup_file2.write(end_name + '\n')
# layer_file_count = 0
# layer_count -= 1

# rename_recursive([], path_zzz)
# rename_recursive(['Green Dice'], 'test_vid11')
# rename_recursive('Pictures/test/Done', 'Green Dice')

# def test_1():
#     a = 111
#     layer_file_count = 0
#
#     def test_2():
#         print(a)
#         print(layer_file_count)
#         # layer_file_count = 1
#
#         print(layer_file_count)
#     test_2()
#
#
# test_1()

# rename_for_folder_1('Green Dice', 'test_vid11')
# rename_for_folder_1('Green Dice', 'test_vid16')
# rename_for_folder_1('Green Dice', 'test_vid19')
# rename_for_folder_1('Green Dice', 'test_vid22')
# rename_for_folder_1('Green Dice', 'test_vid25')
# rename_for_folder_1('Green Dice', 'test_vid28')

# rename_for_folder_1('Black_Dice', 'black 3 (vid3)')
# rename_for_folder_1('Black_Dice', 'black 5 (vid4)')
# rename_for_folder_1('Black_Dice', 'yellow 1 (vid6)')

# for index, file in enumerate(files):
#     if os.path.isdir(file):
#         rename_recursive(path_list_2, file)
#
#     else:
#         pic_name = str(path_name_to_add) + str(index)
#         os.rename(os.path.join(path, file),  os.path.join(path, ''.join([pic_name, '.jpg'])))
#         add_to_backup(backup_file, os.path.join(path, file), has_done)
#         has_done = True
#         # backup_file.write(layer_file_name + str(layer_count) + '\n')
#         # layer_file_count += 1

# backup_file_name = 'copy.txt'
# file1 = open(str(backup_file_name), "w")
# file1.write("Your text goes here\n")
# file1.write("Your text goes here")
# file1.write("Your text goes here")
# file1.close()

# path = 'Pictures/test/Done/' + folder_0 + '/' + folder_1 + '/' + folder_2
# path2 = path + '/' + folder_name
# global layer_count
# global layer_file_count

# backup_file.write(layer_name + str(layer_count) + '\n')
# backup_file.write(folder_name + str(layer_count) + '\n')
# backup_file.write(folder_name + '\n')
# layer_count += 1
# layer_file_count = 0


# # separate Directories and Items, then do Items first
# dir_set, item_set = get_dir_and_items(path)
#
# count = 0
# if len(item_set):
#     for item in item_set:
#         pic_name = str(path_name_to_add) + str(count)
#         count += 1
#         file_format = item[item.rfind('.') :]  # .jpg
#         old_name = os.path.join(path, item)
#         new_name = os.path.join(path, ''.join([pic_name, file_format]))
#         os.rename(old_name, new_name)
#         # add_to_backup(backup_file, os.path.join(path, item), has_done)
#         together_name = old_name + backup_delimiter + new_name
#         backup_file.write(str(together_name) + '\n')
#
# for directory in dir_set:
#     rename_recursive(path_list_2, directory, backup_file)


# def rename_for_folder_2(folder_0, folder_1, folder_2):
#     path = 'Pictures/test/Done/' + folder_0 + '/' + folder_1 + '/' + folder_2
#     files = os.listdir(path)
#     foo = 1
#     for index, file in enumerate(files):
#         # foo = foo + 1
#         pic_name = str(folder_1) + "_" + str(folder_2) + "_" + str(index)
#         os.rename(os.path.join(path, file),  os.path.join(path, ''.join([pic_name, '.jpg'])))
#
#
# def rename_for_folder_1(folder_0, folder_1):
#     dice_face = 7 * ['']
#     dice_face[0] = 'Nothing'
#     dice_face[1] = '1_one'
#     dice_face[2] = '2_Two'
#     dice_face[3] = '3_Three'
#     dice_face[4] = '4_Four'
#     dice_face[5] = '5_Five'
#     dice_face[6] = '6_Six'
#
#     for i in dice_face:
#         rename_for_folder_2(folder_0, folder_1, i)
#
#
