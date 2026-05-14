# Lambda Calculator & console application
## Lambda calculator triggered by HTTP API
### POST request with JSON of following structure
{ "op1": < float number >, "op2": < float number >, "operation" : < string [+/*-] >} 
#### Normal Flow (valid JSON)
returns code 200 and result of arithmetic operation
#### Alternative Flow (invalid JSON)
returns code 400 and appropriate message:<br>
- Field op1 missing<br>
- Field op2 missing<br>
- Field operation missing <br>
- op1 not number <br>
- op2 not number
#### Alternative Flow (unsupported Operation)
returns code 404 with message "Operation < value of field operation > not found"
## Console application
- Loop with handling KeyInterrupt  or input containing "exit" <br>
- The client should enter one input line containing two numbers and operation separated by either space or comma or sharp (#)<br>
- Output should eiter "result=..." or error message

