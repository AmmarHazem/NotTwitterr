$(document).ready(function(){

    /////////////////////////////////////////////////////////////////////////////////////////////////////
    // mouse enter and mouse leave events for the following button
    function mouseEnter (){
        $('.following > button').mouseenter(function(event){
            var $this = $(this);
            $this.removeClass('btn-primary');
            $this.addClass('btn-danger');
            $this.text('Unfollow');
        });
    }

    function mouseLeave (){
        $('.following > button').mouseleave(function(event){
            var $this = $(this);
            $this.removeClass('btn-danger');
            $this.addClass('btn-primary');
            $this.text('Following');
        });
    }

    mouseEnter();
    mouseLeave();

    /////////////////////////////////////////////////////////////////////////////////////////////////////
    // follow button functionality

    function followSuccess(form){
        var btn = form.find('button');
        form.removeClass('follow');
        form.addClass('following');
        form.attr('action', '/unfollow/');
        btn.removeClass('btn-outline-primary');
        btn.addClass('btn-primary');
        btn.text('Following');
        form.unbind();
        btn.unbind();
        var following = $('.following');
        following.bind('submit', mouseEnter());
        following.bind('submit', mouseLeave());
        following.bind('submit', unfollowForm());
    }

    function followError(form){
        var btn = form.find('button');
        btn.removeClass('btn-primary');
        btn.addClass('btn-outline-primary');
        btn.text('Follow');
    }

    function followForm(){
        $('.follow').on('submit', function(event){
            event.preventDefault();
            var $this = $(this);
            var slug = $this.attr('data-slug');
            var data = {'slug' : slug};
            var endPoint = $this.attr('action');
            var method = $this.attr('method');

            followSuccess($this);

            $.ajax({
                url : endPoint,
                method : method,
                data : data,
                success : function(data){
                    console.log('Success Follow', data);
                    if (typeof data == 'string'){
                        var next = window.location.href
                        window.location.href = '/accounts/login/?next=' + next;
                    }
                },
                error : function(error){
                    console.log('Error', error);
                    followError($this);
                }
            });
        });
    }
    followForm();

    /////////////////////////////////////////////////////////////////////////////////////////////////////
    // unfollow button functionality

    function successUnfollow(form){
        var btn = form.find('button');
        form.removeClass('following');
        form.addClass('follow');
        form.attr('action', '/follow/');
        btn.removeClass('btn-danger');
        btn.removeClass('btn-primary');
        btn.addClass('btn-outline-primary');
        btn.text('Follow');
        form.unbind();
        btn.unbind();
        form.bind('submit', followForm());
    }

    function faildUnfollow(form){
        console.log('faild unfollow');
        var btn = form.find('button');
        form.removeClass('follow');
        form.addClass('following');
        btn.addClass('btn-primary');
        btn.text('Following');
        btn.removeClass('btn-outline-primary');
        btn.bind('mouseenter', mouseEnter);
        btn.bind('mouseleave', mouseLeave);
        form.bind('submit', unfollowForm);
    }

    // handel click event
    function unfollowForm(){
        $('.following').on('submit', function(event){
            event.preventDefault();
            var $this = $(this);
            var slug = $this.attr('data-slug');
            var data = {'slug' : slug};
            var endPoint = $this.attr('action');
    
            successUnfollow($this);
    
            $.ajax({
                url : endPoint,
                method : 'POST',
                data : data,
                success : function(response){
                    console.log('Success Unfollow', response);
                    if (typeof response == 'string'){
                        var next = window.location.href
                        window.location.href = '/accounts/login/?next=' + next;
                    }
                },
                error : function(error){
                    console.log('Error', error);
                    faildUnfollow($this);
                }
            });
        });
    }
    unfollowForm();


    /////////////////////////////////////////////////////////////////////////////////////////////////////
    // like button

    function likeSuccess(form, response){
        btn = form.find('button');
        if (btn.hasClass('liked'))
        {
            btn.remove();
            form.append(
                '<button type="submit" class="btn btn-link py-0"><i class="far fa-heart fa-fw mr-1"></i>' + response.likes + '</button>'
            )
        }
        else
        {
            btn.remove();
            form.append(
                '<button type="submit" class="btn btn-link py-0 liked"><i class="fas fa-heart fa-fw mr-1"></i>' + response.likes + '</button>'
            )
        }
    }


    $('.likeForm').on('submit', function(event){
        event.preventDefault();

        var $this = $(this);
        var method = $this.attr('method');
        var endPoint = '/tweet/like/';
        var tweetId = $this.attr('data-tweet-id');
        data = {'tweetId' : tweetId};

        $.ajax({
            url : endPoint,
            method : method,
            data : data,

            success : function(response){
                console.log(response);
                likeSuccess($this, response);
            },
            error : function(error){
                console.log(error);
            }
        });
    });




    /////////////////////////////////////////////////////////////////////////////////////////////////////
    // file input
    var inputs = $('.inputfile');
    Array.prototype.forEach.call(inputs, function(input)
    {
        var label = input.nextElementSibling,
            labelVal = label.innerHTML;

        input.addEventListener('change', function(e)
        {
            var fileName = '';
            if(this.files && this.files.length > 1)
                fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
            else
                fileName = e.target.value.split('\\').pop();

            if( fileName )
                label.querySelector('span').innerHTML = fileName;
            else
                label.innerHTML = labelVal;
        });
    });


    input.addEventListener('focus', function(){ input.classList.add('has-focus');});
    input.addEventListener('blur', function(){ input.classList.remove('has-focus');});

});