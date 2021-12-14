$.get("https://buffer.s3.didiyunapi.com/tytk.json", data => {
    let voidAns = 0;
    for (let x of $('a[id$="_title"]')) {
        if (data[x.innerText.trim()] == undefined) {
            voidAns++;
            let redtext = document.createAttribute("style");
            redtext.nodeValue = "color: red;";
            x.attributes.setNamedItem(redtext);
            continue;
        }
        let y = x.nextElementSibling.nextElementSibling;
        let choice = 0;
        let hasChoice = false;
        while (y.tagName === 'P') {
            if (data[x.innerText.trim()] === y.innerText.trim().substr(2)) {
                hasChoice = true;
                break;
            }
            choice++;
            y = y.nextElementSibling;
        }
        if (hasChoice) {
            $('input[name=' + x.id.split('_')[0] + ']')[choice].click()
        } else {
            voidAns++;
            let redtext = document.createAttribute("style");
            redtext.nodeValue = "color: red;";
            x.attributes.setNamedItem(redtext);
        }
    };
    if (voidAns) {
        alert("还有" + voidAns + "题自己找找吧");
    } else {
        alert("全部题目都完成了");
    }
});
