# --------------------------------------------------
# modpatcat.py
# Author: etesoro@snaplogic.com
#
# To run:
#   python t:\tools\modpatcat.py local\dir\of\files stage/elastic/endpointUrl username password
# Example:
#   python t:\tools\modpatcat.py W:\patcat\test003 stage me@snaplogic.com myP@ssw0rd
#   python t:\tools\modpatcat.py W:\patcat\test002 https://stage.elastic.snaplogicdev.com/api/2/52e4561939244e3fe08bea2e/rest/pattern me@snaplogic.com myP@ssw0rd
#
# To "compile" to pyc:
#   python -m py_compile modpatcat.py
#
# To be fixed:
#   * The correct pod ID for Elastic (sUrlBaseElastic).
#
# Known limitations:
#   * If you specify a URL as the endpointUrl, its validity is not tested.
#   * The settings file is processed BEFORE the .slp, image file, and .md files.
#     Therefore, values in the settings file can be overwritten by these files.
#   * The settings file can only handle immediate children of response_map, not deeper settings.
#   * Values are replaced by the values in the settings file, not appended.
# --------------------------------------------------

import sys
import requests
import base64
import json
from pathlib import Path


# VARIABLES ----------------------------------------

skImgPrefix = "data:image/jpeg;base64,"

sMdDir = sys.argv[1]
sPod   = sys.argv[2]
sUser  = sys.argv[3]
sPass  = sys.argv[4]

sUrlBaseStage   = "https://stage.elastic.snaplogicdev.com/api/2/52e4561939244e3fe08bea2e/rest/pattern"
sUrlBaseElastic = "https://stage.elastic.snaplogicdev.com/api/2/52e4561939244e3fe08bea2e/rest/pattern"

sTemplatePattern = "template.json"
sSettingsPattern = "settings.json"
sImgPattern = "*.png"
sSlpPattern = "*.slp"
sCsvPattern = "*.csv"

sId = ""
sUrlBase = ""
sUrlwID = ""
jSettings = ""
sJsonFile = ""
jJsonOut = ""


# FUNCTIONS ----------------------------------------

def getFn( sPath, sPattern ):
  for path in Path(sPath).glob(sPattern):
    return( path )
  return( "" )

def getJson( fJsonFullPath ):
  with open( fJsonFullPath, "r" ) as fJson:
    sJson = json.load( fJson )
    fJson.close()
  # print( sJson.keys() )
  return( sJson )

def img2b64( fImgFullPath ):
  with open( fImgFullPath, "rb" ) as fImg:
    b64str = base64.b64encode( fImg.read() ).decode('utf-8')
    fImg.close()
  return( b64str )

def escSlp( fSlpFullPath ):
  with open( fSlpFullPath, "r" ) as fSlp:
    sSlp = fSlp.read()
    fSlp.close()
  return( sSlp )
  # return( sSlp.replace( "\"", "\\\"" ) ).replace( "\\\\\"", "\\\"" )

def procMd( fMdFullPath ):
  with open( fMdFullPath, "r" ) as fMd:
    lMd = fMd.readlines()
    fMd.close()
  return( "".join( lMd[2:] ) )
  # return( "\\n".join( lMd[2:] ).replace( "\n", "" ) )


def printerr( errmsg ):
  print( "ERROR: " + errmsg + "\n\n--------------------------------------------------\n" )

def printwarn( errmsg ):
  print( "WARNING: " + errmsg + "\n\n--------------------------------------------------\n" )


# MAIN ---------------------------------------------

# What is the target pod or endpoint?
sUrlBase = sPod
if sPod.lower() == "stage":
  sUrlBase = sUrlBaseStage
if sPod.lower() == "elastic":
  sUrlBase = sUrlBaseElastic


# What is the id?
try:
  sSettingsFile = getFn( sMdDir, sSettingsPattern )
  if sSettingsFile != "":
    jSettings = getJson( sSettingsFile )
    sId = jSettings["_id"]
    sUrlwID = sUrlBase + "/" + sId
except:
  printerr( "An exception occurred while opening or retrieving the settings.json file." )
  exit()


# If the template.json file exists, read the pattern and create the entry with POST.
# If the template.json file does not exist, GET the pattern and update the entry with PUT.
try:
  sJsonFile = getFn( sMdDir, sTemplatePattern )
  if sJsonFile == "":
    # GET the JSON file to modify.
    response = requests.get( sUrlwID, auth=( sUser, sPass ) )
    fullJson = response.json()
    innerJson = fullJson[ "response_map" ]
  else:
    # Open the JSON file to modify.
    fullJson = getJson( sJsonFile )
    innerJson = fullJson[ "response_map" ]
except:
  printerr( "An exception occurred while opening or retrieving the template.json file." )
  exit()


# Delete _id and http_status_code.
try:
  if "_id" in innerJson.keys():
    del innerJson["_id"]
  if "http_status_code" in fullJson.keys():
    del fullJson["http_status_code"]
except:
  print( "An exception occurred while deleting _id and http_status_code.\n" + hori )
  exit()


# Replace values based on settings json.
try:
  if sJsonFile == "" and sSettingsFile != "":
    for key in jSettings.keys():
      if key != "_id":
        innerJson[key] = jSettings[key]
except:
  printerr( "An exception occurred while replacing values." )
  exit()


# Convert the image file to Base 64 and plug into "pattern_image".
try:
  sImgFile = getFn( sMdDir, sImgPattern )
  if sImgFile != "":
    sImgB64 = skImgPrefix + img2b64( sImgFile )
    innerJson["pattern_image"] = sImgB64
except:
  printerr( "An exception occurred while reading the image file." )
  exit()


# Process the .slp file and plug into "slp".
try:
  sSlpFile = getFn( sMdDir, sSlpPattern )
  if sSlpFile != "":
    sSlp = escSlp( sSlpFile )
    innerJson["slp"] = sSlp
except:
  printerr( "An exception occurred while converting the .slp file." )
  exit()


# Process the Markdown files and plug into the appropriate keys.
try:
  mddict = innerJson["markdown"]
  if getFn( sMdDir, "overview.md" ) != "":
    sOverview = procMd( sMdDir + "\\overview.md" )
    innerJson["description"] = sOverview
  if getFn( sMdDir, "requirements.md" ) != "":
    sRequirements = procMd( sMdDir + "\\requirements.md" )
    mddict["requirements"] = sRequirements
  if getFn( sMdDir, "using-this-pattern.md" ) != "":
    sUsage = procMd( sMdDir + "\\using-this-pattern.md" )
    mddict["usage"] = sUsage
except:
  printerr( "An exception occurred while processing the Markdown files." )
  exit()


# Dump back to JSON and replace response_map with pattern.
try:
  jJsonOut = json.dumps(fullJson, indent=2, separators=(", ", " : ")).replace( "response_map", "pattern" )
  # print( jJsonOut )
except:
  printerr( "An exception occurred while preparing the body (JSON)." )
  exit()


# PUT or POST
try:
  sHeaders = { "Content-Type": "application/json" }
  if sJsonFile == "":
    # Update the existing entry.
    print( "Updating the existing entry: " + sId )
    response = requests.put( sUrlwID, data=jJsonOut, headers=sHeaders, auth=( sUser, sPass ) )
  else:
    # Create a new entry.
    print( "Creating a new entry." )
    response = requests.post( sUrlBase, data=jJsonOut, headers=sHeaders, auth=( sUser, sPass ) )
  print( response.json() )
except:
  printerr( "An exception occurred during PUT/POST." )
  print( response.json() )
  exit()


# --------------------------------------------------
