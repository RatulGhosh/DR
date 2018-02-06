import os
import glob
from joblib import Parallel, delayed

in_dir = 'nosymptoms/'
out_dir = 'nosymptoms_new/'
IMAGE_SIZE = 128

from PIL import Image, ImageChops
JPEG_FILES = glob.glob(in_dir+'*.jpeg')
def convert(img_file):
	im = Image.open(img_file)
	im.resize((IMAGE_SIZE,IMAGE_SIZE)).save(out_dir + os.path.basename(img_file), 'JPEG')

Parallel(n_jobs=32, verbose=10)(delayed(convert)(f) for f in JPEG_FILES)
	
