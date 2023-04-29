# Exam chalange nr0

Artis Ābolts - exam0_user0
Dainis Ciguzis - exam0_user1
Imants Ērglis - exam0_user2
Kārlis Mālnieks - exam0_user3
Māris Pafrats - exam0_user4
Denys Shabelnyk - exam0_user5

## Task

This challange requres for you to understand where buffer owerflow is located and exploit it.

## Flag

After succesful exploitation you should recieve flag in form `VIA[__flag_for_user <aditional value>]`

## Generic workflow

Generic workflow you can follow to solw this challange.

1. Locate the vulnerable function;
2. Understand how many bytes is alocated fow buffer, in IDA these walues are displayed at the begining of the function as hex value
3. You can generate and test found size by supplaing this amount of `A` characters as argument (look for boundary when you have sementation fault and when you dont). you can generate them like this:

```
$(python3 -c "import sys; sys.stdout.buffer.write(b'A'* 111)")
```

4. When you have found size just before owerflow try to give same amount of As into IDA, put breakpoint rigth after `strcpuy()` and run the program. Observe how stack looks like and how far you have filled it with As. From register RBP you can see where base pointer is are you owerflowing it?
5. When you are sure that you owerflow the base pointer then add jump to the flag function to you exploit

```
$(python3 -c "import sys; sys.stdout.buffer.write(b'A'* 111 + b'addres_in reverse')")
```
