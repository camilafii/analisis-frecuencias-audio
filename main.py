import os
from moviepy import AudioFileClip
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

carpeta_mp4 = "audios_mp4"
carpeta_wav = "audios_wav"

# crear carpeta wav 
os.makedirs(carpeta_wav, exist_ok=True)

for archivo in os.listdir(carpeta_mp4):
    if archivo.endswith(".mp4"):
        
        ruta_mp4 = os.path.join(carpeta_mp4, archivo)
        nombre = archivo.replace(".mp4", "")
        ruta_wav = os.path.join(carpeta_wav, nombre + ".wav")

        print("Procesando:", archivo)

        # convertir a wav
        audio = AudioFileClip(ruta_mp4)
        audio.write_audiofile(ruta_wav)

        # leer audio
        sample_rate, data = wavfile.read(ruta_wav)

        if len(data.shape) > 1:
            data = data[:, 0]

        # Fourier
        fft = np.fft.fft(data)
        frecuencias = np.fft.fftfreq(len(fft), d=1/sample_rate)

        # solo positivas
        mask = frecuencias >= 0

        # gráfico
        plt.figure()
        plt.plot(frecuencias[mask], np.abs(fft)[mask])
        plt.xlim(0, 3000)
        plt.title(f"Espectro - {nombre}")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud")

        # guardar imagen
        ruta_img = nombre + "_resultado.png"
        plt.savefig(ruta_img, dpi=300)
        plt.show()

        plt.close()