class script(object):
    START_TXT = """Hello {},
Myself <a href=https://t.me/{}>{}</a>,\n\nTrust me ! I can't even imagine how super-fast i can drive your Database channel \n\nAre you ready for Long Drive Baby...ð"""
    HELP_TXT = """Êá´Ê {}
Here is the help for my COMMANDS."""
    ABOUT_TXT = """â¯ á´Ê É´á´á´á´: {}
â¥ á´Ê á´á´¡É´á´Ê : <a href=https://t.me/PharmacistBoy1>â¨ï¸sá´á´á´Éªá´ÊÉªsá´â¨ï¸â¢ï¸</a>"  
â¥ á´Êá´á´á´á´Ê: <a href=https://t.me/Syrus_143_hpy>äº ððð¡ðð¬ |â¡|</a>
â¥ ÊÉªÊÊá´ÊÊ: Éªá´á´
â¥ Êá´É´É¢á´á´É¢á´: Éªá´á´
â¥ Êá´Ç« É¢Êá´á´á´: <a href=https://t.me/newyear2023group>á´á´ | á´É´á´á´Êá´á´ÉªÉ´á´á´É´á´</a>"
â¥ ð±ð¾ð ðð´ððð´ð: Éªá´á´
â¥ Êá´ÉªÊá´ sá´á´á´á´s: v1.0.1 [ Éªá´á´ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Lazy Princess is an open source project. 
- Owner - <a href=https://t.me/PharmacistBoy1>â¨ï¸sá´á´á´Éªá´ÊÉªsá´â¨ï¸â¢ï¸</a>"  

<b>Êá´Êá´á´Ê:</b>
- <a href=https://t.me/Syrus_143_hpy>äº ððð¡ðð¬ |â¡|</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and LazyPriness will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/newyear2023group)</code>
 
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Lazy Princess

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
