# fefare

## Feature Face Recognition using Eigenfaces method

### About fefare
`fefare` is the piece of software that serves primarily educational purposes. It was designed and implemented in the course of the Individual Project for the 4th semester of Warsaw University of Technology.

The tool is designed to classify images of faces using the Eigenfaces method (see Used Resources).

### Usage

The command `python fefare -h` will produce:

```bash
usage: [-h] [--version] [--part PART] [-c TRAIN TEST | --gui]

optional arguments:
  -h, --help            show this help message and exit
  --version, -ver, -v   the version of the software
  --part PART, -p PART  the share of the Eigenfaces to be used, float 0.0 - 1.0
  -c TRAIN TEST         run via text-based CLI, requires paths to training and
                        testing sets
  --gui, --GUI, -g      run via GUI
```

Launch from the console example:

```bash
$ python fefare -c datasets/google_photos/training_set datasets/google_photos/testing_set/photoman1.jpg
```
Output:
```
7 images loaded from datasets/google_photos/training_set/photoman2
7 images loaded from datasets/google_photos/training_set/photoman1
7 images loaded from datasets/google_photos/training_set/photoman3
Result: photoman1
```

Note: TRAIN parameter points to the directory in which N (N = 3 in the example above) other directories is stored, where N is the number of distinct people ("classes"). The more photos of the same person each of them contains, the better is the performance. TEST parameter points to a new face image, not from the training set.

Note: In order to see the Eigenfaces, the code must be opened in a IDE (e.g. PyCharm) since MatPlotLib is used.


### Used resources

* [A Comprehensive Guide To Facial Recognition Algorithm](https://www.baseapp.com/computer-vision/a-comprehensive-guide-to-facial-recognition-algorithms/)

* [Eigenfaces, for Facial Recognition](https://jeremykun.com/2011/07/27/eigenfaces/)

* [[Explanation] Face Recognition using Eigenfaces](http://laid.delanover.com/explanation-face-recognition-using-eigenfaces/)

* [Eigenfaces for Face Detection/Recognition](http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf)

* [KNN Algorithm - How KNN Algorithm Works With Example | Data Science For Beginners | Simplilearn](https://www.youtube.com/watch?v=4HKqjENq9OU&list=PLSKUQv7Cc75IgbbleL_69p9w54OhEhaLF&index=5&t=0s)

* [Principal Component Analysis (PCA)](https://www.youtube.com/watch?v=g-Hb26agBFg)

* [PCA 10: eigen-faces](https://www.youtube.com/watch?v=_lY74pXWlS8)
