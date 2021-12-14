import requests
import re
import json
import sys

def main():
    output = list()
    nums = list()
    url = 'http://tygl.zstu.edu.cn/index.php?module=examination&file=exam_ajax&title=stuexamination&action=continueExamination&isAjax=1'
    header = \
    {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Cookie': sys.argv[1]
    }
    data = \
    {
        'paperno' : '20112022010201'
    }
    num_pattern = re.compile(r'(\w{10})_title')
    cnt = 1
    for paperno in range(20112022010201, 20112022010501):
        data['paperno'] = paperno
        res = json.loads(requests.post(url, data=data, headers=header).text)
        if 'content' in res and len(res['content']) != 0:
            res = res['content']
        choice = ['A', 'B', 'C', 'D']
        for num in num_pattern.findall(res):
            if num in nums:
                continue
            nums.append(num)
            sub_pattern = re.compile(r'<a id="{}_title" > (.*?)</a>'.format(num))
            sub = sub_pattern.search(res).group(1)
            choices = list()
            for ch in choice:
                choice_pattern = re.compile(r'<input name="{}" type="radio" value="{}"/>{}.(.*?)</label>'.format(num, ch, ch))
                ans = choice_pattern.search(res)
                if ans is not None:
                    choices.append(ans.group(1))
            result = tuple([num, sub] + choices)
            output.append(result)
        print('第{}轮,当前题库数量:{}'.format(cnt, len(output)))
        cnt += 1
    with open('./data.txt', 'a', encoding='utf-8') as f:
        f.write(str(output))
if __name__ == '__main__':
    main()