# Emotive Image Blog Generator

An application that generates emotion-focused blog posts from uploaded images using AWS services like Amazon Rekognition and Amazon Bedrock.

## Overview

The Emotive Image Blog Generator is a serverless application that analyzes images to detect objects, scenes, and text, and then uses AI to generate emotionally engaging blog posts based on the image content. The application leverages AWS services including:

- **Amazon S3**: Stores uploaded images
- **AWS Lambda**: Processes images and generates blog content
- **Amazon Rekognition**: Detects labels and text in images
- **Amazon Bedrock**: Generates creative blog content using AI models

## Architecture

The application follows a serverless architecture pattern:

1. Images are uploaded to an S3 bucket
2. A Lambda function is triggered to process the image
3. The Lambda function uses Amazon Rekognition to analyze the image content
4. The Lambda function uses Amazon Bedrock to generate a blog post based on the image analysis
5. The generated blog post is returned to the user

## Project Structure

motive-image-blog-generator/ <br>
├── cdk/ # AWS CDK infrastructure code <br>
│ ├── cdk/ <br>
│ │ ├── backend/ # Backend infrastructure stacks <br>
│ │ │ └── create_backend_process_stack.py <br>
│ │ ├── configs/ # Configuration files <br>
│ │ │ ├── config.py <br>
│ │ │ └── props.json <br>
│ │ └── lambda_code/ # Lambda function code <br>
│ ├── app.py # CDK application entry point <br>
│ ├── requirements.txt # Python dependencies for CDK <br>
│ └── requirements-dev.txt # Development dependencies <br>


## Prerequisites

- AWS Account
- AWS CLI configured with appropriate credentials
- Python 3.9 or higher
- Node.js 14.x or higher (for AWS CDK)
- AWS CDK installed globally (`npm install -g aws-cdk`)

## Configuration

The application is configured using the `props.json` file in the `cdk/cdk/configs/` directory. The current configuration includes:

- Project prefix: "Emotive Image Blog Generator"
- S3 bucket name: "emotive-image-to-blog-generator-input-bucket" ```Modify with unique bucket name``` 
- Default image key: "20230910_165848.jpg" ```Update image name with extension``` 
- Amazon Bedrock model: "amazon.nova-micro-v1:0" ```Consider any genAI Model``` 

## Deployment

1. Set up your AWS environment variables:
   ```bash
    export AWS_ACCOUNT=your-aws-account-id
    export AWS_REGION=your-preferred-region
    export CDK_DEFAULT_ACCOUNT=your-aws-account-id
    export CDK_DEFAULT_REGION=your-preferred-region

2. Install the required dependencies:
    ```bash
        cd cdk
        pip install -r requirements.txt

3. Synth and Deploy the CDK stack:
    ```bash
        cdk synth
        cdk deploy

## Usage
Upload an image to the S3 bucket:

    aws s3 cp path/to/your/image.jpg s3://emotive-image-to-blog-generator-input-bucket/


Trigger Lambda function to process the image and generate a blog post.

Retrieve the generated blog post from the Lambda function output.

## Security
The application implements several securities best practices:

- S3 bucket with blocked public access

- S3 bucket with server-side encryption

- SSL enforcement for S3 bucket

- IAM permissions following the principle of least privilege

## Development
To set up the development environment:

Install dependencies:

    pip install -r requirements.txt
    pip install -r requirements-dev.txt

## Future Scope

### S3-Event Driven Architecture
The current implementation requires manual triggering of the Lambda function. Future enhancements will include:

- **S3 Event Notifications**: Configure automatic Lambda function triggers when new images are uploaded to the S3 bucket
- **Amazon EventBridge**: Implement event-driven workflows for more complex processing pipelines
- **AWS Step Functions**: Orchestrate multi-step processing workflows for more complex blog generation scenarios

### Frontend Application
Develop a user-friendly web application to interact with the blog generation service:

- **React/Vue.js Frontend**: Create an intuitive UI for image uploads and blog viewing
- **Amazon Amplify**: Host and deploy the frontend application with CI/CD capabilities
- **Amazon Cognito**: Add user authentication and authorization
- **API Gateway**: Create RESTful APIs to interact with the backend services

### Enhanced Features
- **Blog Management**: Save and manage generated blogs in a database (Amazon DynamoDB)
- **Image Gallery**: Display previously uploaded images and their generated blogs
- **Social Sharing**: Add capabilities to share generated blogs on social media platforms
- **Custom Styling**: Allow users to customize the appearance and style of generated blogs
- **Multiple Language Support**: Generate blogs in different languages using Amazon Translate

### Performance Optimizations
- **Image Preprocessing**: Implement image optimization before analysis
- **Caching**: Add caching mechanisms for frequently accessed content
- **Serverless Architecture Enhancements**: Optimize Lambda functions for cost and performance

This roadmap will transform the application from a basic proof-of-concept into a fully-featured, production-ready blog generation platform with a seamless user experience.

### Automated Testing Framework
Implement comprehensive automated testing to ensure reliability and quality:

- **Unit Testing**: Develop unit tests for Lambda functions using pytest to verify individual components
- **Integration Testing**: Create integration tests to validate the interaction between services
- **Infrastructure Testing**: Implement CDK testing using tools like cdk-nag to validate infrastructure compliance
- **Mock Services**: Use moto or localstack to mock AWS services for testing without incurring costs
- **Test Automation**: Set up CI/CD pipelines with GitHub Actions or AWS CodePipeline for automated test execution
- **Test Coverage Reports**: Generate and maintain test coverage reports to identify untested code paths
- **Property-Based Testing**: Implement property-based testing for handling various image types and content
- **Performance Testing**: Create benchmarks and load tests to ensure the system scales appropriately
- **Security Testing**: Implement automated security scanning for infrastructure and code
- **Regression Testing**: Build regression test suites to prevent reintroduction of fixed bugs

## License
See the LICENSE file for details.


    This README provides a comprehensive overview of your Emotive Image Blog Generator project, including its architecture, setup instructions, and usage guidelines. You can customize it further based on additional details about your project.

