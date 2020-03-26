

def write_log(timenow,input_keyword,predicted_answer,distance_value):
    Log_obj={
        'time':timenow,
        'input':input_keyword,
        'answer': predicted_answer,
        'distance':distance_value
    }
    print('wrote log')
    return Log_obj
def write_untrain(timenow,input_keyword,predicted_answer,distance_value):
    Untrain ={
        'time':timenow,
        'input':input_keyword,
        'answer': predicted_answer,
        'distance':distance_value
    }
    print('wrote untrain')
    return  Untrain