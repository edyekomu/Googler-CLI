# Googler CLI

A simple google search command line tool that calls **SerpAPI**

## Installation
1. `git clone https://github.com/edyekomu/Googler-CLI.git`
2. `pip install -r requirements.txt`

## Usage
1. **Set API key**  
`python googler.py --set-key [YOUR API KEY]`
2. **Query SerpAPI**
`python googler.py -q [query]`

## Features
`-h, --help: show this help message and exit`  

`-q [QUERY], --query [QUERY]: Search query`  

`-n [NUM], --num [NUM]: Number of results shown. Default is 5`  

`--set-key [SET_KEY]: set API key, creates JSON file`  
