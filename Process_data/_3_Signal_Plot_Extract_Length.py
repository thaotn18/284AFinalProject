import matplotlib.pyplot as plt
import numpy as np

import pod5 as p5


# Using the input pod5 file provided
input_pod5 = "./DeepSimulator/BC/fast5/BC.pod5"

signal_array = []
length = []

with p5.Reader(input_pod5) as reader:
  
  for read_record in reader.reads():
    # Read the selected read from the pod5 file
    # next() is required here as Reader.reads() returns a Generator
    read = next(reader.reads(selection=[read_record.read_id]))

    # Get the signal data and sample rate
    sample_rate = read.run_info.sample_rate
    signal = read.signal

    # Compute the time steps over the sampling period
    time = np.arange(len(signal)) / sample_rate

    with open('TimeSignalBC.txt', 'a') as f:
        print(time, file=f)
        print(signal, file=f)
        
    signal_array.append(signal)
    length.append(len(signal))

    # Plot using matplotlib
    plt.plot(time, signal)
    plt.title(label="Synthetic signals for BC (n=100)")
    plt.xlabel('Time')
    plt.ylabel('Current Signal')
    plt.savefig('SynSignals_BC')
    

signal_array = np.array(signal_array)
length = np.array(length)
    
with open('.DeepSimulator/BC/fast5/signalBC.txt','w') as f:
  np.savetxt(f,signal_array)

with open('signalBC_l','a') as f:
  np.savetxt(f,length)

