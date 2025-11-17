class project:
    def __init__(self):
        self.__all = [] #0,1를 저장할 변수
        self.__group = [] #0,1,2,3,4개 그룹핑 변수
        self.__change_bit = [] #000- 00-0 이런식으로 바꾼 항 저장 변수
        self.__prime_implicants = {} # 000- 와 100- 이런 식으로 숫자가 다른 값을 추출 후 선택표에 씀
        self.__EPI = {} # 선택 표에서 겹치는 숫자가 안나온 항을 저장
        self.__minimum_SOL = {} #식 함축 f(x) = ----- 이런식


    def main(self):
        self.__value_input()
        self.__show_all()
        self.__grouping()
        self.__show_group()




    def __grouping(self):
        self.__group = [[],[],[],[],[]]

        i = 0
        while i < 16:
            bit,value = self.__all[i]

           
            one = 0
            j = 0

            while j < 4:
                if bit[j] == '1':
                    one += 1
                j += 1


            self.__group[one].append((bit,i))
            i += 1
        return
    

    def __show_group(self):
        k = 0

        while k < 5:
            print("1의 개수 :",k , ":")


            group_list = self.__group[k]

            if len(group_list) == 0:
                print("없음")
            
            else :
                t = 0 
                while t < len(group_list):
                    bit, idx = group_list[t]

                    print(" ", bit,"(",idx,")")
                
                    t += 1


            print()
            k += 1

        return



    def __value_input(self):
        self.__all = {}
        self.__all = []
        

        temp = []
        c = 0
        while c < 16:
            v = int(input("0 or 1 입력:"))

            if v == 0:
                temp.append(0)
                c += 1

            elif v == 1:
                temp.append(1)
                c += 1

            else:
                print("0 or 1 만 입력 가능")


    

        i = 0
        while i < 16:
            bit = format(i, '04b')
            value = temp[i]
            self.__all[i] = (bit , value)
            self.__all.append((bit,value))
            i += 1
        
        return
    
    def __show_all(self):
        i = 0
        while i < 16:
            bit,value = self.__all[i]
            print(bit , "(",i,")",value)
            i += 1

        return




p = project()
p.main()


