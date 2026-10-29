class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs =[]
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed")
        else:
            print(f"'{song}' is not found in playlist")

    def display(self):
        print(f"{self.name} ({self.genre})")
        if self.songs:
            for i, song in enumerate(self.songs, 1): 
                print(f" {i}. {song}")
        else:
            print("No songs added yet, add some to make a playlist")

    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted")

my_playlist = Playlist("Road Trip Mix", "Pop")

while True:
    print("1.Add song  2. Remove song  3. View Playlist  4. Delete & Quit")
    choice = input("Enter your choice:")
    if choice == "1":
        song = input("Enter song name:")
        my_playlist.add_song(song)
    elif choice =="2":
        song = input("Enter song to remove:")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice =="4":
        del my_playlist 
    else:
        print("Invalid choice , enter 1, 2, 3,or 4")