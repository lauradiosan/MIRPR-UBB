Dataset structure:

* `train.csv`: CSV with id,url,landmark_id fields. `id` is a 16-character string, `url` is a string, `landmark_id` is an integer. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train.csv`](https://s3.amazonaws.com/google-landmark/metadata/train.csv)
* `train_clean.csv`: CSV with landmark_id,images fields. `landmark_id` is an integer, `images` is a space-separated list of string train image IDs. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_clean.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_clean.csv). Courtesy of team `smlyaka` (see [their paper](https://arxiv.org/abs/2003.11211)).
* `train_attribution.csv`: CSV with id,url,author,license,title fields. `id` is a 16-character string, and the other fields are strings of variable length. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_attribution.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_attribution.csv).
* `train_label_to_category.csv`: CSV with landmark_id,category fields: `landmark_id` is an integer, `category` is a Wikimedia URL referring to the class definition. Available at: [`https://s3.amazonaws.com/google-landmark/metadata/train_label_to_category.csv`](https://s3.amazonaws.com/google-landmark/metadata/train_label_to_category.csv).