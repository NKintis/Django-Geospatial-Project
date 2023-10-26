# Django-Geospatial-Project
**Description**
The Django Geospatial Project leverages pre-built containers and user inputs to streamline the download and processing of Sentinel images. Users select a container image, provide authentication credentials, and input values for the Sentinel image description. Once the image download and processing are complete, the refined data is seamlessly uploaded to JupyterLab, providing users easy access through a provided link.

Steps:
**1. Download geoproject file**

**2. Run Geoproject in terminal:**
```shell
cd geoproject
```
```shell
python3 manage.py runserver
```
**3. On the app fill the form with the appropriate values of the sentinel image you want downloaded and processed:**
* PASSWORD: your passowrd.
* USERNAME: your username.
* MIN_LON: bbox value for minimum longitude.
* MIN_LAT: bbox value for minimum latitude.
* MAX_LON: bbox value for maximum longitude.
* MAX_LAT: bbox value for maximum latitude.
* START_DATE: Starting date of the sentinel image.
* END_DATE: End date of the setninel image.

**Example:**
* PASSWORD: Apassword1234.
* USERNAME: Nikos1253.
* MIN_LON: 22.792511
* MIN_LAT: 38.462192
* MAX_LON: 23.041077
* MAX_LAT: 38.550313
* START_DATE: 2018-01-01
* END_DATE: 2018-01-02 


