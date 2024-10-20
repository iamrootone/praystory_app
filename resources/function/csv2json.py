import pandas as pd
import json

def extract_age_name(text):
    x = text.split(' ')
    return (int(x[0][1:]), x[1])

def sort_dict_by_custom_key(input_dict, custom_function):
    # custom_function을 키의 정렬 기준으로 사용
    sorted_keys = sorted(input_dict.keys(), key=custom_function, reverse=True)
    
    # 정렬된 키를 사용하여 새로운 dictionary 생성
    sorted_dict = {key: input_dict[key] for key in sorted_keys}
    
    return sorted_dict

def replace_plus(text, a, b):
    text = text.replace(f"{a}", f"{b}")
    text = text.replace(f"{b}", f"{b} ")
    text = text.replace(f"{b}   ", f"{b} ")
    text = text.replace(f"{b}  ", f"{b} ")

    text = text.replace(f"{b}", f" {b}")
    text = text.replace(f"   {b}", f" {b}")
    text = text.replace(f"  {b}", f" {b}")
    return text

def convert(text):
    text = text.replace("\n", " ")
    nums = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    icons = ["⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩"]
    for num, icon in zip(nums, icons):
        text = replace_plus(text, f"({num})", f"{icon}")
        text = replace_plus(text, f"{num})", f"{icon}")
        # text = replace_plus(text, f"{num}.", f"{icon}")

    if text[0] == "남" or text[0] == "여":
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
    else:
        id = text.index("①")
        text = text[id:]
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")

    text = text.replace(f"( 감사)", f"(감사)")
    text = text.replace(f"(감사 )", f"(감사)")
    text = text.replace(f"( 감사 )", f"(감사)")
    text = text.replace(f"(감사)", f"(감사) ")
    text = text.replace(f"(감사)   ", f"(감사) ")
    text = text.replace(f"(감사)  ", f"(감사) ")
    text = text.replace(u'\xa0', u'')

    ## 감사 추가
    # 각 1번 기도제목마다 감사 추가
    texts_1= text.split('①')
    text = ""
    for text_1 in texts_1:
        if len(text_1.split('②')) > 1:
            x = text_1.split('②')[0]
        else:
            x = text_1
        if '(감사)' not in x and '감사' in x:
            if '감사 ' in x or '감사.' in x or '감사합니다' in x or '감사드립니다' in x:
                text_1 = " (감사)" + text_1

        text += text_1 + '①'

    text = text[:-1]

    # 각 2번 기도제목마다 감사 추가
    texts_2= text.split('②')
    text = ""
    for text_2 in texts_2:
        if len(text_2.split('③')) > 1:
            x = text_2.split('③')[0]
        else:
            x = text_2.split('①')[0]

        if '(감사)' not in x and '감사' in x:
            if '감사 ' in x or '감사.' in x or '감사합니다' in x or '감사드립니다' in x:
                text_2 = " (감사)" + text_2

        text += text_2 + '②'

    text = text[:-1]

    return text

def no_name(text):
    id = text.index("①")
    return text[id:]


def GBS_split(text, isEBS = False):
    text0 = text

    male_index = []
    num = 0
    while True:
        try:
            id = text.index("남")
        except:
            break
        try:
            if int(text[id+1]) > 0 and int(text[id+1]) < 10:
                male_index.append(num + id)
        except:
            u = ""

        try:
            if text[id+1] == " " and int(text[id+2]) > 0 and int(text[id+2]) < 10:
                male_index.append(num + id)
        except:
            u = ""

        num += id + 1
        text = text[id+1:]

    female_index = []
    num = 0
    text = text0
    while True:
        try:
            id = text.index("여")
        except:
            break
        try:
            if int(text[id+1]) > 0 and int(text[id+1]) < 10:
                female_index.append(num + id)
        except:
            u = ""

        try:
            if text[id+1] == " " and int(text[id+2]) > 0 and int(text[id+2]) < 10:
                female_index.append(num + id)
        except:
            u = ""
        
        num += id + 1
        text = text[id+1:]

    x = list(set(male_index).union(set(female_index)))
    x.sort()

    data = {}
    pray = text0[:x[0]]
    if isEBS:
        data["EBS 기도제목"] = pray
    else:
        data["GBS 기도제목"] = pray

    for i in range(len(x)):
        if i == (len(x)-1):
            pray = text0[x[i]:]
        else:
            pray = text0[x[i]:x[i+1]]

        try:
            mid = pray.index("①")
        except:
            continue
        name = pray[:mid].strip()
        if name[1] == " ":
            name = name[0] + name[2:]
        
        y = name[2]
        if y != " ":
            nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if y not in nums:
                name = name.replace(name[1], name[1] + " ")

        data[name] = pray[mid:].strip()

    return data

def pray2name(pray):
    position = pray.index("1)")
    name = pray[:position]
    name = name.strip()
    return name

def csv2json(csv_path):
    df = pd.read_csv(csv_path)

    data = {}

    ## 예닮공 & 교역자 기도제목
    df_0 = df[df["기도제목 범주"] == "공동체 & 교역자 기도제목"]
    try:
        data["예닮공 기도제목"] = convert(df_0["공동체 기도제목"].to_list()[0])
    except:
        print("공동체 기도제목이 없습니다.")
    
    try:
        data["교역자 기도제목"] = {
            df_0["이름"].to_list()[0].strip()[:3].strip(): convert(df_0["교역자 기도제목"].to_list()[0])
        }
    except:
        print("교역자 기도제목이 없습니다.")


    ## 간사 & 지기 기도제목 
    df_1 = df[df["기도제목 범주"] == "간사 & 지기 기도제목"]
    positions_1 = df_1["직분"].to_list()
    prays_1 = df_1["기도제목"].to_list()
    data_1 = {}
    data_jigi = {}
    for position, pray in zip(positions_1, prays_1):
        name = pray2name(pray)

        if "간사" in position:
            data_1[name + " " + position] = no_name(convert(pray))

        if "지기" in position:
            data_jigi[name + " " + position] = no_name(convert(pray))
        

    data["간사 기도제목"] = sort_dict_by_custom_key(data_1, extract_age_name)


    ## 새돌리더 기도제목
    df_2 = df[df["기도제목 범주"] == "새돌리더 기도제목"]
    positions_2 = df_2["직분.1"].to_list()
    prays_2 = df_2["기도제목.1"].to_list()
    data_2 = {}
    for position, pray in zip(positions_2, prays_2):
        name = pray2name(pray)
        data_2[name + " " + position] = no_name(convert(pray))

    data["새돌리더 기도제목"] = data_2

    ## 학년 기도제목
    df_3 = df[df["기도제목 범주"] == "학년 기도제목"]
    numbers_3 = df_3["학년"].to_list()
    numbers_3 = [int(x[:-2]) for x in numbers_3]
    names_3 = df_3["학년 이름"].to_list() # 학년 이름 (1학년은 새돌이라고 입력)
    prays_3 = df_3["기도제목.2"].to_list()

    data_3 = {}
    for number, name, pray, _ in sorted(zip(numbers_3, names_3, prays_3, range(len(numbers_3))), key=lambda k: (k[0], k[3])):
        data_3[str(number) + "학년 " + name.strip()] = convert(pray)

    data["학년 기도제목"] = data_3

    ## 제자반 기도제목
    df_4 = df[df["기도제목 범주"] == "제자반 기도제목"]
    names_4 = df_4["제자반 이름"].to_list()
    semesters = df_4["제자반 학기"].to_list()
    days = df_4["제자반 요일"].to_list()
    prays_4 = df_4["기도제목.3"].to_list()
    data_4 = {}
    for name, day, semester, pray in zip(names_4, days, semesters, prays_4):
        # 화요 2학기제자반 &lt;반딧불이&gt;
        data_4[f"# {day.strip()[:2]} {semester.strip()}제자반 &lt;{name.strip()}&gt;"] = convert(pray)

    data["제자반 기도제목"] = data_4

    ## 섬김팀 기도제목
    df_5 = df[df["기도제목 범주"] == "섬김팀 기도제목"]
    names_5 = df_5["섬김팀"].to_list()
    prays_5 = df_5["기도제목.4"].to_list()
    data_5 = {}
    for name, pray, _ in sorted(zip(names_5, prays_5, range(len(names_5))), key=lambda k: (k[0], k[2])):
        real_key = name.strip()
        data_5[real_key] = convert(pray)

    data["섬김팀 기도제목"] = data_5

    ## GBS 기도제목
    jigis = list(set(df["지기 이름"].to_list()))
    jigis = [x for x in jigis if x == x]
    jigis.sort()

    data_6 = {}
    for jigi in jigis:
        df_x = df[df["지기 이름"] == jigi]
        names_x = df_x["리더 이름"].to_list()
        prays_GBS = df_x["GBS 기도제목"].to_list()
        prays_members = df_x["리더 & 조원 기도제목"].to_list()

        data_x = {}
        jigi_name = [x for x in data_jigi.keys() if (jigi in x) and "지기" in x]
        if len(jigi_name) > 0:
            jigi_pray = data_jigi[jigi_name[0]]
            jigi_name = jigi_name[0].replace("지기", "").strip()
            data_x[jigi_name] = convert(jigi_pray)

        for name, pray_GBS, pray_member, _ in sorted(zip(names_x, prays_GBS, prays_members, range(len(names_x))), key=lambda k: (k[0], k[3])):
            try:
                if name.strip() not in pray_member:
                    print(f"{name} GBS 검토 필요. 리더님의 기도제목이 리더&조원 기도제목에 없습니다.")
                    pray_member = f"남99 {name.strip()} 1) 기도제목이 없습니다 2) 기도제목을 입력해주세요 3) 기도제목 Please " + pray_member
                
                result = GBS_split(convert(pray_GBS) + " " + convert(pray_member))

                if result == {}:
                    print(f"{name} GBS 검토 필요. 기도제목이 비어있습니다.")
                else:
                    data_x[name.strip()] = result
            except:
                print(f"{name} GBS 검토 필요.")

        data_6[jigi] = data_x

    data["GBS"] = data_6

    ## 새가족 EBS 기도제목
    names_EBS_leaders = df["리더 이름.1"].to_list()
    prays_EBS = df["EBS 기도제목"].to_list()
    prays_EBS_members = df["리더 & 조원 기도제목.1"].to_list()

    names_EBS_leaders = [x for x in names_EBS_leaders if x == x]
    prays_EBS = [x for x in prays_EBS if x == x]
    prays_EBS_members = [x for x in prays_EBS_members if x == x]

    data_7 = {}

    for name, pray_EBS, pray_member, _ in sorted(zip(names_EBS_leaders, prays_EBS, prays_EBS_members, range(len(names_EBS_leaders))), key=lambda k: (k[0], k[3])):
        try:
            if name.strip() not in pray_member:
                print(f"{name} EBS 검토 필요. 리더님의 기도제목이 리더&조원 기도제목에 없습니다.")
                pray_member = f"남99 {name.strip()} 1) 기도제목이 없습니다 2) 기도제목을 입력해주세요 3) 기도제목 Please " + pray_member
            
            result = GBS_split(convert(pray_EBS) + " " + convert(pray_member), isEBS=True)

            if result == {}:
                print(f"{name} EBS 검토 필요. 기도제목이 비어있습니다.")
            else:
                data_7[name.strip()] = result
        except:
            print(f"{name} EBS 검토 필요.")

    data["새가족 EBS"] = data_7

    ## 새돌 EBS 기도제목

    return data


if __name__ == "__main__":
    csv_path = "/Users/geunwon/Desktop/Dalpha/code/pray_story/9월 예닮공 기도이야기(응답) - 설문지 응답 시트1.csv"
    data, error_message = csv2json(csv_path)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
