import numpy as np
import os.path
import scipy
import argparse
import scipy.io as sio
import matplotlib
#import matplolib.colors as colors
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
import cv2
import sys
import imageio
import time

# Make sure that caffe is on the python path:
caffe_root = '/home/rish/caffe-segnet-cudnn5-master/' 			# Change this to the absolute directoy to SegNet Caffe
sys.path.insert(0, caffe_root + 'python')

import caffe

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--colours', type=str, required=True)
parser.add_argument('--data', type=str, required=True)
parser.add_argument('--save', type=str, required=False,default=1)
args = parser.parse_args()

filename, file_extension = os.path.splitext(args.model)
print filename
if os.path.isdir(filename) == False:
	os.mkdir(filename)

if os.path.isdir(filename+'/image/') == False:
	os.mkdir(filename+'/image/')
if os.path.isdir(filename) == False:
	os.mkdir(filename)
if os.path.isdir(filename+'/gt/') == False:
	os.mkdir(filename+'/gt/')
if os.path.isdir(filename+'/out/') == False:
	os.mkdir(filename+'/out/')
if os.path.isdir(filename+'/whole/') == False:
	os.mkdir(filename+'/whole/')
if os.path.isdir(filename+'/uncertainity/') == False:
	os.mkdir(filename+'/uncertainity/')
if os.path.isdir(filename+'/predictions/') == False:
	os.mkdir(filename+'/predictions/')

caffe.set_mode_gpu()

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

input_shape = net.blobs['data'].data.shape
#out_img = Image.new('RGB', (input_shape[3]*3, input_shape[2]*3))
label_colours = cv2.imread(args.colours).astype(np.uint8)
k=0;
images=[]
with open(args.data) as f:
    for line in f:
	start = time.time()
        input_image_file, ground_truth_file = line.split()
	input_image_raw = caffe.io.load_image(input_image_file)
	inp = cv2.imread(input_image_file)
	ground_truth = cv2.imread(ground_truth_file, 0)
	end = time.time()
	print '%30s' % 'Grabbed Input and Label in ', str((end - start)*1000), 'ms'

	start = time.time()
	#print input_image_raw
	input_image = caffe.io.resize_image(input_image_raw, (input_shape[2],input_shape[3]))
	input_image = input_image*255
	input_image = input_image.transpose((2,0,1))
	input_image = input_image[(2,1,0),:,:]
	input_image = np.asarray([input_image])
	input_image = np.repeat(input_image,input_shape[0],axis=0)
	end = time.time()
	print '%30s' % 'Preprocess image in ', str((end - start)*1000), 'ms'
	start = time.time()	
	out = net.forward_all(data=input_image)
	end = time.time()

	print '%30s' % 'Executed SegNet in ', str((end - start)*1000), 'ms'

	start = time.time()
	predicted = net.blobs['prob'].data

	output = np.mean(predicted,axis=0)
	uncertainty = np.var(predicted,axis=0)
	ind = np.argmax(output, axis=0)

	segmentation_ind_3ch = np.resize(ind,(3,input_shape[2],input_shape[3]))
	segmentation_ind_3ch = segmentation_ind_3ch.transpose(1,2,0).astype(np.uint8)
	segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)

	b,g,r = cv2.split(segmentation_ind_3ch)
	gt_ind_3ch = np.resize(ground_truth,(3,input_shape[2],input_shape[3]))
	gt_ind_3ch = gt_ind_3ch.transpose(1,2,0).astype(np.uint8)
	gt_rgb = np.zeros(gt_ind_3ch.shape, dtype=np.uint8)

	cv2.LUT(segmentation_ind_3ch,label_colours,segmentation_rgb)
	cv2.LUT(gt_ind_3ch,label_colours,gt_rgb)
	
	uncertainty = np.transpose(uncertainty, (1,2,0))

	average_unc = np.mean(uncertainty,axis=2)
	min_average_unc = np.min(average_unc)
	max_average_unc = np.max(average_unc)
	max_unc = np.max(uncertainty)
	
	# uncomment to save results
	
	outimg = np.concatenate((np.concatenate((inp,gt_rgb),axis=1),segmentation_rgb),axis=1)
	end = time.time()
	print '%30s' % 'Processed results in ', str((end - start)*1000), 'ms\n'
	if args.save == 0:
		cv2.imshow("SegNet", outimg)
		#key = cv2.waitKey(1)
		#if key == 27: # exit on ESC
		#    break
	else:
		cv2.imwrite(filename+'/out/img'+str(k)+'.png',segmentation_rgb)
		cv2.imwrite(filename+'/gt/img'+str(k)+'.png',gt_rgb)
		cv2.imwrite(filename+'/whole/img'+str(k)+'.png',outimg)
	
		cm = matplotlib.pyplot.get_cmap('bone_r') 
		matplotlib.image.imsave(filename+'/uncertainity/img'+str(k)+'.png',average_unc,cmap=cm, vmin=0, vmax=max_average_unc)
		cv2.imwrite(filename+'/predictions/img'+str(k)+'.png',b)
		#images.append(outimg.astype(float)/255)	
		k=k+1
print 'Processed: ', k
#imageio.mimsave(filename+'/movie.gif',images,'GIF', fps=5)
if args.save == 0:
	cv2.destroyAllWindows()
print 'Success!'

