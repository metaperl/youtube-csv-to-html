# youtube-csv-to-html
Convert a CSV of Youtube liked videos to a browseable HTML file and 
a CSV file that includes the titles of the videos.

When using "Google takeout" to export your entire youtube account, one of the
files you might export is a file of liked videos in CSV format.

After searching about, there wasnt an easy way to make this browseable...
Soundiiz looked promising but too complicated for me.

So I hacked together this script that does what I need. 


# Installation and Usage

Install python then install [`poetry` for python](https://python-poetry.org).

Clone this repository and then type `poetry shell`.

Replace `liked-videos.csv` with your CSV of liked videos.

Run `python main.py` to create an HTML file `out.html` as well as `out.csv`
that contains the videos that you like.

# IMPORTANT USAGE NOTE:

![image](https://user-images.githubusercontent.com/21293/221414687-1d12d3e9-55e5-4c5f-bfdb-9136ff747ca0.png)

You must remove the first 3 rows of the `liked-videos.csv` file. Furthermore Google takeout names this file `Liked videos.csv` 
and this program currently requires the file to be named `liked-videos.csv`.

# NOTES

It does take quite awhile to run. 
I had about 1400 videos in my CSV file and it took about 20 minutes.
