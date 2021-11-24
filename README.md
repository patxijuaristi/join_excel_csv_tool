# Tool to Join Excel or CSV Files into a Single File 📄

This is a really simple script developed with Python and its data managment library Pandas. **It joins multiple spreadsheets and create a single CSV file with all the content**.

[![Google Maps Scraper](https://juaristech.com/wp-content/uploads/2021/11/juntar-varios-excel-en-uno.jpg)](https://juaristech.com/herramienta-unir-ficheros-excel-y-csv "JuarisTech")

## Online Tool

I have also included the script in the website, so if you prefer you can use the tool, online for free. You can find the tool in the next link:

- Online Tool: https://juaristech.com/herramienta-unir-ficheros-excel-y-csv

[![Google Maps Scraper](https://juaristech.com/wp-content/uploads/2021/11/tool-to-join-excel-files.jpg)](https://juaristech.com/herramienta-unir-ficheros-excel-y-csv "JuarisTech")

I have done it by connecting my Wordpress site to a Flask API located on a subdomain of my own, and creating a custom Wordpress plugin to do all this process and comunication.

## How to Run It in Local

To execute this script you need to run it in the command prompt.

```bash
unir_excels_juaristech.exe
```

Then, you will need to specify where you have stored the spreadsheets:

You can specify a complete path (*D:\Projects\spreadsheets\cars*) or if you have the spreadsheets in the same directory as the script, you can type "." or press enter without introducing nothing.

```bash
[1] Introduce the path to of sheets folder: 
```

Then the script starts to work, and when it finished, the output CSV file would appear in the folder. If you open the file in an editor, and the output is strange, you need to specify to set the text in columns to display the output correctly. For example in Excel, you will need to go to *Data -> Text in columns -> Delimited -> Tabulation -> Finish*. Take into account that the **delimiter is tabulation**.

---

For any doubts about how to use the program, you can read the article of our web or see the demo video.

- Online Tool: https://juaristech.com/herramienta-unir-ficheros-excel-y-csv
- Demo video: https://youtu.be/G2hLEhCXDgI

## Requirements

The used requirements are specified in the requierements.txt file. If you want to execute the *.py* script from python, you can install the dependencies with the next command:

```bash
pip install -r requirements.txt
```

## Contact

- Website: [JuarisTech](https://juaristech.com/)
- Email: admin@juaristech.com

