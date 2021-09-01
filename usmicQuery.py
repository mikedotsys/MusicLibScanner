import os
from tinytag import TinyTag
import csv


def main():

    # set counter
    a = 0

    # directory to scan
    scan_dir = 'Z:/Unsorted/80\'s'  # directory to scan

    # output file
    outfile = 'music.csv'  # name of csv file to output

    # open out file and write
    with open(outfile, 'w', newline='', encoding="utf-8") as f:
        music_scan = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        music_scan.writerow(
            ['file_path', 'file_name', 'file_ext', 'artist', 'title', 'album', 'track', 'track_total', 'disc',
             'disc_total',
             'duration', 'genre', 'year', 'filesize', 'bitrate'])

        # scan the directories
        for root, dirs, files in os.walk(scan_dir):
            for file in files:

                # filter files based on extension
                if file.endswith((".mp3", ".MP3", ".ogg", ".m4a")):
                    line = str(os.path.join(root, file))
                    tag = TinyTag.get(os.path.join(root, file))
                    file_name = file[:-4]
                    file_ext = file.split(".")[-1]
                    music_scan.writerow(
                        [line, file_name, file_ext, tag.artist, tag.title, tag.album, tag.track, tag.track_total,
                         tag.disc,
                         tag.disc_total, tag.duration, tag.genre, tag.year, tag.filesize, tag.bitrate])

                    a = a + 1

        # print counter of files scanned
        print("Files Scanned: " + str(a))


if __name__ == "__main__":
    main()
