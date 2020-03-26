import stringdist
import numpy as np
from db_connect import read_data, send_data
import stringdist as sd
from write_log import write_log,write_untrain
import  pendulum

def find_distance(input_keyword):
    distance_list = []
    theshold = 0.9
    timenow = pendulum.now('Asia/Bangkok')
    keyword_list, intent_list  = read_data('chatdata')
    for compare_keyword in keyword_list:
        distance = sd.levenshtein_norm(input_keyword,compare_keyword)
        distance_list.append(distance)
    neartest_idx = np.armin(distance_list)
    distance_value = min(distance_list)

    if distance_value > theshold:
        predicted_answer = 'ไม่เข้าใจครับ'
        untrain =write_untrain(timenow,input_keyword,predicted_answer,distance_value)
        send_data('untraindata',untrain)
        log = write_log(timenow,input_keyword,predicted_answer,distance_value)
        send_data('chatlog',log)
        return  predicted_answer 
        
    elif distance_value<=theshold:
        predicted_answer = intent_list[neartest_idx]  
        write_log(timenow,input_keyword,predicted_answer,distance_value)
        send_data('chatlog',log)
        return  predicted_answer 

    


