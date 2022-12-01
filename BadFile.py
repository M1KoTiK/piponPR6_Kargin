import json
from datetime import datetime 
JSON_PATH = ""
TXT_PATH = ""

def process_result(start_string :str, finish_string :str) -> datetime:
    start : datetime = datetime.strptime(start_string,"%H:%M:%S,%f")
    finish : datetime = datetime.strptime(finish_string,"%H:%M:%S,%f")
    total : datetime = finish - start
    return total
    


def main():
    JSON_PATH = r'C:\Users\User\source\reposPython\PR6_Kargin\competitors2.json'
    TXT_PATH = r'C:\Users\User\source\reposPython\PR6_Kargin\results_RUN.txt'  
    json_competitors = open(JSON_PATH,'r', encoding="UTF-8")
    string_competitors = json_competitors.read()
    dict_competitors = json.loads(string_competitors)
    json_competitors.close()
    dict_results = {}
    txt_results = open(TXT_PATH, 'r')
    while True:
        line_start = txt_results.readline()
        line_finish = txt_results.readline()
        if not line_start or not line_finish:
            break
        list_start = line_start.split()
        list_finish = line_finish.split()
        time = process_result(list_start[2],list_finish[2])
        sportsman_number = list_start[0]
        dict_results[sportsman_number]= time   

    def sort_sportsman(key: str):
        return dict_results[key].total_seconds()
    print("Занятое место \t Нагрудный номер \t Имя \t Фамилия \t Результат")
    i = 1
    for sportsman_number in sorted(dict_results, key = sort_sportsman):
        print(f"{i} \t {sportsman_number} \t {dict_competitors[sportsman_number]['Name']} \t {dict_competitors[sportsman_number]['Surname']} \t {dict_results[sportsman_number]}")
        i +=1



if __name__ == "__main__":
    main()
    

