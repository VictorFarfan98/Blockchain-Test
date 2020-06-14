import cgi, cgitb

cgitb.enable()

print("Content-type:text/html\n\n")
print("""
<html>
    <head>
        <title>
            Real Time Temperature
        </title>
        
    </head>
    <body>
        <h1>Real Time Temperature:</h1>
        <div id="mine"></div>
    </body>
</html>
""")