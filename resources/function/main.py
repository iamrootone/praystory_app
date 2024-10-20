from xmlstructures import *
import shutil
from pathlib import Path
import json
from csv2json import csv2json
from xml.dom.minidom import parse, parseString
import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def read_json_file(file_path):
    """주어진 경로의 JSON 파일을 읽고 파이썬 객체로 반환합니다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def format_xml(xml_string):
    """주어진 XML 문자열을 들여쓰기하여 반환합니다."""
    dom = parseString(xml_string)
    return dom.toprettyxml()


def load_xml_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        dom = parse(file)
        return dom.toxml()
    
    
def hwpStage(data, date, xml_path, xsl_path):
    # result_save_path = Path(f"results/{date}")
    result_save_path = Path(f"function/results")
    

    try:
        text = xml_prompt0(date, data["예닮공 기도제목"])
    except:
        text = xml_prompt0(date, "")
    
    try:
        text += xml_prompt1_noformat(data["교역자 기도제목"], "교역자 기도제목")
    except:
        text += xml_prompt1_noformat("", "교역자 기도제목")

    text += xml_prompt1_noformat(data["간사 기도제목"], "간사 기도제목")
    text += xml_prompt1_noformat(data["새돌리더 기도제목"], "새돌리더 기도제목")
    text += xml_prompt1_noformat(data["학년 기도제목"], "학년 기도제목")
    text += xml_prompt2_noformat(data["제자반 기도제목"], "제자반 기도제목")
    text += xml_prompt2_noformat(data["섬김팀 기도제목"], "섬김팀 기도제목")

    

    # GBS
    jigis = data["GBS"].keys()
    for jigi in jigis:
        text += xml_prompt_noformat_LBS(data["GBS"][jigi], f"{jigi[1:]} 두레 기도제목")

    # EBS
    try:
        text += xml_prompt_noformat_EBS(data["새가족 EBS"], "새가족 EBS 기도제목")
    except:
        print(f"새가족 EBS 기도제목이 없습니다.")

    text += xml_end()


    try:
        formatted_xml = format_xml(text)
    except:
        print("xml 변환이 안됩니다")

    with open(xml_path, "w", encoding='utf-8') as xml_file:
        xml_file.write(formatted_xml)

    shutil.copy2(xsl_path, xml_path[:-3] + 'xsl')

    return text

def print_info1(text=" "):
    print(f"[INFO_1]{text}")

def print_info2(text=" "):
    print(f"[INFO_2]{text}")

def print_info3(text=" "):
    print(f"[INFO_3]{text}")

if __name__ == "__main__":

    # 입력 인자: CSV 파일 경로, 출력할 XML 파일 경로, 년도, 월
    csv_path = sys.argv[1]
    xml_save_path = sys.argv[2]
    xsl_format_path = sys.argv[3]
    year = sys.argv[4]
    month = sys.argv[5]
    date = year + month

    data = csv2json(csv_path)
    print_info1()
    print_info1("제출한 인원 명단")
    
    for key in data.keys():
        if key == "GBS":
            for gbs_key in data[key].keys():
                print_info2()
                print_info2(f"{gbs_key} 두레")
                print_info3(", ".join(list(data[key][gbs_key].keys())))
        else:
            print_info2()
            print_info2(key)
            print_info3(", ".join(list(data[key].keys())))

    hwpStage(data, date, xml_save_path, xsl_format_path)
