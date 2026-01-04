## Smart File Organizer

# Description:
  >> Organizes files into categories based on file types
  >> Duplicate detection
  >> Customizable rules

# Key Features:
  1. Multiple organization methods (file type, date, or extension)
  2. Duplicate detection (Uses MD5 hashing to identify duplicates files)
  3. Dry run mode (Preview changes before actually moving the files)
  4. Conflict handling (Automatically renames files if file name already exists)
  5. Detailed logging (Shows progress and summary statistics)

# File Categories:
  - Images
  - Documents
  - Videos
  - Audio
  - Archives
  - Code
  - Executables
  - Others

# How to use:
  1. Change **SOURCE_DIRECTORY** to your target folder path
  2. Choose organization method 
     - type
     - date
     - extension
  3. Run the script - it will first show a dry run
  4. Uncomment the confirmation section to actually organize the files