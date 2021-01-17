# mirpr-jepiimici

Project contributors

* https://github.com/pbeltechi
* https://github.com/vivere-dally
* https://github.com/andreibangau99
* https://github.com/SurubariuRazvan


Find the best location based on user's input which can be anything from text, filters to images. Thepurpose of this is to offer best results to a specific search problem such as finding the best location foryour vacation.

This problem was a little bit challenging in the way of choosing the best algorithm to perform thesearch based on the input which can be numerical (price, no of bedrooms), string (description of thevacation, location), jpg image (user wants to visit something close with this photo) or voice (user canrecord the desired description of the holiday).

So, taking them one by one, we decided to use basic filtering for numerical input, a content-basedrecommendation system for string input, which recommends vacations to a user by taking the similarityof the descriptions of a vacation and for images we chose the pre-trained DELF (DEep Local Feature) module which was trained with Google-Landmarks data-set and basically describes each noteworthypoint in a given image with 40-dimensional vectors known as feature descriptor.

##### Datasets webpage:

* Data used for DELF can be found [here](https://github.com/cvdfoundation/google-landmark), and DELF TensorFlow Hub can be found [here](https://tfhub.dev/google/delf/1).

  * Dataset structure:

    * `train.csv`: CSV with id,url,landmark_id fields. `id` is a 16-character string, `url` is a string, `landmark_id` is an integer. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train.csv`](https://s3.amazonaws.com/google-landmark/metadata/train.csv)
    * `train_clean.csv`: CSV with landmark_id,images fields. `landmark_id` is an integer, `images` is a space-separated list of string train image IDs. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_clean.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_clean.csv). Courtesy of team `smlyaka` (see [their paper](https://arxiv.org/abs/2003.11211)).
    * `train_attribution.csv`: CSV with id,url,author,license,title fields. `id` is a 16-character string, and the other fields are strings of variable length. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_attribution.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_attribution.csv).
    * `train_label_to_category.csv`: CSV with landmark_id,category fields: `landmark_id` is an integer, `category` is a Wikimedia URL referring to the class definition. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_label_to_category.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_label_to_category.csv).
  * Dataset size:

    * There are around 761,757 images which can be downloaded separately in 100 TAR files, each of size ~850MB containing JPG-encoded images.
    * After resizing them to our needed dimension (256x256) there is around 11GB of images.
* Data used for Landscape Detection can be found [here](https://www.kaggle.com/puneet6060/intel-image-classification).

  * Dataset structure:
    * overall this dataset contains `~ 25k` images of size `150x150`
    * `seg_pred` contains a list with`7301` images that can be used for predictions
    * `seg_train` contains a folder for each label (buildings, forest, glacier, mountain, sea and street) each containing `~ 2191` files.
    * `seg_test` has the same structure as `seg_train`but it has fewer images`~ 437`
  * The glacier label is deleted since is not useful for this project
* Data used for text processing is based on AirBnB in various cities like: [Madrid](https://www.kaggle.com/rusiano/madrid-airbnb-data?select=listings_detailed.csv), [Melbourne](https://www.kaggle.com/tylerx/melbourne-airbnb-open-data?select=cleansed_listings_dec18.csv),
  [Stockholm](https://www.kaggle.com/liubacuzacov/stockholm-sweden-airbnb-listings?select=listings_detailed.csv), [Seattle](https://www.kaggle.com/airbnb/seattle?select=listings.csv), [Rio de Janeiro](https://www.kaggle.com/leonardopena/rio-de-janeiro-brazil-airbnb-data?select=listings.csv), [Tokyo](https://www.kaggle.com/fuyutaro/tokyo-airbnb-detailed-open-data?select=listings.csv), [London](https://www.kaggle.com/labdmitriy/airbnb?select=listings.csv), [LA](https://www.kaggle.com/oindrilasen/la-airbnb-listings)

  * Most of the datasests respect the following pattern: `main_dataset.csv`: CSV with the columns: `listing_id` - integer, `title` - string, `description` - string, `city` - string, `average_price_per_night` - float, `url` - string, `bedrooms_count` -integer
  * These datasets were filtered with different techniques like:
    * removing `65%` non-english words
    * removing only foreign words from sentences that contain only `35%` non-english words
    * removed `duplicate` rows, and those that conain `null` values
    * removed descriptions shorter than `10`
  * Dataset size:
    * There were around `120,000` rows in our dataset consisting of about `~ 350MB`.
    * After all the preprocessing we downsized the dataset down to `~78000` rows with the size of `~ 76MB`.


##### Workflow

A form is completed on the FrontEnd resulting in a POST Request with the following structure:

```
{
   "image": base64 encoded image,
   "budget": float,
   "city": string,
   "description": string,
   "minBedrooms": integer
}

```

After reaching the BackEnd, the image is first decoded and transformend into a Tensor which is then passed to the Image Processing algorithms (landscape classification and landmark detection). The results are then included in the title and description which goes to the text Processing algorithms.

The results are then filtered by a threshold and sent back to the FrontEnd. The result contains a link to the AirBnB Website.


##### Technologies used

* TensorFlow for most operations related to DELF. Reading images, resizing and shaping them
* NumPy
* Pandas
* Pillow
* peewee as our ORM for storing Landmarks and their features in a SQLite Database
* Keras for image classification
* Word2Vec and TF-IDF for text processing
* Flask
* Angular for our Frontend
* Jupyter Notebooks for presentations
* Pickle


##### Technologies examples

* TensorFlow image processing

```
    def prepare_image(self, image: bytes):
        image = tf.image.decode_jpeg(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize(image, DELF_IMG_QUERY_SIZE, antialias=True)
        return image
```

* DELF Querying

```
    delf_output = self.__delf_hub.signatures['default'](
        image=image,
        image_scales=self.__image_scales,
        score_threshold=self.__score_threshold,
        max_feature_num=self.__max_feature_num
    )
```

* Keras Model

```
Sequential([
        layers.experimental.preprocessing.RandomFlip("horizontal", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        layers.experimental.preprocessing.RandomRotation(0.1),
        layers.experimental.preprocessing.RandomZoom(0.1),
        layers.experimental.preprocessing.Rescaling(1. / 255),
        layers.Conv2D(16, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(NO_CLASSES)
    ])
```

* peewee ORM

```
sqlite_db = PooledSqliteDatabase(
    DB_PATH,
    max_connections=32,
    stale_timeout=300
)

class Entity(Model):
    class Meta:
        database = sqlite_db

```

* Flask endpoint

```
@app.route('/holiday-request', methods=['POST'])
@cross_origin()
def index():
    description = request.json.get('description', '')
    city = request.json.get('city', '')
    picture = request.json.get('picture', '')
    minBedrooms = request.json.get('minBedrooms', 0)
    budget = request.json.get('budget', 100000)
    sliderValue = request.json.get('sliderValue', '')
    return getRecommandation(description, city, picture, minBedrooms, budget, sliderValue)
```



##### Paper references

> ```
> @inproceedings{weyand2020GLDv2,
>   author = {Weyand, T. and Araujo, A. and Cao, B. and Sim, J.},
>   title = {{Google Landmarks Dataset v2 - A Large-Scale Benchmark for Instance-Level Recognition and Retrieval}},
>   year = {2020},
>   booktitle = {Proc. CVPR},
> }
> ```
