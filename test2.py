
import re

str = '��&gt;</span><br />��񡢱�<br />�������������̡�����<br />�����������α�<br />���������沱��<br />�βγ������θ���<br />�ѱ׶��ѱ׶�<br />�ٷ<br />�۳����۵ϲ۵ϡ��۵�۵�<br />����<br />�����<br />���ա����⡢���<br />���⡢��ߡ�����<br />��մ��ڰ��񡢲��<br />��롢��Ʋ<br />��������Ÿ��<br />����<span style="font-size:9pt;" _foo="font-size:9pt;"> </span><br /><span style="font-size:36pt;" _foo="font-size:36pt;">&lt;��'

strlist = re.findall(">(.*?)<",str)

for s in strlist:
    print(s)
