const BASE_URL = 'http://localhost:8000/';
const BASE_API_URL = BASE_URL + 'api/';


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }
    console.log(url)
    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return response;
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}



async function onAdd(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;
    console.log(url)
    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        }
    catch (error) {
        console.log(error);
    }

    likeBtn.classList.add('hidden');
    const unlikeBtn = likeBtn.parentElement.getElementsByClassName('unlike')[0];
    unlikeBtn.classList.remove('hidden');
}

async function onRemove(event) {
    event.preventDefault();
    let unlikeBtn = event.target;
    let url = unlikeBtn.href;
    console.log(url)
    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }

    unlikeBtn.classList.add('hidden');
    const likeBtn = unlikeBtn.parentElement.getElementsByClassName('like')[0];
    likeBtn.classList.remove('hidden');
}



window.addEventListener('load', function() {
    const likeButtons = document.getElementsByClassName('like');
    const unlikeButtons = document.getElementsByClassName('unlike');

    for (let btn of likeButtons) {btn.onclick = onAdd}
    for (let btn of unlikeButtons) {btn.onclick = onRemove}
});
