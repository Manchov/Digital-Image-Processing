
# Digital Image Processing Course Homework

This repository contains the homework assignments completed for a Digital Image Processing course. Below are descriptions and instructions for each script included in the repository.

## CompassOperator.py
**Purpose:** Implements edge detection using the Compass operator.
**Details:**
- Applies different directional masks to an input image to detect edges.
- Displays the image with detected edges.

## index.py
**Purpose:** Indexes images by extracting features.
**Details:**
- Processes each image in the specified dataset to calculate and store features.
- The features are serialized and stored in an index file for later retrieval.

## search.py
**Purpose:** Searches for images based on indexed features.
**Details:**
- Loads the serialized index file.
- Uses the features to perform searches within the dataset to find images with similar features.

## thresh.py
**Purpose:** Applies binary thresholding to images.
**Details:**
- Reads each image from a specified directory, applies a binary threshold, and saves the results.
- Useful for preprocessing images for further analysis or feature extraction.

### Usage
To use these scripts, you will need Python 2.7 and OpenCV installed on your system. Each script can be run from the command line, and you must provide necessary arguments as specified in the scripts.

```bash
python CompassOperator.py --image path_to_image
python index.py --dataset path_to_dataset
python search.py --dataset path_to_dataset --index path_to_index_file
python thresh.py --dataset path_to_dataset
```

Make sure to replace `path_to_image`, `path_to_dataset`, and `path_to_index_file` with actual paths to your files.
