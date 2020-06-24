## Instabot
Instabot is a Python script for automating actions on your instagram account.

### Contributing

Feel free to help, pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

### Installation (while on development)

Clone the repository and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the modules on requirenments.txt:
```bash
pip install -r requirements.txt , or pip3 install -r requirements.txt
```
Make sure to have the chromedriver or firefoxdriver installed. The easiest (and fastest) way is to use a package manager to add the webdriver to your system path.

##### On MacOS, in your terminal window with the Homebrew package manager:
```bash
brew cask install chromedriver
brew install geckodriver
```
Further installation options [here](https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)

##### On Windows, in your terminal window with the Chocolatey package manager:
```shell
choco install chromedriver
```
Further installation options [here](https://www.kenst.com/2019/02/installing-chromedriver-on-windows/)

### Usage (for debug and tests) 
```bash
export USERNAME='''instagramusername@example.com'''
export PASSWORD='''instagrampassword'''
```
```bash
python app.py
```
