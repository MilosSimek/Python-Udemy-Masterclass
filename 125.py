albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for album in albums:
    print(f"Album: {album[0]}, Artist: {album[1]}, Year: {album[2]}")

for (name, artist, year) in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")


for album in albums:
    name, artist, year = album
    print(f"Album: {name}, Artist: {artist}, Year: {year}")