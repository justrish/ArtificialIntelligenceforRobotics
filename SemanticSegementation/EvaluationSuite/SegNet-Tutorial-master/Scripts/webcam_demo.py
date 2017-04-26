import numpy as np
import matplotlib.pyplot as plt
import os.path
import scipy
import argparse
#import mathcv
import cv2
import sys
import time


#sys.path.append('/usr/local/lib/python2.7/site-packages')
# Make sure that caffe is on the python path:
caffe_root = '/home/rish/caffe-segnet-cudnn5-master/'
sys.path.insert(0, caffe_root + 'python')
import caffe

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--colours', type=str, required=True)
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--save', type=str, required=False,default=0)
args = parser.parse_args()

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

caffe.set_mode_gpu()

input_shape = net.blobs['data'].data.shape
output_shape = net.blobs['argmax'].data.shape

label_colours = cv2.imread(args.colours).astype(np.uint8)
#print np.asarray([label_colours])
#cv2.namedWindow("Input")
#cv2.namedWindow("SegNet")

##cap = cv2.VideoCapture(0) # Change this to your webcam ID, or file name for your video file
lines = [line.rstrip('\n') for line in open(args.input)]
image = [i.split()[0] for i in lines]
gt = [i.split()[1] for i in lines]
rval = True
## creating folders
filename, file_extension = os.path.splitext(args.model)
print filename
if args.save == 1:
	images = []
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
	if os.path.isdir(filename+'/predictions/') == False:
		os.mkdir(filename+'/predictions/')
k=0

##while rval:
for i in range(len(image)):
	start = time.time()
	## for Handling video inputs
	#rval, frame = cap.read()

        #if rval == False:
        #    break
	frame = cv2.imread(image[i])
	ref = cv2.imread(gt[i],0)
	end = time.time()
	print '%30s' % 'Grabbed camera frame in ', str((end - start)*1000), 'ms'

	start = time.time()
	frame = cv2.resize(frame, (input_shape[3],input_shape[2]))
	input_image = frame.transpose((2,0,1))
	# input_image = input_image[(2,1,0),:,:] # May be required, if you do not open your data with opencv2
	input_image = np.asarray([input_image])
	end = time.time()
	print '%30s' % 'Preprocess image in ', str((end - start)*1000), 'ms'

	start = time.time()
	out = net.forward_all(data=input_image)
	end = time.time()
	print '%30s' % 'Executed SegNet in ', str((end - start)*1000), 'ms'

	start = time.time()
	segmentation_ind = np.squeeze(net.blobs['argmax'].data)
    	segmentation_ind_3ch = np.resize(segmentation_ind,(3,input_shape[2],input_shape[3]))
	segmentation_ind_3ch = segmentation_ind_3ch.transpose(1,2,0).astype(np.uint8)
	segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)
	
	cv2.LUT(segmentation_ind_3ch,label_colours,segmentation_rgb)
	b,g,r = cv2.split(segmentation_ind_3ch)
	#segmentation_rgb = segmentation_rgb.astype(float)/255

	ref_ind_3ch = np.resize(ref,(3,input_shape[2],input_shape[3]))
	ref_ind_3ch = ref_ind_3ch.transpose(1,2,0).astype(np.uint8)
	ref_rgb = np.zeros(ref_ind_3ch.shape, dtype=np.uint8)
	
	cv2.LUT(ref_ind_3ch,label_colours,ref_rgb)
	#ref_rgb = ref_rgb.astype(float)/255

	outimg = np.concatenate((np.concatenate((frame,ref_rgb),axis=1),segmentation_rgb),axis=1)
	end = time.time()
	print '%30s' % 'Processed results in ', str((end - start)*1000), 'ms\n'
	
	print args.save
	if args.save == 0:
		cv2.imshow("SegNet", segmentation_rgb)
		cv2.imshow("Input", frame)
		#key = cv2.waitKey(1)
		#if key == 27: # exit on ESC
		#    break
	else:		
		cv2.imwrite(filename+'/image/img'+str(k)+'.png',frame)
		cv2.imwrite(filename+'/gt/img'+str(k)+'.png',ref_rgb)
		cv2.imwrite(filename+'/predictions/img'+str(k)+'.png',b)
		cv2.imwrite(filename+'/out/img'+str(k)+'.png',segmentation_rgb)		
		plt.imsave(filename+'/whole/img'+str(k)+'.png', outimg)
		#images.append(outimg.astype(float)/255)
		k=k+1
#cap.release()
#import matplotlib.animation as animation
#def build_gif(imgs, show_gif=False, save_gif=True, title=''):
 
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    ax.set_axis_off()
 
#    ims = map(lambda x: (ax.imshow(x), ax.set_title(title)), imgs)
 
#    im_ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=0, blit=False)
 
#    if save_gif:
#        im_ani.save(filename+'/movie.gif', writer='imagemagick')
 
#    if show_gif:
#        plt.show()
 
#    return

#build_gif(images)
if args.save == 0:
	cv2.destroyAllWindows()
print 'Success!'

