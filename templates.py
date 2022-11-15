FOOTER_TEMPLATE = ('''
<hr>
Created by Nickolas Casalinuovo and Saadi Ahmad.
<hr>
''')

HEADER_TEMPLATE = ('''
<h1>Registrar's Office</h1>
''')

FORM_TEMPLATE = ('''
<hr>
<form action="" method="get">
    <table>
        <tbody><tr>
        <td align="right">Dept:</td>
        <td><input type="text" name="dept" value="{{dept}}"><br></td>
        </tr>

        <tr>
        <td align="right">Number:</td>
        <td>
            <input type="text" name="coursenum" value="{{coursenum}}"><br>
        </td>
        </tr>

        <tr>
        <td align="right">Area:</td>
        <td><input type="text" name="area" value="{{area}}"><br></td>
        </tr>

        <tr>
        <td align="right">Title:</td>
        <td>
            <input type="text" name="title" value="{{title}}"><br>
        </td>
        </tr>

        <tr>
        <td></td>
        <td><input type="submit"></td>
        </tr>

    </tbody></table>
</form>
<hr>
''')


SEARCH_RESULTS_TEMPLATE =  ('''
    <table>
        <tbody>
            <tr>
                <td><strong>ClassId</strong></td>
                <td><strong>Dept</strong></td>
                <td><strong>Num</strong></td>
                <td><strong>Area</strong></td>
                <td><strong>Title</strong></td>
            </tr>
            {{results}}
        </tbody>
    </table>
''')

INDEX_TEMPLATE = ('''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Registrar's Office</title>
        </head>
        <body>
            {{header}}
            <h2>Class Search</h2>
            {{form}}
            {{search_results}}
            {{footer}}
        </body>
    </html>
''')

REG_DETAILS_TEMPLATE = ('''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Registrar's Office</title>
        </head>
        <body>
            {{header}}
            <hr>
            <h2>Class Details (class id {{class_id}})</h2>
            <strong>Course Id: </strong>{{course_id}} <br/>
            <strong>Days: </strong>{{days}} <br/>
            <strong>Start time: </strong>{{start_time}} <br/>
            <strong>End time: </strong>{{end_time}} <br/>
            <strong>Building: </strong>{{building}} <br/>
            <strong>Room: </strong>{{room}} <br/>

            <hr>
            <h2>Course Details (course id {{course_id}})</h2>

            {{dept_and_num}} <br/>
            <strong>Area: </strong>{{area}} <br/>
            <strong>Title: </strong>{{title}} <br/>
            <strong>Description: </strong>{{description}} <br/>
            <strong>Prerequisites: </strong>{{prerequisites}} <br/>
            {{professors}}

            <hr>
            <p> Click here to do <a href="/">another class search</a></p>
            {{footer}}
        </body>
    </html>
''')

ERROR_PAGE_TEMPLATE = ('''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Registrar's Office</title>
        </head>
        <body>
            {{header}}
            <hr>
            <p><i>{{error}}</i></p>
            <hr>
            <p> Click here to do <a href="/">another class search</a></p>
            {{footer}}
        </body>
    </html>
''')
