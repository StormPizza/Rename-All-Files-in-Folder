# Rename-All-Files-in-Folder

[download](https://trello-attachments.s3.amazonaws.com/6091d5b4be0a898d713e6ca8/60bfd9c1392e1734bffc5ee0/c1bf2218de88a00ee58ff7161a414bb0/rename_file.py) 

What it does (Part 1 : Rename)
---------------- 
Run once to rename all files in target folder

      Example 1:
      Folder [home]      contains folder [Temp] & file [rename_file.py]
      Folder [home/Temp] contains file [Foo.jpeg]
      
      File   [Foo.jpeg] is renamed to [Temp_1.jpeg]
      
If folder contains a subfolder, all files inside subfolder will be renamed as well.
This is repeated for all contained folders.

      Example 2:
      Folder [home]            contains folder [Temp] & file [rename_file.py]
      Folder [home/Temp]       contains folder [SubTemp]
      Folder [home/Temp/SubTemp] contains file [Foo2.jpeg]
      
      File   [Foo2.jpeg] is renamed to [SubTemp_Temp_1.jpeg]
      
Naming convention : Deepest folder first, followed by enclosing folders, followed by number

What it does (Part 2 : Restore)
---------------- 
Run again to undo renaming and restore original names

When run the first time, it saves the original file names into a backup txt file called *Renaming_backup.txt*. 

NOTE: If backup text file is removed, script will assume that this is the first time it used, and will proceed to begin renaming

To use:
---------------- 

- Place python file in same directory as target folder (not inside it)
- Specify name of target folder by either:

      1) Edit the python script at default variable 'arg1'
            arg1 = 'target_folder'
      2) Run (from terminal) with target folder name as argument
            $ python rename_file.py target_folder


NOTE: Applying the script does NOT PRESERVE THE ORDER of the items in the folder, so if you already have names such as *file_1*, *file_2* etc.
the script may assign name *folder_1* to *file_2* instead of *file_1*.
However, restoring the original names will also return the original order of files in folder.

