# ==============================================================================
# purpose: experiments with the Amazon ML service
# author: tirthankar chakravarty
# created: 15/6/15
# revised: 
# comments:
# 1. Download the zip file containing the data from the UCI data repository:
#   http://mlr.cs.umass.edu/ml/machine-learning-databases/00222/
# 2. Extract the files to a local location, and make the change of the target variable encoding
# 3. Create a new S3 bucket to hold the data and the data schema
# 4. Change the permissions on the S3 bucket resource to allow the current IAM user to get
#   and list objects from the bucket
# 5. Change the current IAM user's permissions to allow using the ML service using the API
# 6. During the creation of the data source, create a separate scoring dataset, for model evaluation
# 7. Create a bucket to store the outputs.
# Notes:
# 1. There is no option to respecify the data source characteristics, even in the console
#   Any failure of the data to load means starting from the beginning.
# 2. Limited by the number of models that can be built.
# 3. Is there any way to increase the speed of the training? Since we do not know the algorithm that was
#   used, I cannot be sure whether it should be taking this much time or not.
#==============================================================================

import boto.s3 as s3
from boto.s3.key import Key
import boto.machinelearning as ml
from zipfile import ZipFile
import pandas as pd
import numpy as np
import boto.iam as iam
import json

# unzip the CSV files
zip_bank = ZipFile("Data/bank_marketing/bank.zip")
zip_bank.extractall("Data/bank_marketing/")
df_bank = pd.read_csv("Data/bank_marketing/bank-full.csv", sep=";")
df_bank["y"] = df_bank["y"].apply(lambda x: 1 if x == "yes" else 0)
# np.mean(df_bank["y"])
df_bank[["y", "age", "job", "marital", "education", "loan", "campaign", "duration"]].to_csv(
    "Data/bank_marketing/bank_marketing.csv", sep=",", header=False, index=False)

# create a new S3 bucket and upload the data
conn = s3.connect_to_region("us-east-1")
bucket_ml = conn.create_bucket("ml_experiment_tc")
key_bank_marketing = Key(bucket_ml)

# save the data
key_bank_marketing.key = "data_bank_marketing"
key_bank_marketing.set_contents_from_filename("Data/bank_marketing/bank_marketing.csv")

# save the schema
key_bank_marketing.key = "schema_bank_marketing"
key_bank_marketing.set_contents_from_filename("Data/bank_marketing/bank_marketing.csv.schema")

# grant ML service permissions to the bucket
iam_tc = iam.IAMConnection()
policy_ml_s3 = {
    "Version": "2008-10-17",
    "Statement": [{
                      "Effect": "Allow",
                      "Principal": {"Service": "machinelearning.amazonaws.com"},
                      "Action": "s3:GetObject",
                      "Resource": "arn:aws:s3:::ml_experiment_tc/*"
                  },
                  {
                      "Effect": "Allow",
                      "Principal": {"Service": "machinelearning.amazonaws.com"},
                      "Action": "s3:ListBucket",
                      "Resource": "arn:aws:s3:::ml_experiment_tc"
                  }]
}
json_policy_ml = json.dumps(policy_ml_s3, indent=2)
bucket_ml.set_policy(json_policy_ml)

# grant the current user the permissions to use the ML services via API
policy_ml_ml = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "machinelearning:Create*",
                "machinelearning:Describe*",
                "machinelearning:Delete*",
                "machinelearning:Get*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
iam_tc.put_user_policy(user_name="tirthankarc@fractalanalytics.com",
                       policy_name="ml_experiment_ml",
                       policy_json=json.dumps(policy_ml_ml, indent=2))

# create a new datasource
conn_ml = ml.connect_to_region("us-east-1")
ds_ml_experiment = conn_ml.create_data_source_from_s3(
    data_source_id="ml_experiment_14",
    data_spec={"DataLocationS3": "s3://ml_experiment_tc/data_bank_marketing",
               "DataSchemaLocationS3": "s3://ml_experiment_tc/schema_bank_marketing"},
    data_source_name="Data source for first AWS ML classification example",
    compute_statistics=True)
conn_ml.get_data_source(data_source_id=ds_ml_experiment["DataSourceId"])
# [conn_ml.delete_data_source(data_source) for data_source in ["ml_experiment_%s" % num for num in range(1, 10)]] # delete failed attempts

# create a simple machine learning model
model_1 = conn_ml.create_ml_model(ml_model_id="ml_experiment_model_3", ml_model_name="First classification model using AWS ML",
                     ml_model_type="BINARY", training_data_source_id="ml_experiment_14")
# conn_ml.describe_ml_models()
conn_ml.describe_data_sources()
conn_ml.get_ml_model(ml_model_id="ml_experiment_model_3")
model_evaluation_1 = conn_ml.create_evaluation(evaluation_id="ml_experiment_evaluation_1",
                                               ml_model_id="ml_experiment_model_3",
                                               evaluation_data_source_id="ml_experiment_14")
conn_ml.get_evaluation(evaluation_id="ml_experiment_evaluation_1")