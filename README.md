# Automation Script – File Organizer

## Project Overview
This Python automation script organizes files in a given directory based on their file types. It categorizes files into folders such as Documents, Images, Videos, or other extensions dynamically using file extensions. This project was developed as part of the internship at Infotact Solutions.

## Features
- Automatically scans and categorizes files
- Creates folders based on file types
- Handles duplicate filenames using timestamps
- Skips directories during scanning
- Logs all activities and errors to a log file
- Easy to use via terminal/command line

## Tech Stack
- Language: Python 3.x
- Modules Used: shutil, pathlib, datetime, logging

## How It Works
The File Organizer script scans the specified directory and identifies all files within it. For each file, it reads the file extension and dynamically creates a folder named after that extension (e.g., pdf, jpg, txt). It then moves each file into its respective folder, effectively organizing the contents of the directory. The script intelligently handles edge cases such as files with no extension, duplicate filenames (by appending a timestamp), and already existing folders. Throughout the process, it logs all file movements and any errors encountered to a file_organizer.log file, providing a reliable execution trace.

## How to Use
1. Clone or download this repository.
2. Open a terminal and run:
   python file_organizer.py
3. Enter the path of the directory you want to organize.
4. The script will automatically:
   - Create folders (based on extensions)
   - Move files into their respective folders
   - Log actions into file_organizer.log

## Team Contributions
- Member 1: Core logic, file classification
- Member 2: Logging, error handling
- Member 3: Documentation & User Guide
- Member 4: Testing, folder setup, review
