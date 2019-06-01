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
- It will generate a nms.so and a bbox.so in current folder.
***
# demo
- follow setup to build the library 
- download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- put checkpoints_mlt/ in text-detection-ctpn/
- put your images in data/demo, the results will be saved in data/res, and run demo in the root 
```shell
python ./main/demo.py
```
***
# training
- follow setup to build the library 
- download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- put checkpoints_mlt/ in text-detection-ctpn/
- Download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)
## prepare data(using original data)
- Download the dataset we prepared from [google drive](https://drive.google.com/file/d/1npxA_pcEvIa4c42rho1HgnfJ7tamThSy/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1nbbCZwlHdgAI20_P9uw9LQ). put the downloaded data in data/dataset/mlt, then start the training.
## prepare data(using your own data)
- Also, you can prepare your own dataset according to the following steps. 
- Prepare your own dataset(images) and annotation files(.txt files)
(Annotation file format can be found in [gt_img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/gt_img_859.txt).)
- Modify the DATA_FOLDER and OUTPUT in utils/prepare/split_label.py according to your dataset. And run split_label.py in the root
```shell
python ./utils/prepare/split_label.py
```
- it will generate the prepared data in data/dataset/


## train 
- Modify parameters(learning rate, max_steps(=epoch), ...) of file 'main/train.py'(line 13-24)
- Because pre-trained weight is saved at 50000, max_steps must be larger than 50000(The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.)
```shell
python ./main/train.py
```
***
