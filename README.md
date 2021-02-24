### CarrierWatch
![Alt text](images/CarrierWatch.png "CarrierWatch Upload Settings Dialog")

#### Global Main
Carrier Dump Report is generated and emailed to the supplied email address.
* Login to Global Main
* From AP Menu
    * Type /DUMP, Press Enter
    * Select 2, Press Enter
    * Type ALL, Press Enter
    * Type email address to send report to, Press Enter


#### Outlook
Steps to convert cardump.txt (Space-Delimited) to a csv file
* Download cardump.txt to CarrierWatch folder.
* run python carrierDump.py
* Select option 1
* Open cardump.csv
* **Need to modify to convert to Dat format**


#### DAT Power - Upload
Steps to upload GM Carrier Dump Report to Carrier Watch
* Login to [Load Board](https://power.dat.com)
* From the toolbox in the top right select CarrierWatch from the drop down menu.
* Select Add new carriers in the file to my WatchList
    * DO NOT SELECT REPLACE!!!
    * ![Alt text](images/cw_upload.png "CarrierWatch Upload Settings Dialog")
* Confirmation emails are forwarded to llanerost@odysseylogistics.com. If you need them please request it, as we do not know who uploaded the files.


#### DAT Power - Download
Steps to download the Watchlist and convert to upload to Global Main
* Click Download Watchlist
    * ![Alt text](images/cw_download.png "CarrierWatch Download Settings Dialog")
* Save download.tsv to the CarrierWatch folder
* run python carrierWatch.py
* Select option 2




# Steps to outline
1. get cardump gm
2. convert cardump py
3. upload cardump cw
4. download watchlist cw
5. convert watchlist py
6. upload watchlist gm

