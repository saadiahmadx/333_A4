FOOTER_TEMPLATE = ('''

<center class="footer"> Created by Nickolas Casalinuovo and Saadi Ahmad. </center>

''')

HEADER_TEMPLATE = ('''
<center><h1 style="background-color:#E77500; color:white" >Registrar's Office: Class Search</h1></center>
''')

FORM_TEMPLATE = ('''

<form action="" method="get">
    <div class='search' style="">
            <input type="text" style="color:white" name="dept" placeholder="Department" value="{{dept}}">
            <input type="text" name="coursenum" placeholder="Number" value="{{coursenum}}">
            <input type="text" name="area" placeholder="Area" value="{{area}}">
            <input type="text" name="title" placeholder="Title" value="{{title}}">
    </div>
</form>
<br>
''')


SEARCH_RESULTS_TEMPLATE = ('''
    <table>
        <tbody>
            <tr>
                <th><strong>ClassId</strong></th>
                <th><strong>Dept</strong></th>
                <th><strong>Num</strong></th>
                <th><strong>Area</strong></th>
                <th><strong>Title</strong></th>
            </tr>
            {{results}}
        </tbody>
    </table>
''')

INDEX_TEMPLATE = ('''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Registrar's Office Class Search</title>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <style>
                h1 {
                margin-bottom: 10px;
                padding-top: 10px;
                font-family: "Lato";
                font-size:calc(2vw + 20px);
                
                }
                body {
                font-family: "Lato";
                
                }
                input         {
                font-size:20px;
                margin: 5px;
                padding:10px 10px 10px 15px;

                border:1px solid #FFFFFF;
                border-radius: 25px;
                background-color:#E77500;
                color:#FFFFFF;
                min-width: 420px;

                }
                table {
                width: 100%;
                }
                th {
                color:#000000;;
                background:#ffdfbf;
                //border-bottom:4px solid #9ea7af;
                font-size:16px;
                font-weight: 100;
                padding:10px;
                text-align:left;
                text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
                vertical-align:middle;
                }

                th:first-child {
                border-top-left-radius:20px;
                }

                th:last-child {
                border-top-right-radius:20px;
                border-right:none;
                }

                tr {
                color:#666B85;
                font-size:16px;
                font-weight:normal;
                text-shadow: 0 1px 1px rgba(256, 256, 256, 0.05);
                }

                tr:hover td {
                background:#4E5066;
                color:#FFFFFF;
                }

                tr:first-child {
                border-top:none;
                }

                tr:last-child {
                border-bottom:none;
                }

                tr:nth-child(odd) td {
                background:#EBEBEB;
                }

                tr:nth-child(odd):hover td {
                background:#4E5066;
                }

                tr:last-child td:first-child {
                border-bottom-left-radius:3px;
                }

                tr:last-child td:last-child {
                border-bottom-right-radius:3px;
                }

                td {
                background:#FFFFFF;
                padding:8px;
                text-align:left;
                vertical-align:middle;
                font-weight:300;
                font-size:16px;
                }

                td:last-child {
                border-right: 0px;
                }
                .search {
                display: flex;
                flex-wrap: wrap;
                flex-direction: row;
                justify-content:center;
                }
                ::placeholder {
                color: #FFFFFF;
                opacity: 0.6;
                font-style: italic; 
                }

                .footer {
                background-color:#E77500; 
                color:white;
                padding: 10px;
                border-radius: 25px;
                border-top-left-radius:0px;
                border-top-right-radius:0px;
                }
            
            </style>
        </head>
        <body>
        <div style="background-color:#E77500;border-radius: 15px;">
            {{header}}
            <div style="">
            {{form}}
            </div>
            
        </div>
            {{search_results}}
            {{footer}}
        </body>
    </html>
''')

REG_DETAILS_TEMPLATE = ('''
    <!DOCTYPE html>
        <html>
        <head>
            <title>Registrar's Office: Class Details</title>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:bold,normal">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                h1 {
                    font-family: "Lato";
                    font-size:calc(2vw + 20px);

                }
                body {
                    font-family: "Lato";
                    line-height: 1.5rem;

                }
                .footer {
                    background-color:#E77500; 
                    color:white;
                    padding: 10px;
                    border-radius: 25px;
                    border-top-left-radius:0px;
                    border-top-right-radius:0px;
                }
                strong {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
        <div style="background-color:#E77500;">
            <center><h1 style="background-color:#E77500; color:white; padding:40px;" >Registrar's Office: Class Details</h1></center>
        </div>
        <div style="padding:0px 10px;">
            <h2>Class Details (class id {{class_id}})</h2>
            <strong>Course Id: </strong>{{course_id}} <br/>
            <strong>Days: </strong>{{days}} <br/>
            <strong>Start time: </strong>{{start_time}} <br/>
            <strong>End time: </strong>{{end_time}} <br/>
            <strong>Building: </strong>{{building}} <br/>
            <strong>Room: </strong>{{room}} <br/> <br/>

            <hr>
            <h2>Course Details (course id {{course_id}})</h2>

            {{dept_and_num}} <br/>
            <strong>Area: </strong>{{area}} <br/>
            <strong>Title: </strong>{{title}} <br/>
            <strong>Description: </strong>{{description}} <br/>
            <strong>Prerequisites: </strong>{{prerequisites}} <br/>
            {{professors}} <br/>
        </div>
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
