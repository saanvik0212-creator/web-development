class ArtGallery:

    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location

        self.artworks = []

        print(f"\nWelcome to {self.gallery_name}!")
        print(f"Location: {self.location}")
        print("Art gallery collection is ready.")

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the gallery collection.")

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has been removed from the gallery collection.")
        else:
            print(f"'{artwork}' was not found in the gallery collection, try again!")

    def display_artworks(self):
        print(f"\n{self.gallery_name} Art Collection")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks have been found, add some.")

    def __del__(self):
        print(f"\nClosing {self.gallery_name}. Thank you for organising the art collection!")


gallery = ArtGallery("World of Arts Gallery", "Bengaluru")

while True:
    print("\nART GALLERY MENU")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Display Art Collection")
    print("4. Exit from gallery")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork_name = input("Enter the artwork name to add it to the gallery: ")
        gallery.add_artwork(artwork_name)

    elif choice == "2":
        artwork_name = input("Enter the artwork name to remove from the gallery: ")
        gallery.remove_artwork(artwork_name)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        print("Exiting from the Art Gallery Collection.")

        del gallery
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
