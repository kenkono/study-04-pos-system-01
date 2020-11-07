import csv

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_number_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)

    # 個数の登録
    def add_item_number(self,item_number):
        self.item_number_list.append(item_number)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    # 個数の表示
    def view_item_number(self):
        for item in self.item_number_list:
            print("商品個数:{}".format(item))
    
    def view_order_list(self):
        for master in self.item_master:
            print("商品名:{} 価格:{}".format(master.item_name,master.price))

class Master:
    def read_master_item(self, csv_file):
        with open(csv_file) as f:
            item_master=[]
            reader=csv.reader(f)
            for row in reader:
                item_master.append(Item("{}".format(row[0]),"{}".format(row[1]),"{}".format(row[2])))
            return item_master

### メイン処理
def main():
    master=Master()
    item_master=master.read_master_item('master.csv')
    # # マスタ登録
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    order=Order(item_master)
    order_number=input("商品コードを入力してください。")
    order.add_item_order(order_number)
    # 個数入力
    item_number=input("商品個数を入力してください。")
    order.add_item_number(item_number)
    
    # オーダー表示
    order.view_item_list()
    # 個数表示
    order.view_item_number()
    # 商品名と価格の表示
    order.view_order_list()
    
if __name__ == "__main__":
    main()