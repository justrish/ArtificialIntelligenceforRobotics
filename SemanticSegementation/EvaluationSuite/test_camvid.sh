
#run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/webcam_demo.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/segnet_basic_camvid.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/segnet_basic_camvid.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid11.png --input /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt > SegNet-Tutorial-master/segnet_basic_camvid.log

#run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/test_bayesian_segnet.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/bayesian_segnet_basic_camvid.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/bayesian_segnet_basic_camvid.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid11.png --data /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt  > SegNet-Tutorial-master/bayesian_segnet_basic_camvid.log
#run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/test_bayesian_segnet.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/bayesian_segnet_camvid.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/bayesian_segnet_camvid.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid11.png --data /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt > SegNet-Tutorial-master/bayesian_segnet_camvid.log

#run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/test_bayesian_segnet.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/bayesian_segnet_basic_camvidw.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/bayesian_segnet_basic_camvidw.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid11.png --data /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt > SegNet-Tutorial-master/bayesian_segnet_basic_camvidw.log
#run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/test_bayesian_segnet.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/bayesian_segnet_camvidw.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/bayesian_segnet_camvidw.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid11.png --data /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt > SegNet-Tutorial-master/bayesian_segnet_camvidw.log

##run
python /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/webcam_demo.py --model /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/segnet_model_driving_webdemo.prototxt --weights /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Models/Inference/segnet_weights_driving_webdemo.caffemodel --colours /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/Scripts/camvid12.png --input /home/rish/caffe-segnet-cudnn5-master/SegNet-Tutorial-master/CamVid/test.txt --save 0 > SegNet-Tutorial-master/segnet_model_driving_webdemo.log

