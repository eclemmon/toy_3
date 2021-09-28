# Toy 3

**About:**

toy_3 is an algorithmically generated computer music work that was composed for Ensemble Decipher, to be presented alongside a film graphically rendered
by the K computer at the RIKEN Center for Computational Science for Hideo Sekino. The music
generating program utilizes a hard-coded formal structure to synthesize a sequence of sections
evocative of some of the imagery in the film, while at the same time, members of the laptop
ensemble interact with a central TCP/IP server through their personal clients to trigger water-
inspired sound events.

**Setup:**

List of required materials and staging:

- Six laptops that are WIFI-enabled and have python 3.7 installed on them, one laptop acts
    as the chat-server, and music generator, and the five others act as chat-clients.
- Appropriate audio output cables to connect the server laptop to the performance space’s
    sound system.
- A sound system with at least two speakers arranged in stereo at the front of the hall.
    Performers can choose to set up a larger array of speakers in front, just know that the
    program as it stands currently is not designed to do anything further with surround sound
    or ambisonics.
- A projector and a projector screen to display the graphically rendered video.
- Highly recommended: your own WIFI router so that TCP/IP routing ‘locally’ is very
    simple.

Setting Up:

- The server laptop must install pyo (http://ajaxsoundstudio.com/software/pyo/) on their
    laptop. There are multiple ways to install pyo, either through compiling from the source
    code, using their installer, git, or brew. It is highly recommended that the server client
    laptop installs their Python 3.7 and pyo packages to operate in a virtual environment,
    especially on Mac, otherwise pyo will compile to the native installation of python that
    comes with OSX (Python 2.7). This will break the main chat_serv.py and
    Music_Handler.py scripts. Further, altering the native installation of Python on your Mac
    will break some of your programs, or break installations and updates of programs! Email
    the composer with any questions or concerns (ec.lemmon@gmail.com).
- The server laptop will also need to download both the chat_serv.py and Music_Handler.py
    scripts from https://github.com/eclemmon/Toy3. If they would also like to chat, the server
laptop may also do so from a separate shell window. In this case, also download
chat_clnt.py.
- The chat client laptops must install Python 3.7 and download the chat_clnt.py script from
    https://github.com/eclemmon/Toy3.

Once python and pyo have been downloaded and installed, booting the software should be fairly
simple. To start:

1. Open the chat_serv.py file in your favorite IDE, and find the HOST variable. In between
    the quotation marks, change the string to the IP address that your computer has been
    assigned. On Mac you can find this information in the System Preferences app under
    ‘Network’. Future versions (after 3/1/19) will not require you to edit the code in line, but
    will request it from the console.
2. Open terminal and change your directory to the location of your virtual environment and
    the scripts. You may install your vitual environment in the directory path of your choosing,
    it is just easier for them to be in a similar location.


3. Type in source virtualenv_directory/bin/activate to activate your
    virtual environment.
4. Type in python3 user/path/chat_serv.py. This can be achieved by following
    the call to book python with dragging the file into your terminal window on Mac.
5. The server is now booted and ready to accept chat clients.

_Instructions for chat clients:_

1. Chatters have it easy. Simply open your terminal or UNIX shell and type in: python
    user/path/chat_clnt.py.


2. Once you run it (by hitting enter) a chat window will pop up, but it does not work yet.
    Staying in your terminal you must enter the host’s IP Address, which the server laptop
    operator will read off to you from their computer’s system preferences. They will also tell
    you the port number to enter, which is set to 33000 by default.
3. Your chat window is now operational, but you must enter a user name before you can begin
    chatting. If all goes according to plan, once you enter a user name, you will be in the chat
    room, although no sound will be generated until you type more text and hit enter.
4. Type in words and phrases that are inspired by water or the video!


