import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend, windows, welch

def hvsr(horizontal, vertical, fs):
    """
    Compute the Horizontal-to-Vertical Spectral Ratio (HVSR) from seismic data.

    Parameters:
    horizontal (numpy array): Horizontal component of the seismic data.
    vertical (numpy array): Vertical component of the seismic data.
    fs (float): Sampling frequency of the data.

    Returns:
    freqs (numpy array): Frequencies corresponding to the HVSR.
    hvsr (numpy array): HVSR values.
    """
    # Detrend the data
    horizontal = detrend(horizontal)
    vertical = detrend(vertical)

    # Apply a window (e.g., Hanning window)
    window = windows.hann(len(horizontal))
    horizontal *= window
    vertical *= window

    # Compute the Fourier transform
    n = len(horizontal)
    fft_horizontal = np.fft.rfft(horizontal)
    fft_vertical = np.fft.rfft(vertical)

    # Compute the power spectral density (PSD)
    freqs = np.fft.rfftfreq(n, d=1/fs)
    psd_horizontal = np.abs(fft_horizontal) ** 2
    psd_vertical = np.abs(fft_vertical) ** 2

    # Compute the HVSR
    hvsr = np.sqrt(psd_horizontal / psd_vertical)

    return freqs, hvsr

# Example usage
if __name__ == "__main__":
    # Example data (replace with your actual data)
    fs = 10000.0  # Sampling frequency (Hz)
    t = np.arange(0, 10, 1/fs)  # Time vector
    horizontal = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.1, len(t))  # Horizontal component
    vertical = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.1, len(t))  # Vertical component

    # Compute HVSR
    freqs, hvsr = hvsr(horizontal, vertical, fs)

    # Plot the HVSR
    plt.figure(figsize=(10, 6))
    plt.semilogx(freqs, hvsr)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('HVSR')
    plt.title('Horizontal-to-Vertical Spectral Ratio (HVSR)')
    plt.grid(True, which="both", ls="--")
    plt.show()
