import random

cnt_main = 0

# members = ["jaehong", "dowan", "seohyeon", "soobin", "daye", "sinae", "seeun", "yun", "jeoungtack", "suyong", "juye"]
members = ["재홍", "도완", "서현", "수빈", "다예", "신애", "세은", "윤", "정택", "수용", "주예"]

tueAm = ["수용", "주예"]
tuePm = ["수용", "다예"]
wedAm = ["정택", "수용", "주예"]
wedPm = ["윤", "신애", "수빈"]
thuAm = ["수용", "주예", "정택"]
thuPm = ["수빈", "다예"]
friAm = ["서현", "정택", "수용"]
friPm = ["서현", "수용", "윤", "수빈", "다예"]
satAm = ["서현", "세은", "재홍"]
satPm = ["서현", "윤", "세은", "정택", "신애", "수빈", "재홍", "도완", "다예"]



print("큐티모임 멤버의 시간표를 입력해주세요")
# tueAm = list(input("화 오전: ").split())
# tuePm = list(input("화 오후: ").split())
# wedAm = list(input("수 오전: ").split())
# wedPm = list(input("수 오후: ").split())
# thuAm = list(input("목 오전: ").split())
# thuPm = list(input("목 오후: ").split())
# friAm = list(input("금 오전: ").split())
# friPm = list(input("금 오후: ").split())
# satAm = list(input("토 오전: ").split())
# satPm = list(input("토 오후: ").split())




finTueAm = []
finTuePm = []
finWedAm = []
finWedPm = []
finThuAm = []
finThuPm = []
finFriAm = []
finFriPm = []
finSatAm = []
finSatPm = []


# 가능한 요일 리스트
days = []
days.append(tueAm)
days.append(tuePm)
days.append(wedAm)
days.append(wedPm)
days.append(thuAm)
days.append(tuePm)
days.append(friAm)
days.append(friPm)
days.append(satAm)
days.append(satPm)



# 최종 결과 배정
finDays = []
finDays.append(finTueAm)
finDays.append(finTuePm)
finDays.append(finWedAm)
finDays.append(finWedPm)
finDays.append(finThuAm)
finDays.append(finThuPm)
finDays.append(finFriAm)
finDays.append(finFriPm)
finDays.append(finSatAm)
finDays.append(finSatPm)


# 하루만 가능한 멤버, 2일 가능 멤버, 3일 가능 멤버, 4일 가능 멤버, 5일 전부 가능 멤버
oneDay = []
twoDay = []
threeDay = []
fourDay = []
fiveDay = []
sixDay = []
sevenDay = []
eightDay = []
nineDay = []
tenDay = []

possibleDays = []
possibleDays.append(oneDay)
possibleDays.append(twoDay)
possibleDays.append(threeDay)
possibleDays.append(fourDay)
possibleDays.append(fiveDay)
possibleDays.append(sixDay)
possibleDays.append(sevenDay)
possibleDays.append(eightDay)
possibleDays.append(nineDay)
possibleDays.append(tenDay)


def findMemberIndex(member):
    index = []
    for i, day in enumerate(days):
        for m in day:
            if m == member:
                index.append(i)
                break
    return index


def addNumberOfPossibleDays():
    for member in members:
        index = findMemberIndex(member)
        for i, day in enumerate(possibleDays):
            if (len(index) == i+1):
                day.append(member)



# 해당 멤버를 요일에 1차로 배정한다
def selectDay(member):
    possibleDayIndex = findMemberIndex(member)

    randomIndex = random.choice(possibleDayIndex)
    finDays[randomIndex].append(member)



def placeMembers():
    for day in possibleDays:
        for member in day:
            selectDay(member)



def showResult(finDays):
    print("\n최종 선정 결과")
    print("화 오전:", finDays[0])
    print("화 오후:", finDays[1])
    print("수 오전:", finDays[2])
    print("수 오후:", finDays[3])
    print("목 오전:", finDays[4])
    print("목 오후:", finDays[5])
    print("금 오전:", finDays[6])
    print("금 오후:", finDays[7])
    print("토 오전:", finDays[8])
    print("토 오후:", finDays[9])


def clear():
    for day in days:
        if (len(day) <= 2):
            day.clear()

    for day in possibleDays:
        day.clear()

    for day in finDays:
        day.clear()



def run():

    #배열 초기화
    clear()

    # print("가능한 요일")
    # print(days)
    # print()
    
    # 하루가능한 사람들, 이틀 가능한 사람들, ... , 열흘 가능한 사람들 파악
    addNumberOfPossibleDays()
    
    # 랜덤으로 가능한 요일들에 멤버 배치
    placeMembers()



    


def threeGroup():
    cnt = [0] * 20

    for _ in range(20000):  
        run()

        for day in finDays:
            cnt[len(day)] += 1

        # <3, 4, 4>
        if (cnt[3] == 1 and cnt[4] == 2):
            showResult(finDays)
            pass
        # <3, 3, 5>
        if (cnt[3] == 2 and cnt[5] == 1):
            # showResult(finDays)
            pass
        
        cnt = [0] * 20

    


def fourGroup():
    cnt = [0] * 10

    for _ in range(20000):  
        run()

        for day in finDays:
            cnt[len(day)] += 1

        #<5, 6>
        if (cnt[5] == 1 and cnt[6] == 1):
            showResult(finDays)
            pass
        #<4, 7> 
        if (cnt[4] == 1 and cnt[7] == 1):
            # showResult(finDays)
            pass
        #<3, 8> 
        if (cnt[3] == 1 and cnt[8] == 1):
            # showResult(finDays)
            pass
            

        cnt = [0] * 20




# run  
threeGroup()
# fourGroup()

print("End")
        


     

    

    

            
