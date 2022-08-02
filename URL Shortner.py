
import pyshorteners
link=input("Enter the url here:")
shortner=pyshorteners.Shortener()
final_link=shortner.tinyurl.short(link)
print(final_link)