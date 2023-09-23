import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

def create_spectrograms(train_folder):
    # Create an "images" folder inside the train folder
    images_folder = os.path.join(train_folder, "images")
    os.makedirs(images_folder, exist_ok=True)

    # Iterate through subfolders in the train folder
    for root, _, files in os.walk(train_folder):
        if root != train_folder:  # Skip the main "train" folder
            subfolder_name = os.path.basename(root)
            subfolder_images_folder = os.path.join(images_folder, subfolder_name)
            os.makedirs(subfolder_images_folder, exist_ok=True)

            for file in files:
                if file.endswith(".wav"):
                    # Load the .wav file
                    wav_file_path = os.path.join(root, file)
                    x, sr = librosa.load(wav_file_path, sr=44100)

                    # Generate the spectrogram
                    X = librosa.stft(x)
                    Xdb = librosa.amplitude_to_db(abs(X))

                    # Create a figure for the spectrogram
                    plt.figure(figsize=(10, 5))
                    ax = plt.axes()
                    ax.set_axis_off()
                    plt.set_cmap('hot')
                    librosa.display.specshow(Xdb, y_axis='log', x_axis='time', sr=sr)

                    # Save the spectrogram image in the subfolder
                    output_path = os.path.join(subfolder_images_folder, os.path.splitext(file)[0] + ".png")
                    plt.savefig(output_path, bbox_inches='tight', transparent=True, pad_inches=0.0)
                    plt.close()

if __name__ == "__main__":
    train_folder = "./train"  # Change this to the path of your "train" folder
    create_spectrograms(train_folder)
