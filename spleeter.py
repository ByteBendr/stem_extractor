import os
import subprocess
import colorama
from colorama import Fore, Style
from click import pause
from tkinter import Tk, filedialog

colorama.init()

def extract_stems(audio_file_path, output_directory, model='htdemucs'):
    """
    Extracts stems from an audio file using Demucs.

    Parameters:
    - audio_file_path (str): Path to the input audio file.
    - output_directory (str): Directory to save the output stems.
    - model (str): Model to use for separation (e.g., 'htdemucs').
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Run Demucs separation with the specified model
    command = [
        'demucs',
        '-n', model,
        '--out', output_directory,
        audio_file_path
    ]
    subprocess.run(command)

def main():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Prompt user for input file and output directory
    print(f'''{Fore.LIGHTWHITE_EX + Style.BRIGHT}
========================================
-----        Stems Extractor       -----
========================================\n''')
    
    audio_file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3 *.wav *.flac")])
    if not audio_file_path:
        print(f"[err] Error: No file selected.")
        return

    output_directory = filedialog.askdirectory(title="Select Output Directory")
    if not output_directory:
        print(f"[err] Error: No directory selected.")
        return

    # Check if the provided audio file path exists
    if not os.path.isfile(audio_file_path):
        print(f"[err] Error: The file {audio_file_path} does not exist.")
        return

    # Extract stems from the audio file using the best model
    extract_stems(audio_file_path, output_directory, model='htdemucs')

    pause('\nPress any key to exit.')

    Style.RESET_ALL

if __name__ == "__main__":
    main()
