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

Assuming someone already has conda (either Anaconda or Miniconda) installed on their local machine, the simplest way to replicate the environment used for this geospatial backend development test is to use the `environment.yml` file provided in the root directory of this repository. The environment can be created with all necessary packages installed by running the following command:

`conda env create -f environment.yml`

**NOTE:** a similar virtual environment could be configured manually using pip or conda. For example, one can first install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) using their installation instructions for either Windows, Mac or Linux machines. Then with conda installed, run these commands to create an environment and install the packages:

1. Create a conda virtual environment:
`conda create -n backend-test`

2. Activate the virtual environment:
`conda activate backend-test`

3. Install required packages:
`conda install -c conda-forge pydantic pytest geopandas fastapi uvicorn`

## Application Execution



## Automated Tests

