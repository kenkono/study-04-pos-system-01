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
            print("注文商品コード:{}".format(item))

    # 個数の表示
    def view_item_number(self):
        for item in self.item_number_list:
            print("注文商品個数:{}".format(item))
    
    # マスター情報の表示
    def view_order_list(self):
        for master in self.item_master:
            print("マスター情報 ID:{} 商品名:{} 価格:{}".format(master.item_code,master.item_name,master.price))

    # オーダー商品の合計金額
    def sum_order_price(self):
        sum_price = 0
        for order_item in self.item_order_list:
            for master in self.item_master:
                if master.item_code == order_item:
                    sum_price+=int(master.price)
        return sum_price

    # オーダー商品の合計個数
    def sum_order_quantity(self):
        sum_quantity=0
        for number in self.item_number_list:
            sum_quantity+=int(number)
        print("合計個数:{}".format(sum_quantity))
        return sum_quantity

class Master:
    def __init__(self):
        pass

    def read_master_item(self, csv_file):
        with open(csv_file) as f:
            item_master=[]
            reader=csv.reader(f)
            for row in reader:
                item_master.append(Item("{}".format(row[0]),"{}".format(row[1]),"{}".format(row[2])))
            return item_master

    # 支払い金額登録
    def pay_amount(self):
        pay_amount=input("お支払い金額を入力してください。")
        return pay_amount

### メイン処理
def main():
    master=Master()
    item_master=master.read_master_item('master.csv')
    # # マスタ登録
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    
    # オーダー商品コード登録
    order=Order(item_master)
    order_number=input("商品コードを入力してください。")
    order.add_item_order(order_number)
    
    # オーダー個数入力
    item_number=input("商品個数を入力してください。")
    order.add_item_number(item_number)
    
    # オーダー商品コード表示
    order.view_item_list()

    # オーダー個数表示
    order.view_item_number()

    # マスターの商品名と価格の表示
    order.view_order_list()

    # オーダーの合計個数表示
    sum_order_quantity=order.sum_order_quantity()

    # オーダーの合計金額表示
    sum_order_price=sum_order_quantity*order.sum_order_price()
    print("合計金額:{}".format(sum_order_price))

    # お釣りの表示
    change=int(master.pay_amount())-(sum_order_price)
    print("お釣り:{}".format(change))
    
if __name__ == "__main__":
    main()