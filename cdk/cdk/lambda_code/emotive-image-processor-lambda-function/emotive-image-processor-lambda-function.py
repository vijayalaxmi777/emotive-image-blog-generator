"""Function to process image and create a blog"""
import boto3
import json

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
bedrock = boto3.client('bedrock-runtime')


def lambda_handler(event, context):
    try:
        # ToDo: Event-Driven - Get bucket and key from the S3 event 
        # bucket = event['Records'][0]['s3']['bucket']['name']
        # key = event['Records'][0]['s3']['object']['key']
        bucket = event['bucket']
        key = event['image_key']
        model_id = event['model_id']

        # Call Rekognition to detect labels
        label_response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=10
        )

        # Detect text
        text_response = rekognition.detect_text(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}}
        )

        # Process and combine results
        labels = [label['Name'] for label in label_response['Labels']]
        texts = [text['DetectedText'] for text in text_response['TextDetections'] if text['Type'] == 'WORD']

        # Prepare prompt for Bedrock
        prompt = f"Create a beautiful memory in 300-400 words based on an image containing the following elements:\n\nLabels: {', '.join(labels)}\n\nDetected Text: {', '.join(texts)}\n\nMake it emotional and vivid, incorporating both the visual elements and any text found in the image."

        # Prepare the request body
        request_body = {
            "messages": [
                {
                    "role": "user",
                    "content":
                    [
                        {"text": prompt}
                    ]
                }
            ]
        }

        # Invoke the model
        response = bedrock.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )

        # Parse and return the response
        response_body = json.loads(response['body'].read())
        # print(response_body)
        generated_prompt = response_body["output"]['message']['content'][0]['text']
        print(generated_prompt)

        return {
            'statusCode': 200,
            'body': json.dumps({'memory': generated_prompt})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
