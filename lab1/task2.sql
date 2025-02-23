CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,    -- первинний ключ
	name TEXT NOT NULL
);
  
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,    -- первинний ключ
	course_name TEXT NOT NULL
);

CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY,     -- первинний ключ
	student_id INT NOT NULL,              -- зовнішній ключ
    course_id INT NOT NULL,               -- зовнішній ключ
    grade DECIMAL(4, 2) CHECK (grade >= 0.00 AND grade <= 5.00),
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE
);

INSERT INTO Student (student_id, name) VALUES 
    (1, 'Alice'),
    (2, 'Charlie');
	
INSERT INTO Course (course_id, course_name) VALUES 
    (1, 'Advanced Algorithms'),
    (3, 'Molecular Biology');
	
INSERT INTO Enrollment (student_id, course_id, grade) VALUES 
    (1, 1, 4.00),
    (2, 3, 4.00); 

------------------------------------------------------------
  



-- 2. Самоз'єднання та перетин
-- Запит 2: Знайти студентів з однаковими оцінками в різних курсах
SELECT DISTINCT 
    s1.name as student1, 
    s2.name as student2,
    e1.grade,
    e1.course_id as course1,
    e2.course_id as course2
FROM Student s1
JOIN Enrollment e1 ON s1.student_id = e1.student_id
JOIN Student s2 ON s1.student_id < s2.student_id
JOIN Enrollment e2 ON s2.student_id = e2.student_id
WHERE e1.grade = e2.grade AND e1.course_id != e2.course_id;

/* Очікуваний результат:
student1 | student2 | grade | course1 | course2
Alice|"Charlie"|"4.00"|"1"|"3"student
*/


