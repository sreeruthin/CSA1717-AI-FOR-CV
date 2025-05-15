% Facts: Student-Teacher-Subject-Code Database
teaches(mr_smith, math, 101).
teaches(ms_johnson, physics, 102).
teaches(mr_brown, chemistry, 103).
teaches(ms_clark, biology, 104).
teaches(mr_white, english, 105).

studies(alice, math, 101).
studies(bob, physics, 102).
studies(charlie, chemistry, 103).
studies(diana, biology, 104).
studies(ella, english, 105).

% Rule to find the teacher of a student along with the subject code
teacher_of(Student, Teacher, Subject, Student_Code, Teacher_Code) :-
    studies(Student, Subject, Student_Code),
    teaches(Teacher, Subject, Teacher_Code).
