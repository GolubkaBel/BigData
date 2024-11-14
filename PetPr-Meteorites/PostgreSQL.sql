WITH cond1 AS ( -- ученики
  SELECT users.id AS user_id, users.last_name AS user_name, users.city_id AS user_city_id
  FROM users INNER JOIN user_roles ON users.user_role_id=user_roles.id
  WHERE user_roles.name='student'
), cond2 AS ( -- годовые курсы (ЕГЭ/ОГЭ)
  SELECT courses.id AS course_id, courses.name AS course_name, 
  	courses.subject_id AS c_sub_id, courses.starts_at AS course_start
  FROM courses INNER JOIN course_types ON courses.course_type_id=course_types.id
  WHERE course_types.name='Годовой'
), cond3 AS ( -- годовые курсы и соответствующие им предметы
  SELECT cond2.course_id AS course_id, subjects.name AS subject_name, 
  	subjects.project AS subject_type 
  FROM cond2 INNER JOIN subjects ON cond2.c_sub_id=subjects.id  
), cond4 AS ( -- ученик и кол-во выполненного им дз, если такие есть
  SELECT cond1.user_id AS user_id, COUNT(homework_done) AS count_homework_done
  FROM cond1 LEFT JOIN homework_done ON cond1.user_id = homework_done.user_id
  GROUP BY cond1.user_id
), cond5 AS ( -- ученики и их города, если такие имеются
  SELECT cond1.user_id AS user_id, cities.name AS city_name
  FROM cond1 LEFT JOIN cities ON cond1.user_city_id=cities.id
) 
-- объединение всех наработок в итоговую таблицу через табл. course_users 
SELECT 
	cond2.course_id, cond2.course_name,
	(SELECT cond3.subject_name FROM cond3 WHERE course_users.course_id=cond3.course_id),
    (SELECT cond3.subject_type FROM cond3 WHERE course_users.course_id=cond3.course_id),
    cond2.course_start, cond1.user_id, cond1.user_name,
    (SELECT cond5.city_name FROM cond5 WHERE course_users.user_id=cond5.user_id),
    course_users.created_at AS open_course, --дата создания записи о присвоение курса ученику
	EXTRACT(MONTH FROM AGE(DATE(TO_TIMESTAMP(cond2.course_start, 'YYYY-MM-DD HH24:MI:SS.MS') + INTERVAL '1 year'), CURRENT_DATE))
            AS full_month_to_end, --полных месяцев осталось сравнительно текущей даты от начала курса
    cond4.count_homework_done       
FROM course_users INNER JOIN cond1 ON course_users.user_id=cond1.user_id
INNER JOIN cond2 ON course_users.course_id=cond2.course_id
LEFT JOIN cond4 ON course_users.user_id=cond4.user_id;
