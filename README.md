This code has 3 libraries requests , BeautifulSoup and os which are all inbuilt in general but if not for you then you can use pip to install them.
Input for this code is the topis you want to read. The topic is searched on 'google.com' and among all the results link of wikipedia is taken and further explored. 
Then we take upto 10 paragraph from the wikipedia page and check is character is valid or not. If they are we add them to result and add the final result to the file.
Here you need to add path of the file where you want to store the data. This code automatically push the older result to the bottom and keep the latest one on the top instead of appending them at the end.
