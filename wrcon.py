
import json



def write_config(config_name,modelwrite):
    with open("./config/"+config_name+".json",'w+',encoding='utf-8') as json_file:
        json.dump(modelwrite,json_file,ensure_ascii=False)
    print('已读取'+str(modelwrite))


def read_config(config_name):
    modelread={} #存放读取的数据
    with open("./config/"+config_name+".json",'r',encoding='utf-8') as json_file1:
        modelread=json.load(json_file1)
    return modelread

