# Audio Frequency Analysis using Fourier Transform

## Description
This project analyzes meditation audio signals using the Fourier Transform (FFT) to identify dominant frequency components and compare spectral patterns across different recordings.

## Objective
To explore whether meditation audios share common frequency characteristics or present distinct spectral signatures.

## Methodology
- Audio files were converted to WAV format
- Signals were processed using Python
- The Fast Fourier Transform (FFT) was applied
- Frequency spectra were visualized using Matplotlib

## Results
The analysis shows that each audio presents a different spectral distribution.  

In particular, significant magnitudes were observed in the frequency ranges around 780–800 Hz and near 888 Hz in some of the analyzed signals.  

No common dominant frequency was consistently found across all samples, indicating that each audio has its own spectral characteristics.

## Example Result
### Audio 1
![Audio 1](med1_resultado.png)

### Audio 2
![Audio 2](med2_resultado.png)

### Audio 3
![Audio 3](med3_resultado.png)

## Limitations

- Small number of audio samples analyzed  
- No noise filtering applied  
- Results depend on audio quality

## Technologies
- Python
- NumPy
- SciPy
- Matplotlib

## Future Work
- Analyze a larger dataset of audio samples
- Apply filtering techniques to reduce noise
