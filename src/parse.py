from os import path
from typing import Tuple
import pandas as pd

data_dir = path.join(path.dirname(__file__), "../cleaned_data")

def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    videos = pd.read_csv(path.join(data_dir, "USvideos.csv"), dtype={
        'video_id': str,
        'title': str,
            'channel_title': str,
        'category_id': int,
        'tags': object,
        'views': int,
        'likes': int,
        'dislikes': int,
        'comment_total': int,
        'thumbnail_link': str,
        'date': str
    })

    # Parse video tags into list
    videos["tags"] = videos["tags"].map(lambda tag: [] if tag == "[none]" else tag.split('|'))

    comments = pd.read_csv(path.join(data_dir, "UScomments.csv"), dtype={
        'video_id': str,
        'comment_text': str,
        'likes': int,
        'replies': int
    })

    comments.dropna(inplace = True) #drop entries with null values

    return videos, comments

def main():
    videos, comments = load_data()

    print("Video DF Info:")
    videos.info()

    print("\nComment DF Info:")
    comments.info()

if __name__ == "__main__":
    main()
