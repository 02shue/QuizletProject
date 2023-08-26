# Quizlet Project

This Quizlet project allows users to create tests and quizzes for themselves for a given Quizlet URL. It is meant to give the users more chances to input the correct answer and allow the user to repeat missed or unknown questions.

## Installation

First, check to see if Selenium is installed on by using [pip](https://pip.pypa.io/en/stable/).

```bash
pip3 --version
```

If not installed, install pip (for Mac)

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

Then, install Selenium

```bash
pip3 install selenium
```

## Usage

After running the file, the user will be able to input the
- Quizlet URL

allowing the user to receive the test within the terminal allowing them to answer the question in three ways
- Give an answer, which will give two results of "Correct" or "Wrong. Correct Answer: ..." allowing the user to see the correct answer, which is then repeated again in the future.
- Type "hint", which will give the user the correct answer and skip the question, allowing the user to see it again in the future.
- Type "end", which will end the quiz prematurely, allowing the user to see their score at that given time.

This works for any Quizlet URL, although smaller answer Quizlets are recommended as it is easier to write the correct, full answer.

## Authors and Acknowledgments 

This project was completed Winter 2022 by Minsuk "Sean" Hue and Sangsoo "Andy" Lim.
