## Scrape tweets with Twint 
import twint
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("           _         _             _    _  ")
print("     /\   | |       | |           | |  (_) ")
print("    /  \  | | ____ _| |_ ___ _   _| | ___  ")
print("   / /\ \ | |/ / _` | __/ __| | | | |/ / | ")
print("  / ____ \|   < (_| | |_\__ \ |_| |   <| | ")
print(" /_/    \_\_|\_\__,_|\__|___/\__,_|_|\_\_| \n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("Note: dont get over 3200 tweets \n " )


search = input("What are you searching for?\n")
city = input("Near a city?\n")
Limit = input("How many tweets?\n")
Out = input("output?\n")


c = twint.Config()
c.Search = search
c.Near = city
c.Limit = Limit
c.Output = Out
c.Store_json = True
c.Store_csv = True
c.Store_object = True


twint.run.Search(c)
