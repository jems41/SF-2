import os
import datetime
import time
import subprocess

def find_best_date(file_path):
    # Try extracting multiple date fields
    date_tags = ['DateTimeOriginal', 'MediaCreateDate', 'CreateDate']
    for tag in date_tags:
        result = subprocess.run(
            ['exiftool', f'-{tag}', '-s3', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        date_value = result.stdout.strip()
        if date_value:
            print(f"📅 Found date from {tag}: {date_value}")
            return date_value
    return None

def set_file_modified_time(file_path, new_date_str):
    """
    Set the file system modified time using os.utime().
    Expects date format like 'YYYY:MM:DD HH:MM:SS' (removes timezones if present).
    """
    try:
        # Remove timezone if present (e.g. "-04:00")
        cleaned_date = new_date_str.split('+')[0].split('-')[0].strip()

        # Parse cleaned Exif date
        dt = datetime.datetime.strptime(cleaned_date, "%Y:%m:%d %H:%M:%S")
        mod_time = time.mktime(dt.timetuple())
        os.utime(file_path, (mod_time, mod_time))
        print(f"🕒 File system modified time set for {file_path}")
    except Exception as e:
        print(f"⚠️ Failed to set modified time: {e}")

def update_date_taken(file_path):
    ext = file_path.lower()
    if not ext.endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov')):
        print(f"⏩ Skipped unsupported file: {file_path}")
        return

    best_date = find_best_date(file_path)
    if not best_date:
        print(f"❌ No usable date found for {file_path}")
        return

    # Apply best_date to still images
    if ext.endswith(('.jpg', '.jpeg', '.png')):
        subprocess.run([
            'exiftool',
            f'-DateTimeOriginal={best_date}'
            '-overwrite_original',
            file_path
        ])

    # MP4 files (can usually write DateTimeOriginal)
    elif ext.endswith('.mp4'):
        subprocess.run([
            'exiftool',
            '-DateTimeOriginal<MediaCreateDate',
            '-CreateDate<MediaCreateDate',
            '-TrackCreateDate<MediaCreateDate',
            '-MediaCreateDate<MediaCreateDate',
            '-DateTimeOriginal+=11:00',  # adjust if needed
            '-overwrite_original',
            file_path
        ])

    # MOV files (use QuickTime-compatible tags only)
    elif ext.endswith('.mov'):
        subprocess.run([
            'exiftool',
            '-QuickTime:CreateDate<MediaCreateDate',
            '-QuickTime:ModifyDate<MediaCreateDate',
            '-TrackCreateDate<MediaCreateDate',
            '-MediaCreateDate<MediaCreateDate',
            '-QuickTime:CreateDate+=03:00',  # adjust if needed
            '-QuickTime:ModifyDate+=03:00',
            '-TrackCreateDate+=03:00',
            '-MediaCreateDate+=03:00',
            '-overwrite_original',
            file_path
        ])

    # Optional but recommended: Also try syncing FileModifyDate
    subprocess.run([
        'exiftool',
        '-FileModifyDate<DateTimeOriginal',
        '-overwrite_original',
        file_path
    ])

    # Force Windows to reflect the file system "Date Modified"
    set_file_modified_time(file_path, best_date)

    print(f"✅ Updated metadata for {file_path}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            update_date_taken(filepath)

# 🔁 Run on your folder
process_folder("C:\\Users\\combj\\Downloads\\test")
