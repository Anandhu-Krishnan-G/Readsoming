import io

from gtts import gTTS
#pip install gTTS for malayalam language speaking
from playsound import playsound
#pip install playsound for playing the malayalam text
fp=io.open("book.txt",mode="r",encoding="utf-8")
#utf-8 is included becase it is a malayalam content
book_content=fp.read()
ob=gTTS(book_content,lang='ml')
ob.save("book.mp3")
playsound("book.mp3")