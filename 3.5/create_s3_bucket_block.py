import json
from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


# prefecthq.github.io/prefect-aws/s3
def load_credential():
    # run in prefect-mlops-zoomcamp folder
    with open("./3.5/creds.json", "r") as f:
        creds = json.load(f)
    return creds


def create_aws_creds_block():
    creds = load_credential()

    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id=creds["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=creds["AWS_SECRET_ACCESS_KEY"],
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="kade-mlops-zoomcamp-2023",
        credentials=aws_creds,
    )
    my_s3_bucket_obj.save(name="s3-bucket-block", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
