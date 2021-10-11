class ScoreSystem:

    def __init__(self):
        self.select_menu = 0

    def SelectMenu(self):
        print("<메인 메뉴>")
        print("1.성적입력")
        print("2.성적출력")
        print("3.성적검색")
        print("4.성적수정")
        print("5.관리자 모드")
        print("6.종료")

        self.select_menu = int(input())
        if self.select_menu < 1 or self.select_menu > 6:
            raise NotImplementedError('잘못된 입력 값입니다')

    def InputScore(self):
        while True:
            id = int(input("학번:"))

            # id 로 이름과 학과를 검색

            sub_gameAnalysis = input("게임분석:")
            sub_gameNetwork = input("게임네트워크 프로그래밍:")
            sub_gameEngine = input("게임엔진:")
            sub_math = input("이산수학:")
            sub_graphicProgramming = input("게임그래픽프로그래밍:")
            info = (sub_gameAnalysis, sub_gameNetwork, sub_gameEngine, sub_math, sub_graphicProgramming)

    def Run(self):

        while True:
            try:
                self.SelectMenu()

            except NotImplementedError as error:
                print(error.args)



