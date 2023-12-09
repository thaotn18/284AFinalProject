import matplotlib.pyplot as plt
import numpy as np

import pod5 as p5


# Using the input pod5 file
input_pod5 = "./DeepSimulator/BC/fast5/BC.pod5"

signal_z_array = []
z_signal_array = []
length = np.genfromtxt('./DeepSimulator/BC/fast5/signalBC_l.txt',delimiter=None)


with p5.Reader(example_pod5) as reader:
  
  for read_record in reader.reads():
    # Read the selected read from the pod5 file
    # next() is required here as Reader.reads() returns a Generator
    read = next(reader.reads(selection=[read_record.read_id]))

    # Get the signal data
    signal = read.signal

    if len(signal) < max(length):
      z = np.zeros(int(max(length)-len(signal)))
      signal_z = np.append(signal,z)
      z_signal. = np.append(z,signal)
        
    signal_array.append(signal)

signal_z_array = np.array(signal_z_array)
z_signal_array = np.array(z_signal_array)

with open('./DeepSimulator/BC/fast5/signal_BC_z.txt','w') as f:
  np.savetxt(f,signal_z_array)

with open('./DeepSimulator/BC/fast5/signal_z_BC.txt','w') as f:
  np.savetxt(f,z_signal_array)
