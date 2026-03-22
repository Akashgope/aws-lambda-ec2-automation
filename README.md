# Automated EC2 Instance Management with AWS Lambda and Boto3

## Objective
Automatically stop EC2 instances tagged `Auto-Stop` and start instances tagged `Auto-Start` using an AWS Lambda function.

## Steps Followed

### 1. EC2 Setup
- Launched two `t2.micro` instances in the `ap-south-1` (Mumbai) region.
- Tagged the first instance with **Key = `Action`**, **Value = `Auto-Stop`**.
- Tagged the second instance with **Key = `Action`**, **Value = `Auto-Start`**.


**Screenshot:**  
<img width="1630" height="794" alt="Screenshot 2026-03-22 at 2 21 50 PM" src="https://github.com/user-attachments/assets/632e883c-6c1f-46b8-99f7-2c0c72467e1c" />

<img width="1662" height="813" alt="Screenshot 2026-03-22 at 2 23 24 PM" src="https://github.com/user-attachments/assets/5778b0c0-bbd6-480b-93e7-d8d5fbb209eb" />


### 2. IAM Role for Lambda
- Created an IAM role named `LambdaEC2ManagementRole`.
- Attached policies:
  - `AmazonEC2FullAccess` – to describe, stop, and start EC2 instances.
  - `AWSLambdaBasicExecutionRole` – to write logs to CloudWatch.

**Screenshot:**  
<img width="1674" height="785" alt="Screenshot 2026-03-22 at 2 27 30 PM" src="https://github.com/user-attachments/assets/4a312dd9-e8f9-4d47-bcd3-446a08bb01e0" />


### 3. Lambda Function
- Runtime: Python 3.14.
- Timeout set to 1 minute.
- Code: See `lambda_function.py` in this repository.

The function:
- Uses `boto3` to filter EC2 instances by the `Action` tag.
- Stops instances with value `Auto-Stop`.
- Starts instances with value `Auto-Start`.
- Logs the instance IDs affected.

### 4. Testing
- Manually invoked the Lambda function.
- Verified in EC2 console that the `Auto-Stop` instance stopped and the `Auto-Start` instance started (or remained running if already started).

**Screenshot:**  
<img width="1682" height="621" alt="Screenshot 2026-03-22 at 2 28 39 PM" src="https://github.com/user-attachments/assets/ab49e48a-3cd0-4733-a680-405bd08ad4e9" />
 
<img width="1427" height="76" alt="Screenshot 2026-03-22 at 2 31 09 PM" src="https://github.com/user-attachments/assets/70297d58-a8bc-4628-aa06-ace7273c7808" />


## Code
The Lambda function code is available in [`lambda_function.py`](lambda_function.py).

## Conclusion
The automation works as expected. This demonstrates how Lambda can manage EC2 instances based on tags.
