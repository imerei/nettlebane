# nettlebane
Nettlebane is an automated testing framework developed entirely in Python (2.7.10) in conjunction with Selenium. Its purpose is to design clean automated test cases with easy editing in order to yield results quickly and efficiently.
(Yes, this framework is named after an item in The Elder Scrolls 5: Skyrim)

## Setup
This repo currently has a premade test case to log into Meetup.com.
In order to start this test case, perform the following:
* Clone this repo to a local machine
* Open the Nettlebane direcotry
* Double-click on Nettlebane.py

## Configuration
Creating automated test cases on websites with Nettlebane utilizes four aspects (**xpaths**, **input data**, **test steps**)

### Configuring Xpaths
Using a desired tool to obtained xpaths, open **xpathRepo.py**, declare a variable and assign the xpath to it.

### Configuring Input data
Open **stored_data.csv** and add the necessary data to the csv file.

### Configuring Keywords
Open **Keywords.py** and place the xpath (along with the data if applicable) into the desired action.

### Configuring Nettlebane
Open **Nettlebane.py** and add that action (ie., test_steps.inputEmail.())
