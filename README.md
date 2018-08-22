# http-server
- Co Lab Nick and Jason

## Usage
- create a .env file with PORT=5000 before creating pipenv
 - if you do remove the environemnt with pipenv --rm, then quit, create .env file and re build pipenv
- http localhost:5000/cow?message=Linux+is+the+best

## Features
- [X]In server.py create the following endpoints:
- [X]GET / - returns a valid HTML formatted response with a project description and an anchor tag which references a new request to GET /cow.
- NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose. ```html <!DOCTYPE html>
</body> </html> ```
- [X]GET /cow?msg=text - returns a cowpy response which correctly displays a default cow object including the text from your query string.
- NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose.
```
 _____________
 < text >
 -------------
 \         __------~~-,
  \      ,'            ,
      /               \
      /                :
      |                  '
      |                  |
      |                  |
      |   _--           |
      _| =-.     .-.   ||
      o|/o/       _.   |
      /  ~          \ |
  (____\@)  ___~    |
      |_===~~~.`    |
  _______.--~     |
  \________       |
              \      |
          __/-___-- -__
          /            _ \
```
- [X]POST /cow msg=text - returns a cowpy response with a JSON body {"content": "<cowsay cow>"}
- NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose.
  {
      "content": " _____________ \n< hello world >\n ------------- \n   \\         __------~~-,\n    \\      ,'            ,\n        /               \\\n         /                :\n        |                  '\n        |                  |\n        |                  |\n         |   _--           |\n         _| =-.     .-.   ||\n         o|/o/       _.   |\n         /  ~       \\ |\n       (____\\@)  ___~    |\n          |_===~~~.`    |\n       _______.--~     |\n       \\________       |\n            \\      |\n              __/-___-- -__\n             /            _ \\"
  }
- [X]Both GET and POST should handle any paths that are not defined by you, and return with the appropriate 404 Not Found response and headers.
- [X]Ensure that each of your valid routes are also able to handle a malformed request, which should return a 400 Bad Request response and headers. For example, a request to GET /cow which does not include a query string message is not properly formatted for your API, and should respond properly.

- [ ]Stretch Goals
- Add the ability to pass additional key/value pairs to both GET and POST requests to allow your endpoints the ability to further define the Cowpy objects. For example, change the default cow object to a dragon. If you extend your application, test your additional features as well!

## Change Log
- Set up readme file.
- switched to cowpy.
- Added custom messge to user on 404 error
- Setup root page to link and instructions to cowsay

## Testing
- 

### Commands
```
pipenv --three
pipenv shell
pipenv install pytest
pipenv install requests
pipenv install cowpy
pip install --upgrade pip setuptools
pip install --upgrade httpie

pipenv --rm
```