"""
Server code for Princeton Registrar Application with GUI
"""
import sys
import contextlib
import sqlite3

# Sanitize text input


def sanitize(field):
    """
    input: string field
    output: string with '%' and '_' formatted for SQL
    """
    sanitized = field.replace("%", "\\%")
    sanitized = sanitized.replace("_", "\\_")
    return sanitized


# Generate query based on available user input
def generate_query(dept, num, area, title):
    """
    Generates query body given inputs
    inputs:
    department,
    course #,
    course area,
    course title
    output:
    generated SQL query body,
    generated SQL query args
    """
    query_body = ""
    if dept or num or area or title:
        query_body = "WHERE "
    first = True
    query_args = []
    if dept:
        if not first:
            query_body += " AND "
        query_body += "cross.dept LIKE ?"
        query_args.append("%" + sanitize(dept) + "%")
        first = False
    if area:
        if not first:
            query_body += " AND "
        query_body += "co.area LIKE ?"
        query_args.append("%" + sanitize(area) + "%")
        first = False
    if title:
        if not first:
            query_body += " AND "
        query_body += "co.title LIKE ?"
        query_args.append("%" + sanitize(title.lower()) + "%")
        first = False
    if num:
        if not first:
            query_body += " AND "
        query_body += "cross.coursenum LIKE ?"
        query_args.append("%" + sanitize(str(num)) + "%")
        first = False
    if dept or num or area or title:
        query_body += "ESCAPE '\\'"
    return query_body, query_args


# returns all classes with specified attrebutes
def filter_classes(dept=None, num=None, area=None, title=None):
    """
    Inputs:
    -d dept   show only those classes whose department contains dept
    -n num    show only those classes whose course number contains num
    -a area   show only those classes whose distrib area contains area
    -t title  show only those classes whose course title contains title
    Outputs:
    Class descriptions filtered on inputs
    """
    try:
        with sqlite3.connect("reg.sqlite",
                             isolation_level=None) as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                query_head = """
                    SELECT cl.classid, cross.dept, cross.coursenum,
                    co.area, co.title
                    FROM classes as cl
                        INNER JOIN
                        courses as co
                        ON cl.courseid = co.courseid
                        INNER JOIN
                        crosslistings as cross
                        ON cl.courseid = cross.courseid
                """
                query_body, query_args = generate_query(
                    dept, num, area, title)
                query_closing = """
                    ORDER BY cross.dept ASC,
                    cross.coursenum ASC,
                    cl.classid ASC
                """
                cursor.execute(query_head + query_body +
                               query_closing, query_args)
                results = cursor.fetchall()

                output = []
                for result in results:
                    class_object = {
                        "id": str(result[0]),
                        "dept": str(result[1]),
                        "coursenum": str(result[2]),
                        "area": str(result[3]),
                        "title": str(result[4]),
                    }
                    output.append(class_object)
                return output

    except Exception:
        print(
            """A server error occured.
            Please contact the system administrator.""",
            file=sys.stderr,
        )
        return False


# returns details for a given class_id
def get_class_details(class_id):
    """
    Input:
    class_id
    Output:
    -> Course ID
    -> Days
    -> Start Time
    -> End Time
    -> Building
    -> Room
    -> Dept and Number
    -> Area
    -> Title
    -> Description
    -> Prereqs
    -> Professor
    """
    output = {}
    try:
        with sqlite3.connect("reg.sqlite",
                             isolation_level=None)as connection:
            with contextlib.closing(connection.cursor()) as cursor:
                class_query = """
                    SELECT *
                    FROM
                    classes as cl,
                    courses as co
                    WHERE cl.courseid = co.courseid
                    AND cl.classid = ?
                """
                cross_query = """
                    SELECT dept,coursenum,prereqs
                    FROM
                    crosslistings as cross,
                    classes as cl,
                    courses as co
                    WHERE cross.courseid = co.courseid
                    AND cl.courseid = co.courseid
                    AND cl.classid = ?
                    ORDER BY dept ASC, coursenum ASC
                """
                prof_query = """
                    SELECT profname
                    FROM classes AS cl
                    INNER JOIN coursesprofs AS cp ON (cl.courseid = cp.courseid)
                    INNER JOIN profs AS p ON (p.profid = cp.profid)
                    WHERE cl.classid =  ?
                    ORDER BY profname ASC
                """
                cursor.execute(class_query, [class_id])
                class_result = cursor.fetchone()

                if not class_result:
                    return print(
                        sys.argv[0] + ": no class with classid " +
                        class_id + " exists",
                        file=sys.stderr,
                    )

                output["course_id"] = str(class_result[1])
                output["days"] = str(class_result[2])
                output["start_time"] = str(class_result[3])
                output["end_time"] = str(class_result[4])
                output["building"] = str(class_result[5])
                output["room"] = str(class_result[6])

                cursor.execute(cross_query, [class_id])
                cross_result = cursor.fetchall()
                dept_and_num = []
                for c_result in cross_result:
                    dept_and_num.append(c_result[0] + " " + c_result[1])

                output["dept_and_num"] = dept_and_num

                output["area"] = class_result[8]
                output["title"] = class_result[9]
                output["description"] = class_result[10]
                output["prerequisites"] = class_result[11]

                cursor.execute(prof_query, [class_id])
                prof_result = cursor.fetchall()
                professors = []
                for prof in prof_result:
                    professors.append(prof[0])

                output["profs"] = professors
                return output

    except Exception as ex:
        print(sys.argv[0] + ": " + str(ex), file=sys.stderr)
        return 0
