
def xml_prompt0(date, prays):
    if prays is None or prays == "":
        text = f"""<?xml version="1.0" encoding="UTF-8" standalone="no" ?><?xml-stylesheet type="text/xsl" href="{date[:4]}년_{date[4:]}월_기도이야기.xsl"?><HWPML Style="export" SubVersion="9.0.1.0" Version="2.9"><BODY><SECTION Id="0"><P ColumnBreak="false" PageBreak="false" ParaShape="13" Style="15"><TEXT CharShape="12"><PAGENUM FormatType="Digit" Pos="BottomCenter" SideChar="-"/><CHAR>{date[:4]}년 {date[4:]}월 예닮공 기도이야기</CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="13"/></P><P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {date[4:]}월 예닮공 기도제목</CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="15"><CHAR>①</CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="15"><CHAR>② </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="15"><CHAR>③ </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
        return text

    text = f"""<?xml version="1.0" encoding="UTF-8" standalone="no" ?><?xml-stylesheet type="text/xsl" href="{date[:4]}년_{date[4:]}월_기도이야기.xsl"?><HWPML Style="export" SubVersion="9.0.1.0" Version="2.9"><BODY><SECTION Id="0"><P ColumnBreak="false" PageBreak="false" ParaShape="13" Style="15"><TEXT CharShape="12"><PAGENUM FormatType="Digit" Pos="BottomCenter" SideChar="-"/><CHAR>{date[:4]}년 {date[4:]}월 예닮공 기도이야기</CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="13"/></P><P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {date[4:]}월 예닮공 기도제목</CHAR></TEXT></P>"""
    icons = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧"]
    for i in range(len(icons)):
        try:
            start = prays.index(icons[i])
            end = prays.index(icons[i+1])
            pray = prays[start:end]
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="15"><CHAR>""" + pray + """</CHAR></TEXT></P>"""
        except:
            start = prays.index(icons[i])
            pray = prays[start:]
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="15"><CHAR>""" + pray + """</CHAR></TEXT></P>"""
            break

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt1(formats, prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    formats = formats[key]

    if prays is None or prays == "":
        sub_names = []
    else:
        sub_names = prays.keys()

    for format in formats:
        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{prays[sub_name]}</CHAR></TEXT></P>"""
                isexist = True
                break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""

    return text

def xml_prompt1_noformat(prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""

    if prays is None or prays == "":
        sub_names = []
        formats = []
    else:
        sub_names = prays.keys()
        formats = list(prays.keys())

    for format in formats:
        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{prays[sub_name]}</CHAR></TEXT></P>"""
                isexist = True
                break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""

    return text

def xml_prompt2(formats, prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    formats = formats[key]

    sub_names = prays.keys()
    for format in formats:
        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>{format} </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="8"><CHAR>{prays[sub_name]}</CHAR></TEXT></P>"""
                isexist = True
                break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>{format} </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt2_noformat(prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    # formats = formats[key]
    formats = list(prays.keys())

    sub_names = prays.keys()
    for format in formats:
        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>{format} </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="8"><CHAR>{prays[sub_name]}</CHAR></TEXT></P>"""
                isexist = True
                break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>{format} </CHAR></TEXT></P><P ParaShape="13" Style="15"><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt_LBS(formats, prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    formats = []
    for i, x in enumerate(prays.keys()):
        if i == 0:
            formats.append(x)
        else:
            formats.append("GBS 기도제목")
            formats.append(list(prays[x])[1])


    formats = formats[key]

    ## formats 에 추가 (단, 속하지 않는 것만 각 EBS 뒤에 추가)
    new_formats = []
    sub_names = []
    for i, format in enumerate(formats):
        new_formats.append(format)
        if format == "GBS 기도제목": ## EBS 시작
            leader_name = formats[i+1].split(' ')[-1] ## 김지인A 같은 경우 안됨
            
            try:
                sub_names = prays[leader_name].keys()
            except:
                if leader_name[-1] in ['A', 'B', 'C', 'D', 'E']:
                    leader_name = leader_name[:-1]
                    try:
                        sub_names = prays[leader_name].keys()
                    except:
                        sub_names = []
                else:
                    sub_names = []
        if i == (len(formats)-1):
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)
        elif formats[i+1] == "GBS 기도제목":
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)


    for i, format in enumerate(new_formats):
        if i == 0: ## 지기님 기도제목
            sub_names = prays.keys()

        if format == "GBS 기도제목": ## GBS 시작
            leader_name = new_formats[i+1].split(' ')[-1]

            try:
                sub_names = prays[leader_name].keys()
            except:
                if leader_name[-1] in ['A', 'B', 'C', 'D', 'E']:
                    leader_name = leader_name[:-1]
                    try:
                        sub_names = prays[leader_name].keys()
                    except:
                        sub_names = []
                else:
                    sub_names = []
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="8"/></P>"""
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>[#] {leader_name} GBS</CHAR></TEXT></P>"""

        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                if i == 0:
                    pray = prays[sub_name]
                else:
                    pray = prays[leader_name][sub_name]
                
                if pray != "":
                    text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{pray}</CHAR></TEXT></P>"""
                    isexist = True
                    break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt_noformat_LBS(prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    formats = []
    jigi_submit = False
    for i, x in enumerate(prays.keys()):
        if i == 0 and any(element.isdigit() for element in x):
            jigi_submit = True
            formats.append(x)
        else:
            formats.append("GBS 기도제목")
            for j in range(1, len(prays[x])):
                if x in list(prays[x])[j]:
                    formats.append(list(prays[x])[j])
                    break

    ## formats 에 추가 (단, 속하지 않는 것만 각 EBS 뒤에 추가)
    new_formats = []
    sub_names = []
    for i, format in enumerate(formats):
        new_formats.append(format)
        if format == "GBS 기도제목": ## EBS 시작
            leader_name = formats[i+1].split(' ')[-1] ## 김지인A 같은 경우 안됨
            
            try:
                sub_names = prays[leader_name].keys()
            except:
                if leader_name[-1] in ['A', 'B', 'C', 'D', 'E']:
                    leader_name = leader_name[:-1]
                    try:
                        sub_names = prays[leader_name].keys()
                    except:
                        sub_names = []
                else:
                    sub_names = []
        if i == (len(formats)-1):
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)
        elif formats[i+1] == "GBS 기도제목":
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)

    for i, format in enumerate(new_formats):
        if i == 0: ## 지기님 기도제목
            sub_names = prays.keys()

        if format == "GBS 기도제목": ## GBS 시작
            leader_name = new_formats[i+1].split(' ')[-1]

            try:
                sub_names = prays[leader_name].keys()
            except:
                if leader_name[-1] in ['A', 'B', 'C', 'D', 'E']:
                    leader_name = leader_name[:-1]
                    try:
                        sub_names = prays[leader_name].keys()
                    except:
                        sub_names = []
                else:
                    sub_names = []
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="8"/></P>"""
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>[#] {leader_name} GBS</CHAR></TEXT></P>"""

        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                if i == 0 and jigi_submit:
                    pray = prays[sub_name]
                else:
                    pray = prays[leader_name][sub_name]
                
                
                if pray != "":
                    text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{pray}</CHAR></TEXT></P>"""
                    isexist = True
                    break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt_EBS(formats, prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""

    formats = []
    for i, x in enumerate(prays.keys()):
        if i == 0:
            formats.append(x)
        else:
            formats.append("GBS 기도제목")
            formats.append(list(prays[x])[1])

    ## formats 에 추가 (단, 속하지 않는 것만 각 EBS 뒤에 추가)
    new_formats = []
    sub_names = []
    for i, format in enumerate(formats):
        new_formats.append(format)
        if format == "EBS 기도제목": ## EBS 시작
            leader_name = formats[i+1].split(' ')[-1]
            try:
                sub_names = prays[leader_name].keys()
            except:
                sub_names = []
        if i == (len(formats)-1):
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)
        elif formats[i+1] == "EBS 기도제목":
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)

    for i, format in enumerate(new_formats):
        if format == "EBS 기도제목": ## EBS 시작
            leader_name = new_formats[i+1].split(' ')[-1]
            try:
                sub_names = prays[leader_name].keys()
            except:
                sub_names = []
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="8"/></P>"""
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>[#] {leader_name} EBS</CHAR></TEXT></P>"""
        

        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                pray = prays[leader_name][sub_name]
                
                if pray != "":
                    text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{pray}</CHAR></TEXT></P>"""
                    isexist = True
                    break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_prompt_noformat_EBS(prays, key): # formats = ["노주찬 목사님", "김신천 전도사님"]
    text = f"""<P ParaShape="13" Style="15"><TEXT CharShape="14"><CHAR>[★] {key}</CHAR></TEXT></P>"""
    formats = []
    for i, x in enumerate(prays.keys()):
        formats.append("EBS 기도제목")
        formats.append(list(prays[x])[1])

    ## formats 에 추가 (단, 속하지 않는 것만 각 EBS 뒤에 추가)
    new_formats = []
    sub_names = []
    for i, format in enumerate(formats):
        new_formats.append(format)
        if format == "EBS 기도제목": ## EBS 시작
            leader_name = formats[i+1].split(' ')[-1]
            try:
                sub_names = prays[leader_name].keys()
            except:
                sub_names = []
        if i == (len(formats)-1):
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)
        elif formats[i+1] == "EBS 기도제목":
            for sub_name in sub_names:
                include = False
                for x in formats:
                    if sub_name in x:
                        include = True
                if not include:
                    new_formats.append(sub_name)

    for i, format in enumerate(new_formats):
        if format == "EBS 기도제목": ## EBS 시작
            leader_name = new_formats[i+1].split(' ')[-1]
            try:
                sub_names = prays[leader_name].keys()
            except:
                sub_names = []
            text += """<P ParaShape="13" Style="15"><TEXT CharShape="8"/></P>"""
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="19"><CHAR>[#] {leader_name} EBS</CHAR></TEXT></P>"""
        

        isexist = False
        for sub_name in sub_names:
            if sub_name in format:
                pray = prays[leader_name][sub_name]
                
                if pray != "":
                    text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>{pray}</CHAR></TEXT></P>"""
                    isexist = True
                    break
        if not isexist:
            text += f"""<P ParaShape="13" Style="15"><TEXT CharShape="16"><CHAR>{format} </CHAR></TEXT><TEXT CharShape="8"><CHAR>① (감사)  ②  ③  ④  ⑤</CHAR></TEXT></P>"""

    text += """<P ParaShape="13" Style="15"><TEXT CharShape="10"/></P>"""
    return text

def xml_end():
    text = "</SECTION></BODY></HWPML>"
    return text


xml_prompt1_1 = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?><?xml-stylesheet type="text/xsl" href="
9월 기도이야기 (하람, 영진, 성범, 시온, 지원, 근원).xsl
"?>"""


xml_prompt1_2 = """<HWPML Style="export" SubVersion="9.0.1.0" Version="2.9"><BODY><SECTION Id="0"><P ColumnBreak="false" PageBreak="false" ParaShape="14" Style="15"><TEXT CharShape="13"><CHAR>
2023년 9월 예닮공 기도이야기
</CHAR></TEXT></P><P ParaShape="14" Style="15"><TEXT CharShape="14"/></P><P ParaShape="14" Style="15"><TEXT CharShape="15"><CHAR>
[★1] 9월 예닮공 기도제목
</CHAR></TEXT></P><P ParaShape="14" Style="15"><TEXT CharShape="16"><CHAR>
① 
</CHAR></TEXT></P><P ParaShape="14" Style="15"><TEXT CharShape="16"><CHAR>
② 
</CHAR></TEXT></P><P ParaShape="14" Style="15"><TEXT CharShape="16"><CHAR>
③ 
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="11"/></P>"""

xml_prompt2_1 = """<P ParaShape="14" Style="15"><TEXT CharShape="15"><CHAR>
[★2] 교역자 기도제목
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="17"><CHAR>
노주찬 목사님
</CHAR></TEXT><TEXT CharShape="18"><CHAR> </CHAR></TEXT><TEXT CharShape="9"><CHAR>
① (감사)  ②  ③  ④  ⑤
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="11"/></P>"""

xml_prompt2_2 = """<P ParaShape="14" Style="15"><TEXT CharShape="15"><CHAR>
[★3] 간사 기도제목
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="17"><CHAR>
여13 최유진 사역간사
</CHAR></TEXT><TEXT CharShape="18"><CHAR> </CHAR></TEXT><TEXT CharShape="9"><CHAR>
① (감사)  ②  ③  ④  ⑤
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="17"><CHAR>
여12 김민경 예배간사
</CHAR></TEXT><TEXT CharShape="18"><CHAR> </CHAR></TEXT><TEXT CharShape="9"><CHAR>
① (감사)  ②  ③  ④  ⑤
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="17"><CHAR>
여8 김지수 새가족간사
</CHAR></TEXT><TEXT CharShape="18"><CHAR> </CHAR></TEXT><TEXT CharShape="9"><CHAR>
① (감사)  ②  ③  ④  ⑤  ⑥  ⑦  ⑧
</CHAR></TEXT></P>
<P ParaShape="14" Style="15"><TEXT CharShape="19"/></P>"""


xml_prompt1_1 = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?><?xml-stylesheet type="text/xsl" href="
(sample.xsl)
"?>"""




xml_prompt1_2 = """<HWPML Style="export" SubVersion="10.0.0.0" Version="2.91"><BODY><SECTION Id="0"><P ColumnBreak="false" InstId="2757524817" PageBreak="false" ParaShape="19" Style="0"><TEXT CharShape="7"><CHAR>
(■ 기업명)
</CHAR></TEXT></P><P ParaShape="0" Style="0"><TEXT CharShape="7"><TABLE BorderFill="4" CellSpacing="0" ColCount="4" PageBreak="Cell" RepeatHeader="true" RowCount="8"><SHAPEOBJECT InstId="1140567613"/><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="0" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>주 제</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="1" ColSpan="3" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="0" RowSpan="1" Width="33752"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="9"><CHAR>
(주 제)
</CHAR></TEXT></P></PARALIST></CELL></ROW><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="1" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>회 차</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="8" ColAddr="1" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="1" RowSpan="1" Width="10783"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="16"><CHAR>x차</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="5" ColAddr="2" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="1" RowSpan="1" Width="7083"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>구 분</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="8" ColAddr="3" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="1" RowSpan="1" Width="15886"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="21" Style="21"><TEXT CharShape="10"><CHAR>맞춤형 컨설팅</CHAR></TEXT></P></PARALIST></CELL></ROW><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="2" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>일 시</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="1" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="2" RowSpan="1" Width="10783"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="16"><CHAR>
(날짜)
</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="5" ColAddr="2" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="2" RowSpan="1" Width="7083"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>장 소</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="6" ColAddr="3" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="2" RowSpan="1" Width="15886"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="21" Style="21"><TEXT CharShape="16"><CHAR>온라인</CHAR></TEXT></P></PARALIST></CELL></ROW><ROW><CELL BorderFill="7" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="4438" Protect="false" RowAddr="3" RowSpan="2" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>참 석 자</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="1" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="3" RowSpan="1" Width="10783"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="22" Style="21"><TEXT CharShape="11"><CHAR>
(기업명)
</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="2" ColSpan="2" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="3" RowSpan="1" Width="22969"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="0" Style="0"><TEXT CharShape="13"><CHAR>
(참석자 1), (참석자 2)
</CHAR></TEXT></P></PARALIST></CELL></ROW><ROW><CELL BorderFill="9" ColAddr="1" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="4" RowSpan="1" Width="10783"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="22" Style="21"><TEXT CharShape="11"><CHAR>탭엔젤파트너스</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="2" ColSpan="2" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="2219" Protect="false" RowAddr="4" RowSpan="1" Width="22969"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="19" Style="22"><TEXT CharShape="13"><CHAR>
(참석자 1), (참석자 2)
"""

xml_prompt2_1 = """</CHAR></TEXT></P></PARALIST></CELL></ROW><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="31014" Protect="false" RowAddr="5" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>컨설팅 내용</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="1" ColSpan="3" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="31014" Protect="false" RowAddr="5" RowSpan="1" Width="33752"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center">"""

xml_prompt2_2_1 = """<P InstId="
" ParaShape="23" Style="2"><TEXT CharShape="12"><CHAR>
(키워드 1)
</CHAR></TEXT></P>
"""

xml_prompt2_2_2 = '<P InstId="2369843571" ParaShape="25" Style="0"><TEXT CharShape="17"/></P>'

xml_prompt2_3_1 = """<P ParaShape="30" Style="0"><TEXT CharShape="13"><CHAR>
(세부사항 1-1)
</CHAR></TEXT></P>"""

xml_prompt2_3_2 = """<P ParaShape="24" Style="0"><TEXT CharShape="13"/></P>"""

xml_prompt3_1 = """</PARALIST></CELL></ROW><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="7273" Protect="false" RowAddr="6" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="20" Style="21"><TEXT CharShape="8"><CHAR>향후 계획</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="9" ColAddr="1" ColSpan="3" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="7273" Protect="false" RowAddr="6" RowSpan="1" Width="33752"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center">"""
xml_prompt3_2_1 = """<P InstId="3105608238" ParaShape="26" Style="0"><TEXT CharShape="14"><CHAR>
(다음 주제 1)
</CHAR></TEXT></P>
"""

xml_prompt3_2_2 = """<P ParaShape="26" Style="0"><TEXT CharShape="14"><CHAR>
(다음 주제 2,3)
</CHAR></TEXT></P>
"""

xml_prompt3_3 = """</PARALIST></CELL></ROW><ROW><CELL BorderFill="5" ColAddr="0" ColSpan="1" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="14202" Protect="false" RowAddr="7" RowSpan="1" Width="8801"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="27" Style="21"><TEXT CharShape="11"><CHAR>현장 사진</CHAR></TEXT></P></PARALIST></CELL><CELL BorderFill="6" ColAddr="1" ColSpan="3" Dirty="false" Editable="false" HasMargin="true" Header="false" Height="14202" Protect="false" RowAddr="7" RowSpan="1" Width="33752"><CELLMARGIN Bottom="140" Left="510" Right="510" Top="140"/><PARALIST LineWrap="Break" LinkListID="0" LinkListIDNext="0" TextDirection="0" VertAlign="Center"><P ParaShape="28" Style="21"><TEXT CharShape="14"><CHAR> </CHAR></TEXT></P><P ParaShape="28" Style="21"><TEXT CharShape="14"><CHAR>  </CHAR></TEXT></P></PARALIST></CELL></ROW></TABLE></TEXT><TEXT CharShape="6"><CHAR/></TEXT></P></SECTION></BODY></HWPML>"""
