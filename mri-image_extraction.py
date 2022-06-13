import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


mask = nib.load("C:/Users/LENOVO/Downloads/Control_project/PPMI/3000/AX_T2_FLAIR/2011-02-01_08_05_22.0/S102118/PPMI_3000_MR_AX_T2_FLAIR__br_raw_20110322143440789_17_S102118_I224561.nii").get_fdata()
print(np.min(mask), np.max(mask), mask.shape, type(mask))

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data = np.random.rand(5, 5)

for i in range (1,5):
    imgSlice = mask[:,:,9+i]
    plt.subplot(1, 4, i)
    plt.axis('off')
    plt.imshow(imgSlice,cmap='gray')
    
