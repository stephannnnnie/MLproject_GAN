# GAN for self-driving data argumentation

#### This is the final project of the CS 405: Machine Learning

November 10, 2021
## Introduction

     As a popular hot-spot issue, the lack of training data for self-driving cars or autonomous cars is a tough problem. With such problems, much research has been conducted on data argumentation, among which GAN is an ideal method to generate a bunch of proper datasets in many situations according to limited images.  
     
​	  Based on the guided essays, we attempted to implement the UNIT model, which is an unsupervised Image-to-Image translation network. The model aims to learn the joint distribution of images in different domains by using images from the marginal distributions in individual domains. However, we identified that there are still some areas that require further attention. Firstly, we can broaden the application aspects of the models. Secondly, we were inspired by starGAN to make our training multi-domain to increase efficiency. Thirdly, we still seek to generate more precise and realistic images, and we are exploring appropriate methods to achieve this goal.

    Our team comprises Dengheng Shi, Yilin Hou, Tongshu Pang and Chenlu Huang.

## Research Question 

​	  To solve the problem of unknown situations in self-driving which might affect the performance of the perception module in self driving and result in dangerous accident, a reliable detection of those situations is studied. That's using data argumentation to create more conditions for the model to be trained. 


​	  With the use of GAN, data argumentation provides more chances and possibilities to represent more abundant and precise results.  In [1], GAN is said to be impressive and can capture subtle expressions. Compared to the application in autonomous driving, GAN is commonly used in image-to-image translation for style transfer. For AD, the system must be highly robust and requires a training model with all possible real-life scenarios. The use of  GAN can create realistic datasets to improve the performance of the  model.  


​	  Therefore, our research will now be based on the study of data argumentation with GAN and will raise our ideas and suggestions as much as possible.

## Research goals

1. In the baseline of the code UNIT: Unsupervised Image-to-Image Translation, the images of  different seasons and different time in a day are generated. We hope we can create more similar images in other circumstances, which might be rare for now. For example, the situation of extreme weather------ drought, hurricane, rainstorm, frost. Or the situation of coming across crowds, children, animals...
   
2. What we want to achieve also consists of generating more precise and realistic images for AD system. The images generated now might be not so precise when the situation is complicated. For example, the reconstruction of traffic sign might not be clear and the  poles on the side of the street might be curved. Here is an example comparison of original generation and the expected images. In the final generated images, there are many details updated and except some little distortion on the lines, the images are relatively clear.

3. Last but not least, we hope we can use better models for increasing the efficiency of training. In detail, it's expected to get more types of images during the same training time for the model.  We are now inspired by a model called starGAN. To handle multiple domains, cross-domain models should be built for every pair of image domains. StarGAN is capable of learning mappings among multiple domains using a single generator[2]. The figure represents a star topology connecting multi-domains. So we can reach a better performance in relatively shorter time than simply use a cross-domain models when we want to generate more images from different aspects.


## Reference

[1] Uřičář, Michal, Křížek, Pavel,  Hurych, D. ,  Sobh, I. ,  Yogamani, S. , &  Denny, P. . (2019). Yes, we gan: applying adversarial techniques for autonomous driving. Electronic Imaging.

[2] Choi, Y. ,  Choi, M. ,  Kim, M. ,  Ha, J. W. , &  Choo, J. . Stargan: unified generative adversarial networks for multi-domain image-to-image translation.




