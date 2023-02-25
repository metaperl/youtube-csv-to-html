# youtube-csv-to-html
Convert a CSV of Youtube liked videos to a browseable HTML file

When using "Google takeout" to export your entire youtube account, one of the
files you might export is a file of liked videos in CSV format.

After searching about, there wasnt an easy way to make this browseable...
Soundiiz looked promising but too complicated for me.

So I hacked together this script that does what I need. 


# Installation and Usage

Install python then install [`poetry` for python](https://python-poetry.org).

Clone this repository and then type `poetry shell`.

Replace `liked-videos.csv` with your CSV of liked videos.

Run `python main.py` to create an HTML file `liked-videos.html`
that contains the videos that you like.