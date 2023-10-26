# Django-Geospatial-Project
**Description**
The Django Geospatial Project leverages pre-built containers and user inputs to streamline the download and processing of Sentinel images. Users select a container image, provide authentication credentials, and input values for the Sentinel image description. Once the image download and processing are complete, the refined data is seamlessly uploaded to JupyterLab, providing users easy access through a provided link.

Usage Guide:

**1: Download the 'geoproject' Repository**

* Begin by downloading the 'geoproject' repository to your local system.

**2: Launch Geospatial Application**

* Open your terminal and navigate to the 'geoproject' directory.
    
```shell
cd geoproject
```

* Start the application server.

```shell
python3 manage.py runserver
```

**3. Fill out the Form on the app**
* In the application, complete the form with the relevant details for the Sentinel image you wish to download and process:
  * PASSWORD: Your passowrd.
  * USERNAME: Your username.
  * MIN_LON: Minimum longitude value for the bounding box.
  * MIN_LAT: Minimum latitude value for the bounding box.
  * MAX_LON: Maximum longitude value for the bounding box. 
  * MAX_LAT: Maximum latitude value for the bounding box.
  * START_DATE: Start date of the Sentinel image (YYYY-MM-DD).
  * END_DATE: End date of the Sentinel image (YYYY-MM-DD).

**Example:**
* PASSWORD: Apassword1234.
* USERNAME: Nikos1253.
* MIN_LON: 22.792511
* MIN_LAT: 38.462192
* MAX_LON: 23.041077
* MAX_LAT: 38.550313
* START_DATE: 2018-01-01
* END_DATE: 2018-01-02 


