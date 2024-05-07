# This is a class to scrape the pronunciation of a word from google search
# After that, it will save the pronunciation to a file
import logging
import requests
import os
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


class LearningVocabularyPronunciation:
    def __init__(self):
        self.url = "https://www.google.com.hk/search?q=definition+of+"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3"
        }
        self.abs_p = os.path.dirname(os.path.abspath(__file__))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def get_pronunciation_link(self, word):
        response = requests.get(self.url + word, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the 'audio' tag
        audio_tag = soup.find('audio')

        # Get the 'src' attribute which contains the mp3 link
        mp3_link = audio_tag['src']

        return mp3_link

    def save_pronunciation(self, word):
        mp3_link = self.get_pronunciation_link(word)
        response = requests.get(mp3_link)
        file_path = self.abs_p + "/pronunciation/" + word + ".mp3"
        # Ensure the directory exists, if not, create it
        os.makedirs(self.abs_p + "/pronunciation/", exist_ok=True)

        # only write to the file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(response.content)
            self.logger.info("Pronunciation of the word '{}' has been saved to file".format(word))
        else:
            self.logger.info("Pronunciation of the word '{}' already exists".format(word))


 # I want to upload this mp3 file to a cloud storage like AWS S3
# are there any cloud storages that you are familiar with?
# I am familiar with AWS S3, Google Cloud Storage, and Azure Blob Storage
# I can help you with that
# Which one do you want to use?
# Let's use Google Cloud Storage
# Sure, I will help you with that
# I will create a new class called GoogleCloudStorage
# I will create a method called upload_file
# I will upload the file to Google Cloud Storage
# I will also create a method called delete_file
# I will delete the file from Google Cloud Storage
# I will also create a method called download_file
# I will download the file from Google Cloud Storage
# I will also create a method called list_files
# I will list all the files in the Google Cloud Storage
# I will also create a method called get_file_metadata
# I will get the metadata of the file from Google Cloud Storage
# I will also create a method called copy_file
# do i need to create a new .py file for this?
# Yes, you need to create a new .py file for this
# What should I name the file?


if __name__ == "__main__":
    lvp = LearningVocabularyPronunciation()
    lvp.save_pronunciation("sherbet")
