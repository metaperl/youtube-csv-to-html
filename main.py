import csv
from pytube import YouTube
from traitlets import HasTraits, Int, Unicode, default
from traitlets.config import Application
from loguru import logger


class Video(HasTraits):
    video_id = Unicode()
    video_html_link = Unicode()

    def video_url(self):
        return f"http://youtube.com/watch?v={self.video_id}"

    def video_title(self):
        try:
            y = YouTube(self.video_url())
            video_title = y.title
        except Exception as e:
            video_title = f"Could not obtain title for {self.video_url()}: {e}"

        return video_title

    @default('video_html_link')
    def video_html_link(self):
        return f"""<a href="{self.video_url()}">{self.video_title()}</a>"""


class App(Application):

    def start(self):
        with open('liked-videos.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            with open('liked-videos.html', 'w') as html_out:
                for row_index, row in enumerate(csv_reader):
                    if i == 0:
                        continue
                    logger.debug(f"creating video instance from {row_index=}, {row[0]}")
                    v = Video(video_id=row[0])

                    logger.debug(f"{v.video_id=}, {v.video_url()} ")
                    logger.debug(f"\t{v.video_title()}")

                    html_out.write(f"{v.video_url}")


if __name__ == "__main__":
    App.launch_instance()
