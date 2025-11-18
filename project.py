class project:
    def __init__(self):
        self.__all = {}          # i(0~15) -> 0 또는 1
        self.__group = {}        # 1의 개수(0~4) -> [i, i, ...]
        self.__change_bit = []   # 나중에 머지 결과(패턴, 커버 항목들) 넣을 곳
        self.__prime_implicants = {}  # 나중에 PI 저장
        self.__EPI = {}               # 나중에 EPI 저장
        self.__minimum_SOL = {}       # 최종 최소 논리식 정보


    def main(self):
        self.__value_input()
        self.__show_all()
        self.__grouping()
        self.__show_group()
        self.__changing()
        self.__show_changing()


    # -----------------------------
    # 값 입력
    # -----------------------------
    def __value_input(self):
        self.__all = {}

        temp = []
        c = 0
        while c < 16:
            v = int(input("0 or 1 입력: "))

            if v == 0 or v == 1:
                temp.append(v)
                c = c + 1
            else:
                print("0 or 1 만 입력 가능")

        i = 0
        while i < 16:
            value = temp[i]
            # i 자체가 패턴(정수 0~15), 값은 0,1
            self.__all[i] = value
            i = i + 1

        return


    # 1단계 진리표 출력 (ABCD로 나눠서)
    # -----------------------------
    def __show_all(self):
        print("A B C D")

        i = 0
        while i < 16:
            value = self.__all[i]

            # i를 2진수 4비트로 풀어서 A,B,C,D 만들기
            bits = format(i, '04b')
            a = bits[0]
            b = bits[1]
            c = bits[2]
            d = bits[3]

            print(a, b, c, d, " ", "(", i, ")", value)
            i = i + 1

        print()  # 줄 띄우기
        return


    # 2단계: 1의 개수(0~4)로 그룹핑
    # -----------------------------
    def __grouping(self):
        # 0,1,2,3,4 그룹을 딕셔너리로 준비
        self.__group = {0: [], 1: [], 2: [], 3: [], 4: []}

        i = 0
        while i < 16:
            value = self.__all[i]


            bit = format (i,'04b')


            one = 0
            j = 0
            while j < 4:
                if bit[j] == '1':
                    one += 1
                j += 1
            
            
            self.__group[one].append(i)
            i += 1

        return
    

    def __show_group(self):

        return
    

    def __changing(self):

        return
    
    def __show_changing(self):

        return
    
    
p = project()
p.main()

            # i 안에 들어 있는 1의 개수 세기 (패턴 기준)
