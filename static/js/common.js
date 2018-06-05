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

//学习/检测页面用户结果转换
  function  showUserResult(userResult) {
        if(userResult == 0) {
                $('#userResult').text('不通过');
            } else {
                if (userResult == 1) {
                    $('#userResult').text('通过');
                } else if (userResult == 2) {
                    $('#userResult').text('不存在');
                } else if (userResult == 3) {
                    $('#userResult').text('不知道');
                }
            }
    }
    //学习/检测页面标准答案转换
  function  showStdResult(stdResult) {
        if(stdResult == 0) {
            $('#stdResult').text('不通过');
        }else if(stdResult == 1){
            $('#stdResult').text('通过');
        }else if (stdResult == 2) {
            $('#stdResult').text('不存在');
        }
    }

    //主iframe加载完成时将加载信息隐藏
    function mainIframeLoaded() {
      $('#loadingIframe').css('display','none');
    }

    // 规则折叠
    $('#showRuleSpecific').change(function() {
        $('#ruleSpecific').slideToggle();
    });





