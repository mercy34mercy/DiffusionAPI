import text2emotion as te
import nltk

from store import createemotion

def emotion2(text,diaryid):
    nltk.download('omw-1.4')
    emotion = te.get_emotion(text)
    print(emotion["Happy"])
    
    createemotion(diaryid,emotion["Happy"],emotion["Angry"],emotion["Fear"],emotion["Surprise"],emotion["Sad"])
    return emotion