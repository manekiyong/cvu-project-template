# cvu-project-template

## Project Structure

### Repository Root
1) Linting + Pre-commit hooks
    ```
    # It’s recommended to use a virtual or conda environment for this.
    # However, if your pre-commit setup is consistent across projects,
    # installing it in your base Python environment is fine.
    pip install -r requirements-dev.txt
    pre-commit install
    ```
2) `.gitignore`:
    - Add rules to exclude files that should not be committed to GitHub — for example, `.pt`, `.bin`, or `.safetensors` model files, as well as the `data/` folder.

3) `build/.env`
    - Specify the image name and version here.
    - Include all global environment variables such as port numbers, project names, and other configuration values.

4) `build/docker-compose.yaml`
    - Use `docker-compose` to define resources (e.g. memory, GPU), ports, and volumes. This helps streamline conversion into Helm charts for later deployment.
    - If GPU support is needed, indicate it explicitly; otherwise, omit it.
    - It’s much cleaner to run `docker compose up` than to memorize long `docker run` commands.
    - You can also volume-mount source code for rapid experimentation.

5) `README.md`
    - Refer to [below](#actual-readme-structure)

### Components Folder
1) `component_x/build/requirements.txt`
    - Exclude libraries already provided by the base image to prevent dependency conflicts (e.g. remove `torch`, `torchvision`, etc. if using a PyTorch base image).
    - Align your `transformers` version with the corresponding `torch` version so that `transformers` does not trigger a reinstallation of `torch`.

2) `component_x/build/Dockerfile`
    - Set the base image in the `FROM repository/image:tag` line.
    - If PyTorch is required, use a torch-runtime image; otherwise, use a `python:slim` image.
    - _(Optional)_ Add extra setup steps such as building packages from wheels.
    - Set `WORKDIR` to the script’s directory.
    - Define the `CMD` to start the service.

3) `component_x/build/.env`
    - Specify the image name and version.
    - Include all **component-specific** environment configurations here.


### Source Codes
1) `component_x/src/main.py`
    - `main.py` should implement a FastAPI service exposing the component’s functionality.
    - Document the available endpoints and HTTP methods (`GET`, `POST`, etc.) in `README.md`, along with example request bodies.

2) `tests/test.py`
    - It’s good practice to include test cases to verify that your functions and endpoints work correctly.
    - This file can also serve as a usage reference for calling your endpoints.

## Spinning Up Services
First time build:
```
cd build
docker-compose up -d --build
```

Subsequent runs (no rebuild):
```
cd build
docker-compose up -d
```

Notes:
- The -d flag runs docker-compose in detached mode (it returns control to your terminal once containers are up).
- To list containers, run docker ps -a — the container name appears under the NAMES column.
- After identifying your container, you can run commands inside it using docker exec.


----------------------------------------
----------------------------------------
----------------------------------------
# Actual README Structure
----------------------------------------
----------------------------------------
----------------------------------------

# Project Name

Write project description here. Describe some of its features too. You may also indicate any pre-requisite this project might have (e.g., assume that the database is hosted elsewhere etc)

## Quick Start

Inform users on what to configure. Some examples include:
- Downloading & placing of model weights
- Configuring the environment variables


## API Usage
Details of each of the endpoints, how they can be used and what is the required body.
