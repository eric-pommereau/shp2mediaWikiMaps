#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import json
from osgeo import ogr

shp = r"./shp/departements-20140306-100m.shp"
shp = r"./shp/30-100/departements-simpl.shp"
shp = r"./shp/10-100/departements-simpl.shp"
shp = r"./shp/5-100/departements-simpl.shp"
shp = r"./shp/3-100/departements-simpl.shp"
shp = r"./shp/1.4-100/departements-simpl.shp"

fieldName = "code_insee"
tilde = '~'
aPolygons = []
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shp, 0) # 0 means read-only. 1 means writeable.
layer = dataSource.GetLayer()
layerDefinition = layer.GetLayerDefn()


for i in range(layerDefinition.GetFieldCount()):
    print layerDefinition.GetFieldDefn(i).GetName()


# Check to see if shapefile is found.
if dataSource is None:
    print 'Could not open %s' % (shp)
else:
    print 'Opened %s' % (shp)

    for i in range(0, layer.GetFeatureCount()):

        feature = layer.GetFeature(i)
        geom = feature.GetGeometryRef()
        geomJson = json.loads(geom.ExportToJson())
        s=""
        for coordinate in geomJson['coordinates'][0]:
            s = s + "%s,%s:" % (coordinate[1], coordinate[0])

        s = s[:-1] # virer le dernier caractère
        wikiPolygon = "%s~%s~ ~%s~ ~ ~%s~ ~" % (s,feature.GetField(fieldName), '#0B4173','#3373CC')
        aPolygons.append(wikiPolygon)

    #insee = feature.GetField(fieldName)
    print(len(aPolygons))
    print(";".join(aPolygons))
