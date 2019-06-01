# ctpn_korean

***
- Reference <https://github.com/eragonruan/text-detection-ctpn>
***
# setup
- nms and bbox utils are written in cython, hence you have to build the library first.
```shell
cd utils/bbox
chmod +x make.sh
./make.sh
```
- If demo or train command(shown below) doesn't work than please setup again
***
# demo
- Follow setup to build the library 
- Download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- Put checkpoints_mlt/ in text-detection-ctpn/
- Put your images in data/demo, the results will be saved in data/res, and run demo in the root 
```shell
python ./main/demo.py
```
***
# training
- Follow setup to build the library 
- Download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- Put checkpoints_mlt/ in text-detection-ctpn/
- Download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)
## prepare data(using original data)
- Download the dataset we prepared from [google drive](https://drive.google.com/file/d/1npxA_pcEvIa4c42rho1HgnfJ7tamThSy/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1nbbCZwlHdgAI20_P9uw9LQ). put the downloaded data in data/dataset/mlt, then start the training.
## prepare data(using your own data)
- Also, you can prepare your own dataset according to the following steps. 
- Prepare your own dataset(images) in (your_path)/image and annotation files(.txt files) in (your_path)/label
(Annotation file format can be found in [gt_img_859.txt](https://github.com/HONUBIN/ctpn_korean/tree/master/data/readme/gt_img_859.txt). The format is x1,y1(left top),x2,y2(right top),x3,y3(right bottom),x4,y4(left botton),language tag,object tag.)
- Annotation file's name must be gt_(image).txt (if image file's name is img_1 than annotation file must be gt_img_1.txt.)
- Modify the DATA_FOLDER in utils/prepare/split_label.py according to your dataset(your_path). And run split_label.py in the root
```shell
python ./utils/prepare/split_label.py
```
- It will generate the prepared data in data/dataset/mlt


## train 
- Modify parameters(learning rate, max_steps(=epoch), ...) in main/train.py(line 13-24)
- Because pre-trained weight was saved at 50000, max_steps must be larger than 50000(The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.)
```shell
python ./main/train.py
```
***
- No train logs displayed until the end of training in Window-10(linux is fine)
