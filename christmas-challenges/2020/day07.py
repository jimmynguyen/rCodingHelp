# CSS can be interesting... sometimes (Day 7)
# Challenge :
# What is the name of the css class on the first paragraph on this article? https://codinghelp.site/wiki/discord-bot/how-do-i-make-a-discord-bot-ping-me-when-it-responds/
from pyquery import PyQuery

url = "https://codinghelp.site/wiki/discord-bot/how-do-i-make-a-discord-bot-ping-me-when-it-responds/"
pq = PyQuery(url)
print("class of first <p> tag:",pq("p").attr("class"))
print("class of parent <div> containing first actual paragraph:",pq("div.site-content p").parent().attr("class"))