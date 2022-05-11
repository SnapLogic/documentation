# README for ModPatCat

This Python script serves as a stop-gap solution to easily create or modify patterns in the Pattern Catalog using the internal APIs.


## PREREQUISITES
* Python 3.10 or later (https://www.python.org/downloads/)
* requests library
  ```
  python.exe -m pip install requests
  ```


## KNOWN LIMITATIONS
* If you specify a URL as the endpointUrl, its validity is not tested.
* The settings file is processed BEFORE the .slp, image file, and .md files.
  Therefore, values in the settings file can be overwritten by these files.
* The settings file can only handle immediate children of response_map, not deeper settings.
* Values are replaced by the values in the settings file, not appended.


## HOW TO USE
1. Create a folder with the following files:
   * template.json – A JSON file similar to a response to a GET.
     * If creating a new pattern, required.
     * If updating an existing pattern, must not exist.
   * *.png – The image of the pipeline of the pattern. Include only if you want the image to be replaced.
   * *.slp – The .slp of the pipeline of the pattern. Include only if you want the slp to be replaced.
   * overview.md – GitBook file for the pattern description. Include only if you want to replace the pattern description.
   * requirements.md – GitBook file for the pattern requirements. Include only if you want to replace the pattern requirements.
   * using-this-pattern.md – GitBook file for the pattern usage. Include only if you want to replace the pattern usage.
   * settings.json - A flat JSON file with settings to replace values of immediate child keys of `response_map`.
     * If creating a new pattern, enter the values directly in template.json. If you prefer to create this file, set `"_id" : ""`.
     * If updating an existing pattern, required with the correct `_id` of the existing pattern.
2. Run the script.
   ```
   python modpatcat.pyc myFolder stage me@snaplogic.com myP@ssw0rd
   ```
3. If you created a new pattern, save the ID from the response JSON.


## TIPS
* DO NOT SAVE YOUR PASSWORD ON ANY SCRIPT.
* On a Windows machine, you can run `modpatcat.bat`.
  * If %USERNAME%@snaplogic.com is the same as your account username, you can pass `.` as the username.
    ```
    echo %USERNAME%@snaplogic.com
    ```
  * If you are currently in the folder containing the files, you can pass `.` as the folder path.
    ```
    cd /d path\to\the\folder
    ```
  * Example:
    ```
    modpatcat.bat . stage . myP@ssw0rd
    ```
