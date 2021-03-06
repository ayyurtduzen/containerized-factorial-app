# containerized-factorial-app
This app calculates the factorial of non-negative integers.

## Technical Details
- Python version 3.8.6
- Alpine version 3.12


## Manuel Steps
- To run in local:
    - First, go to the repository path (you should be in the path with Dockerfile)
    - Build the Dockerfile with `docker build -t factorial-calculator .`
    - Then, run the with `docker run -it factorial-calculator`

- To work in AWS,
    - First, you should make Docker login to ECR repo created with Terraform in `aws-infra` repository
        * `aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 422689644012.dkr.ecr.eu-west-1.amazonaws.com`
    - Then, built the image:
        * `docker build -t factorial-calculator .`
    - Tag the image with latest:
        * `docker tag factorial-calculator:latest 422689644012.dkr.ecr.eu-west-1.amazonaws.com/factorial-calculator:latest`
    - Push the image to ECR repo:
        * `docker push 422689644012.dkr.ecr.eu-west-1.amazonaws.com/factorial-calculator:latest`,

    - You can otomatize those steps by writting the code same codes in a Jenkins file (or any CI/CD tool) 