import requests
from bs4 import BeautifulSoup

def find_popular_youtube_video_about_chatgpt_in_german():
  """Finds a popular YouTube video about 'using ChatGPT' in German.

  Returns:
    A dictionary containing the video title, URL, view count, likes, and number of subscribers.
  """

  # Get the list of all YouTube videos about 'using ChatGPT' in German.
  url = 'https://www.youtube.com/results?search_query=using+chatgpt+german'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  videos = soup.find_all('div', class_='ytd-video-renderer')

  # Find the most popular video.
  most_popular_video = videos[0]

  # Get the video title, URL, view count, likes, and number of subscribers.
  video_title = most_popular_video.find('a', class_='ytd-video-renderer-title').text
  video_url = most_popular_video.find('a', class_='ytd-video-renderer-thumbnail')['href']
  view_count = most_popular_video.find('span', class_='view-count').text
  likes = most_popular_video.find('span', class_='like-count').text
  subscribers = most_popular_video.find('span', class_='subscriber-count').text

  # Return the video information.
  return {
      'title': video_title,
      'url': video_url,
      'view_count': view_count,
      'likes': likes,
      'subscribers': subscribers,
  }

# Call the function to find the popular YouTube video.
video_info = find_popular_youtube_video_about_chatgpt_in_german()

# Print the video information.
print(video_info)
