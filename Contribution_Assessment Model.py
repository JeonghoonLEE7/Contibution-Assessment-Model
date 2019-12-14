# -*- coding: utf-8 -*-
"""
Spyder Editor

These are Model of assessment for each task and Grade Evaluation.
협력을 독려하는 평가 시스템 - 절대평가 시스템
"""

def Difficulty(): #난이도 별 업무(task) 만점 함수
    while(True):
        Diff = input("Step1. Task Difficulty: ex. ADVANCED/INTERMEDIATE/BASIC ")
        if Diff == 'advanced' or Diff == 'ADVANCED' or Diff == 'a'  or \
        Diff == 'A': 
            ini_score = 70 #난이도 '상' 배점 설정
        elif Diff == 'intermediate' or Diff == 'INTERMEDIATE' or \
        Diff == 'i' or Diff == 'I': 
            ini_score = 50 #난이도 '중' 배점 설정
        elif Diff == 'basic' or Diff == 'BASIC' or Diff == 'b' or Diff == 'B':
            ini_score = 30 #난이도 '하' 배점 설정
        else: #입력 예외처리
            print('Please retry') 
            continue
        break
    return ini_score

def q1_finish(ini_score): #업무(task) 완성률에 따른 평가 함수
    while(True):
        task = input('Step2. Did you complete your task?: Y/N ') #업무 완성 여부
        if task == 'Y' or task == 'y':
            mid_score = ini_score
        elif task == 'N'or task == 'n': #업무 미완성시, 완성률 입력
            fin_percent = int(input('Q3-1. How much did you completed?(%) '))
            mid_score = ini_score * (fin_percent/100)
        else: #입력 예외처리
            print('Please retry')
            continue
        break
    return mid_score

def q2_delay(delayed_day,mid_score): #업무 시간내 완료 여부 평가 함수
    while(True):
        task2 = input('Step3. Did you complete your task in time?: Y/N ') #업무 시간내 완료 여부
        if task2 == 'Y' or task2 == 'y':
            fin_score = mid_score
            return fin_score
        elif task2 == 'N' or task2 == 'n': #업무 지체된 일수만큼 입력
            delayed_day = int(input('Q4-1. How long was the task delayed?: '))
            fin_score = mid_score * (1-(delayed_day*0.2))
        else: #입력 예외처리
            print('Please retry')
            continue
        break
    return fin_score
    
####업무 개별 평가 점수####
sum_fin_score = 0#전체 업무 평가 만점의 총합
num_task = int(input('Step0. How many tasks do you have in total?: '))#개인이 맡은 업무의 수 입력
for i in range(num_task): #업무의 수만큼 업무 평가 위한 정보 입력
    print('')
    print('Task No.',i+1) #입력하는 Task가 몇 번째 Task인지 표시
    ini_score = 0
    delayed_day = 0  
        #1. 수행난이도 결정
    ini_score = Difficulty() 
    print('###1 The Total Score you can get is :', ini_score)
        #2. 프로젝트 목표를 달성하였는가?
    mid_score = q1_finish(ini_score) 
    print('###2 Temporary Evaluation Score is:', mid_score)
        #3. 시간내 완수하였는가?      
    fin_score = q2_delay(delayed_day,mid_score)
    print('###3 Your Task Score is:', round(fin_score,2))
        # 개인이 맡은 Task 평가 점수 합산. 소수점 둘째 자리까지.         
    sum_fin_score += fin_score
print('###4 Your Sum Of Tasks Score is ',round(sum_fin_score,2))


####Total 점수에서 등급 평가####
All_sum_fin_score = int(input('Enter the total Sum Of Task Score of all team members: '))
#만약에, 모든 팀원의 Sum of Task Score의 합이 240일 경우를 가정.
#총 2명의 팀원, 4개의 task : 70, 70, 50, 50
#기여도의 50%이상일 때 A, 30%~50% B, 그 이하 C - 조정 가능.

if sum_fin_score >= (All_sum_fin_score*0.5): 
    print('###5 Your Contribution rating is A') #A등급
elif sum_fin_score >= (All_sum_fin_score*0.3) and sum_fin_score <= (All_sum_fin_score*0.5):
    print('###5 Your Contribution rating is B') #B등급
else:
    print('###5 Your Contribution rating is C') #C등급


"""
print('This is a Task Evaluation Model')
ini_score = 0
delayed_day = 0
#업무의 난이도        
ini_score = Difficulty()
print('The Total Score you can get is :', ini_score)
#업무 목표 수행 달성여부
mid_score = q1_finish(ini_score)
print(mid_score)
fin_score = q2_delay(delayed_day,mid_score)
print('Your Task Score is:', round(fin_score,2))
"""