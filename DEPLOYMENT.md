# Deployment

This document provides instructions for deploying the Investment Report Generator using Docker.

## Docker - Build and Push

1. Docker Build

    Build the container with `latest` tag.

    ```shell
    docker build -t upsonic-investment-report-generator:latest .
    ```

2. Login

    ```shell
    docker login
    ```

3. Tag

    Tag the container to dockerhub registry.

    ! Do not forget to replace `$USERNAME` with your real username

    ```shell
    docker tag upsonic-investment-report-generator:latest $USERNAME/upsonic-investment-report-generator:latest
    ```

4. Push

    Push to official dockerhub container registry.

    ```shell
    docker push $USERNAME/upsonic-investment-report-generator:latest
    ```

## Docker - Pull and Run

1. Pull

    ```shell
    docker pull $USERNAME/upsonic-investment-report-generator:latest
    ```

2. Run

    ```shell
    docker run -p 8000:8000 \
        --env-file .env \
        --detach \
        $USERNAME/upsonic-investment-report-generator:latest
    ```

## Docker - Run with Compose

1. Create a `compose.yml` file.

    ```yaml
    services:
      investment-generator:
        build:
          context: .
          dockerfile: Dockerfile
        container_name: investment-generator
        env_file: .env
        ports:
          - 8000:8000
        volumes:
          - reports-data:/app/reports:rw

    volumes:
      reports-data:
        name: investment-report-generator-data
    ```

2. Up

    ```shell
    docker compose up -d
    ```
