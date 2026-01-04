#!/usr/bin/env python3
import os                        # For interacting with the operating system (file operations, path manipulations, etc.)
import shutil                    # For high-level file operations (copying, moving files, etc.)
from pathlib import Path         # For object-oriented filesystem paths (cross-platform, easier path manipulations, etc.)
from datetime import datetime    # For handling date and time (file timestamps, organizing by date, etc.)
import hashlib                   # For hashing files (to identify duplicates, integrity checks, etc.)
from FileCategories import file_categories  # Custom module for file category definitions

# Main class for Smart File Organizer
class SmartFileOrganizer:
    # Initialize the organizer with source directory and organization criteria
    def __init__(self, source_dir, organize_by="type"):
        self.source_dir = Path(source_dir)
        self.organize_by = organize_by
        self.file_categories = file_categories
    
    
    def get_file_hash(self, file_path):
        """Generate a hash for a file to identify duplicates."""
        hash_md5 = hashlib.md5() # Initialize MD5 hash object
        try:
            with open(file_path, "rb") as f: # Open file in binary read mode
                for chunk in iter(lambda: f.read(4096), b""): # Read file in chunks (to handle large files, avoid memory issues, etc.)
                    hash_md5.update(chunk) # Update hash with each chunk 
            return hash_md5.hexdigest() # Return the hexadecimal digest of the hash
        except Exception as e:
            print(f"Error hashing file {file_path}: {e}")
            return None
        

    def get_category(self, file_extension):
        """Determine the category of a file based on its extension."""
        for category, extensions in self.file_categories.items(): # Iterate through defined categories and their extensions
            if file_extension.lower() in extensions: # Check if the file extension matches any in the current category
                return category
        return 'Others'
    
    
    def get_destination_folder(self, file_path):
        """Determine the destination folder based on organization criteria."""
        if self.organize_by == "type":
            category = self.get_category(file_path.suffix) # Get category based on file extension
            return self.source_dir / category # Return path to category folder
        elif self.organize_by == "date":
            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime) # Get file modification time
            date_folder = mod_time.strftime("%Y-%m") # Format date as "YYYY-MM"
            return self.source_dir / date_folder # Return path to date folder
        else:
            return self.source_dir / 'Others' # Default to 'Others' folder if criteria is unknown
        
    def organize_files(self, remove_duplicates=True, dry_run=False):
        """
            
        Organize files in the source directory based on the specified criteria.

        Args:
            remove_duplicates (bool): Whether to remove duplicate files based on content hash.
            dry_run (bool): If True, simulate the organization without making actual changes.       
        """

        if not self.source_dir.is_dir(): # Check if the source directory exists and is a directory
            print(f"Source directory {self.source_dir} does not exist or is not a directory.")
            return
        
        files_moved = 0
        duplicates_found = 0
        files_skipped = 0
        seen_hashes = {} # Dictionary to track seen file hashes for duplicate detection

        print(f"\n{'🔍 DRY RUN MODE - No files will be moved' if dry_run else '📁 Starting file organization...'}")
        print(f"Source: {self.source_dir}")
        print(f"Organization method: {self.organize_by}\n")

        files = [f for f in self.source_dir.iterdir() if f.is_file()] # List all files in the source directory

        for file_path in files:
            try:
                if file_path.name.startswith('.'): # Skip hidden files
                    files_skipped += 1
                    continue

                if remove_duplicates:
                    file_hash = self.get_file_hash(file_path) # Generate hash for the current file
                    if file_hash:
                        if file_hash in seen_hashes: # Check if this hash has been seen before
                            duplicates_found += 1
                            print(f"Duplicate found: {file_path} (duplicate of {seen_hashes[file_hash]})")
                            if not dry_run:
                                file_path.unlink() # Remove duplicate file
                            continue
                        else:
                            seen_hashes[file_hash] = file_path # Record this hash as seen

                dest_folder_name = self.get_destination_folder(file_path)  # Determine destination folder based on organization criteria
                dest_folder = self.source_dir / dest_folder_name # Full path to destination folder
                dest_path = dest_folder / file_path.name # Full path to destination file

                counter = 1
                while dest_path.exists(): # Handle naming conflicts by appending a counter
                    name_stem = file_path.stem
                    dest_name = dest_folder / f"{name_stem}_({counter}){file_path.suffix}"
                    counter += 1

                if not dry_run:
                    dest_folder.mkdir(parents=True, exist_ok=True) # Create destination folder if it doesn't exist
                    shutil.move(str(file_path), str(dest_path)) # Move file to destination

                files_moved += 1
                print(f"✓ {'Would move' if dry_run else 'Moved'}: {file_path.name} → {dest_folder_name}/")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                files_skipped += 1

        
        # Summary
        print(f"\n{'=' * 50}")   # Print a separator line 
        print(f"   Summary:")
        print(f"   Files {'to be moved' if dry_run else 'moved'}: {files_moved}")
        print(f"   Duplicates found: {duplicates_found}")
        print(f"   Files skipped: {files_skipped}")
        print(f"{'=' * 50}\n")

import sys

if __name__ == "__main__":

    SOURCE_DIRECTORY = sys.argv[1] if len(sys.argv) > 1 else "." # Default to current directory if no argument provided
    ORGANIZE_METHOD = "type"

    organizer = SmartFileOrganizer(SOURCE_DIRECTORY, ORGANIZE_METHOD)

    print("Running in DRY RUN mode first...")
    organizer.organize_files(remove_duplicates=True, dry_run=True)

    confirm = input("\nProceed with actual file organization? (yes/no): ")

    if confirm.lower() == 'yes':
        organizer.organize_files(remove_duplicates=True, dry_run=False)
        print("File organization completed.")
    else:
        print("Operation cancelled.")



