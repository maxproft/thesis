import numpy as np
from PIL import Image

def BWImage(small_intensity,pathToPNG):
    def normalisedata(I):
        I = np.array(I)
        return (((I.max()-I) / (I.max() - I.min())) * 255.9).astype(np.uint8)
    img = Image.fromarray(np.flipud(normalisedata(small_intensity)))
    img.save(pathToPNG)


data = np.loadtxt('import_AllData.csv',delimiter=',').view(complex)
print(np.shape(np.abs(data)))
BWImage(np.abs(data),'name.png')
