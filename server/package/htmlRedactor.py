from bs4 import BeautifulSoup


def generate_chessboard():
    with open('../templates/chess/chess.html', 'rb') as htmlFile:
        htmlText = htmlFile.read()

    chessboard = [[] for _ in range(8)]
    active_array = [[0] * 8 for _ in range(8)]

    figures = set()
    abc = 'abcdefgh'
    soup = BeautifulSoup(htmlText, "html.parser")
    for trTag in soup.find_all("tr"):
        _, thHead, *cells = filter(lambda x: bool(x), trTag.children)
        if thHead.text.isdigit():
            abc_idx = 0
            number = int(thHead.text)
            for cell in cells:
                if cell.text != '\n':
                    cell['onclick'] = "activateFigure(event)"
                    chessboard[number - 1].append(cell.text)
                    cell['id'] = f"{abc[abc_idx]}{number}"
                    abc_idx += 1
                elif len(cell.text.strip()):
                    cell['onclick'] = "activateFigure(event)"
                    # cell['about'] = 'still'
                    # cell['class'] += '0'
                    # print(cell.text)
                    figures.add(cell.text)
                    cell['id'] = f"{abc[abc_idx]}{number}"
                    abc_idx += 1

    # with open('chess2.html', 'w', encoding='utf-8') as file:
    #     file.write(str(soup))

    # print(sures)
    # print(chessboard)
    # print(figures)

    return chessboard


if __name__ == '__main__':
    generate_chessboard()
