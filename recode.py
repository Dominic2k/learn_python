# Define a video class, a video has title and link
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

# Ask an user to enter information of a video
def read_video():
	

# Show information of a video
def print_video(video):
	pass

# Ask an user to enter information of all videos, they first choose how many videos are there
def read_videos():
	pass

# Show information of all videos
def print_videos(videos):
	pass

# Write a video information to a text file
def write_video_txt(video, file):
	pass
	
# Write videos to text file, first line is the total number of videos
def write_videos_txt(videos):
	pass

# Read 2 line from a text file and return a video
def read_video_from_txt(file):
	pass

# Read data.txt and return a list of videos 
def read_videos_from_txt():
	pass

def main():
	# Ask user to enter information of all videos one by one
	videos = read_videos()
	# Write videos information to a text file
	write_videos_txt(videos)	
	# Read the text file to get a videos list
	videos = read_videos_from_txt()
	# Use the list above and show all information of videos inside that list
	print_videos(videos)

main()