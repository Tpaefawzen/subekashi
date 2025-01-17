async function setscore(baseURL, id, score) {
    res = await fetch(
        baseURL + "/api/ai/" + id + "/?format=json",
        {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    "score": score,
                }
            )
        }
    );
}


function devInput(baseURL, id, score) {
    for (s = 1; s <= 5; s++) {
        radioEle = document.getElementById(String(id) + String(s));
        radioEle.checked = false;

    }
    radioEle = document.getElementById(String(id) + String(score));
    radioEle.checked = true;
    setscore(baseURL, id, score);
}


function copygood() {
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-bottom-right",
        "preventDuplicates": false,
        "onclick": null,
        "timeOut": "3000",
        "extendedTimeOut": "0",
        "showEasing": "swing",
        "hideEasing": "linear",
    }

    checkgoodEles = document.getElementsByClassName("lyricdiv");
    copytext = ""
    for (checkgoodEle of checkgoodEles) {
        isbest = checkgoodEle.children[1].children[0].checked;
        if (isbest) {
            copytext += checkgoodEle.children[0].innerText + "\n";
        }
    }

    if (Boolean(navigator.clipboard)) {
        navigator.clipboard.writeText(copytext);
        toastr.success(copytext + " をコピーしました！")
    } else {
        toastr.warning("この機能はセキュリティの関係上、HTTPS環境上でしか動作しません。")
    }
}