import webbrowser
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False
	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist:
	def __init__(self, name, discription, rating, videos):
		self.name = name
		self.discription = discription
		self.rating = rating
		self.videos = videos

#1 video (nhập vào và in ra)
def read_video():
	title = input("Enter title: ") + "\n"
	link = input("Enter link: ") + "\n"
	video = Video(title,link)
	return video

def print_video(video):
	print("Video title: ", video.title, end = "")
	print("Video link: ", video.link, end = "")

#nhiều video(nhập vào và in ra)
def read_videos():
	videos = []
	total_video = int(input("Enter how many video: "))
	for i in range(total_video):
		print("Enter video ", i+1)
		vid = read_video()
		videos.append(vid)
	return videos
def print_videos(videos):
	for i in range(len(videos)):
		print("Video " + str(i+1) + ":")
		print_video(videos[i])

#hàm để gọi ghi vào file text
def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)
#ghi các thông tin vào 1 file text
def write_videos_txt(videos, file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_txt(videos[i], file)

#đọc file txt rồi in thông tin ra
def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_discrition = input("Enter playlist description: ") + "\n"
	playlist_rating = input("Enter rating (1-5): ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_discrition, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.discription)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file)
	print("Successfully write playlist to text")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_discrition = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_discrition, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("----------")
	print("playlist name: " + playlist.name, end = "")
	print("playlist discription: " + playlist.discription, end = "")
	print("playlist rating: " + playlist.rating, end = "")
	print_videos(playlist.videos)

def show_menu():
	print("Main menu:")
	print("----------------------------")
	print("| Option 1: Create playlist |")
	print("| Option 2: Show playlist   |")
	print("| Option 3: Play a video    |")
	print("| Option 4: Add a video     |")
	print("| Option 5: Update playlist |")
	print("| Option 6: Remove video    |")
	print("| Option 7: Save and Exit   |")
	print("----------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	choice = select_in_range("Select a video (1," + str(total) + "): ", 1, total)
	print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end = "")
	playlist.videos[choice-1].open()

def add_video(playlist):
	print("Enter new video information:")
	new_video_title = input("Enter new video title: ") + "\n"
	new_video_link = input("Enter new video link: ") + "\n"
	new_video = Video(new_video_title, new_video_link)
	playlist.videos.append(new_video)
	return playlist

def update_playlist(playlist):
	print("Update playlist: ")
	print("1.Name ")
	print("2.Discription ")
	print("3.Rating ")

	choice = select_in_range("Enter what you want to update (1-3)", 1, 3)
	if choice == 1:
		new_playlist_name = input("Enter new name for playlist: ") + "\n"
		playlist.name = new_playlist_name
		print("Updated Successfully !")
		return playlist
	if choice == 2:
		new_playlist_discription = input("Enter new discription for playlist: ") + "\n"
		playlist.discription = new_playlist_discription
		print("Updated Successfully !")
		return playlist
	if choice == 3:
		new_playlist_rating = str(select_in_range("Enter new rating(1-5): ", 1, 5)) + "\n"
		playlist.rating = new_playlist_rating
		print("Updated Successfully !")
		return playlist

def remove_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Enter video you want to delete: ", 1, len(playlist.videos))
	del playlist.videos[choice-1]
	print("-------------------")
	print("Delete Successfully !")
	return playlist
	# for i in range(len(playlist.videos)):
	# 	if i == choice-1:
	# 		continue
	# 	new_video_list.append(playlist_videos[i])
	# playlist = new_video_list
	# return playlist

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully !!!!")
	except:
		print("Welcome first user!!")

	while True:
		show_menu()
		choice = select_in_range("Select an option (1-7):", 1, 7)
		if choice == 1:
			playlist = read_playlist()
			input("\nPress enter to continue.\n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress enter to continue.\n")
		elif choice == 3:
			play_video(playlist)
			input("\nPress enter to continue.\n")
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress enter to continue.\n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress enter to continue.\n")
		elif choice == 6:
			playlist = remove_video(playlist)
			input("\nPress enter to continue.\n")
		elif choice == 7:
			write_playlist_txt(playlist)
			input("\nPress enter to continue.\n")
			break
		else:
			print("Wrong input, Exit")
			break

main()