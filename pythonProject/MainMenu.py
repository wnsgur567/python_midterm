import ScoreDataManager

# 시작과 종료시 파일저장됨
# admin, 파일 처리는 Manager를 통해 작업
class ScoreSystem:

    def __init__(self):
        ScoreDataManager.ScoreDataManager.static_init()  # 학생 및 학과 관련 정보 초기화

    # system process 실행
    def run(self):
        
        while True:
            try:
                # 메뉴를 선택하여 해당 프로세스 실행
                num = self.select_menu()
                if num == 1:
                    self.input_score()
                elif num == 2:
                    self.print_score()
                elif num == 3:
                    self.search_score()
                elif num == 4:
                    self.modify_score()
                elif num == 5:
                    ScoreDataManager.ScoreDataManager.run()
                elif num == 6:
                    ScoreDataManager.ScoreDataManager.save_data_to_file()
                    print("프로그램을 종료합니다")
                    break;

            except Exception as error:
                print(error.args)

    # y를 선택한 경우 true
    def select_continue(self) -> bool:
        c = input("추가입력(y/n)")
        if c == "y":
            return True
        elif c == "n":
            return False
        else:
            raise NotImplementedError('잘못된 입력 값입니다')

    # 메뉴 선택
    def select_menu(self):
        print("<메인 메뉴>")
        print("1.성적입력")
        print("2.성적출력")
        print("3.성적검색")
        print("4.성적수정")
        print("5.관리자 모드")
        print("6.종료")

        s = int(input("입력:"))
        if s < 1 or s > 6:
            raise NotImplementedError('잘못된 입력 값입니다')
        return s

    def input_score(self):
        while True:
            student_id = input("학번:")

            # id 로 학생 정보 검색
            student_info = ScoreDataManager.ScoreDataManager.find_student_info_by_id(student_id)
            major_id = student_info.major_id
            print("학번:{0}".format(student_info.id))
            print("학과:{0}".format(ScoreDataManager.ScoreDataManager.get_major_name(major_id)))
            # 성적 입력
            scores = []
            for item in ScoreDataManager.ScoreDataManager.major_subjects_list[major_id]:
                s = int(input("{0}:".format(item)))
                scores.append(s)
            student_info.scores = scores
            # 추가 입력 확인
            flag = self.select_continue()
            if not flag:
                break
    
    # 성적 출력 프로세스
    def print_score(self):
        major = ScoreDataManager.ScoreDataManager.select_major()
        print("학과 모든 학생의 성적을 출력합니다...")
        for student_info in ScoreDataManager.ScoreDataManager.major_studentInfo_lists[major]:
            ScoreDataManager.ScoreDataManager.print_student_score(student_info)
        print("성적출력 완료")

    # 성적 검색 프로세스
    def search_score(self):
        student_id = input("학번:")
        # id 로 학생 정보 검색
        student_info = ScoreDataManager.ScoreDataManager.find_student_info_by_id(student_id)
        ScoreDataManager.ScoreDataManager.print_student_score(student_info)

    # 성적 수정 프로세스
    def modify_score(self):
        student_id = input("학번:")

        # id 로 학생 정보 검색
        student_info = ScoreDataManager.ScoreDataManager.find_student_info_by_id(student_id)
        major_id = student_info.major_id
        print("학번:{0}".format(student_info.id))
        print("학과:{0}".format(ScoreDataManager.ScoreDataManager.get_major_name(major_id)))
        # 성적 입력
        scores = []
        for item in ScoreDataManager.ScoreDataManager.major_subjects_list[major_id]:
            s = int(input("{0}:".format(item)))
            scores.append(s)
        student_info.scores = scores


ss = ScoreSystem()
ss.run()
