#!/bin/sh
#echo "Hello World!"

for file in 'ls /etc';
do
        echo $file
done

for skill in Ada COffe Action Java;do
        echo "I am good at ${skill}Script"
done

your_name="qinjx"
greeting="hello,"$your_name" !"
greeting_1="hello,${your_name} !"
echo $greeting $greeting_1

str="abcd"
echo ${#str}

str="runoob is a great site"
echo ${str:1:4}

str="runoob is a great company"
echo `expr index "$str" is`
