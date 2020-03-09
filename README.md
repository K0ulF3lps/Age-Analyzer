# Age Analyzer
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0bd5abc01d3a4b13a99a2d343aafdacd)](https://app.codacy.com/manual/fegor2004/Age-Analyzer?utm_source=github.com&utm_medium=referral&utm_content=FEgor04/Age-Analyzer&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/FEgor04/Age-Analyzer.svg?branch=master)](https://travis-ci.com/FEgor04/Age-Analyzer)
[![codecov](https://codecov.io/gh/FEgor04/Age-Analyzer/branch/master/graph/badge.svg)](https://codecov.io/gh/FEgor04/Age-Analyzer)

## Install

At first, make sure you have this libraries:
  1. requests 
  2. numpy
  3. pandas
  4. sklearn
  5. matplotlib
  6. pyTelegramBotAPI
  
And, if they are not, install them with this command:
```shell script
pip3 install requests numpy pandas sklearn matplotlib pyTelegramBotAPI
```
Then, you should create settings.py.
Here is the settings.py sample.
```python
token = 'your_vk_token'
version = 5.101     # Set latest version
neural_network_file = 'neuronet_file'
                    # You need this if you want to analyze someone's age
target = 'target_vk_id'
analyze = True
log_needed = False
                    # If you want to launch telegram bot you will also need this:
tg_api = 'your_telegram_token'
                    # If you need logging:
log_needed = True
```
## How to analyze someone's age 

Set ``target`` variable equal to target's id or short link <br>
Then launch `__main__.py` file with this:
```shell script
python __main__.py
```
Script will ask you to input target's ID, and then it will print his age.
