# google TTS 로 생성해보기 (무료)
#%%
!pip install gTTS 
#%%
from gtts import gTTS

KOR_SCRIPT = "해리 포터는 냉대받으며 자란 고아로, 11번째 생일에 자신이 마법사이며 호그와트 마법학교에 입학하게 되었음을 알게 된다. 학교에서 친구들을 만나고, 자신과 어둠의 마법사 볼드모트 사이에 얽힌 과거를 조금씩 알게 된다. 첫 해에는 마법사의 돌을 둘러싼 음모를 막으며 용기와 우정, 선택의 의미를 배워나간다."
ENG_SCRIPT = "Harry Potter, an orphan raised by neglectful relatives, discovers on his 11th birthday that he is a wizard and has been accepted to Hogwarts School of Witchcraft and Wizardry. There, he makes close friends and begins to uncover secrets about his past and the dark wizard Voldemort. In his first year, he faces trials to protect the Philosopher’s Stone, learning the value of courage, loyalty, and friendship."
#%%
tts = gTTS(text=KOR_SCRIPT, lang="ko")
tts.save("kor_tts.mp3")
# %%
tts = gTTS(text=ENG_SCRIPT, lang="en")
tts.save("eng_tts.mp3")
# %%
