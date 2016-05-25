# -*- coding: utf-8 -*-

"""
Catalog multiple drives.

As one accumulates multiple drives, hard and flash, containing,
thousands even millions of files, it becomes useful to have a text file
containing an alphabetized catalog list of all files and their locations 
by drive and directory.

The list can be searched by eye or by an editor to locate particular
files.

The list can also be loaded into a script to be filtered 
programmatically as desired.
"""
__author__ = "Jack Trainor"
__date__ = "2016-03-10"

import sys
import os

########################################################################
class FileSpec(object):
    def __init__(self, path, drive_name=""):
        self.drive, self.path_minus_drive = os.path.splitdrive(path)
        self.dir, self.name = os.path.split(path)
        self.corename, self.ext = os.path.splitext(self.name)
        self.ext = self.ext.lower()
        self.dir_minus_drive = self.dir[2:]       
        self.drive_name = drive_name    
        
class CatalogEntry(object):
    def __init__(self, name, drive_name, dir_minus_drive):
        self.name = name
        self.drive_name = drive_name
        self.dir_minus_drive = dir_minus_drive
        
class Affichage(object):
    def __init__(self, choix, readme):
        self.choix = choix
        self.readme = readme
            
########################################################################
def read_file(path):
    bytes_ = ""
    try:
        f = open(path, 'rb')
        bytes_ = f.read()
        f.close()
    except Exception as e:
        sys.stderr.write('read_file failed: %s [%s]\n' % (path, e))  
    return bytes_     

def write_file(path, bytes_, simulated=True):
    try:
        if not simulated:
            f = open(path, 'wb')
            f.write(bytes(bytes_,'UTF-8'))
            f.close()
    except Exception as e:  
        sys.stderr.write('write_file: %s [%s]\n' % (path, e))  

def println(line):
    sys.stdout.write(line + "\n")

########################################################################
def get_files_in_dir(dir_, affichage, onelevel=False):
    paths = []
    for root, dirs, filenames in os.walk(dir_):
        for name in filenames:
            # print (os.path.dirname(os.path.abspath(root)))
            # Enlever le répertoire .git du catalogue.
            if ('.git' in os.path.dirname(os.path.abspath(root))) == True or ('.COMMIT_EDITMSG' in name) == True:
                break
            # Afficher ou non README.md
            elif affichage.readme == 'n' and ('README.md' in name) == True:
                break
            else:
                path = os.path.join(root, name)
                paths.append(path)
        if onelevel:
            break
    return paths
    

########################################################################
def entry_to_line(entry, affichage): 
    if affichage.choix == 1:
        line = "{} {} {}".format(entry.name.ljust(75), entry.drive_name.ljust(15), entry.dir_minus_drive)
        return line
    elif affichage.choix == 2:
        line = "{} {} {}".format(entry.drive_name.ljust(15), entry.dir_minus_drive.ljust(160), entry.name)
        return line

def line_to_entry(line):
    items = line.split(b"\t")
    if len(items) == 3:
        return CatalogEntry(items[0], items[1], items[2])
    return None
    
def path_to_entry(path, drive_name):
    spec = FileSpec(path, drive_name)
    entry = CatalogEntry(spec.name, spec.drive_name, spec.dir_minus_drive)
    return entry
    
def paths_to_entries(paths, drive_name):
    entries = []
    for path in paths:
        spec = FileSpec(path, drive_name)
        entry = CatalogEntry(spec.name, spec.drive_name, spec.dir_minus_drive)
        entries.append(entry)    
    return entries

########################################################################  
def read_catalog_file_entries(catalog_path):
    println("read_catalog_file_entries %s" % catalog_path)
    entries = []
    text = read_file(catalog_path)
    lines = text.splitlines()
    for line in lines:
        entry = line_to_entry(line)
        if entry:
            entries.append(entry)
    return entries
        
def write_catalog_file_entries(catalog_path, entries, affichage):
    println("write_catalog_file_entries %s" % catalog_path)
    lines = []
    for entry in entries:
        line = entry_to_line(entry, affichage)
        if line:
            lines.append(line)
    lines = sorted(lines, key=lambda s: s.lower())
    nom, drive, dir = 'Programmes', 'Disques', 'Répertoires'
    if affichage.choix == 1:
        text = "{} {} {}".format(nom.ljust(75), drive.ljust(15), dir) +"\n"+ "\n".join(lines)
        write_file(catalog_path, text, False)
    elif affichage.choix == 2:
        text = "{} {} {}".format(drive.ljust(15), dir.ljust(160), nom) +"\n"+ "\n".join(lines)
        write_file(catalog_path, text, False)
        
########################################################################  
def write_drive_catalog_file(drive_path, drive_name, catalog_path, affichage):
    println("write_drive_catalog_file %s -> %s" % (drive_path, catalog_path))
    file_paths = get_files_in_dir(drive_path, affichage)   
    entries = paths_to_entries(file_paths, drive_name)   
    write_catalog_file_entries(catalog_path, entries, affichage)

def write_master_catalog_file(catalog_paths, master_catalog_path, affichage):
    println("write_master_catalog_file %s" % master_catalog_path)
    master_entries = []
    for catalog_path in catalog_paths:
        entries = read_catalog_file_entries(catalog_path)
        master_entries += entries
    write_catalog_file_entries(master_catalog_path, master_entries)
    
########################################################################
def sample():
    """ Sample calls for drives located on J and K drives. """
    affichage = Affichage(int(input('Affichage du catalogue: [1] --> Programmes, Disques, Répertoires \n\t\t\t[2] --> Disques, Répertoires, Programmes \n ')), input('Afficher les fichiers README.md: [Yes/No]'))
    if (affichage.readme == 'No' or affichage.readme == 'no' or affichage.readme == 'N' or affichage.readme == 'n'):
        affichage.readme = 'n'
    # write_drive_catalog_file("j:\\", "SANSA2_1G", r"c:\SANSA2_1G.txt", affichage)
    write_drive_catalog_file("C:\Python35", "Python35", r"C:\Python35\Environnement Python\Python3_catalog.txt", affichage)
    # write_master_catalog_file([r"C:\Python35\Python35drive.txt"], r"C:\Python35\Python35master.txt", affichage)
    entries = read_catalog_file_entries(r"C:\Python35\Environnement Python\Python3_catalog.txt")
    for entry in entries:
        println(entry_to_line(entry, affichage))

if __name__ == "__main__":
    print (__file__)
    sample()
    println("Complete.")

os.system("pause")