<html>
<head>
<title>References</title>

<table id="qs_table" border="1">
<thead><tr><th width="3%">Index</th><th width="20%">Author</th><th width="50%">Title</th><th width="5%">Year<th width="40%">Hyperlink</th><th width="70%">Reftype</th><th width="5%">DOI</th></tr></thead>
<tbody>

<tr id="id1" class="parent">
     <td colspan="7">Topics</td>
</tr>

<tr id="id2" class="parent">
	<td>1 </td>
    <td colspan="6"> Database: </td>
</tr>

<tr id="segmentation_database1" class="entry">
	<td>1. a</td>
	<td colspan="6"><a href=""> Semantic Segmentation Dataset 1</a> &nbsp;</td>
</tr>

<tr id="segmentation_database2" class="entry">
	<td>1. b</td>
	<td colspan="6"><a href=""> Semantic Segmentation Dataset 2</a> &nbsp;</td>
</tr>

<tr id="TINGWU WANG" class="entry">
	<td>1. c</td>
	<td>TINGWU WANG</td>
	<td>Intro to Semantic Segmentation <p class="infolinks">[<a href="javascript:toggleInfo('Scharstein','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('TINGWU WANG','review')">Review</a>] 
	<td>2016</td>
	<td><a href="http://www.cs.toronto.edu/~tingwuwang/semantic_segmentation.pdf">DOI</a> &nbsp;</td>
</tr>
<tr id="abs_Scharstein" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>
<li> 1. What is semantic segmentation?</li>
	What is segmentation in the first place?, 
	What is semantic segmentation?, 
	Why semantic segmentation?
<li> 2. Deep Learning in Segmentation</li>
	Semantic Segmentation before Deep Learning,
	Conditional Random Fields, 
	A Brief Review on Detection, 
	Fully Convolutional Network.
<li> 3. Discussions and Demos</li>
	Demos of CNN + CRF, 
	Segmentation from Natural Language Expression, 
	Make CRF Great Again?
	</ul>
	</td>
</tr>
<tr id="rev_Scharstein" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	</td>
</tr>

<tr id="id3" class="parent">
	<td>2 </td>
    <td colspan="6"> Deep Learning: </td>
</tr>

<tr id="Thoma" class="entry">
	<td>2. a</td>
	<td>Martin Thoma</td>
	<td>A Survey of Semantic Segmentation <p class="infolinks">[<a href="javascript:toggleInfo('Zeiler','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Zeiler','review')">Review</a>]</p></td>
	<td>2016</td>
	<td><a href="https://arxiv.org/pdf/1602.06541.pdf">Link</a> &nbsp;</td>
	<td>book</td>
	<td>incollection</td>
	
</tr>
<tr id="abs_Thoma" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>This survey gives an overview over different
techniques used for pixel-level semantic segmentation.
Metrics and datasets for the evaluation of segmentation
algorithms and traditional approaches for segmentation
such as unsupervised methods, Decision Forests
and SVMs are described and pointers to the relevant
papers are given. Recently published approaches with
convolutional neural networks are mentioned and typical
problematic situations for segmentation algorithms are
examined. A taxonomy of segmentation algorithms is
given.
	</ul>
	</td>
</tr>
<tr id="rev_Zeiler" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	<ul>
	  <li>Uses CNNs to extract local and global component in a very efficient and simple way. </li>
	</ul></td>
</tr>


<tr id="Treml" class="entry">
	<td>2. b</td>
	<td>Michael Treml, José Arjona-Medina, Thomas Unterthiner, Rupesh Durgesh2, </td>
	<td>Speeding up Semantic Segmentation for Autonomous Driving <p class="infolinks">[<a href="javascript:toggleInfo('Treml','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Treml','review')">Review</a>] </p></td>
	<td>2016</td>
	<td><a href="https://openreview.net/pdf?id=S1uHiFyyg">Link</a> &nbsp;</td>
	<td>(NIPS 2016)</td>
	<td>29th Conference on Neural Information Processing Systems, Barcelona, Spain</td>
	
</tr>
<tr id="abs_Treml" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>
Deep learning has considerably improved semantic image segmentation. However,
its high accuracy is traded against larger computational costs which makes it unsuitable
for embedded devices in self-driving cars. We propose a novel deep network
architecture for image segmentation that keeps the high accuracy while being
efficient enough for embedded devices. The architecture consists of ELU activation
functions, a SqueezeNet-like encoder, followed by parallel dilated convolutions,
and a decoder with SharpMask-like refinement modules. On the Cityscapes dataset,
the new network achieves higher segmentation accuracy than other networks that
are tailored to embedded devices. Simultaneously the frame-rate is still sufficiently
high for the deployment in autonomous vehicles.


	</ul>
	</td>
</tr>
<tr id="rev_Treml" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	<ul>
	  <li>Uses CNN for optical flow. </li>
	</ul></td>
</tr>


<tr id="Saumitro" class="entry">
	<td>2. b</td>
	<td>Saumitro Dasgupta </td>
	<td>Object Detection for Semantic SLAM using Convolution Neural Networks <p class="infolinks">[<a href="javascript:toggleInfo('Treml','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Treml','review')">Review</a>] </p></td>
	<td>2014</td>
	<td><a href="http://cs229.stanford.edu/proj2014/Saumitro%20Dasgupta,%20Object%20Detection%20for%20Semantic%20SLAM%20using%20Convolutional%20Neural%20Networks.pdf">Link</a> &nbsp;</td>
	<td>Stanford</td>
	<td></td>
	
</tr>
<tr id="abs_Saumitro" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>
Conventional SLAM (Simultaneous Localization and Mapping) systems typically provide odometry estimates
and point-cloud reconstructions of an unknown environment. While these outputs can be used for
tasks such as autonomous navigation, they lack any semantic information. Our project implements a modular
object detection framework that can be used in conjunction with a SLAM engine to generate semantic
scene reconstructions. A semantically-augmented reconstruction has many
potential applications. Some examples include: 
• Discriminating between pedestrians, cars, bicyclists, etc in an autonomous driving system.
• Loop-closure detection based on object-level descriptors. 
• Smart household bots that can retrieve objects given a natural language command.
	</ul>
	</td>
</tr>
<tr id="rev_Saumitro" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	<ul>
	  <li> </li>
	</ul></td>
</tr>
<tr id="Darrell" class="entry">
	<td>2. b</td>
	<td>Jonathan Long∗ Evan Shelhamer∗ Trevor Darrell</td>
	<td>Fully Convolutional Networks for Semantic Segmentation <p class="infolinks">[<a href="javascript:toggleInfo('Treml','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Treml','review')">Review</a>] </p></td>
	<td>2015</td>
	<td><a href="https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf">Link</a> &nbsp;</td>
	<td>Berkley</td>
	<td></td>
	
</tr>
<tr id="abs_Darrell" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>
Convolutional networks are powerful visual models that
yield hierarchies of features. We show that convolutional
networks by themselves, trained end-to-end, pixelsto-pixels,
exceed the state-of-the-art in semantic segmentation.
Our key insight is to build “fully convolutional”
networks that take input of arbitrary size and produce
correspondingly-sized output with efficient inference and
learning. We define and detail the space of fully convolutional
networks, explain their application to spatially dense
prediction tasks, and draw connections to prior models. We
adapt contemporary classification networks (AlexNet [22],
the VGG net [34], and GoogLeNet [35]) into fully convolutional
networks and transfer their learned representations
by fine-tuning [5] to the segmentation task. We then define a
skip architecture that combines semantic information from
a deep, coarse layer with appearance information from a
shallow, fine layer to produce accurate and detailed segmentations.
Our fully convolutional network achieves stateof-the-art
segmentation of PASCAL VOC (20% relative improvement
to 62.2% mean IU on 2012), NYUDv2, and SIFT
Flow, while inference takes less than one fifth of a second
for a typical image.

	</ul>
	</td>
</tr>
<tr id="rev_Darell" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	<ul>
	  <li> </li>
	</ul></td>
</tr>
<tr id="Bearman" class="entry">
	<td>2. b</td>
	<td>Amy Bearman, Olga Russakovsky, Vitto Ferrari, Li Fei-Fei1</td>
	<td>What's the Point: Semantic Segmentation with Point Supervision <p class="infolinks">[<a href="javascript:toggleInfo('Treml','abstract')">Abstract</a>] [<a href="javascript:toggleInfo('Treml','review')">Review</a>] </p></td>
	<td>2016</td>
	<td><a href="https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf">Link</a> &nbsp;</td>
	<td>Stanford, Berkley</td>
	<td></td>
	
</tr>
<tr id="abs_Bearman" class="abstract noshow">
	<td colspan="7"><b>Abstract</b>: 
	<ul>
The semantic image segmentation task presents a trade-off between test time accuracy and training-time annotation cost. Detailed per-pixel annotations enable training accurate models but are very time-consuming to obtain; image-level class labels are an order of magnitude cheaper but result in less accurate models. We take a natural step from image-level annotation towards stronger supervision: we ask annotators to point to an object if one exists. We incorporate this point supervision along with a novel objectness potential in the training loss function of a CNN model. Experimental results on the PASCAL VOC 2012 benchmark reveal that the combined effect of point-level supervision and objectness potential yields an improvement of 12.9% mIOU over image-level supervision. Further, we demonstrate that models trained with point-level supervision are more accurate than models trained with image-level, squiggle-level or full supervision given a fixed annotation budget.

	</ul>
	</td>
</tr>
<tr id="rev_Bearman" class="review noshow">
	<td colspan="7"><b>Review</b>: 
	<ul>
	  <li> </li>
	</ul></td>
</tr>
</tbody>
</table>

https://github.com/mrgloom/Semantic-Segmentation-Evaluation
