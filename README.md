# The Expression - CMPT 419 Project
An Emotional Game for Social Expression Learning

![Demo](Demo.png)

## Requirements
- A webcam

## Dependencies
All the requirement dependencies are listed in requirements.txt

## Structure
Repository structure
- the-expression.py is a driver to run the game. <br>
- Model/model.ipynb is a notebook to test and do experimential with the proposed models, only the VGG16-VA was integrated to the main game. <br>
- Dataset folder contains all the code to process the AFEW-VA dataset, from restructuring original AFEW-VA dataset to extracted facial expressions and packing them into a single h5 file. <br>
- Game_Data/target_samples is the folder for customized target images, the images have to be processed using Dataset/game_target_generator.py before put in to this folder. (refering to Dataset/README.md for more details) <br>

The processed AFEW-VA dataset can be found [here](https://tinyurl.com/AFEW-VA-processed), the link included: <br>
- A trained model of VGG16 transfer learning structure "trained_VGG16-VA.h5"
- An image dataset packed into h5 "facial_data.h5" (the README.md in the dataset folder has more details to unpack this file)
- The true labels from AFEW-VA "label_data.csv"

## How to Use
- Install dependencies
```bash
pip install -r requirements.txt
```
- To play
```bash
python the-expression.py
```

## Supported OS
Python version 3.7.8 on

- Windows 10 <br>
- Linux <br>
- MAC OS (Not tested) <br>

## Self-Evaluation
Overall, we think we have developed and fullfilled all the objectives that we proposed.
- About Game <br>
[:heavy_check_mark:] Game UI <br>
[:heavy_check_mark:] Music <br>
[:heavy_check_mark:] Animation <br>
- Machine Learning Model  <br>
[:heavy_check_mark:] Functional model <br>
[:heavy_check_mark:] Cross-validation <br>
- Dataset <br>
[:heavy_check_mark:] Processing <br>
[:heavy_check_mark:] 20 Self-annotation images <br>
[:heavy_check_mark:] Inter-rater score <br>

However, there are some changes that we have to make, specifically, in the beginning, we thought that our integrated facial landmark model could achieve a good score to be our main model but as a result, the facial landmark integrated model does not satisfy our goal, the predictions are too poor and because of the biased dataset, we have to change to transfer learning to improve the outcomes. Our VGG16-VA prediction is also not perfect, we think that if we are able to get the model training on AffectNet, it will be better but the AffectNet is very hard to get and there aren't many dataset with Arousal-Valence labels.

## Citing
All the game assets and musics in the game are not ours.

* Paimon - discord emoji. Emoji.gg - Discord, Slack &amp; Guilded emojis. (n.d.). Retrieved April 15, 2022, from https://emoji.gg/pack/9403-paimon 
* Free logo maker: Design custom logos | Adobe Express. (n.d.). Retrieved April 15, 2022, from https://www.adobe.com/express/create/logo 
* OpenMoji. (n.d.). Retrieved April 15, 2022, from https://openmoji.org/ 
* Twitch Frog Emotes. (n.d.).
* Face ID icon - face ID icon SVG Png image: Transparent png free download on seekpng. SeekPNG.com. (n.d.). Retrieved April 15, 2022, from https://www.seekpng.com/ipng/u2e6a9t4o0q8t4y3_face-id-icon-face-id-icon-svg/ 
* Royalty free music by BENSOUND. Bensound. (n.d.). Retrieved April 15, 2022, from https://www.bensound.com/ 
* Awesome Free assets for your next video project. Mixkit. (n.d.). Retrieved April 15, 2022, from https://mixkit.co/ 
* Free stock music: Download free music for videos. FiftySounds. (n.d.). Retrieved April 15, 2022, from https://www.fiftysounds.com/ 
