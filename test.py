import subprocess
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


def solution(args):
    url = args[0]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    page_text = soup.get_text()

    occurrences = {str(args[i].lower()): page_text.lower().count(args[i].lower()) for i in range(1, len(args))}

    occurrences = {x[0]: x[1] for x in sorted(occurrences.items())}
    sorted_occurrences = json.dumps(
        {x[0]: x[1] for x in sorted(occurrences.items(), key=lambda x: x[1], reverse=True)})
    return sorted_occurrences


def run_test(args):
    candidate_result = subprocess.run(["python3.7", "main.py"] + args, stdout=subprocess.PIPE, text=True)
    candidate_output = candidate_result.stdout.replace("\n", "")
    correct_output = solution(args)
    return candidate_output == correct_output


def check_test(args):
    test_name = args[0].split('/')[2]
    if run_test(args):
        print("TEST " + test_name + " PASSED")
        return True
    else:
        print("TEST " + test_name + " FAILED")
        return False


if __name__ == '__main__':
    testsList = [["http://example.com", "example", "domain"],
                 ["https://en.wikipedia.org/wiki/Poland ", "Poland", "Warsaw"],
                 ["https://reuters.com", "Business", "Stock", "Currencies"],
                 ["https://telegraph.co.uk", "trade", "business", "$", "ftse", "indices"]]

    passed = 0
    total = 0
    for test_args in testsList:
        total += 1
        if check_test(test_args):
            passed += 1
    print("Passed " + str(passed) + "/" + str(total) + " tests.")
