$(function(){
    $('.dropdown-menu .dropdown-item').click(function(){
        var visibleItem = $('.dropdown-toggle', $(this).closest('.dropdown'));
        visibleItem.text($(this).attr('value'));
    });
});

(function($){
    
    $('#category-btn').on('click', function(){

        const content = $('#modal');
        content
        // モーダル開始前の処理
        .on('show.bs.modal', () => {
            console.log('modal open start');
        })
        // モーダル開始後の処理
        .on('shown.bs.modal', () => {
            console.log('modal open complete');
        })
        // モーダル終了後の処理
        .on('hidden.bs.modal', () => {
            console.log('modal hidden complete');

        // 後片付け
            $('.form-control', content).val('');
        })
        .modal({
            backdrop: 'static',
            keyboard: true
        });

        // Close(手動)ボタン
        $('#close', content).on('click', () => {
            content.modal('hide');
        });
    });
})(jQuery);

//ファイル選択
$('.custom-file-input').on('change', handleFileSelect);
function handleFileSelect(evt) {
    $('#preview').remove();// 繰り返し実行時の処理
    $(this).parents('.input-group').after('<div id="preview"></div>');
    var files = evt.target.files;

    for (var i = 0, f; f = files[i]; i++) {

        var reader = new FileReader();

        reader.onload = (function(theFile) {
            return function(e) {
                if (theFile.type.match('image.*')) {
                    var $html = ['<div class="d-inline-block mr-1 mt-1"><img class="img-thumbnail" src="', e.target.result,'" title="', escape(theFile.name), '" style="height:100px;" /><div class="small text-muted text-center">', escape(theFile.name),'</div></div>'].join('');// 画像では画像のプレビューとファイル名の表示
                } else {
                    var $html = ['<div class="d-inline-block mr-1"><span class="small">', escape(theFile.name),'</span></div>'].join('');//画像以外はファイル名のみの表示
                }

                $('#preview').append($html);
            };
        })(f);

        reader.readAsDataURL(f);
    }

    $(this).next('.custom-file-label').html(+ files.length + '個のファイルを選択しました');
}

//ファイルの取消
$('.reset').click(function(){
    $(this).parent().prev().children('.custom-file-label').html('ファイル選択...');
    $('.custom-file-input').val('');
    $('#preview').remove('');
})

$("#button").on("click", function(){
    $("#large-frame").prepend('<div class="post-frame"><div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static &ldquo;GroupConnect/img/返信アイコン.jpg&rdquo; %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="reply-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form></div>');
    $($('.post-frame').get().reverse()).each(function(i){
        $(this).attr('id','post-frame' + (i+1));
    });
    $($('.post-outside').get().reverse()).each(function(i){
        $(this).attr('id','post-outside' + (i+1));
    });
    $($('.reply').get().reverse()).each(function(i){
        $(this).attr('id','reply' + (i+1));
    });
    $($('.letter-body').get().reverse()).each(function(i){
        var a = $(this).attr('id','letter-body' + (i+1));
    });
    $($('.reply-form').get().reverse()).each(function(i){
        $(this).attr('id','reply-form' + (i+1));
    });
    $($('.reply-button').get().reverse()).each(function(i){
        $(this).attr('id','reply-button' + (i+1));
    });
});