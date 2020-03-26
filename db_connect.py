from pymongo import MongoClient

client = MongoClient(
    'mongodb://pattanunNP:ssrg834@ds359298.mlab.com:59298/heroku_7hhcq7v4?retryWrites=false')
chatbot_db = client["heroku_7hhcq7v4"]

def read_data(collection_name):## อ่านข้้อมูลจาก Database นะครับ
     compare_text =[]
     sentiment_text=[] # สร้าง list ไว้เปรียบเทียบ
     my_collection = chatbot_db[collection_name] #เรียก coloection 
     for all_data in my_collection.find(): #เรียก data ทั้ง db
        keyword_data = all_data['keyword']
        intent_data = all_data['intent']
        compare_text.append(intent_data)
        sentiment_text.append(sentiment_data)
     return compare_text, sentiment_text

def send_data(collection_name,data):## collection ที่ต้องการส่ง และข้อมูล
    my_collection = chatbot_db[collection_name] #เรียก coloection 
    my_collection.insert_one(data) #ส่ง data
    print("collection:",collection_name,"inserted!","data:",data)
