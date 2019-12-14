const baseUrl = 'http://127.0.0.1:8000/api/';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue);
    return cookieValue;
}


function commentCreate() {
    var csrftoken = getCookie('csrftoken');
    var comLabel = $('#comment_label_id');
    let curUser = $('#cur_user_id').val();
    $.ajax({

        url: baseUrl + 'comments/',

        method: 'post',

        headers: {
            "X-CSRFToken": csrftoken
        },

        data: JSON.stringify({
            text: $('#comment-text').val(),
            author: curUser,
            photo: comLabel.attr('data-id')
        }),

        dataType: 'json',

        contentType: 'application/json',

        success: function (response, status) {
            let myDiv = $('.comments');
            let newDiv = $(document.createElement('div'));
            newDiv.addClass('card text-center mt-2');
            newDiv.attr('id', 'comment_id_' + response.id);
            let newDiv1 = $(document.createElement('div'));
            newDiv1.addClass('card-header');
            let hText = $(document.createElement('h4'));
            hText.text(response.author);
            newDiv1.append(hText);
            newDiv.append(newDiv1);
            let newDiv2 = $(document.createElement('div'));
            newDiv2.addClass('card-body');
            let pText = $(document.createElement('p'));
            pText.addClass('card-text');
            pText.text(response.text);
            newDiv2.append(pText);
            let buttonDelete = $(document.createElement('button'));
            buttonDelete.text('x');
            buttonDelete.attr('onclick', 'commentDelete(' + response.id + ')');
            buttonDelete.addClass('btn btn-danger');
            newDiv2.append(buttonDelete);
            newDiv.append(newDiv2);

            let newDiv3 = $(document.createElement('div'));
            newDiv3.addClass('card-footer text-muted');
            newDiv3.text(response.date_create);
            newDiv.append(newDiv3);
            myDiv.prepend(newDiv);
            $('#comment-text').val('')

        },
        error: function () {
            console.log('asd');
        }
    })
}


function commentDelete(num) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: baseUrl + 'comments/' + num + '/',

        method: 'delete',

        dataType: 'json',

        contentType: 'application/json',
        headers: {
            "X-CSRFToken": csrftoken
        },

        success: function () {
            let myDiv = $('#comment_id_' + num);
            myDiv.css('display', 'none');
        }
    })
}


function likePress(num) {
    var csrftoken = getCookie('csrftoken');
    let curUser = $('#cur_user_id').val();
    console.log(curUser);
    $.ajax({
        url: baseUrl + 'rate/' + num + '/',

        method: 'post',

        dataType: 'json',

        contentType: 'application/json',
        headers: {
            "X-CSRFToken": csrftoken
        },
        data: JSON.stringify({'operation': 'plus', 'user': curUser}),

        success: function (response) {
            let myDiv = $('#comment_id_' + num);
            myDiv.css('display', 'none');
            $('#like-button').css('display', 'block');
            $('#dislike-button').css('display', 'none');
            console.log(response.newlike);
            let myStat = $('#likes-text');
            myStat.text(response.newlike);
        }
    });

}

function dislikePress(num) {
    var csrftoken = getCookie('csrftoken');
    let curUser = $('#cur_user_id').val();
    console.log(curUser);
    $.ajax({
        url: baseUrl + 'rate/' + num + '/',

        method: 'post',

        dataType: 'json',

        contentType: 'application/json',
        headers: {
            "X-CSRFToken": csrftoken
        },
        data: JSON.stringify({'operation': 'minus', 'user': curUser}),

        success: function (response) {
            let myDiv = $('#comment_id_' + num);
            myDiv.css('display', 'none');
            let myStat = $('#likes-text');
            myStat.text(response.newlike);
            $('#dislike-button').css('display', 'block');
            $('#like-button').css('display', 'none')
        }
    });

}

