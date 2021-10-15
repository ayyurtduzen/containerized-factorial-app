# containerized-factorial-app
This app calculates the factorial of non-negative integers.

## Technical Details
- Python version 3.8.6
- Alpine version 3.12


## Manuel Steps
- To run in local:
    - First, build the Dockerfile with ```
    - Then, run the with ``

- To work in AWS,
    - First, you should make Docker login to ECR repo created with Terraform in `aws-infra` repository
        * `aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 422689644012.dkr.ecr.eu-west-1.amazonaws.com`
    - Then, built the image:
        * `docker build -t factorial-calculator-ecr .`
    - Tag the image with latest:
        * `docker tag factorial-calculator-ecr:latest 422689644012.dkr.ecr.eu-west-1.amazonaws.com/factorial-calculator-ecr:latest`
    - Push the image to ECR repo:
        * `docker push 422689644012.dkr.ecr.eu-west-1.amazonaws.com/factorial-calculator-ecr:latest`,

    - You can otomatize those steps by writting the code same codes in a Jenkins file (or any CI/CD tool) 