$(document).ready(function(){
    var photo=$('.panel');
    var modal=$('.modal');
    var image=$('#img01');
    var close=$('#close');
    photo.click(function()
    {
        var src=$(this).children('img').attr('src');
        console.log(src);
        modal.css({
            'display':'block'
        });
        image.attr('src',src);
    });
    
    close.click(function(){
       
        modal.css({
            'display':'none'
        })
    });
    image.click(function(w)
    {
        w.stopPropagation()
         modal.css({
            'display':'block'
        });
    })
    modal.click(function(w){
        console.log(w);
        modal.css({
            'display':'none'
        })
    });
    
    
});
