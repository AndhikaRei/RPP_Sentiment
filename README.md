# Sentiment Tracker RPP

## Semester I Tahun 2022/2023

### Tugas IF4070 Representasi Pengetahuan dan Penalaran

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester I Tahun 2022/2023*

## Description
Sebuah program dalam bahasa Python berbasis web dengan framework flask yang mengimplementasikan 
analisis sentimen pada data yang ditambahkan pada web. Proses penentuan sentimen dilakukan dengan
menggunakan machine learning. Alur pembangunan aplikasi dan model machine learning mengikuti 
SKKNI no 123 tahun 2021 yang diketuai oleh Bapak Windy Gambetta. Program ini dibuat untuk memenuhi tugas IF4070
   
## Author
1. Reihan Andhika Putra (13519043)
2. Dzaki Muhammad (13519049)
3. Naufal Yahya Kurnianto (13519141)

## Requirements
- [Python ^3.8](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation) (optional)

## Installation And Run
Clone the repository
```bash
git clone https://github.com/AndhikaRei/RPP_Sentiment.git
```
### Automatic Setup
#### Poetry
1. Make sure you have poetry installed
2. Run the following command
```bash
poetry install
poetry shell
flask db downgrade
flask db upgrade
flask seed run
flask run
```
3. Then open your web browser and go to [localhost:5000](http://localhost:5000)
#### Script
##### First Time Setup
1. Open setup script
2. Wait until the installation is finished
3. The setup will automatically open the web browser
4. If the page failed to load, wait a moment then refresh the page

##### Run
1. Open run script
2. It will automatically open the web browser
3. If the page failed to load, wait a moment then refresh the page

### Manual Setup
After cloning the repository
```bash 
cd src
python -m venv virt
virt\Scripts\activate
pip install -r requirements.txt
flask db downgrade
flask db upgrade
flask seed run
flask run
```
Then open your web browser and go to [localhost:5000](http://localhost:5000)

## Screen Capture 
### Dahsboard
![Screenshot]()
### Add Data
![Screenshot]()
### Contributor
![Screenshot]()
