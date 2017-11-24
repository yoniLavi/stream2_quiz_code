import sys

QUESTION_FILE = 'questions.txt'


def get_questions():
    with open(QUESTION_FILE) as f:
            lines = f.readlines()
    return [(lines[i], lines[i + 1].strip()) for i in range(0, len(lines), 2)]


def main():
    try:
        questions = get_questions()
    except IOError:
        print 'Error: Questions file not found.'
        sys.exit()
    except IndexError:
        print 'Error: All questions in the questions file must have answers.'
        sys.exit()

    score = 0
    for question, answer in questions:
        guess = raw_input(question)
        if guess == answer:
            score += 1
    print 'You got %s out of %s questions right' % (score, len(questions))


if __name__ == '__main__':
    main()
