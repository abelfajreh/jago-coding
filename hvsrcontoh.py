from obspy import read

# Use forward slashes for the file path
file_path = "C:/Users/Lenovo/OneDrive/Documents/College/Metode Komputasi/jago-coding/PS_RGT_GB03_CL4-12_20220630_merged.mseed"

# Read the MSEED file
stream = read(file_path)

# Ensure you have three components (Z, N, E)
if len(stream) != 3:
    raise ValueError("The MSEED file should contain three components (Z, N, E).")

# Extract the components
z_trace = stream.select(component="Z")[0]
n_trace = stream.select(component="N")[0]
e_trace = stream.select(component="E")[0]

# Remove instrument response
z_trace.remove_response(output="VEL")
n_trace.remove_response(output="VEL")
e_trace.remove_response(output="VEL")

# Detrend
z_trace.detrend("linear")
n_trace.detrend("linear")
e_trace.detrend("linear")

# Filter (optional)
z_trace.filter("bandpass", freqmin=0.1, freqmax=50)
n_trace.filter("bandpass", freqmin=0.1, freqmax=50)
e_trace.filter("bandpass", freqmin=0.1, freqmax=50)

# Compute the Fourier transform
z_fft = np.fft.rfft(z_trace.data)
n_fft = np.fft.rfft(n_trace.data)
e_fft = np.fft.rfft(e_trace.data)

# Compute the power spectral density (PSD)
z_psd = np.abs(z_fft) ** 2
n_psd = np.abs(n_fft) ** 2
e_psd = np.abs(e_fft) ** 2

# Compute the horizontal PSD
h_psd = (n_psd + e_psd) / 2

# Compute the HVSR
hvsr = h_psd / z_psd

# Frequency axis
freq = np.fft.rfftfreq(z_trace.data.size, d=1/z_trace.stats.sampling_rate)

# Plot the HVSR
plt.figure(figsize=(10, 6))
plt.semilogx(freq, hvsr)
plt.xlabel('Frequency (Hz)')
plt.ylabel('HVSR')
plt.title('Horizontal-to-Vertical Spectral Ratio (HVSR)')
plt.grid(True, which="both", ls="--")
plt.show()

# Find the index of the maximum HVSR value
fundamental_freq_index = np.argmax(hvsr)
fundamental_freq = freq[fundamental_freq_index]

print(f"Fundamental Frequency: {fundamental_freq} Hz")
