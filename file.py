import shutil
import logging
from pathlib import Path
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ask user for folder path
file_location_path = input("Enter the folder path to organize files: ").strip()

def get_unique_filename(destination_folder, filename):
    """Generates a unique filename if the file already exists in destination."""
    target_path = destination_folder / filename
    if not target_path.exists():
        return target_path

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{target_path.stem}_{timestamp}{target_path.suffix}"
    return destination_folder / new_filename

def organize_files():
    source_path = Path(file_location_path)

    if not source_path.exists():
        print(f" The directory '{source_path}' does not exist.")
        logging.error(f"Directory does not exist: {source_path}")
        return

    print(f"\n Organizing files in: {source_path}\n")
    files_moved = 0

    for item in source_path.iterdir():
        if item.is_dir():
            continue  # Skip already created folders

        if item.is_file():
            extension = item.suffix.lower()

            if not extension:
                print(f" Skipping '{item.name}' (no extension)")
                logging.warning(f"Skipped file with no extension: {item.name}")
                continue

            print(f" Found file: {item.name} (Extension: {extension})")

            folder_name = extension[1:] if extension.startswith('.') else "miscellaneous"
            destination_folder = source_path / folder_name

            destination_folder.mkdir(parents=True, exist_ok=True)

            try:
                target_file = get_unique_filename(destination_folder, item.name)
                shutil.move(str(item), str(target_file))
                files_moved += 1
                print(f" Moved to: {destination_folder.name}/\n")
                logging.info(f"Moved '{item.name}' to '{destination_folder.name}/'")
            except shutil.Error as e:
                print(f" Error moving '{item.name}': {e}")
                logging.error(f"shutil.Error for '{item.name}': {e}")
            except OSError as e:
                print(f" OS error while moving '{item.name}': {e}")
                logging.error(f"OSError for '{item.name}': {e}")
            except Exception as e:
                print(f" Unexpected error for '{item.name}': {e}")
                logging.exception(f"Unexpected error for '{item.name}'")

    if files_moved > 0:
        print(f"\n Successfully moved {files_moved} file(s).")
        logging.info(f"Total files moved: {files_moved}")
    else:
        print("\n No files were moved. Please check the directory and file types.")
        logging.warning("No files moved during execution.")

if __name__ == "__main__":
    organize_files()
    print("\n File organization complete.")
