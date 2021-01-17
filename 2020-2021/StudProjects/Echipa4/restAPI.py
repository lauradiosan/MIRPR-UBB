import base64
import json
import numpy as np

from ai.landscape_detection.load_model import load_model
from ai.landscape_detection.make_model import IMG_HEIGHT, IMG_WIDTH, CLASS_NAMES
from ai.landmark_detection.service.landmark_service import LandmarkService
import tensorflow as tf

from flask import Flask, request
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS, cross_origin

from textUtils import getVector

PIK = "data/pickle.dat"

with open(PIK, "rb") as f:
    [google_model, [tfidf_featureDescription, tfidf_listDescription, tfidf_vectorsDescription],
     [tfidf_featureTitle, tfidf_listTitle, tfidf_vectorsTitle]] = pickle.load(f)

app = Flask("JepiiMici")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

df = pd.read_csv("BestDataset2.csv")
df['average_rate_per_night'] = df['average_rate_per_night'].str.replace('$', '')
df['average_rate_per_night'] = df['average_rate_per_night'].str.replace(',', '')
landscape_detection_model = load_model()
landmarkServ = LandmarkService()


def landscape_prediction(image: str) -> str:
    def __decode_img(img: str):
        with open('decoded_image.png', 'wb') as file_to_save:
            img = base64.decodebytes(img.encode('utf-8'))
            file_to_save.write(img)
            img = tf.io.decode_image(img, channels=3)
            img = tf.image.resize(img, (IMG_HEIGHT, IMG_WIDTH))
            return img

    image = __decode_img(image)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)

    predictions = landscape_detection_model.predict(image)
    scores = tf.nn.softmax(predictions[0])

    prediction = CLASS_NAMES[np.argmax(scores)]
    score = "{:.3f}".format(np.max(scores) * 100)

    print(f"Predicted image is {prediction} with {score}.")
    return prediction


def landmark_prediction(image: str) -> str:
    landmark = landmarkServ.predict(image)
    return landmark.name


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


def getRecommandation(description, city, picture, minBedrooms, budget, sliderValue):
    # recommmendation based on sliderValue
    img_importance = 0.5
    landscape = ''
    if picture:
        landscape = landscape_prediction(picture)
        print(landscape)

    desc = description.split()
    sent_vecDescription = getVector(desc, tfidf_featureDescription, tfidf_listDescription, google_model)
    sent_vecTitle = getVector(desc, tfidf_featureTitle, tfidf_listTitle, google_model)
    cosine_similaritiesDescription = cosine_similarity([sent_vecDescription], tfidf_vectorsDescription)
    cosine_similaritiesTitle = cosine_similarity([sent_vecTitle], tfidf_vectorsTitle)

    sim_scoresDescription = list(enumerate(cosine_similaritiesDescription[0]))
    sim_scoresDescription = [x if x[1] <= 1 else (x[0], 1.0) for x in sim_scoresDescription]

    sim_scoresTitle = list(enumerate(cosine_similaritiesTitle[0]))
    sim_scoresTitle = [x if x[1] <= 1 else (x[0], 1.0) for x in sim_scoresTitle]

    descImg = landscape.split()
    sent_vecDescriptionImg = getVector(descImg, tfidf_featureDescription, tfidf_listDescription, google_model)
    sent_vecTitleImg = getVector(descImg, tfidf_featureTitle, tfidf_listTitle, google_model)
    cosine_similaritiesDescriptionImg = cosine_similarity([sent_vecDescriptionImg], tfidf_vectorsDescription)
    cosine_similaritiesTitleImg = cosine_similarity([sent_vecTitleImg], tfidf_vectorsTitle)

    sim_scoresDescriptionImg = list(enumerate(cosine_similaritiesDescriptionImg[0]))
    sim_scoresDescriptionImg = [x if x[1] <= 1 else (x[0], 1.0) for x in sim_scoresDescriptionImg]

    sim_scoresTitleImg = list(enumerate(cosine_similaritiesTitleImg[0]))
    sim_scoresTitleImg = [x if x[1] <= 1 else (x[0], 1.0) for x in sim_scoresTitleImg]

    sim_scores = [(sd[0], (sd[1] + st[1]) * (1 - img_importance) + (sdi[1] + sti[1]) * img_importance) for sd, st, sdi, sti in
                  zip(sim_scoresDescription, sim_scoresTitle, sim_scoresDescriptionImg, sim_scoresTitleImg)]
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    places_indices = [i[0] for i in sim_scores]

    places = df[['description', 'title', 'url', 'average_rate_per_night', 'bedrooms_count', 'city']]
    recommend = places.iloc[places_indices]

    result = []
    for index, row in recommend.iterrows():
        if (city == '' or row['city'].lower() == city.lower()) and int(row['bedrooms_count']) >= int(minBedrooms) \
                and int(float(row['average_rate_per_night'])) <= int(budget):

            result.append(list(row))
            if len(result) == 10:
                break

    return json.dumps(result)


app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
