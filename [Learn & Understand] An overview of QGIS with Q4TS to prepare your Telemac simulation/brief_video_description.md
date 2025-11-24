# Summary 

This video is a condensed, all-you-need-to-know tutorial on QGIS mesh and boundary-condition preparation. It summarizes the first videos of the Telemac river-flooding tutorial and provides additional tips related to hotstart files.

Most of the steps shown in the video are visual; therefore, we do not give many details here and instead refer the viewer directly to the video.

# URL and data

- The reference background map of France was loaded from the [IGN website](https://geoservices.ign.fr/services-web-essentiels) using a WMS connection, with the following URL:
https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities

- The Corine Land Cover were loaded through a WFS request, as this allows extracting the associated value locally (see `9:52` in the video). This WFS request also comes from the [IGN website](https://geoservices.ign.fr/services-web-essentiels) using the following URL:
https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities


# Finding data for other countries or places

- NASA provides a worldwide elevation database, with various resolutions : https://search.earthdata.nasa.gov/search/
- The european Copernicus program : https://portal.opentopography.org/login
- Other private institutes or national mapping agencies may provide higher-quality data for specific regions (similar to IGN for France).

Feel free to contribute here if you want to share additional tips on QGIS and Q4TS pre-processing.
