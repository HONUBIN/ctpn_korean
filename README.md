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
- Put checkpoints_mlt/ in ctpn_korean/
- Put your images in data/demo, the results will be saved in data/res, and run demo in the root 
```shell
python ./main/demo.py
```
***
# training
- Follow setup to build the library 
- Download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- Put checkpoints_mlt/ in ctpn_korean/
- Download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)

## prepare data(using korean subtitle data)
- Put mlt directory to data/dataset/

## prepare data(using your own data)
- Also, you can prepare your own dataset according to the following steps. 
    1. Prepare your own dataset(images) in data/dataset/own/image
    2. Prepare annotation files(.txt files) in data/dataset/own/label (Annotation file format can be found in [gt_img_859.txt](https://github.com/HONUBIN/ctpn_korean/tree/master/data/readme/gt_img_859.txt). The format is x1,y1(left top),x2,y2(right top),x3,y3(right bottom),x4,y4(left bottom),language tag,object tag. Annotation file's name must be gt_(image).txt)
    3. You can make annotation files by following steps
        1. Using [Vgg Image Annotator 1.0.1](https://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.1.html)
        2. Load images (Image - Load or Add images)
        3. Boxing objects (Mouse dragging)
        4. Save json file to data/dataset/own/label (Annotation - Save as Json, do not change file name)
        5. Convert json to train.txt
            ```shell
            python ./data/dataset/own/label/parser.py
            ```
        6. Convert train.txt to annotation files (gt_(image).txt)
            ```shell
            python ./data/dataset/own/label/change_cordinate.py
            ```
        
    4. Modify the DATA_FOLDER in utils/prepare/split_label.py to data/dataset/own/. And run split_label.py in the root
        ```shell
        python ./utils/prepare/split_label.py
        ```
        - It will generate the prepared data in data/dataset/mlt


## train 
- Modify parameters(learning rate, max_steps(=epoch), ...) in main/train.py (line 13-24.)
- Because pre-trained weight was saved at 50000, max_steps must be larger than 50000 (The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.)
```shell
python ./main/train.py
```
- No train logs displayed until the end of training in Window-10 (linux is fine.)
***
