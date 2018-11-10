#!/bin/bash

echo "---SCRIPT ACTIVATED---"
python HqTriviaSplit.py 
cd ../../..
cd Downloads

tesseract croppedQuestion.jpg OCR1
cat OCR1.txt > FullQuestion.txt
tesseract croppedAnswer1.jpg OCR2
cat OCR2.txt >> FullQuestion.txt
tesseract croppedAnswer2.jpg OCR3
cat OCR3.txt >> FullQuestion.txt
tesseract croppedAnswer3.jpg OCR4
cat OCR4.txt >> FullQuestion.txt

echo ''
echo ''

python FullQuestionQuery.py 
#cat FullQuestion.txt

cd ..
cd Documents/Python-Concepts/3\ -\ Advanced/

