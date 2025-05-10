"""This stack is used to create S3 bucket to store an image,
lambda function to process this image and create a beautiful memory story based on it.
"""
from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_iam as iam,
)
from constructs import Construct
from ..configs.config import Config


class CreateBackendProcessStack(Stack):
    """Process image to create blog"""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        props = Config.deploy_environment()
        # Create an S3 bucket for storing images
        bucket = s3.Bucket(
            self,
            id="emotive-image-bucket-id",
            bucket_name=f"{props['input_bucket_config']['name']}",
            removal_policy=RemovalPolicy.DESTROY,  # For development; use RETAIN for production
            auto_delete_objects=False,  # For development; remove for production
            versioned=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
        )

        # Create a Lambda function for image processing
        image_processor_lambda = lambda_.Function(
            self,
            id="emotive-image-processor-id",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="emotive-image-processor-lambda-function.lambda_handler",
            code=lambda_.Code.from_asset("cdk/lambda_code/"),
            timeout=Duration.seconds(180),
            memory_size=256,
            environment={
                "bucket": f"{props['input_bucket_config']['name']}",
                "image_key": f"{props['input_bucket_config']['object_key']}",
                "model_id": f"{props['bedrock_model']['model_id']}"
            },
            function_name="emotive-image-processor-lambda-function"
        )

        # Grant the Lambda function permissions to read/write to the S3 bucket
        bucket.grant_read_write(image_processor_lambda)

        # Grant the Lambda function permissions to invoke bedrock model
        image_processor_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeModel"],
                resources=["*"],
            )
        )

        # Grant the Lambda function permissions with rekognition access
        image_processor_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                            "rekognition:DetectLabels",
                            "rekognition:DetectText"
                        ],
                resources=["*"],
            )
        )
