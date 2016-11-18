#!/usr/bin/python


# Scipt for the power spectral density measurement using USRP1
# Author: Bilal Parvez

import os
import scipy
import numpy as np

# To execute the gnu radio scipt in a shell


# sampling 10,10 Mhz chunks across the entire 100 Mhz spectrum from 2.4 to 2.5 Ghz
n = [2405000000 ,2415000000 ,2425000000,2435000000,2445000000,2455000000,2465000000,2475000000,2485000000,2495000000]   #for the sampling array
values = [] # array to hold the frequency values

for items in n:
    #argument1 = str(items)

    cmdstring = "./uhd_fft.py -f %s" %(items) # type casting items so that it can be used for os.system call
    os.system(cmdstring) # running the script on the system terminal
    #   os.system('clear')  #clear the terminal
    # print 'Done executing script' #error checking print message


    # A one line python command to read the entire file into a numpy array
    f = scipy.fromfile(open("value"), dtype=scipy.float32)  # file value is the file generated by the gnu radios scripts file sink block
    #f = np.mean(f) # take a mean , is it a good idea ?
    f = max(f) # trying with the maximum value in the array of the fft vector values
    #f = f *10 # converting into decible from bell # done in gnu radio now

    values.append(f) # Putting values in an array to print at the end

os.system('clear')  #clear the terminal

for i in range(0,len(n)):
    print "for" , n[i] ,":" , values[i]   # to print the values of the fft , need to figure this out further, what the values is and so forth


print "total average" , np.mean(values)
#Rest of the psuedo code

#Take value of the first 10 Mhz segment, save in an array , do the same for the rest of the spectrum

# Figure out a way commute the total in the end
