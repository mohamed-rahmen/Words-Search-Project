import sys


def read_wordlist(filename):
    """
    This function reads all the given words inside a specific txt file and
    returns a new list with all those words inside it
    """
    f = open(filename, "r")
    x = f.readline()
    lst = []
    while x != "":
        lst.append(x[:-1])
        x = f.readline()
    f.close()
    return lst


def fill_dictionary(words_list):
    """
    this function takes all the words inside the build word_list
    and inserts them all inside a dictionary, a dictionary that counts how
    many times a word has been repeated in the tests
    and returns the edited dictionary version.
    """
    dic = {}
    for i in words_list:
        dic[i] = 0
    return dic


def read_matrix(filename):
    """
    this functions reads a matrix from a specific given .txt file
    and returns it as a list
    """
    f = open(filename, "r")
    x = f.readline()
    lst = []
    while x != "":
        lst.append(x.strip().split(","))
        x = f.readline()

    f.close()
    return lst


def into_r(matrix):
    newlstR = []
    for i in matrix:
        newlstR.append("".join(i))
    return newlstR


def into_d(matrix):
    newlst = []
    for row in range(len(matrix[0])):
        strnew = ""
        for col in range(len(matrix)):
            strnew += matrix[col][row]
        newlst.append(strnew)
    return newlst


def into_y(matrix):
    newlst = []
    static = 0
    strnew = ""
    for i in range(len(matrix[0])):
        col = 0
        row = static
        while row < len(matrix[0]) and col != len(matrix):
            if i == len(matrix):
                break
            strnew += matrix[col][row]
            row += 1
            col += 1
        if len(strnew) > 0:
            newlst.append(strnew)
        strnew = ""
        static += 1

    static = 0
    for i in range(len(matrix)):
        static += 1
        col = static
        row = 0
        while row < len(matrix[0]):
            if col >= len(matrix):
                break
            strnew += matrix[col][row]
            row += 1
            col += 1
        if len(strnew) > 0:
            newlst.append(strnew)
        strnew = ""

    return newlst


def into_w(matrix):
    newlst = []
    strnew = ""
    for col in range(len(matrix)):
        row = 0
        while col >= 0:
            if row == len(matrix[0]):
                break
            strnew += matrix[col][row]
            row += 1
            col -= 1
        if len(strnew) > 0:
            newlst.append(strnew)
        strnew = ""

    for i in range(len(matrix[0])):
        col = len(matrix) - 1
        row = 1 + i
        while row < len(matrix[0]) and col >= 0:
            strnew += matrix[col][row]
            row += 1
            col -= 1
        if len(strnew) > 0:
            newlst.append(strnew)
        strnew = ""

    return newlst


def reverse(lst):
    newlst = []
    for i in lst:
        newlst.append(i[::-1])
    return newlst


def check_repetition(word, occurred, dic):
    """
    this method gets called from the check_occurrence method and checks
    how many times the word was repeated inside the matrix and then adds
    the amount of repetition to the dictionary

    """
    for i in range(len(word)):
        if word[i:i + len(occurred):] == occurred:
            dic[occurred] += 1


def check_occurrence(lst, word_list, dic):
    """
    this methods takes the returned direction matrix, and then
    checks whither those words inside the matrix are inside the word_list
    and if they are inside it its calls the method check_repetition
    """
    for i in lst:
        for j in word_list:
            if j in i:
                check_repetition(i, j, dic)


def find_words(word_list, matrix, directions):
    dic = fill_dictionary(word_list)
    direction_set = set(directions)
    if (len(matrix) < 1):
        return []
    for i in direction_set:
        newlst = []
        if i == "d":
            newlst = into_d(matrix)
        if i == "u":
            newlst = reverse(into_d(matrix))
        if i == "r":
            newlst = into_r(matrix)
        if i == "l":
            newlst = reverse(into_r(matrix))
        if i == "w":
            newlst = into_w(matrix)
        if i == "x":
            newlst = reverse(into_y(matrix))
        if i == "y":
            newlst = into_y(matrix)
        if i == "z":
            newlst = reverse(into_w(matrix))
        check_occurrence(newlst, word_list, dic)

    Rlist = []
    for word in dic:
        if dic[word] > 0:
            Rlist.append((word, dic[word]))
    return Rlist


def write_output(results, filename):
    folder = open(filename, "w")
    for i in results:
        newstring = str(i).strip("()").replace(" ", "").replace("'", '')
        folder.write(newstring + "\n")
    folder.close()


def run_game():
    """
    a function that gets an arguments from the user, and runs the game
    within those arguments
       """
    args = sys.argv
    word_list = read_wordlist(args[1])
    matrix = read_matrix(args[2])
    directions = args[4]
    write_output(find_words(word_list, matrix, directions), args[3])


if __name__ == '__main__':
    run_game()
