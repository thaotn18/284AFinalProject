# Download the Deepsimulator package
git clone https://github.com/lykaust15/DeepSimulator.git

# Navigate to folder
cd ./DeepSimulator/

#Install all required modules
./install.sh

# Simulate 100 reads from sequence of interst in fasta file format with random noise
# low pass filter cutoff frequency: -f value range from 950-1200Hz
# Gaussian noise at the signal level: -S value range from 1-2
# Gaussian noise the event level: -e value range from 0.5-0.9
for f in {1..100}; do ./deep_simulator.sh -i BC.fa -n 1 -S $(( $RANDOM % 2 + 1 )) -f $(($RANDOM % 251 + 950)) -e 0.$(( $RANDOM % 5 + 5 )) -o ./BC/"BC_"$f; done

# Move all .fast5 single read format to 1 folder 
for f in {1..100}; do mv ./DeepSimulator/BC/BC_$f/fast5/*.fast5 ./DeepSimulator/BC/BC_fast5/; done

# Converts folders containing single_read_fast5 files into multi_read_fast5_files 
single_to_multi_fast5 --input_path ./DeepSimulator/BC/BC_fast5/ --save_path ./DeepSimulator/BC/fast5 --filename_base BC --batch_size 100 --recursive

# Convert .fast5 format to Pod5 format to provide easy access to data and extract raw signal
pod5 convert fast5 BC_0.fast5 --output BC.pod5

