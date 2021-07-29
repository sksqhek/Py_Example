
import re

str = '¤¢&gt;</span><br />±ñ±ñ¡¢±ñ³ª<br />±ö±ö¡¢±ö³­ÀïÀÌ¡¢±ö¾¾<br />²¯±¸¸®¡¢²¯µÎ±â<br />²±²±¡¢²±Ãæ²±Ãæ<br />²Î²Î³ª¹«¡¢²Î¸¶ÀÛ<br />²Ñ±×¶û²Ñ±×¶û<br />²Ù·î³»<br />²Û³»¡¢²ÛµÏ²ÛµÏ¡¢²Ûµé²Ûµé<br />²ßÀû<br />²á²áÀÌ<br />²î°íµÕ¡¢²îµé±â¡¢²î¹Ì<br />²æ°í±â¡¢²æ´ß¡¢²æÀå<br />²ç¶Õ´ÂÀÚ°í¸£¸ñ¡¢²ç¸É<br />²ë´ë¡¢²ëÆ²<br />³¤°¢¡¢³¤Å¸ºÒ<br />³¨³»<span style="font-size:9pt;" _foo="font-size:9pt;"> </span><br /><span style="font-size:36pt;" _foo="font-size:36pt;">&lt;¤¤'

strlist = re.findall(">(.*?)<",str)

for s in strlist:
    print(s)
