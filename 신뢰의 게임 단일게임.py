import random

# 라운드 수 정하기
round = random.randint(3, 7)

#항상 협력꾼
def stranger_1():
    point=0
    for i in range(round):
        me=input('협력하시겠습니까? 배신하시겠습니까?')
        if me=='협력':
            point += 2
            print("당신과 상대는 모두 협력했습니다.")
            print("지금까지의 점수:",point)
        elif me=='배신':
            point+=3
            print("당신은 배신하고, 상대는 협력했습니다.")
            print("지금까지의 점수:", point)
        else:
            print("'협력' 혹은 '배신' 만 입력해주세요")
            break
    print("당신의 총점수:",point)

#항상 배신자
def stranger_2():
    point=0
    for i in range(round):
        me=input('협력하시겠습니까? 배신하시겠습니까?')
        if me=='협력':
            point -= 1
            print("당신은 협력했고, 상대는 배신했습니다.")
            print("지금까지의 점수:",point)
        elif me=='배신':
            print("당신과 상대는 모두 배신했습니다.")
            print("지금까지의 점수:", point)
        else:
            print("'협력' 혹은 '배신' 만 입력해주세요")
            break
    print("당신의 총점수:",point)

#따라쟁이
def stranger_3():
    i=0
    point=0
    repetition=0
    winlose=2
    print(round)###########
    while i>=0:
        if i==round:
            break
        else:
            me = input('협력하시겠습니까? 배신하시겠습니까?')
            if repetition == 0: #첫번째 게임플레이
                if me == '협력':
                    winlose = 1
                    point += 2
                    print("당신과 상대는 모두 협력했습니다.")
                    print("지금까지의 점수:", point)
                    repetition += 1
                    i += 1
                elif me == '배신':
                    winlose = 0
                    point += 3
                    print("당신은 배신하고, 상대는 협력했습니다.")
                    print("지금까지의 점수:", point)
                    repetition += 1
                    i += 1
                else:
                    print("'협력' 혹은 '배신' 만 입력해주세요")
                    break
            else: #2번 이상 게임플레이
                if me == '협력':
                    if winlose == 0:
                        winlose = 1
                        point -= 1
                        print("당신은 협력했고, 상대는 배신했습니다.")
                        print("지금까지의 점수:", point)
                        i += 1
                    else:
                        winlose = 1
                        point += 2
                        print("당신과 상대는 모두 협력했습니다.")
                        print("지금까지의 점수:", point)
                        i += 1
                elif me == '배신':
                    if winlose == 0:
                        winlose = 0
                        print("당신과 상대는 모두 배신했습니다.")
                        print("지금까지의 점수:", point)
                        i += 1
                    else:
                        winlose = 0
                        point += 3
                        print("당신은 배신하고, 상대는 협력했습니다.")
                        print("지금까지의 점수:", point)
                        i += 1
                else:
                    print("'협력' 혹은 '배신' 만 입력해주세요")
                    break
    print("당신의 총점수:", point)



#실행하기
stranger_3()