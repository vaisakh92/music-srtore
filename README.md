# music-store

The Project is that of a Music Store that that works with flask Server the project was developed in a windows machine.
and Mysql Server is the file attached here with first setup the server DB in MySQL 

The Flask system uses mutagen which , is used to identify metadata of in files (in this case MP3 files).
then
use secure_filename feature of Werkzeug utility of python is used to securely identify file directory of both client and server.

Run the following commands to enable the features mentioned above.

```
pip install mutagen
pip install Werkzeug
```

