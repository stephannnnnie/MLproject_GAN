# GAN for self-driving data argumentation

#### This is the final project of the CS 405: Machine Learning

November 10, 2021

## Introduction

​	  As a popular hot-spot issue, the lack of training data for self-driving or autonomous cars is a tough problem. Facing such problems, much research has been conducted on data argumentation, among which GAN is an ideal method to generate a bunch of proper datasets in many situations according to limited images. 

​	In this project, we first do a lot of research on GAN, and we choose VAE-GAN, cGAN, and Star-GAN to conduct a deeper study. Finally, we successfully implement the above three models and  apply them to our dataset. In addition, we are trying to combine the VAE-GAN model and the Star-GAN model so that designing a model has the advantages of both the VAE-GAN and Star-GAN.

​	  Our team comprises Dengheng Shi, Yilin Hou, Tongshu Pang and Chenlu Huang.

## Research Question 

​	  To solve the problem of unknown situations in self-driving which might affect the performance of the perception module in self driving and result in dangerous accident, a reliable detection of those situations is studied. That's using data argumentation to create more conditions for the model to be trained. 


​	  With the use of GAN, data argumentation provides more chances and possibilities to represent more abundant and precise results.  In [1], GAN is said to be impressive and can capture subtle expressions. Compared to the application in autonomous driving, GAN is commonly used in image-to-image translation for style transfer. For AD, the system must be highly robust and requires a training model with all possible real-life scenarios. The use of  GAN can create realistic datasets to improve the performance of the  model.  


​	  Therefore, our research will now be based on the study of data argumentation with GAN and will raise our ideas and suggestions as much as possible.

## Research goals

* In the baseline of the code UNIT: Unsupervised Image-to-Image Translation, the images of  different seasons and different time in a day are generated. We hope we can create more similar images in other circumstances, which might be rare for now. For example, the situation of extreme weather------ drought, hurricane, rainstorm, frost. Or the situation of coming across crowds, children, animals... 

![image-20211118003642226](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/495bbdc4-bd9b-45bf-9207-fc0b22fd30e0)


* What we want to achieve also consists of generating more precise and realistic images for AD system. The images generated now might be not so precise when the situation is complicated. For example, the reconstruction of traffic sign might not be clear and the  poles on the side of the street might be curved. Here is an example comparison of original generation and the expected images. In the final generated images, there are many details updated and except some little distortion on the lines, the images are relatively clear. 

![image-20211118004534873](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/592be7f9-eb51-4a67-8aa7-aa8327dae346)


* Last but not least, we hope we can use better models for increasing the efficiency of training. In detail, it's expected to get more types of images during the same training time for the model.  We are now inspired by a model called starGAN. To handle multiple domains, cross-domain models should be built for every pair of image domains. StarGAN is capable of learning mappings among multiple domains using a single generator[2]. The figure represents a star topology connecting multi-domains. So we can reach a better performance in relatively shorter time than simply use a cross-domain models when we want to generate more images from different aspects.

![image-20211118004649129](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/f970f128-58b0-4e8c-b4fd-495ca5c6004a)

## Result
### starGAN
#####  Initial result on CelebA Dataset

We retrained the model on total iteration = 20000

(Origin image, black hair, gold hair, brown hair, male, old)

![image-20220108164432475](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/48c3f931-19dd-42af-826d-30654c07d14b)

##### Training process on our new dataset

- Iteration = 1000

<img src="https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/1cece0f6-936f-40e0-bedc-e726f2be40a8" alt="image-20220108165007945" style="zoom:300%;" />

- Iteration = 7000

![image-20220109195523167-16417293272405](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/efffe618-ed3b-416d-9e68-9082cbb9decb)

- Iteration = 14000
  
![image-20220109195549748-16417293527236](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/58f68fd8-76b9-4e85-bc9c-23c7caa12e33)

##### Final results

![image-20220109195622185-16417293860927](https://github.com/stephannnnnie/MLproject_GAN/assets/71458749/53ce2d47-3d79-444c-bf60-38fdf628c8b8)

## Reference

[1] Uřičář, Michal, Křížek, Pavel,  Hurych, D. ,  Sobh, I. ,  Yogamani, S. , &  Denny, P. . (2019). Yes, we gan: applying adversarial techniques for autonomous driving. Electronic Imaging.

[2] Choi, Y. ,  Choi, M. ,  Kim, M. ,  Ha, J. W. , &  Choo, J. . Stargan: unified generative adversarial networks for multi-domain image-to-image translation.
