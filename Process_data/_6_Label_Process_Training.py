import matplotlib.pyplot as plt
import numpy as np

import pod5 as p5

length_combination = np.genfromtxt('./DeepSimulator/BC/fast5/signalBC_c_l.txt',delimiter=None)
length_barcode = np.genfromtxt('./DeepSimulator/BC/fast5/signalBC_l.txt',delimiter=None)

size = int(max(length_combination))

z = np.zeros(size-max(length_barcode)))
o = np.ones(int(max(length_barcode))


#y 
p0 = np.empty([100,size])
p1 = np.empty([100,size])
p2 = np.empty([100,size])

for i,s in enumerate(p0):
  #0,BC1
  p0[i] = np.append(o,z)
  p1[i] = np.append(z,o)
  p2[i] = np.zeros(size)
  
for i,s in enumerate(signal):
  #BC1,0
  p0[i] = np.append(z,o)
  p1[i] = np.append(o,z)
  p2[i] = np.zeros(size)
  
for i,s in enumerate(signal):
  #0,BC2
  p0[i] = np.append(o,z)
  p2[i] = np.append(z,o)
  p1[i] = np.zeros(size)
  
for i,s in enumerate(signal):
  #BC2,0
  p0[i] = np.append(z,o)
  p2[i] = np.append(o,z)
  p1[i] = np.zeros(size)
  
y = torch.tensor([p0,p1,p2])

ys = torch.swapaxes(y,0,1)

torch.save(ys, './Data/Nano_train_data/train_BC1/train_tensor_y_0s_BC1.pt')

