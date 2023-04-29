# Exam chalange nr1

Artis Ābolts - exam1_user0
Dainis Ciguzis - exam1_user1
Imants Ērglis - exam1_user2
Kārlis Mālnieks - exam1_user3
Māris Pafrats - exam1_user4
Denys Shabelnyk - exam1_user5

## Task

This challange requres for you to understand where buffer owerflow is located and exploit it. You can exploit it in two ways.

## Flag

After succesful exploitation you should recieve flag in form `VIA[__flag_for_user <aditional value>]`

## Generic workflow

Generic workflow you can follow to solw this challange.

1. Locate the vulnerable function;
2. Understand where and why it is being called;

This is the python oneliner to generate specific amount of characters:

```
$(python3 -c "import sys; sys.stdout.buffer.write(b'A'* 111)")
```

3. When you have found size just before owerflow try to give same amount of As into IDA, put breakpoint rigth after `strcpuy()` and run the program. Observe how stack looks like and how far you have filled it with As. What hawe you owerwritten?

```
$(python3 -c "import sys; sys.stdout.buffer.write(b'A'* 111 + b'addres_in reverse')")
```
