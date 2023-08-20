# Backend GIS Challenge
A simple coding challenge for Geospatial backend development using GeoJSON

- https://geojson.org/

## Requirements

Write a backend REST application with a single POST endpoint `/calculate_properties` to calculate Geojson Feature properties and return them to the user.  

- Accept a plain Geojson Feature (Polygon or Multipolygon).
- Return it back to the user with `properties` and `bbox` added, following GeoJSON standards for response format.
- The following `properties` should be included in the response:
  - `area` in sq meters
  - `centroid`
- Python 3.10+ must be used.
- Instructions should be provided for an evaluator to:
  - Run the app locally and exercise the endpoint.
  - Run any automated tests locally.
- Code should be in a git-clonable repo.

## How the challenge will be evaluated
- Code will be subjectively evaluated as per a normal Code Review for quality.
- Simple, valid requests should work locally.
- Automated tests should run locally and pass.
- Do not focus on edge cases or handling invalid inputs.
- Write code that you feel is production-quality in terms of 
  - Cleanliness
  - Organization
  - Automated Testing
  
**Suggested completion time is 1-4 hours.**

## Environment Installation

### Venv and Pip Install

The simplest and likely most popular method for setting up a Python virtual environment is with `Pip`. This avoids overhead with installation and package files that comes with using `Anaconda`, or even `Miniconda` (as documented below). You can execute this code using the basic `pip install` installation method, but first you will need to make sure `Pip` is installed on your machine and recommended to upgrade the pip version:

`python -m pip install --upgrade pip`

Then, you will need to create a virtual environment to install the appropriate libraries so that the backend service will run:

1. Make sure that the virtualenv library is installed:
`pip install virtualenv`

2. Create a new virtual environment called `venv` (this could be named anything):
`virtualenv venv`

3. Activate the virtual environment so that we install Python packages to it and not our base system installation:
`source venv/bin/activate`

Now that the virtual environment is active, you can install the required dependencies one of two ways:

1. Manually install using the `pip install` command for each library:
`pip install fastapi uvicorn geojson-pydantic pytest geopandas`

2. Use the provided `requirements.txt` file which will do the same thing:
`pip install -r requirements.txt`

### Conda Install

**NOTE:** Miniconda is the installlation method I used, as it was already installed on my system, but was tested using `virtualenv` as well.

Assuming someone already has conda (either Anaconda or Miniconda) installed on their local machine, the simplest way to replicate the environment used for this geospatial backend development test is to use the `environment.yml` file provided in the root directory of this repository. The environment can be created with all necessary packages installed by running the following command:

`conda env create -f environment.yml`

**NOTE:** depending on someones system, `environment.yml` files have been known to cause problems, so a similar virtual environment could be configured manually using pip (above) or conda (below). For example, one can first install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) using their installation instructions for either Windows, Mac or Linux machines. Then with conda installed, run these commands to create an environment and install the packages.

1. Create a conda virtual environment:
`conda create -n backend-test`

2. Activate the virtual environment:
`conda activate backend-test`

3. Install required packages:
`conda install -c conda-forge pydantic pytest geopandas fastapi uvicorn geojson-pydantic`

## Application Execution

`uvicorn main:app --reload`

`http://127.0.0.1:8000/docs`

## Automated Tests



## Future Considerations

* More robust object validation
* Unit tests for more edge cases
* Dynamic handling of CRS inputs/outputs
* Implementation of asynchronous API methods
* Determine other ways to optimize calculations