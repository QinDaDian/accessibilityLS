// add the material magic effect
$.material.init();

//show modal
// function showModal(modalTitle, modalInfo, modalSubBtnVal, modalSubBtnDis, focusId) {
//     $('#modalTitle').html(modalTitle);
//     $('#modalInfo').html(modalInfo);
//     $('#modalSubBtn').html(modalSubBtnVal);
//     $('#modalSubBtn').css('display', modalSubBtnDis);
//     $('#modalCommon').modal('show');
//     $('#modalCommon').on('hidden.bs.modal', function () {
//         $(focusId).focus();
//     });
// }
function showModal(modalTitle, modalInfo, focusId) {
    $('#modalTitle').html(modalTitle);
    $('#modalInfo').html(modalInfo);
    $('#modalCommon').modal('show');
    $('#modalCommon').on('hidden.bs.modal', function () {
        $(focusId).focus();
    });
}
function showModalWithSubBtn(modalWithSubBtnTitle, modalWithSubBtnInfo, modalSubBtnVal, focusId) {
    $('#modalWithSubBtnTitle').html(modalWithSubBtnTitle);
    $('#modalWithSubBtnInfo').html(modalWithSubBtnInfo);
    $('#modalSubBtn').html(modalSubBtnVal);
    $('#modalWithSubBtn').modal('show');
    $('#modalWithSubBtn').on('hidden.bs.modal', function () {
        // document.activeElement.blur();
        $(focusId).focus();
    });
}

//使用js动态加载js/css文件
function loadjscssfile(filename,filetype){

    if(filetype == "js"){
        var fileref = document.createElement('script');
        fileref.setAttribute("type","text/javascript");
        fileref.setAttribute("src",filename);
    }else if(filetype == "css"){

        var fileref = document.createElement('link');
        fileref.setAttribute("rel","stylesheet");
        fileref.setAttribute("type","text/css");
        fileref.setAttribute("href",filename);
    }
    if(typeof fileref != "undefined"){
        document.getElementsByTagName("head")[0].appendChild(fileref);
    }
}

//使用js动态删除js/css文件
function removejscssfile(filename, filetype){
//判断文件类型
    var targetelement=(filetype=="js")? "script" : (filetype=="css")? "link" : "none";
//判断文件名
    var targetattr=(filetype=="js")? "src" : (filetype=="css")? "href" : "none";
    var allsuspects=document.getElementsByTagName(targetelement);
//遍历元素， 并删除匹配的元素
    for (var i=allsuspects.length; i>=0; i--){
        if (allsuspects[i] && allsuspects[i].getAttribute(targetattr)!=null && allsuspects[i].getAttribute(targetattr).indexOf(filename)!=-1)
            allsuspects[i].parentNode.removeChild(allsuspects[i]);
    }
}


